"""Teste da ficha de acesso no lugar de execução (bloco 10a; l. 418): antes de ligar um ambiente na
rotina, o mesmo pedido de teste roda na máquina do GitHub Actions (outro endereço de rede) e o resultado
entra na ficha. Resultado diferente do da conversa entra na ficha e, se barrar, o ambiente fica fora da
rotina (via assistida ou a Falta "fonte inacessível"; l. 419).

O pedido de teste de cada ambiente vem de `ambientes/adaptadores.json` (campo `teste`) ou, sem ele, do
protocolo: VuFind, a busca com `limit=0`; OAI-PMH, o verbo `Identify`. O cliente é o da coleta (robô
identificado, robots.txt, 1 pedido por segundo); proteção anti-robô não se contorna, só se anota.

Uso:
    python scripts/testar_no_runner.py [--ambientes AM-0021,AM-0029] --saida resultado.json   # no runner
    python scripts/testar_no_runner.py --registrar resultado.json --execucao-actions <url>     # na conversa
"""
from __future__ import annotations

import argparse
import json
import platform
import socket
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from _coleta import BloqueioAntiRobo, BloqueioRobos, Cliente, gravar_json  # noqa: E402

VERSAO = "teste-runner-0.1"


def pedido_de_teste(cfg: dict) -> str | None:
    if cfg.get("teste"):
        return cfg["teste"]
    if cfg["adaptador"] == "vufind":
        return cfg["base"] + "?lookfor=cajuina&type=AllFields&limit=0"
    if cfg["adaptador"] == "oai-pmh":
        return cfg["base"] + "?verb=Identify"
    return None


def testar(cli: Cliente, am: str, cfg: dict) -> dict:
    url = pedido_de_teste(cfg)
    r = {"ambiente": am, "data": date.today().isoformat(), "pedido": f"GET {url}" if url else "nenhum"}
    if not url:
        r["resposta"] = f"sem pedido de teste para o adaptador {cfg['adaptador']!r}"
        return r
    try:
        resp = cli.pedir(url)
        r["resposta"] = f"HTTP {resp.status}; {len(resp.bruto)} bytes; início: {resp.corpo[:160]!r}"
        r["abre"] = resp.status < 400
    except (BloqueioAntiRobo, BloqueioRobos) as e:
        r["resposta"], r["abre"] = str(e), False
    except Exception as e:
        r["resposta"], r["abre"] = f"{type(e).__name__}: {e}"[:300], False
    return r


def registrar(arq: Path, execucao: str) -> None:
    dados = carregar_json(arq)
    for r in dados["resultados"]:
        f = RAIZ / "ambientes" / f"{r['ambiente']}.json"
        am = carregar_json(f)
        t = am["ficha_de_acesso"]["teste"]
        nota = (f"Teste no runner do GitHub Actions em {r['data']} ({execucao}; {dados.get('maquina', '')}): "
                f"{r['pedido']} → {r['resposta']}")
        t["observacao"] = (t.get("observacao", "") + " " + nota).strip()
        gravar_json(f, am)
        print(f"{r['ambiente']}: {'abre' if r.get('abre') else 'NÃO ABRE'} no runner")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ambientes")
    ap.add_argument("--saida", type=Path)
    ap.add_argument("--registrar", type=Path)
    ap.add_argument("--execucao-actions", default="execução do Actions")
    a = ap.parse_args()
    if a.registrar:
        registrar(a.registrar, a.execucao_actions)
        return 0
    cfgs = {k: v for k, v in carregar_json(RAIZ / "ambientes" / "adaptadores.json").items()
            if k.startswith("AM-") and v.get("adaptador") != "assistido"}
    if a.ambientes:
        cfgs = {k: v for k, v in cfgs.items() if k in set(a.ambientes.split(","))}
    cli = Cliente()
    res = [testar(cli, am, cfg) for am, cfg in sorted(cfgs.items())]
    saida = {"versao": VERSAO, "maquina": f"{platform.system()} {platform.release()}; {socket.gethostname()}",
             "resultados": res}
    for r in res:
        print(f"{r['ambiente']}: {r['pedido']} → {r['resposta']}")
    if a.saida:
        a.saida.write_text(json.dumps(saida, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
