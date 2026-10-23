"""Calcula μ e λ por linhagens independentes e gera o grafo (bloco 3; l. 116-117, 547-549, 602;
valor mu_lambda de esquemas/valores-provisorios.json).

Linhagem = componente conexo do grafo de deriva_de entre as Fontes (dez textos que copiam o
mesmo autor contam como um). Para cada Proposição, as Evidências ativas (não retiradas) dão as
linhagens a favor e as divergentes, pelas Fontes dos seus Trechos. μ = min(1, a favor / 2);
λ = min(1, divergentes / 2); Dc = μ − λ; Dct = μ + λ − 1; o estado pelos limites do registro.
Nenhum peso por tipo de fonte (D-039). O estado "inconsistente" é a tensão que abre o cartão de
conflito (D-037; bloco 5). A Aresta soma as Evidências das suas Proposições. A W não captada
(uma Falta no lugar da Compreensão local) entra no grafo como "paracompleto".

Saídas, em <raiz>/grafo/ (só o que o script gera): nos.json, arestas.json, tabela-xy.md (X
insumo × Y processo, com "não observada") e tabela-z.md (Z, os períodos).

Uso:
    python scripts/calcular_mu_lambda.py [--raiz <pasta>] [--gravar] [--conferir] [--sem-grafo]
--gravar   regrava mu, lambda, estado, estado_detalhe e versao_regra nas Proposições e Arestas.
--conferir compara com o que está gravado; código 1 se algum valor não bate com o recálculo.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, prefixo  # noqa: E402
from _comum import RAIZ, carregar_valores  # noqa: E402

REGRA = carregar_valores()["valores"]["mu_lambda"]["valor"]
VERSAO = REGRA["versao_regra"]
SAT = REGRA["saturacao"]
LC, LT = REGRA["limites"]["certeza"], REGRA["limites"]["contradicao"]
EPS = 1e-9


def linhagens(indice: dict) -> dict[str, str]:
    """Fonte → representante da linhagem (união-busca sobre deriva_de, sem direção)."""
    pai = {i: i for i, r in indice.items() if prefixo(i) == "FO"}

    def raiz(x):
        while pai.setdefault(x, x) != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x

    for i in list(pai):
        for d in indice[i].get("deriva_de", []):
            a, b = raiz(i), raiz(d)
            if a != b:
                pai[max(a, b)] = min(a, b)
    return {i: raiz(i) for i in pai}


def estado(mu: float, lam: float) -> tuple[str, str | None]:
    dc, dct = mu - lam, mu + lam - 1
    if dc >= LC - EPS and abs(dct) < LT - EPS:
        return "verdadeiro", None
    if dc <= -LC + EPS and abs(dct) < LT - EPS:
        return "falso", None
    if dct >= LT - EPS and abs(dc) < LC - EPS:
        return "inconsistente", None
    if dct <= -LT + EPS and abs(dc) < LC - EPS:
        return "paracompleto", None
    # intermediário: o quadrante, como no para-analisador de 12 estados (Anexo C, F-12, secundária)
    if dc >= 0:
        if dct >= 0:
            nome = "quase-verdadeiro tendendo ao inconsistente" if dc >= dct else "inconsistente tendendo ao verdadeiro"
        else:
            nome = "quase-verdadeiro tendendo ao paracompleto" if dc >= -dct else "paracompleto tendendo ao verdadeiro"
    else:
        if dct >= 0:
            nome = "quase-falso tendendo ao inconsistente" if -dc >= dct else "inconsistente tendendo ao falso"
        else:
            nome = "quase-falso tendendo ao paracompleto" if -dc >= -dct else "paracompleto tendendo ao falso"
    return "intermediário", nome


def graus(evs: list[str], indice: dict, lin: dict) -> dict:
    favor, contra = set(), set()
    for ev in evs:
        e = indice.get(ev)
        if not e or e.get("retirado"):
            continue
        fo = indice.get(e.get("trecho"), {}).get("fonte")
        if fo not in lin:
            continue
        (favor if e.get("sentido") == "a favor" else contra).add(lin[fo])
    mu, lam = min(1.0, len(favor) / SAT), min(1.0, len(contra) / SAT)
    est, det = estado(mu, lam)
    return {"mu": round(mu, 4), "lambda": round(lam, 4), "Dc": round(mu - lam, 4), "Dct": round(mu + lam - 1, 4),
            "estado": est, "estado_detalhe": det, "linhagens_a_favor": len(favor), "linhagens_divergentes": len(contra)}


def calcular(indice: dict) -> dict[str, dict]:
    lin = linhagens(indice)
    res = {}
    for i, r in indice.items():
        if r.get("retirado"):
            continue
        if prefixo(i) == "PR":
            res[i] = graus(r.get("evidencias", []), indice, lin)
        elif prefixo(i) == "AR":
            evs = [e for p in r.get("proposicoes", []) for e in indice.get(p, {}).get("evidencias", [])]
            res[i] = graus(evs, indice, lin)
    return res


def gerar_grafo(raiz: Path, indice: dict, res: dict) -> None:
    pasta = raiz / "grafo"
    pasta.mkdir(exist_ok=True)
    nos = []
    for i, r in sorted(indice.items()):
        if prefixo(i) != "EL" or r.get("retirado"):
            continue
        w = r.get("w", "")
        nos.append({"id": i, "clb": r.get("clb"), "x": r.get("x", []), "y": r.get("y", []), "z": r.get("z"),
                    "w": w, "w_estado": "paracompleto" if prefixo(w) == "F" else "captada",
                    "proposicoes": r.get("proposicoes", [])})
    arestas = [{"id": i, "de": indice[i]["de"], "para": indice[i]["para"], "tipo": indice[i].get("tipo"),
                "proposicoes": indice[i].get("proposicoes", []), "z": indice[i].get("z"), "w": indice[i].get("w"),
                "w_estado": "paracompleto" if prefixo(indice[i].get("w", "")) == "F" else "captada", **g}
               for i, g in sorted(res.items()) if prefixo(i) == "AR"]
    cab = {"gerado_por": "scripts/calcular_mu_lambda.py", "versao_regra": VERSAO}
    (pasta / "nos.json").write_text(json.dumps({**cab, "nos": nos}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (pasta / "arestas.json").write_text(json.dumps({**cab, "arestas": arestas}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ins = sorted(i for i in indice if prefixo(i) == "IN")
    pcs = sorted(i for i in indice if prefixo(i) == "PC")
    nome = lambda i: indice[i].get("nome", i)  # noqa: E731
    cel = {}
    for n in nos:
        for x in n["x"]:
            for y in n["y"]:
                cel.setdefault((x, y), []).append(n["id"])
    linhas = [f"# Tabela X × Y (gerada; {VERSAO})", "", "| X insumo \\ Y processo | " + " | ".join(f"{nome(p)} ({p})" for p in pcs) + " |",
              "|---|" + "---|" * len(pcs)]
    for x in ins:
        linhas.append(f"| {nome(x)} ({x}) | " + " | ".join(", ".join(cel.get((x, p), [])) or "não observada" for p in pcs) + " |")
    (pasta / "tabela-xy.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    porz: dict[str, list[str]] = {}
    for n in nos:
        porz.setdefault(n["z"] or "não informado", []).append(n["id"])
    lz = [f"# Tabela Z (gerada; {VERSAO})", "", "| Z (período) | Elementos |", "|---|---|"]
    lz += [f"| {z} | {', '.join(v)} |" for z, v in sorted(porz.items())]
    (pasta / "tabela-z.md").write_text("\n".join(lz) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--gravar", action="store_true")
    ap.add_argument("--conferir", action="store_true")
    ap.add_argument("--sem-grafo", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    indice, onde, erros = carregar_acervo(raiz)
    if erros:
        print("\n".join(erros))
        return 1
    res = calcular(indice)
    divergencias = []
    for i, g in sorted(res.items()):
        r = indice[i]
        print(f"{i}: μ={g['mu']} λ={g['lambda']} Dc={g['Dc']} Dct={g['Dct']} {g['estado']}"
              f"{' (' + g['estado_detalhe'] + ')' if g['estado_detalhe'] else ''}"
              f" · linhagens {g['linhagens_a_favor']} a favor, {g['linhagens_divergentes']} divergentes")
        if a.conferir:
            for k in ("mu", "lambda", "estado"):
                if r.get(k) != g[k]:
                    divergencias.append(f"{i}: {k} gravado {r.get(k)!r} ≠ recalculado {g[k]!r}")
            if g["estado_detalhe"] and r.get("estado_detalhe") != g["estado_detalhe"]:
                divergencias.append(f"{i}: estado_detalhe gravado {r.get('estado_detalhe')!r} ≠ {g['estado_detalhe']!r}")
        if a.gravar:
            r.update(mu=g["mu"], **{"lambda": g["lambda"]}, estado=g["estado"], versao_regra=VERSAO)
            if g["estado_detalhe"]:
                r["estado_detalhe"] = g["estado_detalhe"]
            else:
                r.pop("estado_detalhe", None)
            onde[i][0].write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tensoes = [i for i, g in res.items() if g["estado"] == "inconsistente"]
    if tensoes:
        print("tensões (abrem cartão de conflito):", ", ".join(sorted(tensoes)))
    if not a.sem_grafo:
        gerar_grafo(raiz, indice, res)
    for d in divergencias:
        print("NÃO BATE:", d)
    print(f"{VERSAO}: {len(res)} registros calculados; {'recálculo bate' if a.conferir and not divergencias else ''}"
          f"{f'{len(divergencias)} divergência(s)' if divergencias else ''}")
    return 1 if divergencias else 0


if __name__ == "__main__":
    sys.exit(main())
