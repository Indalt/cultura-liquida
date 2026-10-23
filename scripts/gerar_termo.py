"""Do Termo, os booleanos, o glossário e os links; fecha o laço termo → booleano → Consulta
nova (bloco 3; princípio 2, l. 103-105). Regra termo-0.1.

Para cada Termo ativo (acervo/termos/*.json, ou os arquivos dados):
  - booleanos em sintaxe genérica: as designações, as variantes e as formas de busca, entre
    aspas e unidas por OR; com descritores processuais (--descritores), o mesmo grupo AND
    (descritores). A tradução para a sintaxe de cada Ambiente fica em
    ambientes/traducao-consultas.json (bloco 4), não aqui;
  - o glossário (<raiz>/acervo/termos/glossario.md): conceito, designações, variantes com
    lugar, período e abonações, formas de busca e relações, com links para os registros;
  - a proposta de Consulta nova (esquemas/consulta.schema.json), impressa e, com --gravar,
    gravada em <raiz>/ambientes/consultas/ com ID da faixa da conversa.
Forma de OCR ou truncada registrada como variante reprova (a mesma regra do validar_acervo.py).

Uso:
    python scripts/gerar_termo.py [<termo.json> ...] [--raiz <pasta>] [--descritores "a,b"] \\
        [--execucao EX-nnnn] [--gravar]
Código 0 = gerado; 1 = Termo com problema (nada é gravado).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, prefixo, proximo_id  # noqa: E402
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from validar_acervo import checar_termo  # noqa: E402

VERSAO = "termo-0.1"


def formas(t: dict) -> list[str]:
    vistos, saida = set(), []
    for f in t.get("designacoes", []) + [v["forma"] for v in t.get("variantes", [])] + t.get("formas_de_busca", []):
        if f.casefold() not in vistos:
            vistos.add(f.casefold())
            saida.append(f)
    return saida


def booleanos(t: dict, descritores: list[str]) -> list[str]:
    grupo = " OR ".join(f'"{f}"' for f in formas(t))
    grupo = f"({grupo})"
    saida = [grupo]
    if descritores:
        saida.append(f"{grupo} AND ({' OR '.join(d if ' ' not in d else f'\"{d}\"' for d in descritores)})")
    return saida


def glossario(termos: list[dict], raiz: Path) -> str:
    ln = [f"# Glossário (gerado por scripts/gerar_termo.py; {VERSAO})", ""]
    for t in sorted(termos, key=lambda x: x["designacoes"][0].casefold()):
        ln += [f"## {t['designacoes'][0]} ({t['id']}, {t['estado']})", "", t["conceito"], ""]
        if len(t["designacoes"]) > 1:
            ln.append(f"- **Designações:** {', '.join(t['designacoes'])}")
        for v in t.get("variantes", []):
            extra = "; ".join(x for x in [", ".join(v.get("lugares", [])), v.get("periodo", ""),
                                           ", ".join(v.get("abonacoes", []))] if x)
            ln.append(f"- **Variante:** {v['forma']} ({v['tipo_variacao']}{'; ' + extra if extra else ''})")
        if t.get("formas_de_busca"):
            ln.append(f"- **Formas de busca (só no booleano):** {', '.join(t['formas_de_busca'])}")
        if t.get("abonacoes"):
            ln.append(f"- **Abonações:** {', '.join(f'[{e}](evidencias/{e}.json)' for e in t['abonacoes'])}")
        for r in t.get("relacoes", []):
            ln.append(f"- **{r['tipo'].capitalize()}:** [{r['termo']}]({r['termo']}.json)")
        ln.append(f"- **Booleanos:** {' · '.join(f'`{b}`' for b in t.get('booleanos', []))}")
        ln.append("")
    return "\n".join(ln)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("termos", nargs="*", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--descritores", default="")
    ap.add_argument("--execucao", default="EX-0000")
    ap.add_argument("--gravar", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    indice, onde, _ = carregar_acervo(raiz)
    if a.termos:
        termos = [(carregar_json(p if p.is_absolute() else RAIZ / p), p if p.is_absolute() else RAIZ / p) for p in a.termos]
    else:
        termos = [(r, onde[i][0]) for i, r in sorted(indice.items()) if prefixo(i) == "TE"]
    termos = [(t, p) for t, p in termos if not t.get("retirado")]
    descr = [d.strip() for d in a.descritores.split(",") if d.strip()]
    problemas = {t["id"]: checar_termo(t) for t, _ in termos}
    problemas = {k: v for k, v in problemas.items() if v}
    if problemas:
        for k, v in problemas.items():
            for e in v:
                print(f"RECUSADO {k}: {e}")
        return 1
    ids = set(indice)
    esq = carregar_esquema("consulta")
    for t, p in termos:
        t["booleanos"] = booleanos(t, descr)
        cid = proximo_id("CO", ids)
        ids.add(cid)
        consulta = {"id": cid, "nome": f"{t['designacoes'][0]}{' + descritores' if descr else ''} ({t['id']})",
                    "tipo": "mista" if descr else "termo", "termos": [t["id"]],
                    "variantes": [f for f in formas(t) if f not in t["designacoes"]], "descritores": descr,
                    "traducao": f"ambientes/traducao-consultas.json#{cid}",
                    "origem_registro": {"criado_por": "scripts/gerar_termo.py", "data": date.today().isoformat(),
                                        "execucao": a.execucao, "versao_regra": VERSAO},
                    "nota": f"proposta gerada do Termo pelo laço termo → booleano → Consulta; booleano: {t['booleanos'][-1]}"}
        erros = validar_objeto(consulta, esq)
        if erros:
            print(f"Consulta inválida para {t['id']}: {'; '.join(erros)}")
            return 1
        print(f"{t['id']}: {' · '.join(t['booleanos'])}")
        print(json.dumps(consulta, ensure_ascii=False, indent=2))
        if a.gravar:
            p.write_text(json.dumps(t, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            pc = raiz / "ambientes" / "consultas"
            pc.mkdir(parents=True, exist_ok=True)
            (pc / f"{cid}.json").write_text(json.dumps(consulta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if a.gravar and termos:
        (raiz / "acervo" / "termos").mkdir(parents=True, exist_ok=True)
        (raiz / "acervo" / "termos" / "glossario.md").write_text(glossario([t for t, _ in termos], raiz) + "\n", encoding="utf-8")
    print(f"{VERSAO}: {len(termos)} Termo(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
