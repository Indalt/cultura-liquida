"""Acrescenta uma linha validada ao log de uma Execução: trilhas/logs/AAAA-MM-DD_<agente>.jsonl.

O log completo de agente é gravado pelo curador (sessão principal) depois de cada chamada de Agent,
porque é ele quem recebe os tokens e as chamadas no retorno do Agent (o número oficial; nunca a
soma pelo transcript). Scripts, rotinas e pessoa gravam com `fonte_do_registro` "script", "rotina"
ou "pessoa", sem os campos de agente e com tokens e chamadas null e o motivo.

Uso:
    python scripts/registrar_log.py <arquivo.json>      # um objeto no formato de esquemas/log.schema.json
    python scripts/registrar_log.py -                   # o objeto vem pela entrada padrão
    python scripts/registrar_log.py <arquivo.json> --simular   # valida e mostra, sem gravar

Preenche `data_hora` (hora local, ISO 8601), `fonte_do_registro` ("curador") e o `id` da
Execução (EX-nnnn, o próximo número livre em trilhas/logs/; prefixo provisório até o registro de
valores do bloco 2) se faltarem.
Reprova (código 1, sem gravar) se:
  - o objeto não passa no esquema de log (com id, o alcance é obrigatório: D-030);
  - aparece dado pessoal de terceiros (scripts/procurar_dado_pessoal.py).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, carregar_valores, validar_objeto  # noqa: E402
from procurar_dado_pessoal import achar  # noqa: E402

PASTA_LOGS = RAIZ / "trilhas" / "logs"
_VALORES = carregar_valores()["valores"]
PREFIXO_ID = "EX"  # o prefixo da Execução no registro de valores (prefixos_id; insumo 28)
assert PREFIXO_ID in _VALORES["prefixos_id"]["valor"]["tipos"]
FAIXA = _VALORES["numeracao_id"]["valor"]["faixas"]["conversa"]  # este script grava pela conversa


def proximo_id() -> str:
    """O maior número da faixa da conversa + 1 (registro de valores: numeracao_id)."""
    menor, teto = FAIXA
    maior = menor - 1
    for arq in PASTA_LOGS.glob("*.jsonl"):
        for m in re.finditer(rf'"id": "{PREFIXO_ID}-([0-9]+)"', arq.read_text(encoding="utf-8")):
            if menor <= int(m.group(1)) <= teto:
                maior = max(maior, int(m.group(1)))
    if maior + 1 > teto:
        raise SystemExit(f"faixa da conversa cheia ({menor}-{teto}): faixa nova só por decisão")
    return f"{PREFIXO_ID}-{maior + 1:04d}"


def preparar(entrada: dict) -> dict:
    e = dict(entrada)
    e.setdefault("data_hora", datetime.now().astimezone().isoformat(timespec="seconds"))
    e.setdefault("fonte_do_registro", "curador")
    if e["fonte_do_registro"] != "hook-SubagentStop":
        e.setdefault("id", proximo_id())
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
