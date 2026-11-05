"""Checagem de links das Entradas (bloco 10a): uma amostra por dia, em rodízio, para achar o link que
deixou de abrir.

- A amostra do dia: as Entradas com link http, em ordem de ID, a partir de um ponto que anda com o
  dia (rodízio): em N dias, todo link passa pela checagem.
- O pedido usa o mesmo cliente da coleta (`_coleta.Cliente`): robô identificado, robots.txt e 1 pedido
  por segundo. Proteção anti-robô (403, captcha) não é link quebrado nem se contorna: fica como
  "barrado ao robô". O robots.txt que veda o caminho também: "não conferido pelo robots.txt".
- **Só grava com novidade (D-048):** o link que respondeu 404, 410 ou erro de rede entra numa linha de
  `trilhas/relatorios/links-quebrados.jsonl` só quando ainda não estava lá; o resto vai à saída, que o
  relatório do dia mostra.
A cópia no Wayback de um link quebrado não se busca aqui: é o `ler_fonte.py` que a usa, quando precisa
ler a fonte (D-048).

Uso:
    python scripts/verificar_links.py [--max 20] [--data AAAA-MM-DD] [--fixtures <pasta>] [--raiz <pasta>]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from _coleta import BloqueioAntiRobo, BloqueioRobos, Cliente  # noqa: E402

VERSAO = "links-0.1"
QUEBRADOS = Path("trilhas") / "relatorios" / "links-quebrados.jsonl"


def amostra(raiz: Path, maximo: int, hoje: date) -> list[dict]:
    ents = sorted((carregar_json(a) for a in (raiz / "entrada").glob("EN-*.json")), key=lambda e: int(e["id"].split("-")[1]))
    ents = [e for e in ents if str(e.get("url_ou_arquivo", "")).startswith("http")]
    if not ents or maximo <= 0:
        return []
    ini = (hoje.toordinal() * maximo) % len(ents)
    return [ents[(ini + i) % len(ents)] for i in range(min(maximo, len(ents)))]


def conferir(cli: Cliente, url: str) -> tuple[str, str]:
    try:
        r = cli.pedir(url, metodo="GET")
    except BloqueioAntiRobo as e:
        return "barrado ao robô", str(e)
    except BloqueioRobos as e:
        return "não conferido pelo robots.txt", str(e)
    except Exception as e:  # rede, DNS, tempo
        return "quebrado", f"{type(e).__name__}: {e}"[:300]
    if r.status in (404, 410):
        return "quebrado", f"HTTP {r.status}"
    if r.status >= 400:
        return "erro da fonte", f"HTTP {r.status}"
    return "abre", f"HTTP {r.status}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max", type=int, default=20)
    ap.add_argument("--data")
    ap.add_argument("--fixtures", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    hoje = date.fromisoformat(a.data) if a.data else date.today()
    cli = Cliente(fixtures=a.fixtures)
    arq = raiz / QUEBRADOS
    ja = {json.loads(x)["entrada"] for x in arq.read_text(encoding="utf-8").splitlines() if x.strip()} if arq.exists() else set()
    contagem: dict[str, int] = {}
    novos = []
    for e in amostra(raiz, a.max, hoje):
        estado, detalhe = conferir(cli, e["url_ou_arquivo"])
        contagem[estado] = contagem.get(estado, 0) + 1
        if estado == "quebrado" and e["id"] not in ja:
            novos.append({"data": hoje.isoformat(), "entrada": e["id"], "url": e["url_ou_arquivo"], "detalhe": detalhe, "versao": VERSAO})
        print(f"{e['id']}: {estado} ({detalhe})")
    if novos:
        arq.parent.mkdir(parents=True, exist_ok=True)
        with arq.open("a", encoding="utf-8", newline="\n") as f:
            for x in novos:
                f.write(json.dumps(x, ensure_ascii=False) + "\n")
    resumo = ", ".join(f"{k} {v}" for k, v in sorted(contagem.items())) or "nenhum link"
    print(f"{VERSAO}: {sum(contagem.values())} link(s) conferido(s): {resumo}; {len(novos)} quebrado(s) novo(s); {cli.pedidos} pedido(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
