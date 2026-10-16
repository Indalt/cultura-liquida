"""Acrescenta uma linha validada ao log de um agente: trilhas/logs/AAAA-MM-DD_<agente>.jsonl.

O log completo é gravado pelo curador (sessão principal) depois de cada chamada de Agent,
porque é ele quem recebe os tokens e as chamadas no retorno do Agent.

Uso:
    python scripts/registrar_log.py <arquivo.json>      # um objeto no formato de esquemas/log.schema.json
    python scripts/registrar_log.py -                   # o objeto vem pela entrada padrão
    python scripts/registrar_log.py <arquivo.json> --simular   # valida e mostra, sem gravar

Preenche `data_hora` (hora local, ISO 8601) e `fonte_do_registro` ("curador") se faltarem.
Reprova (código 1, sem gravar) se:
  - o objeto não passa no esquema de log;
  - aparece dado pessoal de terceiros (scripts/procurar_dado_pessoal.py).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, validar_objeto  # noqa: E402
from procurar_dado_pessoal import achar  # noqa: E402

PASTA_LOGS = RAIZ / "trilhas" / "logs"


def preparar(entrada: dict) -> dict:
    e = dict(entrada)
    e.setdefault("data_hora", datetime.now().astimezone().isoformat(timespec="seconds"))
    e.setdefault("fonte_do_registro", "curador")
    return e


def conferir(e: dict) -> list[str]:
    erros = [f"esquema: {x}" for x in validar_objeto(e, carregar_esquema("log"))]
    texto = json.dumps(e, ensure_ascii=False, indent=0)
    erros += [f"dado pessoal de terceiros: {tipo}: {s}" for _, tipo, s in achar(texto)]
    return erros


def gravar(e: dict) -> Path:
    PASTA_LOGS.mkdir(parents=True, exist_ok=True)
    destino = PASTA_LOGS / f"{e['data_hora'][:10]}_{e['agente']}.jsonl"
    with destino.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
    return destino


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo", help="JSON com a entrada do log, ou - para a entrada padrão")
    ap.add_argument("--simular", action="store_true", help="valida e mostra, sem gravar")
    a = ap.parse_args()
    bruto = sys.stdin.read() if a.arquivo == "-" else Path(a.arquivo).read_text(encoding="utf-8")
    e = preparar(json.loads(bruto))
    erros = conferir(e)
    if erros:
        print("REPROVA: a linha não foi gravada.")
        for x in erros:
            print(f"    - {x}")
        return 1
    if a.simular:
        print("PASSA (simulação, nada gravado)")
        print(json.dumps(e, ensure_ascii=False, indent=2))
        return 0
    destino = gravar(e)
    print(f"PASSA: linha gravada em {destino.relative_to(RAIZ).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
