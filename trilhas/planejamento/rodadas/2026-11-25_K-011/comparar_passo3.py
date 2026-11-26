"""Compara a proposta e a releitura cega do Passo 3 do K-011, sem IA (D-038; revisao-claude-26-11.md, §4).

Regra (revisao-claude-26-11.md, §4): onde as duas leituras divergem no destino, o insumo fica com o destino
mais conservador ("fica como problema da ferramenta") e a divergência vai ao documento da reunião (D-037).
Divergência só em fundamento, via ou junta_a não muda o destino; também vai ao documento.

Uso: python comparar_passo3.py   (grava comparacao.json e comparacao.md nesta pasta; não muda as entradas)
"""
import json
from collections import Counter
from pathlib import Path

VERSAO = "comparar-passo3-0.1"
AQUI = Path(__file__).resolve().parent
CONSERVADOR = "fica como problema da ferramenta"
CAMPOS = ("destino", "fundamento", "via", "junta_a")


def ler(nome):
    linhas = [json.loads(l) for l in (AQUI / nome).read_text(encoding="utf-8").splitlines() if l.strip()]
    return {l["insumo"]: l for l in linhas}


def main():
    p, r = ler("passo3-proposta.jsonl"), ler("passo3-releitura.jsonl")
    if set(p) != set(r):
        raise SystemExit(f"universos diferentes: só na proposta {sorted(set(p) - set(r))}; só na releitura {sorted(set(r) - set(p))}")
    itens = []
    for n in sorted(p):
        dif = [c for c in CAMPOS if p[n].get(c) != r[n].get(c)]
        final = {c: (p[n][c] if c not in dif else None) for c in CAMPOS}
        if "destino" in dif:
            final["destino"] = CONSERVADOR
        itens.append({"insumo": n, "concorda": not dif, "divergem": dif, "final": final,
                      "proposta": {c: p[n].get(c) for c in CAMPOS}, "releitura": {c: r[n].get(c) for c in CAMPOS},
                      "evidencia_proposta": p[n].get("evidencia"), "evidencia_releitura": r[n].get("evidencia")})
    res = {"versao_regra": VERSAO, "total": len(itens), "concordam": sum(i["concorda"] for i in itens),
           "divergem_no_destino": [i["insumo"] for i in itens if "destino" in i["divergem"]],
           "divergem_so_em_outro_campo": [i["insumo"] for i in itens if i["divergem"] and "destino" not in i["divergem"]],
           "destino_final": dict(Counter(i["final"]["destino"] for i in itens)), "itens": itens}
    (AQUI / "comparacao.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    def v(x):
        return "—" if x is None else str(x)
    md = [f"# K-011 · Passo 3 · Comparação da proposta e da releitura cega", "",
          f"Gerado por `comparar_passo3.py` ({VERSAO}), sem IA, de `passo3-proposta.jsonl` (Antigravity) e "
          "`passo3-releitura.jsonl` (Claude Code, gravada sem abrir a proposta). Regra: divergência no destino fica com "
          f"\"{CONSERVADOR}\"; toda divergência vai ao documento da reunião (D-037). Nenhuma entrada foi alterada.", "",
          f"- Insumos: {res['total']}; concordam em tudo: {res['concordam']}.",
          f"- Divergem no destino ({len(res['divergem_no_destino'])}): {', '.join(map(str, res['divergem_no_destino'])) or 'nenhum'}.",
          f"- Divergem só em fundamento, via ou junta_a ({len(res['divergem_so_em_outro_campo'])}): "
          f"{', '.join(map(str, res['divergem_so_em_outro_campo'])) or 'nenhum'}.",
          "- Destino final: " + "; ".join(f"{k}: {n}" for k, n in sorted(res["destino_final"].items())) + ".", "",
          "## Divergências", "",
          "| Insumo | Campo | Proposta | Releitura | Fica |", "|---|---|---|---|---|"]
    for i in itens:
        for c in i["divergem"]:
            md.append(f"| {i['insumo']} | {c} | {v(i['proposta'][c])} | {v(i['releitura'][c])} | "
                      f"{v(i['final'][c]) if i['final'][c] is not None else 'à reunião'} |")
    md += ["", "## Concordam em tudo", "", "| Insumo | Destino | Fundamento | Via | Junta a |", "|---|---|---|---|---|"]
    for i in itens:
        if i["concorda"]:
            f = i["final"]
            md.append(f"| {i['insumo']} | {f['destino']} | {v(f['fundamento'])} | {f['via']} | {v(f['junta_a'])} |")
    (AQUI / "comparacao.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{res['total']} insumos; concordam {res['concordam']}; destino diverge {res['divergem_no_destino']}; "
          f"outro campo {res['divergem_so_em_outro_campo']}")


if __name__ == "__main__":
    main()
