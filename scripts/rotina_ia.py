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

VERSAO = "rotina-ia-0.1"
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
da chamada (Haiku 5.5, tabela do K-115a). Teto: 45 chamadas, contadas como o harness conta; perto do teto,
grave o que tiver, junte, valide e devolva.

Entradas do lote (cada uma em `entrada/<EN>.json`): {ids}.
O texto lido de cada fonte está em `{tmp}/<EN>.txt` (marca `[[p. n]]` por página) e o manifesto em
`{tmp}/lote-{rotulo}.json`; a Entrada sem texto (erro no manifesto) fica em quarentena, sem Evidência.
Leia só por `grep -n` e faixas de linhas. Não leia `acervo/` além do que a habilidade pede, nem `trilhas/`. Sem web.

Para cada Evidência, rode
`python scripts/localizar_trecho.py localizar --fonte {tmp}/<EN>.txt --trecho "<texto exato>" --saida {trab}/trechos/<EN>-<n>.json`
O Trecho vale pelo arquivo do script, nunca pelo texto que você escreve. Pessoa citada só por rótulo local
(`voz.rotulo_pessoa`), nunca pelo nome.

Grave um arquivo pequeno por Entrada em `{trab}/itens/<EN>.json` (um objeto do formato abaixo) e, no fim,
`python scripts/juntar_saida.py {trab}/itens --saida {trab}/saida-avaliador.json --chave entradas --base {trab}/base.json`.
Formato de cada Entrada (o do bloco 7):
{{"entrada": "EN-nnnn", "estado": "aceito" | "quarentena",
 "valencias": {{"lastro": 0-2, "trecho_localizado": 0-2, "voz": 0-2, "versao_regra": "valencias-0.1", "criterio_em_falta": []}},
 "sustenta_aviso_saude_politica": true | false,
 "fonte": {{"titulo": "...", "tipo_documento": "...", "ano": "...", "instituicao": "...", "tipo_evidencia": "...", "perspectiva": "...", "deriva_de": "..."}},
 "evidencias": [{{"arquivo_trecho": "{trab}/trechos/EN-nnnn-1.json", "chave": "<tema>|<valor curto>", "atributo": "...", "valor": "...",
   "periodo_referido": "...", "sentido": "a favor" | "divergente", "voz": {{"tipo": "...", "papel": "..."}},
   "lugares": {{"pratica": null, "publicacao": null, "pesquisa": null}},
   "criterio_pratica_cultural": null, "sustenta_aviso_saude_politica": false}}]}}
A Evidência de outra CLB (outro termo; D-039) leva `"clb": "outra: <termo>"` e fica para o cartão de lista.

Validação (tem de passar): `python scripts/gravar_extracao.py {trab}/saida-avaliador.json --execucao EX-0000 --simular --manifestos {tmp} --privado {trab}/privado`.
Termine com o resultado da validação e o bloco LOG (agente avaliador, habilidade extrair-evidencia, decisões por Entrada, alcance).
"""

PEDIDO_AUDITOR = """# Pedido ao auditor — segunda leitura da rotina com IA (K-113), lote {rotulo}

Habilidade: conferir-fato (olhar mecânico; quem produz não confere; D-026). Modelo: Sonnet 5.5. Teto: 30 chamadas.
Leia: a amostra `{amostra}` (semente e itens sorteados; regra amostra-0.2), o que o lote gravou nesta
ramificação (`git diff --stat origin/main...HEAD` e os arquivos novos de `acervo/`) e, fora da amostra,
todo item marcado "sustenta aviso, saúde ou política" (D-038). Para cada Trecho lido, confira contra o texto
da fonte em `{tmp}/<EN>.txt` (`python scripts/localizar_trecho.py conferir <TR.json> --fonte {tmp}/<EN>.txt`)
e a leitura fiel (a Evidência diz o que o trecho diz; negação e sentido contrário). Sem web.
Devolva em `{trab}/auditor.json`: {{"veredito": "serve" | "serve com ressalvas" | "não serve", "achados": [...],
"lidos": [ids]}} (achados no formato de `esquemas/achado-verificacao.schema.json`) e termine com o bloco LOG
(agente auditor, habilidade conferir-fato, alcance: o que leu e o que ficou fora).
"""


def preparar(a) -> int:
    lote = trilha(a.rotulo) / "lote.json"
    r = rodar(str(S / "fila_ia.py"), "--lote", str(a.lote), "--saida", str(lote))
    if r.returncode:
        return 1
    ids = [x["id"] for x in json.loads(lote.read_text(encoding="utf-8"))["lote"]]
    if not ids:
        print("fila vazia: nada a fazer nesta rodada")
        return 0
    r = rodar(str(S / "ler_fonte.py"), "--rotulo", a.rotulo, "--entrada", ",".join(ids))
    t = trabalho(a.rotulo)
    (t / "itens").mkdir(exist_ok=True)
    (t / "trechos").mkdir(exist_ok=True)
    (t / "base.json").write_text(json.dumps({"lote": a.rotulo}) + "\n", encoding="utf-8")
    pedido = t / "pedido-avaliador.md"
    pedido.write_text(PEDIDO_AVALIADOR.format(rotulo=a.rotulo, ids=", ".join(ids), tmp=tmp().as_posix(),
                                              trab=t.as_posix()), encoding="utf-8")
    print(f"{VERSAO}: lote {a.rotulo} com {len(ids)} Entrada(s); pedido ao avaliador em {pedido.as_posix()}")
    return r.returncode


def filtrar(a) -> int:
    t = trabalho(a.rotulo)
    arq = t / "saida-avaliador.json"
    s = json.loads(arq.read_text(encoding="utf-8"))
    fica, sai = [], []
    for en in s.get("entradas", []):
        if any((ev.get("voz") or {}).get("rotulo_pessoa") for ev in en.get("evidencias", [])):
            sai.append(en["entrada"])
        else:
            fica.append(en)
    s["entradas"] = fica
    (t / "saida-filtrada.json").write_text(json.dumps(s, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (trilha(a.rotulo) / "fora-pessoa-citada.json").write_text(json.dumps(
        {"versao_regra": VERSAO, "motivo": "pessoa citada por rótulo: a tabela código → nome só se grava na "
         "conversa de trabalho (fora do Git e fora da nuvem)", "entradas": sai}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    print(f"{VERSAO}: {len(fica)} Entrada(s) seguem para a gravação; {len(sai)} ficam para a conversa ({', '.join(sai) or '-'})")
    print(f"gravar: python scripts/gravar_extracao.py {(t / 'saida-filtrada.json').as_posix()} --execucao <EX do avaliador> "
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
    pedido = t / "pedido-auditor.md"
    pedido.write_text(PEDIDO_AUDITOR.format(rotulo=a.rotulo, amostra=am, tmp=tmp().as_posix(), trab=t.as_posix()),
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
