"""A pegada reabre se a regra mudar (D-045, item 2; achado A-003 do K-108b).

Relê, pela versão corrente da pré-triagem (`pretriagem.py`), as pegadas "fora do escopo pela regra"
gravadas com outra versão da regra (ou todas, com `--forcar`), com o título e o resumo do cache local
(`metadados.py`, fora do Git) e a Consulta do Recorte de cada pegada:
- se agora segue, o item volta a Entrada de trabalho, com o mesmo EN-nnnn quando a pegada o guardava
  (`deduplicar.registrar`), e a pegada passa a "segue", com o motivo e a versão nova;
- se continua fora, a pegada fica com o motivo e a versão nova (nada se apaga; princípio 10);
- sem metadados no cache, a pegada fica como está, e o relatório o diz.

Uso:
    python scripts/reavaliar_pegadas.py [--forcar] [--simular] [--cache <pasta>] [--raiz <pasta>] [--em-copia]
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from _coleta import Execucao  # noqa: E402
import deduplicar  # noqa: E402
import pretriagem  # noqa: E402
from metadados import ler_cache, pasta_cache  # noqa: E402

VERSAO = "reavaliar-pegadas-0.1"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--forcar", action="store_true", help="relê também as pegadas da versão corrente")
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--cache", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--em-copia", action="store_true")
    ap.add_argument("--entrada-ref", default="reabertura das pegadas pela regra corrente (D-045, item 2)")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    if a.em_copia:
        tmp = tempfile.TemporaryDirectory(prefix="reabrir-")
        copia = Path(tmp.name) / "raiz"
        shutil.copytree(raiz, copia, ignore=shutil.ignore_patterns(".git", ".venv", "legado"))
        raiz = copia
    if a.cache and not a.cache.is_absolute():
        a.cache = RAIZ / a.cache / "metadados"
    gravar = not (a.simular or a.em_copia)
    ex = Execucao("reavaliar-pegadas", a.entrada_ref, simular=not gravar)
    ex.acoes.append("scripts/reavaliar_pegadas.py" + (" --forcar" if a.forcar else "") + (" --simular" if a.simular else ""))
    recortes = {r["id"]: r for r in (carregar_json(f) for f in (raiz / "ambientes" / "recortes").glob("RC-*.json"))}
    ind = deduplicar.Indice(raiz)
    peg = ind.pegadas
    cache: dict[str, dict] = {}
    for am in {r.get("ambiente") for r in recortes.values()}:
        cache.update(ler_cache(pasta_cache(a.cache) / f"{am}.jsonl"))
    reabertas = mantidas = sem_meta = 0
    mudados: set[str] = set()
    for rc, linhas in peg.por_recorte.items():
        for p in linhas:
            if p["triagem"] != pretriagem.FORA or (p["versao_regra"] == pretriagem.VERSAO and not a.forcar):
                continue
            m = cache.get(p["identificador"])
            if not m or rc not in recortes:
                sem_meta += 1
                continue
            r = recortes[rc]
            tri = pretriagem.avaliar(raiz, m.get("titulo"), m.get("resumo"), [r["consulta"]])
            if tri["estado"] == pretriagem.SEGUE:
                ja = ind.achar(p["identificador"], p["link"])
                extra = {} if ja else {"titulo": " ".join((m.get("titulo") or "").split()),
                                       "ano": str(m["ano"])[:4] if m.get("ano") and str(m["ano"])[:4].isdigit() else None,
                                       "pretriagem": {k: tri[k] for k in ("estado", "motivo", "versao_regra")},
                                       "citacao_resumo": tri.get("citacao"), "wayback": p.get("wayback")}
                en, _ = deduplicar.registrar(
                    ind, identificador=p["identificador"], url=p["link"], canal="monitoramento e escavação",
                    origem=ex.origem("scripts/reavaliar_pegadas.py", pretriagem.VERSAO), ambiente=r["ambiente"],
                    recorte=rc, gravar=gravar, id_=p.get("entrada") or peg.en_por_identificador.get(p["identificador"]), extra=extra)
                p.update(triagem=pretriagem.SEGUE, motivo=tri["motivo"], versao_regra=tri["versao_regra"], entrada=en)
                peg.ligar(p["identificador"], en, gravar=False)
                ex.resultados.append(f"{en} reaberta em {rc}: {tri['motivo']}")
                reabertas += 1
            else:
                p.update(motivo=tri["motivo"], versao_regra=tri["versao_regra"])
                mantidas += 1
            mudados.add(rc)
    if gravar:
        for rc in mudados:
            peg.reescrever(rc)
    ex.resultados.insert(0, f"{reabertas} pegada(s) reaberta(s) como Entrada; {mantidas} continuam fora, com a regra {pretriagem.VERSAO}; "
                         f"{sem_meta} sem metadados no cache, como estavam")
    ex.decisoes.append({"item": "reabertura das pegadas fora do escopo", "decisao": "aceito",
                        "motivo": f"regra {pretriagem.VERSAO} (D-045)", "versao_regra": pretriagem.VERSAO})
    ex.olhado.append(f"{peg.total()} pegada(s) em {len(peg.por_recorte)} Recorte(s); cache com {len(cache)} registro(s)")
    if sem_meta:
        ex.fora.append(f"{sem_meta} pegada(s) sem metadados no cache: não relidas")
    for x in ex.resultados:
        print(x)
    print(f"{VERSAO}: {ex.id}; {ex.gravar_log()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
