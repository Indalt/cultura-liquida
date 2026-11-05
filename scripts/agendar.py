"""Agenda das rotinas sem IA (bloco 10a; D-048): o que roda em cada dia, por ambiente.

A D-048 troca o "cada ambiente toda semana" da D-012 por **cada fonte no ritmo que aceita e que rende
novidade, medido pela ferramenta**. A regra (agenda-0.1; os números são provisórios, insumo do K-112):

- **O que a fonte aceita** vem da linha do ambiente em `ambientes/rotinas.json`, tirada da ficha de
  acesso: `cadencia_min_dias` (o menor intervalo; 1 sem limite publicado, maior quando uma passada
  inteira pesa na fonte, como a colheita OAI-PMH) e `cadencia_max_dias` (o maior intervalo, para
  nenhuma fonte ficar esquecida). `teto_chamadas` é o teto da rodada daquele ambiente.
- **O rendimento medido** vem das linhas das rodadas anteriores (`trilhas/relatorios/rodadas.jsonl`,
  uma por ambiente e dia, gravada pela `rotina_diaria.py` com ou sem novidade): o intervalo começa no
  mínimo; uma rodada com novidade (Entrada nova ou pegada nova) o leva de volta ao mínimo; uma rodada
  sem novidade o dobra, até o máximo; uma rodada com erro da fonte o mantém e a repete no dia seguinte.
- O ambiente roda no dia em que `hoje − última rodada ≥ intervalo`. Ambiente sem rodada anterior é
  **porta nova**: só abre com a fila de curadoria abaixo de uma semana (l. 472; `fila_curadoria`).
- Ambiente com `ligado: false` não roda (o motivo fica na linha e no relatório).

Uso:
    python scripts/agendar.py [--data AAAA-MM-DD] [--raiz <pasta>]    # mostra o plano do dia
Importado pela `rotina_diaria.py` (plano(raiz, hoje, fila)).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402

VERSAO = "agenda-0.1"
RODADAS = Path("trilhas") / "relatorios" / "rodadas.jsonl"


def linhas_rotinas(raiz: Path) -> dict[str, dict]:
    arq = raiz / "ambientes" / "rotinas.json"
    cfg = carregar_json(arq) if arq.exists() else {}
    return {k: v for k, v in cfg.items() if k.startswith("AM-")}


def rodadas(raiz: Path) -> list[dict]:
    arq = raiz / RODADAS
    if not arq.exists():
        return []
    return [json.loads(x) for x in arq.read_text(encoding="utf-8").splitlines() if x.strip()]


def intervalo(linha: dict, hist: list[dict]) -> int:
    """O intervalo em dias depois das rodadas dadas (em ordem de data), pela regra agenda-0.1."""
    mini = int(linha.get("cadencia_min_dias", 1))
    maxi = max(mini, int(linha.get("cadencia_max_dias", 28)))
    n = mini
    for r in hist:
        if r.get("erro"):
            continue  # erro da fonte não mede rendimento
        n = mini if (r.get("entradas_novas", 0) or r.get("pegadas_novas", 0)) else min(maxi, n * 2)
    return n


def plano(raiz: Path, hoje: date, fila: int | None = None, fila_max: int = 15) -> list[dict]:
    """Uma linha por ambiente: roda ou não, e por quê."""
    por_amb: dict[str, list[dict]] = {}
    for r in rodadas(raiz):
        por_amb.setdefault(r["ambiente"], []).append(r)
    saida = []
    for am, linha in sorted(linhas_rotinas(raiz).items()):
        hist = sorted(por_amb.get(am, []), key=lambda r: r["data"])
        item = {"ambiente": am, "consultas": linha.get("consultas", []), "teto_chamadas": linha.get("teto_chamadas", 50),
                "roda": False}
        if not linha.get("ligado", False):
            item["motivo"] = f"desligado: {linha.get('motivo', 'sem motivo na linha')}"
        elif not item["consultas"]:
            item["motivo"] = "sem Consulta na linha"
        elif not hist:
            if fila is not None and fila > fila_max:
                item["motivo"] = f"porta nova fechada: fila cheia ({fila} cartões, acima de {fila_max}; l. 472)"
            else:
                item.update(roda=True, motivo="porta nova: primeira rodada", intervalo=int(linha.get("cadencia_min_dias", 1)))
        else:
            n = intervalo(linha, hist)
            ultima = date.fromisoformat(hist[-1]["data"])
            dias = (hoje - ultima).days
            if hist[-1].get("erro") and dias >= 1:
                item.update(roda=True, motivo=f"repete: a última rodada ({ultima}) teve erro da fonte", intervalo=n)
            elif dias >= n:
                item.update(roda=True, motivo=f"intervalo de {n} dia(s) cumprido (última rodada em {ultima})", intervalo=n)
            else:
                item.update(motivo=f"intervalo de {n} dia(s); última rodada em {ultima}; volta em {n - dias} dia(s)", intervalo=n)
        saida.append(item)
    return saida


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data")
    ap.add_argument("--fila", type=int, help="cartões na fila de curadoria (sem ele, não se confere)")
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    hoje = date.fromisoformat(a.data) if a.data else date.today()
    for it in plano(raiz, hoje, a.fila):
        print(f"{it['ambiente']}: {'RODA' if it['roda'] else 'não roda'}; {it['motivo']}")
    print(f"{VERSAO}: plano de {hoje}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
