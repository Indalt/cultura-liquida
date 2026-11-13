"""Executor de habilidade pela API do Gemini, sem o Claude (K-125; D-054). gemini-agente-0.1.

Roda um pedido de uma habilidade do projeto (o SKILL.md e o agente em `.claude/`) num modelo do Gemini, com um
laço de ferramentas restritas, um teto de chamadas e o contador de tokens que a API informa (`usageMetadata`).

Ferramentas que o modelo recebe (e só estas):
- `ler_arquivo(caminho, inicio, fim)`: faixa de linhas (até 400 por chamada) de um arquivo do repositório ou da
  pasta de trabalho; nunca `.env` nem `.git/`, nem os prefixos de `--proibir` (fora da pasta de trabalho).
- `grep(padrao, caminho)`: linhas que batem com a expressão (até 120), num arquivo ou pasta.
- `listar(caminho)`: o conteúdo de uma pasta.
- `gravar_arquivo(caminho, conteudo)`: só dentro da pasta de trabalho (`--pasta`).
- `rodar_script(script, argumentos)`: só os scripts de `scripts/` liberados em `--scripts`, com o Python desta
  execução, sem shell.

Contador (D-054): cada rodada grava uma linha em `--registro` (padrão `trilhas/rotina-ia/consumo-gemini.jsonl`):
tokens de entrada (prompt + ferramentas) e de saída (resposta + pensamento), chamadas à API e às ferramentas.
A semana é a do projeto (D-040: de quarta, 23h de Brasília, a quarta seguinte). Antes de cada pedido à API, a
rodada para se a semana somada à rodada, mais o próximo pedido estimado, passar do teto (1 milhão de entrada,
2 milhões de saída), com o estado `teto_semana`; quem chamou avisa Vicente (Issue do relatório do dia).
Os testes de modelo (`--tipo teste`) entram na soma: o teto é da chave, e contar a mais é o lado seguro.

A chave vem de `GEMINI_API_KEY` (ambiente ou `.env` da raiz, fora do Git); nunca é escrita em arquivo, log ou
mensagem (vai no cabeçalho, não na URL). O gemini-4-carbon nunca roda (D-054).

Uso:
    python scripts/gemini_agente.py --modelo gemini-4-hydrogen --agente avaliador --habilidade extrair-evidencia \
        --pedido <pedido.md> --pasta <dir de trabalho> --teto-chamadas 45 --rotulo <rótulo> \
        [--scripts localizar_trecho.py gravar_extracao.py validar.py] [--proibir acervo/ entrada/ ...] \
        [--tipo rotina|teste] [--registro <jsonl>] [--resumo <json>]
    python scripts/gemini_agente.py --semana          soma da semana corrente no registro
Código de saída: 0 = o modelo terminou; 2 = teto de chamadas; 3 = teto da semana; 1 = erro.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

VERSAO = "gemini-agente-0.1"
RAIZ = Path(__file__).resolve().parents[1]
API = "https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"
REGISTRO = RAIZ / "trilhas" / "rotina-ia" / "consumo-gemini.jsonl"
TETO_ENTRADA = 1_000_000
TETO_SAIDA = 2_000_000
BRT = timezone(timedelta(hours=-3))
MAX_LINHAS = 400
MAX_SAIDA = 8000
SCRIPTS_PADRAO = ["localizar_trecho.py", "gravar_extracao.py", "juntar_saida.py", "validar.py"]

FERRAMENTAS = [{"functionDeclarations": [
    {"name": "ler_arquivo", "description": "Lê uma faixa de linhas (numeradas) de um arquivo do repositório ou da pasta de trabalho. Até 400 linhas por chamada.",
     "parameters": {"type": "object", "properties": {
         "caminho": {"type": "string", "description": "caminho relativo à raiz do repositório, ou absoluto dentro da pasta de trabalho"},
         "inicio": {"type": "integer", "description": "primeira linha (1 = começo)"},
         "fim": {"type": "integer", "description": "última linha"}}, "required": ["caminho"]}},
    {"name": "grep", "description": "Lista as linhas (com número) que batem com uma expressão regular, num arquivo ou numa pasta (recursivo). Até 120 linhas.",
     "parameters": {"type": "object", "properties": {
         "padrao": {"type": "string"}, "caminho": {"type": "string"},
         "ignorar_caixa": {"type": "boolean"}}, "required": ["padrao", "caminho"]}},
    {"name": "listar", "description": "Lista os arquivos e pastas de uma pasta.",
     "parameters": {"type": "object", "properties": {"caminho": {"type": "string"}}, "required": ["caminho"]}},
    {"name": "gravar_arquivo", "description": "Grava (substitui) um arquivo de texto, só dentro da pasta de trabalho.",
     "parameters": {"type": "object", "properties": {
         "caminho": {"type": "string"}, "conteudo": {"type": "string"}}, "required": ["caminho", "conteudo"]}},
    {"name": "rodar_script", "description": "Roda um script liberado de scripts/ com o Python do projeto, a partir da raiz do repositório, sem shell. Devolve o código de saída e a saída.",
     "parameters": {"type": "object", "properties": {
         "script": {"type": "string", "description": "nome do arquivo em scripts/, por exemplo localizar_trecho.py"},
         "argumentos": {"type": "array", "items": {"type": "string"}}}, "required": ["script", "argumentos"]}},
]}]

PONTE = """# Como trabalhar nesta execução (executor {versao}, API do Gemini; K-125, D-054)
Você roda fora do Claude Code. As ferramentas que o pedido cita (Bash, Read, Write, Grep, Glob) **não existem aqui**; use as cinco ferramentas desta execução:
- ler arquivo por faixa: `ler_arquivo`; procurar: `grep`; ver pasta: `listar`;
- gravar: `gravar_arquivo`, só dentro da pasta de trabalho `{pasta}` (um arquivo por chamada, qualquer tamanho);
- onde o pedido mandar rodar `<python> scripts/X.py <args>`, chame `rodar_script` com `script` = "X.py" e `argumentos` = a lista dos args, sem o python e sem aspas de shell (cada argumento um item). Scripts liberados: {scripts}.
Teto: {teto} chamadas de ferramenta nesta execução. Termine com uma resposta em texto (sem ferramenta) que diga o resultado da validação e traga o bloco LOG que o seu agente pede.
"""


def carregar_env() -> None:
    env = RAIZ / ".env"
    if not env.exists():
        return
    for linha in env.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$", linha)
        if m and m.group(1) not in os.environ:
            os.environ[m.group(1)] = m.group(2).strip('"').strip("'")


def sem_frontmatter(texto: str) -> str:
    if texto.startswith("---"):
        fim = texto.find("\n---", 3)
        if fim != -1:
            return texto[fim + 4:].lstrip()
    return texto


def inicio_semana(agora: datetime) -> datetime:
    """Semana do projeto (D-040): começa na quarta, 23h de Brasília."""
    local = agora.astimezone(BRT)
    base = local.replace(hour=23, minute=0, second=0, microsecond=0)
    recuo = (local.weekday() - 2) % 7
    ini = base - timedelta(days=recuo)
    if ini > local:
        ini -= timedelta(days=7)
    return ini


def soma_semana(registro: Path, agora: datetime | None = None) -> dict:
    agora = agora or datetime.now(timezone.utc)
    ini = inicio_semana(agora)
    tot = {"inicio": ini.isoformat(), "entrada": 0, "saida": 0, "rodadas": 0}
    if registro.exists():
        for linha in registro.read_text(encoding="utf-8").splitlines():
            if not linha.strip():
                continue
            r = json.loads(linha)
            if datetime.fromisoformat(r["inicio"]) >= ini:
                tot["entrada"] += r["tokens"]["entrada"]
                tot["saida"] += r["tokens"]["saida"]
                tot["rodadas"] += 1
    return tot


class Caixa:
    """As ferramentas restritas."""

    def __init__(self, pasta: Path, scripts: list[str], proibir: list[str]):
        self.pasta = pasta.resolve()
        self.scripts = set(scripts)
        self.proibir = [p.replace("\\", "/").rstrip("/") + "/" for p in proibir]

    def resolver(self, caminho: str) -> Path:
        p = Path(caminho)
        p = (p if p.is_absolute() else RAIZ / p).resolve()
        return p

    def dentro(self, p: Path, base: Path) -> bool:
        try:
            p.relative_to(base)
            return True
        except ValueError:
            return False

    def pode_ler(self, p: Path) -> str | None:
        if self.dentro(p, self.pasta):
            return None
        if not self.dentro(p, RAIZ):
            return "fora do repositório e da pasta de trabalho"
        rel = p.relative_to(RAIZ).as_posix()
        if rel == ".env" or rel.startswith(".env") or rel.startswith(".git/") or rel == ".git":
            return "arquivo protegido"
        for pre in self.proibir:
            if (rel + "/").startswith(pre):
                return f"proibido nesta execução ({pre})"
        return None

    def ler_arquivo(self, caminho: str, inicio: int = 1, fim: int | None = None) -> str:
        p = self.resolver(caminho)
        if (m := self.pode_ler(p)):
            return f"ERRO: {m}: {caminho}"
        if not p.is_file():
            return f"ERRO: arquivo não existe: {caminho}"
        linhas = p.read_text(encoding="utf-8", errors="replace").splitlines()
        inicio = max(1, int(inicio or 1))
        fim = min(len(linhas), int(fim or inicio + MAX_LINHAS - 1), inicio + MAX_LINHAS - 1)
        corpo = "\n".join(f"{i}\t{linhas[i - 1]}" for i in range(inicio, fim + 1))
        return f"[{caminho}: linhas {inicio}-{fim} de {len(linhas)}]\n{corpo}"

    def grep(self, padrao: str, caminho: str, ignorar_caixa: bool = False) -> str:
        p = self.resolver(caminho)
        if (m := self.pode_ler(p)):
            return f"ERRO: {m}: {caminho}"
        try:
            rx = re.compile(padrao, re.I if ignorar_caixa else 0)
        except re.error as e:
            return f"ERRO: expressão inválida: {e}"
        arquivos = [p] if p.is_file() else sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else []
        out = []
        for a in arquivos:
            if self.pode_ler(a.resolve()):
                continue
            try:
                for i, l in enumerate(a.read_text(encoding="utf-8").splitlines(), 1):
                    if rx.search(l):
                        out.append(f"{a.relative_to(p.parent if p.is_file() else p).as_posix()}:{i}: {l[:300]}")
                        if len(out) >= 120:
                            return "\n".join(out) + "\n[… cortado em 120 linhas]"
            except (UnicodeDecodeError, OSError):
                continue
        return "\n".join(out) or "(nada)"

    def listar(self, caminho: str) -> str:
        p = self.resolver(caminho)
        if (m := self.pode_ler(p)):
            return f"ERRO: {m}: {caminho}"
        if not p.is_dir():
            return f"ERRO: não é pasta: {caminho}"
        itens = sorted(p.iterdir())
        return "\n".join(x.name + ("/" if x.is_dir() else "") for x in itens[:300]) or "(vazia)"

    def gravar_arquivo(self, caminho: str, conteudo: str) -> str:
        p = Path(caminho)
        p = (p if p.is_absolute() else self.pasta / p).resolve()
        if not self.dentro(p, self.pasta):
            return f"ERRO: só se grava dentro da pasta de trabalho {self.pasta.as_posix()}"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(conteudo, encoding="utf-8")
        return f"gravado: {p.as_posix()} ({len(conteudo)} caracteres)"

    def rodar_script(self, script: str, argumentos: list[str]) -> str:
        nome = Path(script.replace("\\", "/")).name
        if nome not in self.scripts:
            return f"ERRO: script não liberado: {script} (liberados: {', '.join(sorted(self.scripts))})"
        env = dict(os.environ, PYTHONUTF8="1")
        env.pop("GEMINI_API_KEY", None)
        try:
            r = subprocess.run([sys.executable, str(RAIZ / "scripts" / nome), *[str(a) for a in argumentos]],
                               cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=300, env=env)
        except subprocess.TimeoutExpired:
            return "ERRO: o script passou de 300 s"
        saida = (r.stdout + ("\n[stderr]\n" + r.stderr if r.stderr.strip() else "")).strip()
        if len(saida) > MAX_SAIDA:
            saida = saida[:MAX_SAIDA] + "\n[… cortado]"
        return f"código {r.returncode}\n{saida}"

    def chamar(self, nome: str, args: dict) -> str:
        f = getattr(self, nome, None) if nome in {"ler_arquivo", "grep", "listar", "gravar_arquivo", "rodar_script"} else None
        if f is None:
            return f"ERRO: ferramenta inexistente: {nome}"
        try:
            return f(**args)
        except TypeError as e:
            return f"ERRO: argumentos inválidos para {nome}: {e}"
        except OSError as e:
            return f"ERRO: {type(e).__name__}: {e}"


def pedir(modelo: str, corpo: dict, chave: str) -> dict:
    dados = json.dumps(corpo).encode("utf-8")
    ultimo = ""
    for tentativa in range(5):
        req = urllib.request.Request(API.format(modelo=modelo), data=dados, method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": chave})
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            ultimo = f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:1500]}"
            if e.code not in (429, 500, 502, 503, 504) or (e.code == 429 and tentativa >= 1):
                break  # 429: uma nova tentativa só; repetir gasta a cota de pedidos (prova de 13/11)
        except (urllib.error.URLError, TimeoutError) as e:
            ultimo = f"rede: {e}"
        time.sleep(min(60, 5 * 2 ** tentativa))
    raise RuntimeError(ultimo.replace(chave, "<chave>") if chave else ultimo)


def uso(resp: dict) -> tuple[int, int, int]:
    u = resp.get("usageMetadata", {})
    entrada = u.get("promptTokenCount", 0) + u.get("toolUsePromptTokenCount", 0)
    pens = u.get("thoughtsTokenCount", 0)
    return entrada, u.get("candidatesTokenCount", 0) + pens, pens, u.get("cachedContentTokenCount", 0)


def executar(a) -> int:
    carregar_env()
    if "carbon" in a.modelo.lower():
        print("ERRO: o gemini-4-carbon nunca roda (D-054).")
        return 1
    chave = os.environ.get("GEMINI_API_KEY", "")
    if not chave:
        print("ERRO: sem GEMINI_API_KEY (ambiente ou .env).")
        return 1
    pasta = Path(a.pasta).resolve()
    pasta.mkdir(parents=True, exist_ok=True)
    caixa = Caixa(pasta, a.scripts, a.proibir)
    agente = sem_frontmatter((RAIZ / ".claude" / "agents" / f"{a.agente}.md").read_text(encoding="utf-8"))
    skill = sem_frontmatter((RAIZ / ".claude" / "skills" / a.habilidade / "SKILL.md").read_text(encoding="utf-8"))
    ponte = PONTE.format(versao=VERSAO, pasta=pasta.as_posix(), scripts=", ".join(sorted(caixa.scripts)),
                         teto=a.teto_chamadas)
    sistema = f"{ponte}\n\n# Agente: {a.agente}\n\n{agente}\n\n# Habilidade: {a.habilidade} (SKILL.md)\n\n{skill}"
    pedido = Path(a.pedido).read_text(encoding="utf-8")
    conteudo = [{"role": "user", "parts": [{"text": pedido}]}]
    registro = Path(a.registro)
    semana = soma_semana(registro)
    inicio = datetime.now(timezone.utc)
    tot = {"entrada": 0, "saida": 0, "pensamento": 0, "em_cache": 0}
    chamadas_api = chamadas_ferr = 0
    estado, motivo, final = "erro", "", ""
    ultimo_prompt = len(sistema + pedido) // 3
    transcrito = (pasta / "transcrito-gemini.jsonl").open("w", encoding="utf-8")
    try:
        while True:
            prox = int(ultimo_prompt * 1.15) + 2000
            if (semana["entrada"] + tot["entrada"] + prox > a.teto_entrada
                    or semana["saida"] + tot["saida"] + 8000 > a.teto_saida):
                estado, motivo = "teto_semana", (f"semana {semana['entrada'] + tot['entrada']}/{a.teto_entrada} de entrada e "
                                                 f"{semana['saida'] + tot['saida']}/{a.teto_saida} de saída; o próximo pedido passaria")
                break
            sem_ferr = chamadas_ferr >= a.teto_chamadas
            corpo = {"systemInstruction": {"parts": [{"text": sistema}]}, "contents": conteudo,
                     "generationConfig": {"temperature": a.temperatura}}
            if not sem_ferr:
                corpo["tools"] = FERRAMENTAS
            resp = pedir(a.modelo, corpo, chave)
            chamadas_api += 1
            e_, s_, p_, c_ = uso(resp)
            tot["em_cache"] += c_  # já contados na entrada; ficam à parte para a calibração (insumo do K-125)
            tot["entrada"] += e_
            tot["saida"] += s_
            tot["pensamento"] += p_
            ultimo_prompt = e_ or ultimo_prompt
            cands = resp.get("candidates") or []
            if not cands or "content" not in cands[0]:
                estado = "erro"
                motivo = f"resposta sem conteúdo: {json.dumps(resp.get('promptFeedback') or (cands[0].get('finishReason') if cands else ''))[:300]}"
                break
            msg = cands[0]["content"]
            msg.setdefault("role", "model")
            conteudo.append(msg)
            chamadas = [p["functionCall"] for p in msg.get("parts", []) if "functionCall" in p]
            texto = "".join(p.get("text", "") for p in msg.get("parts", []) if not p.get("thought"))
            transcrito.write(json.dumps({"api": chamadas_api, "uso": [e_, s_, p_], "texto": texto[:2000],
                                         "chamadas": [{"nome": c["name"], "args": {k: (v if len(json.dumps(v, ensure_ascii=False)) < 400 else "[longo]")
                                                                                     for k, v in (c.get("args") or {}).items()}} for c in chamadas]},
                                        ensure_ascii=False) + "\n")
            if not chamadas:
                final = texto
                estado = "teto_chamadas" if sem_ferr else "concluida"
                motivo = "teto de chamadas atingido; o modelo fechou sem ferramentas" if sem_ferr else ""
                break
            respostas = []
            for c in chamadas:
                chamadas_ferr += 1
                if chamadas_ferr > a.teto_chamadas:
                    res = "ERRO: teto de chamadas atingido; não se executou. Responda agora, sem ferramentas, com o que já gravou."
                else:
                    res = caixa.chamar(c["name"], c.get("args") or {})
                    restam = a.teto_chamadas - chamadas_ferr
                    if restam <= 3:
                        res += f"\n[restam {max(restam, 0)} chamadas de ferramenta: grave, valide e feche]"
                fr = {"name": c["name"], "response": {"resultado": res}}
                if c.get("id"):
                    fr["id"] = c["id"]
                respostas.append({"functionResponse": fr})
            conteudo.append({"role": "user", "parts": respostas})
    except RuntimeError as e:
        estado, motivo = "erro", str(e)
    finally:
        transcrito.close()
    (pasta / "resposta-gemini.md").write_text(final, encoding="utf-8")
    linha = {"versao": VERSAO, "inicio": inicio.isoformat(), "fim": datetime.now(timezone.utc).isoformat(),
             "tipo": a.tipo, "rotulo": a.rotulo, "modelo": a.modelo, "agente": a.agente, "habilidade": a.habilidade,
             "tokens": tot, "chamadas_api": chamadas_api, "chamadas_ferramenta": min(chamadas_ferr, a.teto_chamadas),
             "teto_chamadas": a.teto_chamadas, "estado": estado, "motivo": motivo[:1200]}
    registro.parent.mkdir(parents=True, exist_ok=True)
    with registro.open("a", encoding="utf-8") as f:
        f.write(json.dumps(linha, ensure_ascii=False) + "\n")
    nova = soma_semana(registro)
    linha["semana"] = {**nova, "teto_entrada": a.teto_entrada, "teto_saida": a.teto_saida}
    if a.resumo:
        Path(a.resumo).write_text(json.dumps(linha, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(linha, ensure_ascii=False))
    return {"concluida": 0, "teto_chamadas": 2, "teto_semana": 3}.get(estado, 1)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--semana", action="store_true", help="só mostra a soma da semana")
    ap.add_argument("--modelo")
    ap.add_argument("--agente")
    ap.add_argument("--habilidade")
    ap.add_argument("--pedido")
    ap.add_argument("--pasta")
    ap.add_argument("--teto-chamadas", type=int, default=45)
    ap.add_argument("--rotulo", default="")
    ap.add_argument("--tipo", choices=["rotina", "teste"], default="rotina")
    ap.add_argument("--scripts", nargs="*", default=SCRIPTS_PADRAO)
    ap.add_argument("--proibir", nargs="*", default=[])
    ap.add_argument("--registro", default=str(REGISTRO))
    ap.add_argument("--resumo")
    ap.add_argument("--temperatura", type=float, default=1.0)
    ap.add_argument("--teto-entrada", type=int, default=TETO_ENTRADA)
    ap.add_argument("--teto-saida", type=int, default=TETO_SAIDA)
    a = ap.parse_args()
    if a.semana:
        s = soma_semana(Path(a.registro))
        print(json.dumps({**s, "teto_entrada": a.teto_entrada, "teto_saida": a.teto_saida}, ensure_ascii=False))
        return 0
    falta = [n for n in ("modelo", "agente", "habilidade", "pedido", "pasta") if not getattr(a, n)]
    if falta:
        ap.error("faltam: " + ", ".join("--" + n for n in falta))
    return executar(a)


if __name__ == "__main__":
    sys.exit(main())
