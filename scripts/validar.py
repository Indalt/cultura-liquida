"""Confere um ou mais arquivos JSON (ou JSONL, uma linha por objeto) contra um esquema.

Uso:
    python scripts/validar.py <esquema> <arquivo> [<arquivo>...] [--minimo]

<esquema>: nome em esquemas/ (ex.: conferencia, log) ou caminho.
<arquivo>: "-" lê um objeto JSON da entrada padrão.
--minimo: força o validador mínimo em Python puro (sem jsonschema).
Além do esquema, aplica as regras entre campos de REGRAS (ex.: total visto x informado).
Saída: "PASSA" ou "REPROVA" por arquivo, com os erros. Código 0 se todos passam, 1 se algum reprova.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import carregar_esquema, validar_objeto  # noqa: E402


def _visto_sem_passar(obj: dict, onde: str) -> list[str]:
    """O total visto nunca passa do informado sem explicação (habilidade consulta; §6, l. 592)."""
    inf, vis = obj.get("total_informado"), obj.get("total_visto")
    if isinstance(inf, int) and isinstance(vis, int) and vis > inf and not obj.get("explicacao_total_visto"):
        return [f"{onde}: total_visto {vis} maior que total_informado {inf} sem explicacao_total_visto"]
    return []


# Regras entre campos, que o JSON Schema não exprime, por $id do esquema.
REGRAS = {
    "recorte.schema.json": lambda o: _visto_sem_passar(o, "(raiz)"),
    "estado-consulta.schema.json": lambda o: [e for i, c in enumerate(o.get("consultas") or []) if isinstance(c, dict)
                                              for e in _visto_sem_passar(c, f"consultas/{i}")],
}


def validar_com_regras(obj, esquema: dict, minimo: bool = False) -> list[str]:
    erros = validar_objeto(obj, esquema, minimo)
    regra = REGRAS.get(esquema.get("$id", ""))
    if regra and isinstance(obj, dict):
        erros += regra(obj)
    return erros


def validar_arquivo(caminho: Path, esquema: dict, minimo: bool = False) -> list[str]:
    texto = caminho.read_text(encoding="utf-8")
    if caminho.suffix == ".jsonl":
        erros = []
        for n, linha in enumerate(texto.splitlines(), 1):
            if linha.strip():
                erros += [f"linha {n}: {e}" for e in validar_com_regras(json.loads(linha), esquema, minimo)]
        return erros
    return validar_com_regras(json.loads(texto), esquema, minimo)


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
            if arq == "-":  # objeto JSON pela entrada padrão (agentes sem Write)
                erros = validar_com_regras(json.loads(sys.stdin.read()), esquema, a.minimo)
            else:
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
