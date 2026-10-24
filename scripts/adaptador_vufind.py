"""Adaptador VuFind (l. 430): a busca pela API v1 de um catálogo VuFind (no piloto, a BDTD, AM-0021).

Um adaptador por protocolo, não por fonte: um ambiente novo com VuFind entra com uma linha em
`ambientes/adaptadores.json` (base da API, tamanho da página, limite da fonte, se houver).
A Consulta vai como a tradução testada (`ambientes/traducao-consultas.json`, o `lookfor` do pedido
testado), em UTF-8 percent-encoded (com Latin-1 a BDTD ignora a consulta; insumo 41).
Pede só os campos `id`, `urls`, `title`, `publicationDates` e `summary`: nada de autoria (l. 596).
O título e o resumo servem à pré-triagem por regra (D-045; `pretriagem.py`) e ficam na memória; o hash
é a soma SHA-256 do registro de metadados como a fonte o deu.
O período vira o filtro `publishDate:[A TO B]`, quando não é "todo".

pagina(cliente, cfg, consulta, periodo, cursor) → {total_informado, itens, proximo, saturada}
"""
from __future__ import annotations

import hashlib
import json
import urllib.parse

from deduplicar import chave

PROTOCOLO = "vufind"
TIPO = "busca"  # uma busca por Consulta
CAMPOS = ["id", "urls", "title", "publicationDates", "summary"]


def lookfor(traducao: dict) -> str:
    """O `lookfor` do pedido testado na tradução da Consulta para o ambiente."""
    q = urllib.parse.parse_qs(urllib.parse.urlsplit(traducao["pedido"].split(" ", 1)[-1]).query)
    if "lookfor" not in q:
        raise ValueError("a tradução não traz um pedido testado com lookfor")
    return q["lookfor"][0]


def url_pagina(cfg: dict, consulta: str, periodo: str, pagina: int) -> str:
    params = [("lookfor", consulta), ("type", "AllFields"), ("limit", str(cfg.get("pagina", 100))),
              ("page", str(pagina))] + [("field[]", c) for c in CAMPOS]
    if periodo and periodo != "todo":
        a, b = periodo.split("-")
        params.append(("filter[]", f"publishDate:[{a} TO {b}]"))
    return cfg["base"] + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


def pagina(cliente, cfg: dict, ambiente: str, consulta: str, periodo: str, cursor) -> dict:
    p = int(cursor or 1)
    r = cliente.pedir(url_pagina(cfg, consulta, periodo, p))
    if r.status != 200:
        raise RuntimeError(f"HTTP {r.status} na página {p}")
    try:
        dados = r.json()
    except ValueError as e:
        raise RuntimeError(f"resposta não é JSON na página {p}: {e}") from e
    if dados.get("status") != "OK":
        raise RuntimeError(f"status {dados.get('status')!r} na página {p}")
    total = int(dados.get("resultCount", 0))
    itens = []
    for rec in dados.get("records", []):
        urls = [u["url"] for u in rec.get("urls", []) if isinstance(u, dict) and u.get("url")]
        link = next((u for u in urls if "/handle/" in u or "hdl.handle.net" in u or "doi.org" in u), None)
        itens.append({
            "id_fonte": rec["id"],
            "identificador": chave(ambiente, rec["id"], urls),
            "url": link or cfg["registro"].replace("<id>", urllib.parse.quote(rec["id"])),
            "titulo": rec.get("title") or "",
            "resumo": " ".join(rec.get("summary") or []),
            "ano": (rec.get("publicationDates") or [None])[0],
            "hash": hashlib.sha256(json.dumps(rec, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest(),
        })
    tam = int(cfg.get("pagina", 100))
    limite = cfg.get("limite_fonte")
    return {
        "total_informado": total,
        "itens": itens,
        "proximo": p + 1 if p * tam < total and itens else None,
        "saturada": bool(limite and total > limite),
        "curta": bool(p * tam < total and len(itens) < tam),
    }
