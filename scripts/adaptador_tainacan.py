"""Adaptador Tainacan (l. 430; K-112, insumo 73): a busca pela API REST do Tainacan, o repositório em
WordPress que o IPHAN usa no Banco de Bens Culturais Registrados (BCR, AM-0061).

Um adaptador por protocolo: outro acervo em Tainacan entra com uma linha em `ambientes/adaptadores.json`
(a base da API, o tamanho da página e, se houver, as coleções).
A busca do Tainacan é a do WordPress: as palavras de um pedido se somam (E), sem OU nem aspas. Por isso
a tradução de cada Consulta para o ambiente é uma **lista de buscas** (`buscas`, uma por forma do Termo
ou por par classe + descritor), testada pelo rastreador; o adaptador roda uma após a outra, e o cursor
diz qual busca e qual página ("i:p"). O mesmo item achado por duas buscas é a mesma Entrada (`deduplicar`).
Pede só `id`, `title`, `url` e `collection_id` (nada de autoria; l. 596). O total de cada busca vem do
cabeçalho `X-WP-Total`; o total informado do Recorte é a soma das buscas (com repetidos), pedida na
primeira página (`perpage=1` para as outras buscas).
Sem filtro de data na API: o período é sempre "todo", e a resposta nunca é tratada como saturada.

pagina(cliente, cfg, ambiente, buscas, periodo, cursor) → {total_informado, itens, proximo, saturada}
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import urllib.parse

from deduplicar import chave

PROTOCOLO = "tainacan"
TIPO = "busca"
CAMPOS = "id,title,url,collection_id"


def lookfor(traducao: dict) -> list[str]:
    """As buscas da tradução testada (lista); sem ela, recusa."""
    b = traducao.get("buscas")
    if not b or not isinstance(b, list):
        raise ValueError("a tradução não traz a lista de buscas testada (campo 'buscas')")
    return b


def url_pagina(cfg: dict, busca: str, pagina: int) -> str:
    params = [("search", busca), ("perpage", str(cfg.get("pagina", 50))), ("paged", str(pagina)),
              ("fetch_only", CAMPOS), ("order", "ASC"), ("orderby", "id")]
    return cfg["base"] + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


def _total(headers: dict) -> int | None:
    for k, v in headers.items():
        if k.lower() == "x-wp-total":
            try:
                return int(v)
            except ValueError:
                return None
    return None


def _texto(v) -> str:
    if isinstance(v, dict):
        v = v.get("rendered") or v.get("value") or ""
    return html.unescape(re.sub(r"<[^>]+>", " ", str(v or ""))).strip()


def pagina(cliente, cfg: dict, ambiente: str, buscas: list[str], periodo: str, cursor) -> dict:
    i, p = (int(x) for x in str(cursor or "0:1").split(":"))
    r = cliente.pedir(url_pagina(cfg, buscas[i], p))
    if r.status != 200:
        raise RuntimeError(f"HTTP {r.status} na busca {i + 1} ({buscas[i]!r}), página {p}")
    try:
        dados = r.json()
    except ValueError as e:
        raise RuntimeError(f"resposta não é JSON na busca {i + 1}, página {p}: {e}") from e
    lista = dados.get("items", dados) if isinstance(dados, dict) else dados
    if not isinstance(lista, list):
        raise RuntimeError(f"resposta sem lista de itens na busca {i + 1}, página {p}")
    total = _total(r.headers)
    if cursor is None:  # o total do Recorte é a soma das buscas: as outras se pedem com perpage=1
        for b in buscas[1:]:
            rb = cliente.pedir(url_pagina(dict(cfg, pagina=1), b, 1))
            tb = _total(rb.headers) if rb.status == 200 else None
            total = None if total is None or tb is None else total + tb
    itens = []
    for rec in lista:
        id_ = str(rec.get("id"))
        url = rec.get("url") or cfg.get("registro", "").replace("<id>", id_)
        itens.append({
            "id_fonte": id_,
            "identificador": chave(ambiente, id_, [url] if url else []),
            "url": url,
            "titulo": _texto(rec.get("title")),
            "resumo": "",
            "ano": None,
            "hash": hashlib.sha256(json.dumps(rec, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest(),
        })
    tam = int(cfg.get("pagina", 50))
    da_busca = _total(r.headers)
    ha_mais = bool(itens) and (p * tam < da_busca if da_busca is not None else len(itens) == tam)
    if ha_mais:
        proximo = f"{i}:{p + 1}"
    elif i + 1 < len(buscas):
        proximo = f"{i + 1}:1"
    else:
        proximo = None
    return {
        "total_informado": total if cursor is None else None,  # depois da 1ª página, fica a soma já anotada
        "itens": itens,
        "reinicio": p == 1 and i > 0,
        "proximo": proximo,
        "saturada": False,
        "curta": bool(ha_mais and len(itens) < tam),
    }
