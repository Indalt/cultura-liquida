"""Fila da rotina com IA (K-113, bloco 10b; insumos 116 e 118; D-050): que Entradas a rotina lê primeiro.

Sem IA, pela regra, com a versão gravada (D-038). A rotina com IA tem até 20% da semana (D-050) e lê
poucas Entradas por rodada; o que não cabe segue na fila, nunca se descarta (princípio 10). A ordem:

  1. forma de Termo de CLB nomeada (cajuína, mocororó...; Consultas de Termo de bebida), no título ou no
     resumo: o caso-piloto e as CLB já nomeadas (D-031, D-039);
  2. a forma "bebida" das Consultas gerais (CLB em geral, D-032), no título;
  3. forma do Termo do insumo (caju) no título (D-031: o trabalho começa pelo caju);
  4. a forma "bebida" no resumo, ou a forma do insumo no resumo;
  5. só descritor de processo (Consultas mistas e gerais): espera a pré-triagem das Consultas gerais
     segurar o que não é bebida (insumo 118: concreto, aço, tratamento de água);
  e, em qualquer faixa, a forma ou o descritor colado por hífen a outra palavra ("sajor-caju",
  "pós-colheita") desce para a faixa 5 (insumo 118).

Dentro de cada faixa, uma Entrada por ambiente em rodízio (insumo 116: o Oasisbr, agregador, não ocupa
o lote sozinho), e em cada ambiente pelo número da Entrada. Entram só as Entradas em "bruto" com a
pré-triagem "segue" (ou sem texto, que a regra não decide). O que um Termo é (de bebida ou de insumo)
vem das CLB do acervo: o Termo que identifica uma CLB (D-039) é de bebida; os outros, de insumo.

Uso:
    python scripts/fila_ia.py [--lote 15] [--pular N] [--saida <lista.json>] [--resumo]
Saída: a lista do lote (ids, faixa e motivo), com a versão da regra.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402

VERSAO = "fila-ia-0.1"
MOTIVO = re.compile(r"(forma|descritor) '([^']*)' no (título|resumo) \((CO-\d+)\)")


def _n(s: str) -> str:
    return unicodedata.normalize("NFC", s or "").casefold()


def termos_de_bebida(raiz: Path) -> set[str]:
    """Os Termos que identificam uma CLB (campo `termo` da CLB; D-039). O resto conta como insumo."""
    return {carregar_json(arq).get("termo") for arq in (raiz / "acervo" / "clb").glob("CL-*.json")} - {None}


def consultas(raiz: Path) -> dict[str, list[str]]:
    return {arq.stem: carregar_json(arq).get("termos") or []
            for arq in (raiz / "ambientes" / "consultas").glob("CO-*.json")}


def colado_por_hifen(texto: str, forma: str) -> bool:
    """A forma só aparece colada direto a outra palavra por hífen ("sajor-caju", "pós-colheita"). O
    composto com preposição ("castanha-de-caju", "caju-do-cerrado") conta como a forma solta."""
    f = _n(forma)
    t = re.sub(r"-(de|do|da|dos|das)-", r" \1 ", _n(texto))
    e = re.escape(f)
    soltas = re.findall(rf"(?<![\w-]){e}(?![\w-])", t)
    coladas = re.findall(rf"(?:\w-{e}(?!\w))|(?:(?<!\w){e}-\w)", t)
    return bool(coladas) and not soltas


def faixa(en: dict, bebida: set[str], cons: dict[str, list[str]]) -> tuple[int, str]:
    m = MOTIVO.search(en.get("pretriagem", {}).get("motivo", ""))
    if not m:
        return 4, "sem texto na fonte: a regra não decide (princípio 4)"
    tipo, forma, onde, co = m.groups()
    texto = en.get("titulo", "") if onde == "título" else en.get("citacao_resumo", "")
    if texto and colado_por_hifen(texto, forma):
        return 5, f"'{forma}' só colada por hífen (insumo 118)"
    if tipo == "descritor":
        return 5, f"só descritor '{forma}' ({co}; insumo 118)"
    termos = cons.get(co, [])
    if termos and set(termos) <= bebida:
        return 1, f"forma '{forma}' de Termo de bebida no {onde} ({co})"
    if not termos:  # Consulta geral: a forma é "bebida" ou outra variante da Consulta
        return (2 if onde == "título" else 4), f"forma '{forma}' da Consulta geral no {onde} ({co})"
    return (3 if onde == "título" else 4), f"forma '{forma}' de Termo de insumo no {onde} ({co})"


def fila(raiz: Path = RAIZ) -> list[dict]:
    bebida, cons = termos_de_bebida(raiz), consultas(raiz)
    por_faixa: dict[int, OrderedDict[str, list[dict]]] = {}
    for arq in sorted((raiz / "entrada").glob("EN-*.json"), key=lambda p: int(p.stem[3:])):
        try:
            en = json.loads(arq.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if en.get("estado") != "bruto" or en.get("pretriagem", {}).get("estado", "segue") != "segue":
            continue
        f, motivo = faixa(en, bebida, cons)
        por_faixa.setdefault(f, OrderedDict()).setdefault(en.get("ambiente", "?"), []).append(
            {"id": en["id"], "faixa": f, "ambiente": en.get("ambiente"), "motivo": motivo})
    ordem: list[dict] = []
    for f in sorted(por_faixa):
        listas = [list(v) for v in sorted(por_faixa[f].items())]
        listas = [v for _, v in listas]
        while any(listas):  # rodízio entre ambientes
            for v in listas:
                if v:
                    ordem.append(v.pop(0))
    return ordem


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lote", type=int, default=15)
    ap.add_argument("--pular", type=int, default=0)
    ap.add_argument("--saida")
    ap.add_argument("--resumo", action="store_true")
    ap.add_argument("--raiz", default=str(RAIZ))
    a = ap.parse_args()
    toda = fila(Path(a.raiz))
    lote = toda[a.pular:a.pular + a.lote]
    out = {"versao_regra": VERSAO, "na_fila": len(toda), "lote": lote}
    if a.resumo:
        cont: dict[int, int] = {}
        for x in toda:
            cont[x["faixa"]] = cont.get(x["faixa"], 0) + 1
        out["por_faixa"] = {str(k): cont[k] for k in sorted(cont)}
    txt = json.dumps(out, ensure_ascii=False, indent=1)
    if a.saida:
        Path(a.saida).write_text(txt + "\n", encoding="utf-8")
    print(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
