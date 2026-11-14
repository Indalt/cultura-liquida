"""Manutenção da casa do projeto (manutencao-0.1; sem IA): olha a pasta e diz o que pede arrumação.

O que é: uma vistoria da **casa** (a pasta, o quadro, o harness, o Git), não da base de conhecimento.
A base não tem revisão de rotina (D-037): quem a confere é o validador, o portão e a amostra do auditor.
Esta ferramenta responde a outra pergunta: "a pasta ainda diz a verdade sobre si mesma, e quanto custa
abri-la?". Cada olhar é uma regra mecânica, com versão; nenhum usa IA, rede ou biblioteca de fora
(só Python e Git), para continuar funcionando seja qual for a IA que opere o projeto (princípio 11).

O que ela **nunca** faz: apagar, mover, corrigir ou decidir (princípio 12; D-024: nada se apaga).
Ela propõe; quem arruma é a sessão de trabalho ou Vicente ("quem propõe não aprova", D-038).
A única escrita é o relatório, e só com `--gravar`.

Os olhares (um por regra; `--olhar a,b` escolhe):
- raiz        o que está na raiz da pasta e não é esperado ali (arquivo solto, saída de comando).
- sobras      arquivo vazio, cópia de segurança, temporário ou de nome estranho dentro do Git.
- tamanho     arquivos e megabytes do que o Git versiona, contra o alarme da D-045 (registro de valores).
- contexto    o peso do que toda conversa e todo agente carregam ao abrir (AGENTS.md e CLAUDE.md) e o da
              seção "Passo corrente": histórico ali é custo repetido; o lugar dele é o checklist.
- decisoes    cada decisão do registro (`trilhas/decisoes/`) tem a linha de essência no AGENTS.md, e o inverso.
- quadro      mais de um cartão "Fazendo" no desenvolvimento (D-035: um por vez); cartão repetido.
- retomar     o RETOMAR.md fala de um cartão que ainda está em "Fazendo"?
- harness     o modelo de cada agente no frontmatter bate com a tabela do AGENTS.md; toda habilidade tem
              SKILL.md e `exemplos/`.
- referencias caminho citado nos arquivos de regra (AGENTS, CLAUDE, README, RETOMAR, agentes e
              habilidades) que não existe na pasta.
- scripts     script de `scripts/` que nada chama (rotina, hook, habilidade, teste, outro script, regra).
- logs        dia em que o hook viu agente terminar (`_desconhecido`) e nenhum agente tem o log completo.
- git         arquivo fora do Git, mudança sem commit, commit sem envio, ramificação remota parada.

Graus: **arrumar** (a regra foi quebrada), **olhar** (pode ser falso alarme; alguém decide), e o silêncio
(nada a dizer). Os limites são provisórios (D-034) e ficam na tabela LIMITES, com a versão da regra.

Uso:
    python scripts/manutencao.py                      # vistoria inteira, na tela
    python scripts/manutencao.py --olhar raiz,git     # só alguns olhares
    python scripts/manutencao.py --gravar             # também grava trilhas/relatorios/manutencao-AAAA-MM-DD.md
    python scripts/manutencao.py --json               # saída para máquina
    python scripts/manutencao.py --estrito            # código 1 se houver algo a arrumar (padrão: sempre 0)
    python scripts/manutencao.py --raiz <pasta>       # outra pasta (os casos de teste usam)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

VERSAO = "manutencao-0.1"
RAIZ_PADRAO = Path(__file__).resolve().parent.parent

# Limites provisórios (D-034). Mudar aqui muda a regra: subir a versão e dizer o porquê no Histórico.
LIMITES = {
    "contexto_caracteres": 24000,      # AGENTS.md + CLAUDE.md: carregados em toda conversa e em todo agente
    "passo_corrente_caracteres": 3000,  # a seção "Passo corrente" do AGENTS.md
    "tamanho_arquivos": 20000,          # D-045; o registro de valores (guarda_alarme) vale sobre estes
    "tamanho_mb": 200,
    "tamanho_aviso_fracao": 0.5,        # avisa a partir de metade do alarme
    "ramificacao_parada_dias": 7,
    "retomar_velho_dias": 7,
}

ESPERADOS_RAIZ = {
    "00_Fundacao_Cultura_Liquida.md", "AGENTS.md", "CLAUDE.md", "README.md", "RETOMAR.md", "requirements.txt",
    ".git", ".gitignore", ".gitattributes", ".githooks", ".github", ".claude", ".venv", ".env", ".vscode",
    "acervo", "ambientes", "entrada", "esquemas", "grafo", "legado", "scripts", "testes", "trilhas", "wiki-local",
}
RAMIFICACOES_FIXAS = {"origin/main", "origin/HEAD", "origin/rotinas"}
# Caminhos citados de propósito como coisa que não existe ou que fica fora da pasta
REFERENCIAS_IGNORADAS = {".agents/", ".env"}
SOBRAS = re.compile(r"(\.bak|\.tmp|\.orig|\.rej|~|\.swp)$|(^|/)(Thumbs\.db|desktop\.ini|nul)$|(^|/)__pycache__/", re.I)
EXTENSOES = (".md", ".py", ".json", ".jsonl", ".yml", ".yaml", ".sh", ".txt", ".toml")
MODELOS = {"opus": "opus", "sonnet": "sonnet", "haiku": "haiku", "fable": "fable"}


def git(raiz: Path, *args: str) -> list[str]:
    """Linhas da saída do Git; lista vazia se o comando falhar (pasta sem Git, sem remoto)."""
    try:
        r = subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=raiz, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
    except OSError:
        return []
    return [x for x in r.stdout.splitlines() if x.strip()] if r.returncode == 0 else []


def ler(caminho: Path) -> str:
    try:
        return caminho.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def achado(olhar: str, grau: str, o_que: str, onde: str = "", sugestao: str = "") -> dict:
    return {"olhar": olhar, "grau": grau, "o_que": o_que, "onde": onde, "sugestao": sugestao}


def secao(texto: str, titulo: str) -> str:
    """O trecho de um Markdown entre o título `## titulo` e o próximo `## `."""
    m = re.search(rf"^## {re.escape(titulo)}.*?$", texto, re.M)
    if not m:
        return ""
    resto = texto[m.end():]
    fim = re.search(r"^## ", resto, re.M)
    return resto[:fim.start()] if fim else resto


def cartoes(raiz: Path) -> list[tuple[str, str, str]]:
    """(frente, coluna, K-nnn) de cada linha do quadro."""
    texto = ler(raiz / "trilhas" / "planejamento" / "quadro.md")
    saida, frente = [], ""
    for linha in texto.splitlines():
        if linha.startswith("## "):
            frente = linha[3:].strip()
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*\*\*(K-\d+[a-z]?)\*\*", linha)
        if m:
            saida.append((frente, m.group(1), m.group(2)))
    return saida


# ---------------------------------------------------------------- os olhares

def olhar_raiz(raiz: Path) -> list[dict]:
    fora = sorted(p.name for p in raiz.iterdir() if p.name not in ESPERADOS_RAIZ)
    return [achado("raiz", "arrumar", f"item inesperado na raiz: {n!r}", n,
                   "conferir o que é; se for saída de comando ou sobra, tirar do Git (`git rm`) com commit próprio")
            for n in fora]


def olhar_sobras(raiz: Path) -> list[dict]:
    saida = []
    for nome in git(raiz, "ls-files"):
        p = raiz / nome
        base = nome.rsplit("/", 1)[-1]
        if SOBRAS.search(nome) or base.startswith("-") or len(base) < 3:
            saida.append(achado("sobras", "arrumar", "arquivo de sobra ou de nome estranho no Git", nome,
                                "tirar do Git se não for dado do projeto"))
        elif p.is_file() and p.stat().st_size == 0 and base != "__init__.py" and base != ".gitkeep":
            saida.append(achado("sobras", "olhar", "arquivo vazio no Git", nome, "apagar ou preencher"))
    return saida


def olhar_tamanho(raiz: Path) -> list[dict]:
    lim_arq, lim_mb = LIMITES["tamanho_arquivos"], LIMITES["tamanho_mb"]
    try:  # o registro de valores provisórios vale sobre a tabela daqui
        reg = json.loads(ler(raiz / "esquemas" / "valores-provisorios.json"))
        txt = json.dumps(reg)
        m = re.search(r'"guarda_alarme":\s*\{"valor":\s*\{"arquivos":\s*(\d+),\s*"mb":\s*(\d+)', txt)
        if m:
            lim_arq, lim_mb = int(m.group(1)), int(m.group(2))
    except (ValueError, OSError):
        pass
    nomes = git(raiz, "ls-files", "-co", "--exclude-standard")
    total, pastas = 0, {}
    for n in nomes:
        p = raiz / n
        if p.is_file():
            t = p.stat().st_size
            total += t
            topo = n.split("/", 1)[0] if "/" in n else "(raiz)"
            c, b = pastas.get(topo, (0, 0))
            pastas[topo] = (c + 1, b + t)
    mb = total / 1_048_576
    fr = max(len(nomes) / lim_arq, mb / lim_mb)
    maiores = ", ".join(f"{k} {c} arq. {b / 1_048_576:.1f} MB"
                        for k, (c, b) in sorted(pastas.items(), key=lambda x: -x[1][0])[:4])
    texto = f"{len(nomes)} arquivos e {mb:.1f} MB (alarme: {lim_arq} ou {lim_mb} MB; {fr:.0%} do alarme). Maiores: {maiores}"
    if fr >= 1:
        return [achado("tamanho", "arrumar", texto, "", "comprimir as pegadas de Recortes fechados (D-045) ou levar ao planejamento")]
    if fr >= LIMITES["tamanho_aviso_fracao"]:
        return [achado("tamanho", "olhar", texto, "", "acompanhar; a D-045 permite comprimir pegadas antigas")]
    return [achado("tamanho", "nota", texto)]


def olhar_contexto(raiz: Path) -> list[dict]:
    agents, claude = ler(raiz / "AGENTS.md"), ler(raiz / "CLAUDE.md")
    total = len(agents) + len(claude)
    passo = len(secao(agents, "Passo corrente"))
    saida = []
    custo = f"cerca de {total // 3:,} tokens por conversa e por agente chamado".replace(",", ".")
    if total > LIMITES["contexto_caracteres"]:
        saida.append(achado("contexto", "arrumar",
                            f"AGENTS.md e CLAUDE.md somam {total} caracteres ({custo}); o limite é {LIMITES['contexto_caracteres']}",
                            "AGENTS.md", "enxugar o que é histórico; as essências das decisões ficam"))
    else:
        saida.append(achado("contexto", "nota", f"AGENTS.md e CLAUDE.md somam {total} caracteres ({custo})"))
    if passo > LIMITES["passo_corrente_caracteres"]:
        saida.append(achado("contexto", "arrumar",
                            f'a seção "Passo corrente" tem {passo} caracteres; o limite é {LIMITES["passo_corrente_caracteres"]}',
                            "AGENTS.md", "deixar só Feito (uma linha), Em curso, Próximo e onde ler; o histórico já está no checklist e no quadro"))
    return saida


def olhar_decisoes(raiz: Path) -> list[dict]:
    pasta = raiz / "trilhas" / "decisoes"
    if not pasta.is_dir():
        return []
    arquivos = {p.stem for p in pasta.glob("D-*.json")}
    linhas = set(re.findall(r"^\s*- \*\*(D-\d+)", ler(raiz / "AGENTS.md"), re.M))
    saida = [achado("decisoes", "arrumar", f"{d} está no registro e não tem a linha de essência no AGENTS.md",
                    f"trilhas/decisoes/{d}.json", "acrescentar a essência confirmada (habilidade registrar-decisao)")
             for d in sorted(arquivos - linhas)]
    if arquivos:
        primeiro = min(int(d[2:]) for d in arquivos)
        saida += [achado("decisoes", "arrumar", f"{d} tem linha no AGENTS.md e não tem arquivo no registro", "AGENTS.md",
                         "gravar a decisão no registro ou conferir o número")
                  for d in sorted(linhas - arquivos) if int(d[2:]) >= primeiro]
    return saida


def olhar_quadro(raiz: Path) -> list[dict]:
    cs = cartoes(raiz)
    saida = []
    fazendo = [k for f, col, k in cs if f.startswith("Desenvolvimento") and col.lower().startswith("fazendo")]
    if len(fazendo) > 1:
        saida.append(achado("quadro", "arrumar", f"{len(fazendo)} cartões em Fazendo no desenvolvimento: {', '.join(fazendo)}",
                            "trilhas/planejamento/quadro.md", "um cartão por vez (D-035): fechar ou devolver a A fazer"))
    vistos, repetidos = set(), set()
    for _, _, k in cs:
        (repetidos if k in vistos else vistos).add(k)
    saida += [achado("quadro", "arrumar", f"cartão {k} aparece mais de uma vez", "trilhas/planejamento/quadro.md",
                     "juntar as linhas") for k in sorted(repetidos)]
    if cs:
        cont = {}
        for f, col, _ in cs:
            chave = (f.split()[0], col.split("(")[0].strip())
            cont[chave] = cont.get(chave, 0) + 1
        resumo = "; ".join(f"{f} {c}: {n}" for (f, c), n in sorted(cont.items()))
        saida.append(achado("quadro", "nota", resumo))
    return saida


def olhar_retomar(raiz: Path) -> list[dict]:
    p = raiz / "RETOMAR.md"
    if not p.is_file():
        return []
    m = re.search(r"K-\d+[a-z]?", ler(p))
    saida = []
    if m:
        colunas = [col for _, col, k in cartoes(raiz) if k == m.group(0)]
        if colunas and not any(c.lower().startswith("fazendo") for c in colunas):
            saida.append(achado("retomar", "arrumar", f"o RETOMAR.md fala do {m.group(0)}, que está em {colunas[0]!r} no quadro",
                                "RETOMAR.md", "atualizar ou apagar o RETOMAR.md ao fechar o cartão"))
    idade = (datetime.now() - datetime.fromtimestamp(p.stat().st_mtime)).days
    if idade > LIMITES["retomar_velho_dias"]:
        saida.append(achado("retomar", "olhar", f"o RETOMAR.md não muda há {idade} dias", "RETOMAR.md", "conferir se ainda vale"))
    return saida


def olhar_harness(raiz: Path) -> list[dict]:
    saida = []
    tabela = {}
    for linha in secao(ler(raiz / "AGENTS.md"), "Agentes e habilidades").splitlines():
        cel = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(cel) >= 4 and re.fullmatch(r"[a-z-]+", cel[0]):
            tabela[cel[0]] = next((v for k, v in MODELOS.items() if k in cel[-1].lower()), "")
    for p in sorted((raiz / ".claude" / "agents").glob("*.md")):
        m = re.search(r"^model:\s*(\S+)", ler(p), re.M)
        if not m:
            saida.append(achado("harness", "arrumar", f"agente {p.stem} sem modelo no frontmatter", f".claude/agents/{p.name}"))
            continue
        real = next((v for k, v in MODELOS.items() if k in m.group(1).lower()), m.group(1))
        if p.stem in tabela and tabela[p.stem] and tabela[p.stem] != real:
            saida.append(achado("harness", "arrumar",
                                f"agente {p.stem}: o frontmatter diz {m.group(1)} e a tabela do AGENTS.md diz {tabela[p.stem]}",
                                "AGENTS.md", "acertar a tabela pelo frontmatter, que é o que roda"))
        elif p.stem not in tabela:
            saida.append(achado("harness", "olhar", f"agente {p.stem} fora da tabela do AGENTS.md", f".claude/agents/{p.name}"))
    for d in sorted((raiz / ".claude" / "skills").glob("*")):
        if not d.is_dir():
            continue
        if not (d / "SKILL.md").is_file():
            saida.append(achado("harness", "arrumar", f"habilidade {d.name} sem SKILL.md", f".claude/skills/{d.name}"))
        elif not (d / "exemplos").is_dir():
            saida.append(achado("harness", "olhar", f"habilidade {d.name} sem a pasta exemplos/", f".claude/skills/{d.name}"))
    return saida


def olhar_referencias(raiz: Path) -> list[dict]:
    fontes = [raiz / n for n in ("AGENTS.md", "CLAUDE.md", "README.md", "RETOMAR.md")]
    fontes += sorted((raiz / ".claude" / "agents").glob("*.md")) + sorted((raiz / ".claude" / "skills").glob("*/SKILL.md"))
    scripts = {p.name for p in (raiz / "scripts").glob("*")} if (raiz / "scripts").is_dir() else set()
    versionados = "\n" + "\n".join(git(raiz, "ls-files")) + "\n"
    saida, vistos = [], set()
    for f in fontes:
        for trecho in re.findall(r"`([^`\n]+)`", ler(f)):
            alvo = trecho.split()[0].rstrip(".,;:)")
            if alvo.startswith(("python", "git", "gh")) and len(trecho.split()) > 1:
                alvo = trecho.split()[1].rstrip(".,;:)")
            if (alvo in REFERENCIAS_IGNORADAS or re.search(r"[<>*{}$|=]|nnn|AAAA|\.\.\.|^(https?:|[A-Za-z]:|~|repos/|-)", alvo)
                    or (alvo, f) in vistos):
                continue
            eh_caminho = "/" in alvo and re.match(r"^[\w.À-ÿ-]+/", alvo)
            eh_script = "/" not in alvo and alvo.endswith((".py", ".sh"))
            if not (eh_caminho or eh_script):
                continue
            vistos.add((alvo, f))
            # a citação pode ser relativa à pasta de que o texto fala (`logs/` dentro de `trilhas/`)
            existe = ((raiz / alvo).exists() or f"/{alvo}" in versionados or f"\n{alvo}" in versionados) if eh_caminho else alvo in scripts
            if not existe and eh_caminho and not alvo.endswith("/") and "." not in alvo.rsplit("/", 1)[-1]:
                continue  # palavra com barra que não é caminho (ex.: "e/ou")
            if not existe:
                saida.append(achado("referencias", "olhar", f"caminho citado que não existe: {alvo}",
                                    str(f.relative_to(raiz)).replace("\\", "/"), "corrigir a citação ou dizer que saiu"))
    return saida


def olhar_scripts(raiz: Path) -> list[dict]:
    saida = []
    for p in sorted((raiz / "scripts").glob("*.py")):
        if p.name.startswith("_"):
            continue
        usos = git(raiz, "grep", "-l", "-F", p.stem, "--", ".", f":!scripts/{p.name}", ":!trilhas", ":!RETOMAR.md")
        if not usos:
            saida.append(achado("scripts", "olhar", f"script que nada chama fora das trilhas: {p.name}", f"scripts/{p.name}",
                                "dizer no cabeçalho quando se usa, ligar a um teste, ou levar ao planejamento como sobra"))
    return saida


def olhar_logs(raiz: Path) -> list[dict]:
    """A linha mínima do hook (`_desconhecido`) é esperada; falta algo quando, no mesmo dia, nenhum agente
    tem o log completo que o curador grava com `registrar_log.py`."""
    pasta = raiz / "trilhas" / "logs"
    if not pasta.is_dir():
        return []
    agentes = {p.stem for p in (raiz / ".claude" / "agents").glob("*.md")}
    saida = []
    for p in sorted(pasta.glob("*_desconhecido.jsonl")):
        dia = p.name.split("_", 1)[0]
        completos = [q for q in pasta.glob(f"{dia}_*.jsonl") if q.stem.split("_", 1)[1] in agentes]
        if not completos:
            n = sum(1 for x in ler(p).splitlines() if x.strip())
            saida.append(achado("logs", "olhar", f"{n} agente(s) terminaram em {dia} e nenhum tem log completo nesse dia",
                                f"trilhas/logs/{p.name}", "conferir se o curador gravou o log (registrar_log.py); o hook só guarda a linha mínima"))
    return saida


def olhar_git(raiz: Path) -> list[dict]:
    saida = []
    estado = git(raiz, "status", "--porcelain")
    fora = [x[3:] for x in estado if x.startswith("??")]
    mudados = [x[3:] for x in estado if not x.startswith("??")]
    if fora:
        saida.append(achado("git", "arrumar", f"{len(fora)} arquivo(s) fora do Git: {', '.join(fora[:5])}", "",
                            "versionar, pôr no .gitignore ou apagar"))
    if mudados:
        saida.append(achado("git", "arrumar", f"{len(mudados)} mudança(s) sem commit: {', '.join(mudados[:5])}", "", "commit e envio"))
    adiante = git(raiz, "rev-list", "--count", "@{u}..HEAD")
    if adiante and adiante[0] != "0":
        saida.append(achado("git", "arrumar", f"{adiante[0]} commit(s) sem envio", "", "git push"))
    juntadas = {x.strip() for x in git(raiz, "branch", "-r", "--merged", "origin/main")}
    corte = date.today() - timedelta(days=LIMITES["ramificacao_parada_dias"])
    for linha in git(raiz, "for-each-ref", "refs/remotes", "--format=%(refname:short) %(committerdate:short)"):
        nome, _, dia = linha.partition(" ")
        if nome in RAMIFICACOES_FIXAS or not dia:
            continue
        if nome in juntadas:
            saida.append(achado("git", "olhar", f"ramificação remota já juntada ao main: {nome} ({dia})", nome,
                                "pode ser apagada pelo dono (a exclusão não é da ferramenta)"))
        elif date.fromisoformat(dia) < corte:
            saida.append(achado("git", "olhar", f"ramificação remota parada desde {dia}: {nome}", nome, "juntar, ou dizer por que fica"))
    return saida


OLHARES = {
    "raiz": olhar_raiz, "sobras": olhar_sobras, "tamanho": olhar_tamanho, "contexto": olhar_contexto,
    "decisoes": olhar_decisoes, "quadro": olhar_quadro, "retomar": olhar_retomar, "harness": olhar_harness,
    "referencias": olhar_referencias, "scripts": olhar_scripts, "logs": olhar_logs, "git": olhar_git,
}


def relatorio(achados: list[dict], olhares: list[str], raiz: Path) -> str:
    n_arr = sum(1 for a in achados if a["grau"] == "arrumar")
    n_olh = sum(1 for a in achados if a["grau"] == "olhar")
    linhas = [f"# Manutenção da casa ({date.today().isoformat()}; {VERSAO})", "",
              f"Alcance: os olhares {', '.join(olhares)}, sobre `{raiz.name}`, sem IA e sem rede. "
              "Fora do alcance: o conteúdo da base (validador, portão e amostra do auditor), o estado das rotinas "
              "na nuvem e tudo o que está fora da pasta. A ferramenta não mudou nada.", "",
              f"**A arrumar: {n_arr} · A olhar: {n_olh}**", ""]
    for nome in olhares:
        meus = [a for a in achados if a["olhar"] == nome]
        linhas.append(f"## {nome}")
        if not [a for a in meus if a["grau"] != "nota"]:
            linhas.append("- em ordem")
        for a in meus:
            marca = {"arrumar": "**arrumar**", "olhar": "olhar", "nota": "nota"}[a["grau"]]
            onde = f" (`{a['onde']}`)" if a["onde"] else ""
            sug = f" → {a['sugestao']}" if a["sugestao"] else ""
            linhas.append(f"- {marca}: {a['o_que']}{onde}{sug}")
        linhas.append("")
    return "\n".join(linhas)


def main() -> int:
    ap = argparse.ArgumentParser(description="Vistoria da casa do projeto, sem IA. Não muda nada.")
    ap.add_argument("--olhar", default="", help="olhares separados por vírgula (padrão: todos)")
    ap.add_argument("--raiz", default=str(RAIZ_PADRAO))
    ap.add_argument("--gravar", action="store_true", help="grava o relatório em trilhas/relatorios/")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--estrito", action="store_true", help="código 1 se houver algo a arrumar")
    a = ap.parse_args()
    raiz = Path(a.raiz).resolve()
    olhares = [x.strip() for x in a.olhar.split(",") if x.strip()] or list(OLHARES)
    errados = [x for x in olhares if x not in OLHARES]
    if errados:
        print(f"olhar desconhecido: {', '.join(errados)}. Existem: {', '.join(OLHARES)}", file=sys.stderr)
        return 2
    achados = []
    for nome in olhares:
        try:
            achados += OLHARES[nome](raiz)
        except Exception as e:  # um olhar quebrado não derruba os outros; fica dito
            achados.append(achado(nome, "arrumar", f"o olhar falhou: {type(e).__name__}: {e}", "scripts/manutencao.py"))
    if a.json:
        print(json.dumps({"versao": VERSAO, "data": date.today().isoformat(), "olhares": olhares, "achados": achados},
                         ensure_ascii=False, indent=2))
    else:
        texto = relatorio(achados, olhares, raiz)
        print(texto)
        if a.gravar:
            destino = raiz / "trilhas" / "relatorios" / f"manutencao-{date.today().isoformat()}.md"
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(texto + "\n", encoding="utf-8")
            print(f"gravado: {destino.relative_to(raiz)}")
    n_arr = sum(1 for x in achados if x["grau"] == "arrumar")
    print(f"{VERSAO}: {n_arr} a arrumar, {sum(1 for x in achados if x['grau'] == 'olhar')} a olhar", file=sys.stderr if a.json else sys.stdout)
    return 1 if (a.estrito and n_arr) else 0


if __name__ == "__main__":
    sys.exit(main())
