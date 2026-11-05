"""Feed de novidades por ID não visto (Fundação l. 428; bloco 10a): o Atom das Entradas novas, em
`entrada/feed.xml`, gerado por script próprio, sem servidor de RSS de terceiros.

**Novidade é um ID ainda não visto, nunca uma data** (l. 428): a Entrada só existe quando o
identificador dela não estava no índice (`deduplicar.py`). O feed traz as últimas Entradas pela ordem
de chegada (data de entrada e ID), com o título, o link e a Consulta de origem (os Recortes); nada de
autoria (l. 596). Só se regrava quando há Entrada nova no dia (D-048: só grava com novidade).

Uso:
    python scripts/feed.py [--data AAAA-MM-DD] [--max 100] [--forcar] [--raiz <pasta>]
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402

VERSAO = "feed-0.1"
REPO = "https://github.com/Indalt/cultura-liquida"


def consultas_dos_recortes(raiz: Path) -> dict[str, str]:
    pasta = raiz / "ambientes" / "recortes"
    return {r["id"]: r.get("consulta", "?") for r in (carregar_json(a) for a in pasta.glob("*.json"))} if pasta.exists() else {}


def montar(raiz: Path, maximo: int, hoje: str) -> tuple[str, int]:
    ents = [carregar_json(a) for a in (raiz / "entrada").glob("EN-*.json")]
    novas_hoje = sum(1 for e in ents if e.get("data_entrada") == hoje)
    ents.sort(key=lambda e: (e.get("data_entrada", ""), int(e["id"].split("-")[1])), reverse=True)
    co = consultas_dos_recortes(raiz)
    ln = ['<?xml version="1.0" encoding="utf-8"?>', '<feed xmlns="http://www.w3.org/2005/Atom">',
          "  <title>Cultura Líquida — Entradas novas</title>", f"  <id>{REPO}/blob/main/entrada/feed.xml</id>",
          f'  <link href="{REPO}/tree/main/entrada"/>', f"  <updated>{hoje}T00:00:00Z</updated>",
          f"  <generator>scripts/feed.py ({VERSAO})</generator>"]
    for e in ents[:maximo]:
        origem = sorted({co.get(r, "?") for r in e.get("recortes", [])})
        resumo = f"{e.get('ambiente', 'sem ambiente')}; canal {e.get('canal')}; Consulta de origem: {', '.join(origem) or 'nenhuma'}"
        ln += ["  <entry>", f"    <id>{REPO}/blob/main/entrada/{e['id']}.json</id>",
               f"    <title>{escape(e['id'] + ' — ' + (e.get('titulo') or 'sem título'))}</title>",
               f'    <link href="{escape(str(e.get("url_ou_arquivo", "")))}"/>',
               f"    <updated>{e.get('data_entrada', hoje)}T00:00:00Z</updated>",
               f"    <summary>{escape(resumo)}</summary>", "  </entry>"]
    ln.append("</feed>")
    return "\n".join(ln) + "\n", novas_hoje


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data")
    ap.add_argument("--max", type=int, default=100)
    ap.add_argument("--forcar", action="store_true", help="regrava mesmo sem Entrada nova no dia")
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    hoje = a.data or date.today().isoformat()
    texto, novas = montar(raiz, a.max, hoje)
    arq = raiz / "entrada" / "feed.xml"
    if novas or a.forcar or not arq.exists():
        arq.parent.mkdir(parents=True, exist_ok=True)
        arq.write_text(texto, encoding="utf-8")
        print(f"{VERSAO}: {novas} Entrada(s) nova(s) em {hoje}; entrada/feed.xml regravado")
    else:
        print(f"{VERSAO}: nenhuma Entrada nova em {hoje}; feed sem mudança")
    return 0


if __name__ == "__main__":
    sys.exit(main())
