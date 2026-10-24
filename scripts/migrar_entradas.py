"""Migração das Entradas ao formato do K-108b, sem refundar (D-045, item 5).

Para cada Entrada da coleta por programa (canal "monitoramento e escavação"):
1. lê o título, o ano, o resumo e o hash no cache local (`metadados.py`, fora do Git);
2. aplica a pré-triagem por regra (`pretriagem.py`) com as Consultas dos seus Recortes;
3. grava uma pegada por Recorte de origem (`ambientes/pegadas/RC-nnnn.jsonl`), com o mesmo EN-nnnn;
4. a que segue fica em `entrada/`, com o título, o ano, a pré-triagem e a citação curta do resumo;
   a que não segue sai de `entrada/` e fica só como pegada "fora do escopo pela regra", com o
   EN-nnnn e a captura do Wayback, se havia (nunca se apaga o item; princípio 10).
As Entradas de outros canais (busca assistida, link de Vicente) não passam pela regra.

Conferência por script, no fim: a contagem e o conjunto de EN-nnnn antes e depois (Entradas + EN só
em pegada) são iguais; `validar_acervo.py` e `deduplicar.py --conferir` passam. Se algo falha, o
script diz e devolve 1 (o Git guarda o estado de antes).

Uso:
    python scripts/migrar_entradas.py [--simular] [--cache <pasta>] [--raiz <pasta>] [--em-copia]
    (--em-copia: roda numa cópia temporária da raiz, para os testes; a raiz fica intacta)
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from _coleta import Execucao, gravar_json  # noqa: E402
import deduplicar  # noqa: E402
import pretriagem  # noqa: E402
import validar_acervo  # noqa: E402
from guarda import Pegadas  # noqa: E402
from metadados import ler_cache, pasta_cache  # noqa: E402

VERSAO = "migrar-entradas-0.1"
CANAL_COLETA = "monitoramento e escavação"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--cache", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--em-copia", action="store_true")
    ap.add_argument("--entrada-ref", default="K-108b, migração das Entradas sem refundar (D-045, item 5)")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    if a.em_copia:  # cópia que se apaga no fim, sem .git, .venv e legado/ (A-002)
        tmp = tempfile.TemporaryDirectory(prefix="migracao-")
        copia = Path(tmp.name) / "raiz"
        shutil.copytree(raiz, copia, ignore=shutil.ignore_patterns(".git", ".venv", "legado"))
        raiz = copia
    if a.cache and not a.cache.is_absolute():
        a.cache = RAIZ / a.cache / "metadados"
    ex = Execucao("migrar-entradas", a.entrada_ref, simular=a.simular or a.em_copia)
    ex.acoes.append("scripts/migrar_entradas.py" + (" --simular" if a.simular else ""))
    arqs = sorted((raiz / "entrada").glob("EN-*.json"))
    ents = {f: carregar_json(f) for f in arqs}
    antes = {e["id"] for e in ents.values()}
    consulta_do = {r["id"]: r["consulta"] for r in (carregar_json(f) for f in (raiz / "ambientes" / "recortes").glob("RC-*.json"))}
    cache: dict[str, dict] = {}
    for am in {e.get("ambiente") for e in ents.values() if e.get("ambiente")}:
        cache.update(ler_cache(pasta_cache(a.cache) / f"{am}.jsonl"))
    peg = Pegadas(raiz)
    esq = carregar_esquema("entrada")
    segue = fora = sem_meta = outros = 0
    por_motivo: dict[str, int] = {}
    for f, e in ents.items():
        if e.get("retirado") or e.get("canal") != CANAL_COLETA:
            outros += 1
            continue
        m = cache.get(e.get("identificador"))
        cos = list(dict.fromkeys(consulta_do[rc] for rc in e.get("recortes", []) if rc in consulta_do))
        if m:
            tri = pretriagem.avaliar(raiz, m.get("titulo"), m.get("resumo"), cos)
        else:
            sem_meta += 1
            tri = {"estado": pretriagem.SEGUE, "motivo": "sem registro de metadados na fonte: a regra não decide sem texto",
                   "versao_regra": pretriagem.VERSAO}
        chave_motivo = tri["motivo"].split(" (")[0] if tri["estado"] == pretriagem.SEGUE else pretriagem.FORA
        por_motivo[chave_motivo] = por_motivo.get(chave_motivo, 0) + 1
        id_fonte = (m or {}).get("id_fonte") or e["identificador"].split(":", 1)[-1]
        for rc in e.get("recortes", []):
            linha = {"id_fonte": str(id_fonte).replace(" ", "_"), "identificador": e["identificador"], "link": e["url_ou_arquivo"],
                     "data": e["data_entrada"], "hash": (m or {}).get("hash"), "triagem": tri["estado"],
                     "motivo": tri["motivo"], "versao_regra": tri["versao_regra"], "entrada": e["id"]}
            if tri["estado"] == pretriagem.FORA and e.get("wayback"):
                linha["wayback"] = e["wayback"]
            peg.acrescentar(rc, linha, gravar=not a.simular)
        if tri["estado"] == pretriagem.SEGUE:
            segue += 1
            if m:
                if m.get("titulo"):
                    e["titulo"] = " ".join(m["titulo"].split())
                if m.get("ano") and str(m["ano"])[:4].isdigit():
                    e["ano"] = str(m["ano"])[:4]
            e["pretriagem"] = {k: tri[k] for k in ("estado", "motivo", "versao_regra")}
            if tri.get("citacao"):
                e["citacao_resumo"] = tri["citacao"]
            erros = validar_objeto(e, esq)
            if erros:
                ex.erros.append(f"{e['id']}: {'; '.join(erros)}")
                continue
            if not a.simular:
                gravar_json(f, e)
        else:
            fora += 1
            if not a.simular:
                f.unlink()
    depois_ent = {carregar_json(f)["id"] for f in (raiz / "entrada").glob("EN-*.json")} if not a.simular else antes - {
        e["id"] for e in ents.values() if False}
    depois = (depois_ent | Pegadas(raiz).ens) if not a.simular else antes
    ex.resultados.append(f"{len(antes)} Entradas antes: {segue} seguem, {fora} só como pegada ({pretriagem.FORA}), "
                         f"{outros} de outros canais; {sem_meta} sem metadados seguiram")
    for k, v in sorted(por_motivo.items(), key=lambda x: -x[1]):
        ex.resultados.append(f"  {v}: {k}")
    falhas = []
    if not a.simular:
        if depois != antes:
            falhas.append(f"EN-nnnn diferentes: faltam {sorted(antes - depois)[:10]}, sobram {sorted(depois - antes)[:10]}")
        if len(depois_ent) != segue + outros:
            falhas.append(f"Entradas de trabalho: {len(depois_ent)}, esperadas {segue + outros}")
        erros_acervo = validar_acervo.validar(raiz)
        falhas += [f"validar_acervo: {x}" for x in erros_acervo[:10]]
        ind = deduplicar.Indice(raiz)
        falhas += [f"deduplicação: {x}" for x in (ind.duplicatas + deduplicar.conferir_pegadas(ind))[:10]]
        ex.resultados.append(f"conferência: {len(antes)} EN-nnnn antes e {len(depois)} depois (Entradas {len(depois_ent)} + só em pegada "
                             f"{len(depois - depois_ent)}); validar_acervo e deduplicação {'OK' if not falhas else 'com falha'}")
    ex.erros += falhas
    ex.decisoes.append({"item": "pré-triagem das Entradas migradas", "decisao": "aceito",
                        "motivo": f"regra {pretriagem.VERSAO} (D-045)", "versao_regra": pretriagem.VERSAO})
    ex.olhado.append(f"{len(antes)} Entradas de entrada/ e o cache local de metadados ({len(cache)} registros)")
    if sem_meta:
        ex.fora.append(f"{sem_meta} Entrada(s) sem registro de metadados na fonte, que seguiram sem a regra")
    for x in ex.resultados:
        print(x)
    for x in ex.erros[:20]:
        print("ERRO", x)
    print(f"{VERSAO}: {ex.id}; {ex.gravar_log()}")
    return 1 if ex.erros else 0


if __name__ == "__main__":
    sys.exit(main())
