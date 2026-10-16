"""Confere um ou mais arquivos JSON (ou JSONL, uma linha por objeto) contra um esquema.

Uso:
    python scripts/validar.py <esquema> <arquivo> [<arquivo>...] [--minimo]

<esquema>: nome em esquemas/ (ex.: conferencia, log) ou caminho.
--minimo: força o validador mínimo em Python puro (sem jsonschema).
Saída: "PASSA" ou "REPROVA" por arquivo, com os erros. Código 0 se todos passam, 1 se algum reprova.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import carregar_esquema, validar_objeto  # noqa: E402


def validar_arquivo(caminho: Path, esquema: dict, minimo: bool = False) -> list[str]:
    texto = caminho.read_text(encoding="utf-8")
    if caminho.suffix == ".jsonl":
        erros = []
        for n, linha in enumerate(texto.splitlines(), 1):
            if linha.strip():
                erros += [f"linha {n}: {e}" for e in validar_objeto(json.loads(linha), esquema, minimo)]
        return erros
    return validar_objeto(json.loads(texto), esquema, minimo)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("esquema")
    ap.add_argument("arquivos", nargs="+")
    ap.add_argument("--minimo", action="store_true")
    a = ap.parse_args()
    esquema = carregar_esquema(a.esquema)
    falhou = False
    for arq in a.arquivos:
        try:
            erros = validar_arquivo(Path(arq), esquema, a.minimo)
        except (OSError, json.JSONDecodeError) as e:
            erros = [f"não foi possível ler: {e}"]
        print(f"{'PASSA' if not erros else 'REPROVA'}  {arq}")
        for e in erros:
            print(f"    - {e}")
        falhou |= bool(erros)
    return 1 if falhou else 0


if __name__ == "__main__":
    sys.exit(main())
