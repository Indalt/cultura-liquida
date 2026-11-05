"""Do Termo, os booleanos, o glossário e os links; fecha o laço termo → booleano → Consulta
nova (bloco 3; princípio 2, l. 103-105). Regra termo-0.2 (K-106, insumo 30: a designação é
um objeto com a forma e, quando a fonte a der, a língua; o booleano não muda).

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

Consultas gerais (--gerais; regra consultas-gerais-0.1; bloco 10a, l. 361; K-112): tira do acervo do
piloto, sem IA, os descritores processuais e propõe as Consultas por que a ferramenta acha CLB que não
são as do piloto (princípios 2 e 7; D-032, D-039):
  - descritores processuais: o `tipo` de cada Processo (Y) que tem Proposição, menos os genéricos da
    regra (P3: coleta, circulação, adição), e o `tipo` de cada Insumo (X) que nomeia um processo
    ("agente de <processo>" dá "<processo>", se já não estiver);
  - a classe: "bebida", o que toda CLB é (Fundação, §1);
  - Consulta só por descritores: a classe (em `variantes`) E um dos descritores (o filtro local da
    colheita e a tradução de cada ambiente pedem os dois);
  - Consulta mista de CLB em geral: para cada Termo atestado que não é do piloto (--termos-piloto), as
    formas dele E os descritores; hoje nenhum (as CLB de outro termo nascem candidatas, D-039, e entram
    aqui quando atestadas).
  Consulta igual a uma já gravada (mesmos termos, variantes e descritores) não se repete.

Uso:
    python scripts/gerar_termo.py --gerais [--termos-piloto TE-0001,TE-0002] [--execucao EX-nnnn] [--gravar]
    python scripts/gerar_termo.py [<termo.json> ...] [--raiz <pasta>] [--descritores "a,b"] \\
        [--execucao EX-nnnn] [--gravar]
Código 0 = gerado; 1 = Termo com problema (nada é gravado).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, prefixo, proximo_id  # noqa: E402
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from validar_acervo import checar_termo  # noqa: E402

VERSAO = "termo-0.2"
VERSAO_GERAIS = "consultas-gerais-0.1"
GENERICOS = {"coleta", "circulação", "adição"}  # tipos de Processo genéricos demais para descritor (P3)
CLASSE = "bebida"  # o que toda CLB é (Fundação, §1)


def designacoes(t: dict) -> list[str]:
    return [d["forma"] for d in t.get("designacoes", [])]


def rotulo(d: dict) -> str:
    return f"{d['forma']} ({d['lingua']})" if d.get("lingua") else d["forma"]


def formas(t: dict) -> list[str]:
    vistos, saida = set(), []
    for f in designacoes(t) + [v["forma"] for v in t.get("variantes", [])] + t.get("formas_de_busca", []):
        if f.casefold() not in vistos:
            vistos.add(f.casefold())
            saida.append(f)
    return saida


def booleanos(t: dict, descritores: list[str]) -> list[str]:
    grupo = " OR ".join('"' + f.replace('"', '\\"') + '"' for f in formas(t))  # aspas internas escapadas
    grupo = f"({grupo})"
    saida = [grupo]
    if descritores:
        saida.append(f"{grupo} AND ({' OR '.join(d if ' ' not in d else f'\"{d}\"' for d in descritores)})")
    return saida


def glossario(termos: list[dict], raiz: Path) -> str:
    ln = [f"# Glossário (gerado por scripts/gerar_termo.py; {VERSAO})", ""]
    for t in sorted(termos, key=lambda x: designacoes(x)[0].casefold()):
        ln += [f"## {designacoes(t)[0]} ({t['id']}, {t['estado']})", "", t["conceito"], ""]
        if len(t["designacoes"]) > 1 or t["designacoes"][0].get("lingua"):
            ln.append(f"- **Designações:** {', '.join(rotulo(d) for d in t['designacoes'])}")
        for v in t.get("variantes", []):
            extra = "; ".join(x for x in [", ".join(v.get("lugares", [])), v.get("periodo", ""),
                                           ", ".join(v.get("abonacoes", []))] if x)
            lingua = f"; {v['lingua']}" if v.get("lingua") else ""
            ln.append(f"- **Variante:** {v['forma']} ({v['tipo_variacao']}{lingua}{'; ' + extra if extra else ''})")
        if t.get("formas_de_busca"):
            ln.append(f"- **Formas de busca (só no booleano):** {', '.join(t['formas_de_busca'])}")
        if t.get("abonacoes"):
            ln.append(f"- **Abonações:** {', '.join(f'[{e}](evidencias/{e}.json)' for e in t['abonacoes'])}")
        for r in t.get("relacoes", []):
            ln.append(f"- **{r['tipo'].capitalize()}:** [{r['termo']}]({r['termo']}.json)")
        ln.append(f"- **Booleanos:** {' · '.join(f'`{b}`' for b in t.get('booleanos', []))}")
        ln.append("")
    return "\n".join(ln)


def descritores_processuais(indice: dict) -> list[str]:
    ds: list[str] = []
    for i, r in sorted(indice.items()):
        if prefixo(i) == "PC" and r.get("proposicoes") and not r.get("retirado"):
            t = (r.get("tipo") or "").strip()
            if t and t.casefold() not in GENERICOS:
                ds.append(t)
    for i, r in sorted(indice.items()):
        if prefixo(i) == "IN" and not r.get("retirado"):
            m = re.match(r"agente de (.+)$", (r.get("tipo") or "").strip(), re.I)
            if m:
                ds.append(m.group(1))
    return list(dict.fromkeys(ds))


def consultas_gerais(indice: dict, piloto: set[str], execucao: str) -> list[dict]:
    ds = descritores_processuais(indice)
    origem = {"criado_por": "scripts/gerar_termo.py --gerais", "data": date.today().isoformat(),
              "execucao": execucao, "versao_regra": VERSAO_GERAIS}
    bool_ds = " OR ".join(d if " " not in d else f'"{d}"' for d in ds)
    saida = [{"nome": f"{c} + descritores processuais do piloto (só descritores)", "tipo": "só descritores",
              "variantes": [c], "descritores": ds, "origem_registro": origem,
              "nota": f"Consulta geral ({VERSAO_GERAIS}): a classe E um descritor; booleano: \"{c}\" AND ({bool_ds})"}
             for c in [CLASSE]]
    for i, t in sorted(indice.items()):
        if prefixo(i) == "TE" and t.get("estado") == "atestado" and i not in piloto and not t.get("retirado"):
            saida.append({"nome": f"{designacoes(t)[0]} + descritores processuais do piloto ({i})", "tipo": "mista",
                          "termos": [i], "variantes": [f for f in formas(t) if f not in designacoes(t)],
                          "descritores": ds, "origem_registro": origem,
                          "nota": f"Consulta geral ({VERSAO_GERAIS}), mista de CLB de outro termo; booleano: {booleanos(t, ds)[-1]}"})
    return saida


def gerais(a, raiz: Path, indice: dict) -> int:
    piloto = {x.strip() for x in a.termos_piloto.split(",") if x.strip()}
    pasta = raiz / "ambientes" / "consultas"
    existentes = [carregar_json(p) for p in pasta.glob("CO-*.json")] if pasta.exists() else []

    def chave(c: dict) -> tuple:
        return tuple(c.get("termos", [])), tuple(c.get("variantes", [])), tuple(c.get("descritores", []))

    ja = {chave(c) for c in existentes}
    ids = set(indice) | {c["id"] for c in existentes}
    esq = carregar_esquema("consulta")
    novas = 0
    for c in consultas_gerais(indice, piloto, a.execucao):
        if chave(c) in ja:
            print(f"já gravada: {c['nome']}")
            continue
        cid = proximo_id("CO", ids)
        ids.add(cid)
        c = {"id": cid, **c, "traducao": f"ambientes/traducao-consultas.json#{cid}"}
        erros = validar_objeto(c, esq)
        if erros:
            print(f"Consulta inválida ({c['nome']}): {'; '.join(erros)}")
            return 1
        print(json.dumps(c, ensure_ascii=False, indent=2))
        novas += 1
        if a.gravar:
            pasta.mkdir(parents=True, exist_ok=True)
            (pasta / f"{cid}.json").write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{VERSAO_GERAIS}: {novas} Consulta(s) geral(is) nova(s){' gravada(s)' if a.gravar else ' (proposta, sem --gravar)'}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("termos", nargs="*", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--descritores", default="")
    ap.add_argument("--execucao", default="EX-0000")
    ap.add_argument("--gravar", action="store_true")
    ap.add_argument("--gerais", action="store_true", help="propõe as Consultas gerais (consultas-gerais-0.1)")
    ap.add_argument("--termos-piloto", default="TE-0001,TE-0002")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    indice, onde, _ = carregar_acervo(raiz)
    if a.gerais:
        return gerais(a, raiz, indice)
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
        consulta = {"id": cid, "nome": f"{designacoes(t)[0]}{' + descritores' if descr else ''} ({t['id']})",
                    "tipo": "mista" if descr else "termo", "termos": [t["id"]],
                    "variantes": [f for f in formas(t) if f not in designacoes(t)], "descritores": descr,
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
        gerados = {t["id"]: t for t, _ in termos}  # o glossário é sempre do acervo inteiro (achado A-007)
        todos = {i: r for i, r in indice.items() if prefixo(i) == "TE" and not r.get("retirado")} | gerados
        (raiz / "acervo" / "termos" / "glossario.md").write_text(glossario(list(todos.values()), raiz) + "\n", encoding="utf-8")
    print(f"{VERSAO}: {len(termos)} Termo(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
