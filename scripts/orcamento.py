"""Conta do orçamento antes de abrir um agente (brief, regra 2; D-023).

Regras:
  1. consumido + estimativa <= teto;
  2. não abrir lote se a folga (teto - consumido) for menor que 2x o maior lote já medido.

Uso:
    python scripts/orcamento.py --teto 300000 --medidos 81852 77351 --estimativa 60000
    (--medidos: consumo de cada agente já rodado na semana; vazio na primeira vez)
    Sem --teto e sem --estimativa, valem os do registro de valores provisórios
    (esquemas/valores-provisorios.json, orcamento): 300 mil por semana e 60 mil.
Código 0 = PODE abrir; 1 = PARAR (com o estado salvo).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import carregar_valores  # noqa: E402


def conta(teto: int, medidos: list[int], estimativa: int) -> tuple[bool, list[str]]:
    consumido = sum(medidos)
    folga = teto - consumido
    maior = max(medidos) if medidos else 0
    linhas = [
        f"consumido = {consumido:,}".replace(",", "."),
        f"folga = {teto:,} - {consumido:,} = {folga:,}".replace(",", "."),
        f"consumido + estimativa = {consumido + estimativa:,} (teto {teto:,})".replace(",", "."),
        f"2x maior lote medido = {2 * maior:,}".replace(",", "."),
    ]
    ok1 = consumido + estimativa <= teto
    ok2 = folga >= 2 * maior
    if not ok1:
        linhas.append("regra 1 falhou: a estimativa não cabe no teto")
    if not ok2:
        linhas.append("regra 2 falhou: folga menor que 2x o maior lote")
    return ok1 and ok2, linhas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    orc = carregar_valores()["valores"]["orcamento"]["valor"]  # registro de valores provisórios
    ap.add_argument("--teto", type=int, default=orc["teto_semanal"])
    ap.add_argument("--medidos", type=int, nargs="*", default=[])
    ap.add_argument("--estimativa", type=int, default=orc["estimativa_sem_medida"])
    a = ap.parse_args()
    pode, linhas = conta(a.teto, a.medidos, a.estimativa)
    for l in linhas:
        print(l)
    print("PODE abrir o agente" if pode else "PARAR: salvar o estado e encerrar a janela")
    return 0 if pode else 1


if __name__ == "__main__":
    sys.exit(main())
