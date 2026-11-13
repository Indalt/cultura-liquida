"""As partes sem IA da rotina com IA (bloco 10b, camada 2; K-113; D-050, D-053). A rotina do Claude Code
(na assinatura de Vicente) roda estes passos e chama os agentes só onde a habilidade pede IA.

Subcomandos:
  preparar --rotulo R [--lote 15]   escolhe o lote pela fila (`fila_ia.py`, regra fila-ia-0.1), lê o texto
                                    das fontes (`ler_fonte.py`, pasta temporária, fora do Git) e escreve o
                                    pedido ao avaliador (extrair-evidencia, Haiku 5.5 pela tabela do K-115a)
                                    na pasta temporária; grava `trilhas/rotina-ia/R/lote.json`.
  filtrar --rotulo R                tira da saída do avaliador a Entrada com pessoa citada por rótulo
                                    (`voz.rotulo_pessoa`): a tabela código → nome fica fora do Git e fora
                                    da nuvem (D-021; K-110), e só a conversa de trabalho a grava. A Entrada
                                    fica em "bruto", dita no relatório; volta numa conversa de trabalho.
  amostra --rotulo R                sorteia a amostra da segunda leitura (`sortear_amostra.py --gravar`,
                                    regra amostra-0.2, semente gravada) e escreve o pedido ao auditor.
  fechar --rotulo R --execucao EX --auditor EX --veredito V
                                    grava `trilhas/rotina-ia/R/segunda-leitura.json` (o que o portão da
                                    camada 2 confere) e o relatório do lote (`fila_curadoria.py`).
A pasta temporária é `$CL_FONTES_TMP` (padrão do `localizar_trecho.py`); a de trabalho do lote fica nela,
em `<tmp>/rotina-ia/R/`. Nada de texto de fonte no Git.

Uso:
    python scripts/rotina_ia.py preparar --rotulo RIA-2026-11-13 [--lote 15]
    python scripts/rotina_ia.py filtrar --rotulo RIA-2026-11-13
    python scripts/rotina_ia.py amostra --rotulo RIA-2026-11-13
    python scripts/rotina_ia.py fechar --rotulo RIA-2026-11-13 --execucao EX-50100 --auditor EX-50101 --veredito serve
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402

VERSAO = "rotina-ia-0.2"
PY = sys.executable
S = Path(__file__).resolve().parent


def tmp() -> Path:
    return Path(os.environ.get("CL_FONTES_TMP") or Path(tempfile.gettempdir()) / "cultura-liquida" / "fontes")


def trabalho(rotulo: str) -> Path:
    p = tmp() / "rotina-ia" / rotulo
    p.mkdir(parents=True, exist_ok=True)
    return p


def trilha(rotulo: str) -> Path:
    p = RAIZ / "trilhas" / "rotina-ia" / rotulo
    p.mkdir(parents=True, exist_ok=True)
    return p


def rodar(*cmd: str) -> subprocess.CompletedProcess:
    r = subprocess.run([PY, *cmd], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    print((r.stdout or "")[-3000:], (r.stderr or "")[-1500:], sep="\n")
    return r


PEDIDO_AVALIADOR = """# Pedido ao avaliador — rotina com IA (K-113), lote {rotulo}

Habilidade: extrair-evidencia (leia `.claude/skills/extrair-evidencia/SKILL.md` antes de tudo). Modelo: o
da rodada (`ambientes/rotinas-ia/rotinas.json`; K-115a, D-054). Teto: 45 chamadas, contadas como o harness conta; perto do teto,
grave o que tiver, junte, valide e devolva.

Entradas do lote (cada uma em `entrada/<EN>.json`): {ids}.
O texto lido de cada fonte está em `{tmp}/<EN>.txt` (marca `[[p. n]]` por página) e o manifesto em
`{tmp}/lote-{rotulo}.json`; a Entrada sem texto (erro no manifesto) fica em quarentena, sem Evidência.
Leia só por `grep -n` e faixas de linhas. Não leia `acervo/` além do que a habilidade pede, nem `trilhas/`. Sem web.

Para cada Evidência, rode
`{py} scripts/localizar_trecho.py localizar --fonte <arquivo> --trecho "<texto exato>" --saida {trab}/trechos/<EN>-<n>.json`
com `<arquivo>` = o campo `arquivo` da Entrada no manifesto (o `.pdf` ou o `.html` lido), **nunca o `.txt`**: o `.txt`
traz as marcas `[[p. n]]` e o hash dele não bate com o do manifesto (a gravação reprova; rodada de 13/11). Leia o `.txt`
para achar o trecho, e localize no `arquivo`. O Trecho vale pelo arquivo do script, nunca pelo texto que você escreve.
Texto que é página de verificação de navegador ("Verificando seu navegador", captcha) não é fonte: a Entrada vai à
quarentena, sem Evidência (anti-robô nunca se contorna). Pessoa citada só por rótulo local
(`voz.rotulo_pessoa`), nunca pelo nome.

Grave um arquivo pequeno por Entrada em `{trab}/itens/<EN>.json` (um objeto do formato abaixo) e, no fim,
`{py} scripts/juntar_saida.py {trab}/itens --saida {trab}/saida-avaliador.json --chave entradas --base {trab}/base.json`.
Formato de cada Entrada (o do bloco 7):
{{"entrada": "EN-nnnn", "estado": "aceito" | "quarentena",
 "valencias": {{"lastro": 0 a 2, "trecho_localizado": 0 a 2, "voz": 0 ou 1, "versao_regra": "valencias-0.1", "criterio_em_falta": []}},
 "sustenta_aviso_saude_politica": true | false,
 "fonte": {{"titulo": "...", "tipo_documento": "...", "ano": "...", "instituicao": "...", "tipo_evidencia": "...", "perspectiva": "...", "deriva_de": "..."}},
 "evidencias": [{{"arquivo_trecho": "{trab}/trechos/EN-nnnn-1.json", "chave": "<tema>|<valor curto>", "atributo": "...", "valor": "...",
   "periodo_referido": "...", "sentido": "a favor" | "divergente", "voz": {{"tipo": "...", "papel": "..."}},
   "lugares": {{"pratica": null, "publicacao": null, "pesquisa": null}},
   "criterio_pratica_cultural": null, "sustenta_aviso_saude_politica": false}}]}}
Domínios (escala `escala_valencias` de `esquemas/valores-provisorios.json`, valencias-0.1): `voz` só 0 ou 1;
`criterio_em_falta` só com os nomes `"lastro"`, `"trecho_localizado"` e `"voz"` (os que ficaram em 0), sem texto livre;
o motivo vai ao log. Entrada sem texto lido: os três em 0, estado "quarentena", `criterio_em_falta` com os três.
A Evidência de outra CLB (outro termo; D-039) leva `"clb": "outra: <termo>"` e fica para o cartão de lista.

Validação (tem de passar): `{py} scripts/gravar_extracao.py {trab}/saida-avaliador.json --execucao EX-0000 --simular --manifestos {tmp} --privado {trab}/privado`.
Termine com o resultado da validação e o bloco LOG (agente avaliador, habilidade extrair-evidencia, decisões por Entrada, alcance).
"""

PEDIDO_AUDITOR = """# Pedido ao auditor — segunda leitura da rotina com IA (K-113), lote {rotulo}

Habilidade: conferir-fato (olhar mecânico; quem produz não confere; D-026). Modelo: o da rodada (`ambientes/rotinas-ia/rotinas.json`; D-054). Teto: 30 chamadas.
Leia: a amostra `{amostra}` (semente e itens sorteados; regra amostra-0.2), o que o lote gravou nesta
rodada (a lista em `{trab}/gravado.txt`, feita por script, e os arquivos novos de `acervo/` que ela aponta) e, fora da amostra,
todo item marcado "sustenta aviso, saúde ou política" (D-038). Para cada Trecho lido, confira contra o arquivo lido
da fonte (o campo `arquivo` da Entrada em `{tmp}/lote-{rotulo}.json`, o `.pdf` ou o `.html`; nunca o `.txt`):
`{py} scripts/localizar_trecho.py conferir <TR.json> --fonte <arquivo>`
e a leitura fiel (a Evidência diz o que o trecho diz; negação e sentido contrário). Sem web.
Devolva em `{trab}/auditor.json`: {{"veredito": "serve" | "serve com ressalvas" | "não serve", "achados": [...],
"lidos": [ids]}} (achados no formato de `esquemas/achado-verificacao.schema.json`) e termine com o bloco LOG
(agente auditor, habilidade conferir-fato, alcance: o que leu e o que ficou fora).
"""


AGREGADORES = {"AM-0022": "https://oasisbr.ibict.br/vufind/api/v1/record"}


def original_do_agregador(en: dict) -> str | None:
    """O Oasisbr é agregador (insumo 116), e a página do registro pede verificação de navegador (ficha do
    AM-0022; nunca se contorna). O link do texto vem pela API do VuFind (a via da ficha): o primeiro `urls`
    do registro, no repositório de origem. Sem link, a Entrada vai pela página (e fica sem texto)."""
    from _coleta import Cliente  # noqa: E402
    rid = en.get("identificador", "").split(":", 1)[-1]
    if not rid:
        return None
    try:
        resp = Cliente().pedir(f"{AGREGADORES[en['ambiente']]}?id={rid}&field[]=urls")
        urls = (resp.json().get("records") or [{}])[0].get("urls") or []
    except Exception as e:  # noqa: BLE001
        print(f"{en['id']}: API do agregador sem resposta ({e})")
        return None
    return urls[0]["url"] if urls else None


def preparar(a) -> int:
    lote = trilha(a.rotulo) / "lote.json"
    r = rodar(str(S / "fila_ia.py"), "--lote", str(a.lote), "--saida", str(lote))
    if r.returncode:
        return 1
    ids = [x["id"] for x in json.loads(lote.read_text(encoding="utf-8"))["lote"]]
    if not ids:
        print("fila vazia: nada a fazer nesta rodada")
        return 0
    diretas, originais = [], []
    for en_id in ids:
        en = json.loads((RAIZ / "entrada" / f"{en_id}.json").read_text(encoding="utf-8"))
        url = original_do_agregador(en) if en.get("ambiente") in AGREGADORES else None
        if url:
            originais += ["--url", f"{en_id}={url}"]
        else:
            diretas.append(en_id)
    args = ["--rotulo", a.rotulo] + (["--entrada", ",".join(diretas)] if diretas else []) + originais
    r = rodar(str(S / "ler_fonte.py"), *args)
    t = trabalho(a.rotulo)
    (t / "itens").mkdir(exist_ok=True)
    (t / "trechos").mkdir(exist_ok=True)
    (t / "base.json").write_text(json.dumps({"lote": a.rotulo}) + "\n", encoding="utf-8")
    pedido = t / "pedido-avaliador.md"
    pedido.write_text(PEDIDO_AVALIADOR.format(rotulo=a.rotulo, ids=", ".join(ids), tmp=tmp().as_posix(),
                                              trab=t.as_posix(), py=Path(PY).as_posix()), encoding="utf-8")
    print(f"{VERSAO}: lote {a.rotulo} com {len(ids)} Entrada(s); pedido ao avaliador em {pedido.as_posix()}")
    return r.returncode


def filtrar(a) -> int:
    t = trabalho(a.rotulo)
    arq = t / "saida-avaliador.json"
    s = json.loads(arq.read_text(encoding="utf-8"))
    fica, sai, outra = [], [], []
    for en in s.get("entradas", []):
        evs = en.get("evidencias", [])
        if any((ev.get("voz") or {}).get("rotulo_pessoa") for ev in evs):
            sai.append(en["entrada"])
        # Evidência de outra CLB (D-039): não entra na CLB do lote; a Entrada fica para a conversa, que grava com
        # `--clb` na CLB candidata e manda o detalhe de povo nomeado à pasta local (D-043, 3; rodada de 13/11)
        elif any(str(ev.get("clb", "")).startswith("outra") for ev in evs):
            outra.append(en["entrada"])
        else:
            fica.append(en)
    s["entradas"] = fica
    (t / "saida-filtrada.json").write_text(json.dumps(s, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (trilha(a.rotulo) / "fora-pessoa-citada.json").write_text(json.dumps(
        {"versao_regra": VERSAO, "motivo": "pessoa citada por rótulo: a tabela código → nome só se grava na "
         "conversa de trabalho (fora do Git e fora da nuvem)", "entradas": sai,
         "outra_clb": outra, "motivo_outra_clb": "Evidência de outra CLB (D-039): a conversa grava com --clb e manda o "
         "detalhe de povo nomeado à pasta local (D-043, 3)"}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    print(f"{VERSAO}: {len(fica)} Entrada(s) seguem para a gravação; {len(sai) + len(outra)} ficam para a conversa "
          f"({', '.join(sai + outra) or '-'})")
    print(f"gravar: {Path(PY).as_posix()} scripts/gravar_extracao.py {(t / 'saida-filtrada.json').as_posix()} --execucao <EX do avaliador> "
          f"--manifestos {tmp().as_posix()} --privado {(t / 'privado').as_posix()}")
    return 0


def amostra(a) -> int:
    antes = set((RAIZ / "trilhas" / "amostras").glob("*.json"))
    r = rodar(str(S / "sortear_amostra.py"), "--gravar")
    if r.returncode:
        return 1
    novos = sorted(set((RAIZ / "trilhas" / "amostras").glob("*.json")) - antes) or \
        sorted((RAIZ / "trilhas" / "amostras").glob(f"{date.today().isoformat()}_amostra*.json"))
    am = novos[-1].relative_to(RAIZ).as_posix()
    t = trabalho(a.rotulo)
    (t / "amostra.txt").write_text(am + "\n", encoding="utf-8")
    # o que o lote gravou (o executor do Gemini não tem git; K-125): arquivos mudados ou novos do acervo e de entrada/
    g = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    (t / "gravado.txt").write_text("\n".join(x[3:] for x in g.stdout.splitlines()
                                             if x[3:].startswith(("acervo/", "entrada/"))) + "\n", encoding="utf-8")
    pedido = t / "pedido-auditor.md"
    pedido.write_text(PEDIDO_AUDITOR.format(rotulo=a.rotulo, amostra=am, tmp=tmp().as_posix(), trab=t.as_posix(), py=Path(PY).as_posix()),
                      encoding="utf-8")
    print(f"{VERSAO}: amostra {am}; pedido ao auditor em {pedido.as_posix()}")
    return 0


def fechar(a) -> int:
    t = trabalho(a.rotulo)
    am = (t / "amostra.txt").read_text(encoding="utf-8").strip()
    aud = json.loads((t / "auditor.json").read_text(encoding="utf-8")) if (t / "auditor.json").exists() else {}
    veredito = aud.get("veredito") or a.veredito
    sl = {"versao_regra": VERSAO, "lote": a.rotulo, "execucao_avaliador": a.execucao, "execucao_auditor": a.auditor,
          "veredito": veredito, "amostra": am, "achados": aud.get("achados", []), "lidos": aud.get("lidos", [])}
    (trilha(a.rotulo) / "segunda-leitura.json").write_text(json.dumps(sl, ensure_ascii=False, indent=1) + "\n",
                                                           encoding="utf-8")
    rodar(str(S / "fila_curadoria.py"), "--execucao", a.execucao, "--saida", str(trilha(a.rotulo) / "relatorio.md"))
    print(f"{VERSAO}: segunda leitura gravada (veredito: {veredito})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("preparar")
    p.add_argument("--rotulo", required=True)
    p.add_argument("--lote", type=int, default=15)
    for nome in ("filtrar", "amostra"):
        sub.add_parser(nome).add_argument("--rotulo", required=True)
    f = sub.add_parser("fechar")
    f.add_argument("--rotulo", required=True)
    f.add_argument("--execucao", required=True)
    f.add_argument("--auditor", required=True)
    f.add_argument("--veredito", default="")
    a = ap.parse_args()
    return {"preparar": preparar, "filtrar": filtrar, "amostra": amostra, "fechar": fechar}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
