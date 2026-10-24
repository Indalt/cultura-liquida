"""Resumo legível da coleta (K-108): Entradas por fonte e por ano, e títulos de exemplo sorteados.

Lê as Entradas de `entrada/` (e, depois do K-108b, as pegadas de `ambientes/pegadas/`) e os metadados
do cache local (`scripts/metadados.py`, fora do Git). O ano e o título vêm do cache; sem eles, "sem
ano" e "sem título no cache". Os títulos de exemplo são sorteados com semente registrada, para que o
sorteio se refaça; título é metadado (padrão da F-0003), nunca resumo.

Uso:
    python scripts/resumo_coleta.py [--exemplos 20] [--semente 20261024] [--saida <arquivo.md>]
        [--cache <pasta>] [--raiz <pasta>]
"""
from __future__ import annotations

import argparse
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from metadados import ler_cache, pasta_cache  # noqa: E402

VERSAO = "resumo-coleta-0.1"


def decada(ano) -> str:
    try:
        a = int(str(ano)[:4])
    except (TypeError, ValueError):
        return "sem ano"
    return f"{a // 10 * 10}–{a // 10 * 10 + 9}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exemplos", type=int, default=20)
    ap.add_argument("--semente", type=int, default=20261024)
    ap.add_argument("--saida", type=Path)
    ap.add_argument("--cache", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    nomes = {}
    for f in (raiz / "ambientes").glob("AM-*.json"):
        d = carregar_json(f)
        nomes[d["id"]] = d.get("nome") or d["id"]
    ents = [carregar_json(f) for f in sorted((raiz / "entrada").glob("EN-*.json"))]
    cache: dict[str, dict] = {}
    for am in {e.get("ambiente") for e in ents if e.get("ambiente")}:
        cache.update(ler_cache(pasta_cache(a.cache) / f"{am}.jsonl"))
    por_fonte = Counter(e.get("ambiente") or e.get("canal") for e in ents)
    por_decada: dict[str, Counter] = {}
    com_meta = []
    for e in ents:
        m = cache.get(e.get("identificador"))
        por_decada.setdefault(e.get("ambiente") or "?", Counter())[decada(m["ano"]) if m else "sem metadados"] += 1
        if m and m.get("titulo"):
            com_meta.append((e, m))
    linhas = [f"# Resumo da coleta ({VERSAO})", "",
              f"Gerado por `scripts/resumo_coleta.py` sobre `entrada/` e o cache local de metadados (fora do Git). "
              f"{len(ents)} Entradas; {len(com_meta)} com título no cache.", "", "## Entradas por fonte", "",
              "| Fonte | Entradas |", "|---|---|"]
    linhas += [f"| {nomes.get(k, k)} ({k}) | {v} |" for k, v in por_fonte.most_common()]
    linhas += ["", "## Entradas por década de publicação (ano do registro na fonte)", ""]
    decs = sorted({d for c in por_decada.values() for d in c}, key=lambda x: (not x[0].isdigit(), x))
    fontes = sorted(por_decada)
    linhas += ["| Década | " + " | ".join(fontes) + " | Total |", "|---" * (len(fontes) + 2) + "|"]
    for d in decs:
        vals = [por_decada[f][d] for f in fontes]
        linhas.append(f"| {d} | " + " | ".join(str(v) for v in vals) + f" | {sum(vals)} |")
    rnd = random.Random(a.semente)
    amostra = sorted(rnd.sample(com_meta, min(a.exemplos, len(com_meta))), key=lambda x: x[0]["id"])
    linhas += ["", f"## {len(amostra)} títulos de exemplo (sorteio com semente {a.semente})", "",
               "| Entrada | Fonte | Ano | Título | Link |", "|---|---|---|---|---|"]
    for e, m in amostra:
        t = " ".join(m["titulo"].split()).replace("|", "/")
        linhas.append(f"| {e['id']} | {e.get('ambiente')} | {m.get('ano') or '—'} | {t} | {e['url_ou_arquivo']} |")
    texto = "\n".join(linhas) + "\n"
    if a.saida:
        a.saida.write_text(texto, encoding="utf-8")
    print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
