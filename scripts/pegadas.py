"""Matriz de Pegadas e Vácuos (l. 416; P89): gerada das Execuções e dos Recortes, com todos os
critérios menos o tempo (ambiente × Consulta × período × modo), para que, ao voltar ao mesmo local e
período, se pegue o que ainda não foi visto.

- **Pegada:** só a passada completa e não saturada ("percorrido pela busca" ou "lido por inteiro").
- **Vácuo de busca:** a combinação ambiente × Consulta das fontes do piloto (linhas de
  `ambientes/adaptadores.json` × `ambientes/consultas/`) sem pegada, com o porquê (não rodado,
  em curso, interrompido por teto, via humana). Não se confunde com os vácuos de conhecimento da
  matriz X×Y (§5.7), que são do grafo.
- A última Execução de cada Recorte vem dos logs (`trilhas/logs/*.jsonl`, campo `recortes`).

Uso:
    python scripts/pegadas.py [--saida <arquivo.md>] [--raiz <pasta>]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402

VERSAO = "pegadas-0.1"
FINAIS = ("percorrido pela busca", "lido por inteiro")


def ultimas_execucoes(raiz: Path) -> dict[str, str]:
    saida: dict[str, str] = {}
    for arq in sorted((raiz / "trilhas" / "logs").glob("*.jsonl")) if (raiz / "trilhas" / "logs").exists() else []:
        for ln in arq.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(ln)
            except json.JSONDecodeError:
                continue
            for rc in e.get("recortes", []) or []:
                saida[rc] = f"{e.get('id', '?')} ({str(e.get('data_hora', ''))[:10]})"
    return saida


def matriz(raiz: Path) -> tuple[list[dict], list[str]]:
    rcs = [carregar_json(a) for a in sorted((raiz / "ambientes" / "recortes").glob("*.json"))] \
        if (raiz / "ambientes" / "recortes").exists() else []
    rcs = [r for r in rcs if not r.get("retirado")]
    ex = ultimas_execucoes(raiz)
    for r in rcs:
        r["_execucao"] = ex.get(r["id"], r.get("origem_registro", {}).get("execucao", "?"))
    cfg_arq = raiz / "ambientes" / "adaptadores.json"
    cfg = {k: v for k, v in carregar_json(cfg_arq).items() if k.startswith("AM-")} if cfg_arq.exists() else {}
    cons = sorted(p.stem for p in (raiz / "ambientes" / "consultas").glob("CO-*.json")) \
        if (raiz / "ambientes" / "consultas").exists() else []
    vacuos = []
    for am, c in sorted(cfg.items()):
        for co in cons:
            doam = [r for r in rcs if r.get("ambiente") == am and r.get("consulta") == co]
            if any(r["estado"] in FINAIS for r in doam):
                continue
            if c.get("adaptador") == "assistido" and not doam:
                motivo = f"via humana (modo assistido): {c.get('motivo', '')}"
            elif not doam:
                motivo = "não rodado"
            else:
                motivo = "; ".join(f"{r['id']} {r['estado']} ({r.get('proxima_acao', '')})" for r in doam)
            vacuos.append(f"{am} × {co}: {motivo}")
    return rcs, vacuos


def texto(rcs: list[dict], vacuos: list[str]) -> str:
    ls = ["# Matriz de Pegadas e Vácuos", "",
          f"Gerada por `scripts/pegadas.py` ({VERSAO}) das Execuções e dos Recortes; todos os critérios menos o tempo (l. 416).", "",
          "| Recorte | Ambiente | Consulta | Período | Modo | Estado | Visto / informado | Pegada | Última Execução |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rcs, key=lambda r: (r.get("ambiente", ""), r.get("consulta", ""), r.get("periodo", ""))):
        ls.append(f"| {r['id']} | {r.get('ambiente')} | {r.get('consulta')} | {r.get('periodo', 'todo')} | {r.get('modo')} | "
                  f"{r['estado']} | {r.get('total_visto')} / {r.get('total_informado') if r.get('total_informado') is not None else '?'} | "
                  f"{'sim' if r['estado'] in FINAIS else 'não'} | {r['_execucao']} |")
    if not rcs:
        ls.append("| (nenhum Recorte) | | | | | | | | |")
    ls += ["", f"## Vácuos de busca ({len(vacuos)})", ""] + [f"- {v}" for v in vacuos or ["nenhum"]]
    return "\n".join(ls) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--saida", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    rcs, vacuos = matriz(raiz)
    t = texto(rcs, vacuos)
    if a.saida:
        s = a.saida if a.saida.is_absolute() else RAIZ / a.saida
        s.parent.mkdir(parents=True, exist_ok=True)
        s.write_text(t, encoding="utf-8")
    print(t)
    print(f"{VERSAO}: {len(rcs)} Recorte(s), {sum(r['estado'] in FINAIS for r in rcs)} pegada(s), {len(vacuos)} vácuo(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
