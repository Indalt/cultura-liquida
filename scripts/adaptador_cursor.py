"""Adaptador "API com cursor" (l. 430; bloco 10a, K-112): a busca numa API em JSON que pagina por um
cursor opaco (a resposta traz o marcador da página seguinte). No piloto, a OpenAlex (AM-0026) e a busca
do Internet Archive pela Scrape API (AM-0007); outra API do mesmo tipo entra com uma linha em
`ambientes/adaptadores.json`, sem código novo:

    "adaptador": "api-cursor", "base": <endereço da busca>, "param_busca": <nome do parâmetro da consulta>,
    "param_cursor": <nome do parâmetro do cursor>, "cursor_inicial": <valor do 1º pedido, ou null>,
    "fixos": {<parâmetros fixos: campos, tamanho da página>}, "pagina": <itens por página>,
    "caminhos": {"itens", "total", "proximo", "id", "titulo", "ano", "resumo"?, "url"?} (caminhos com ponto),
    "registro": <link do item com <id>>, e o período: "filtro_periodo" (um parâmetro, como
    "filter=publication_year:{a}-{b}") ou "periodo_na_busca" (um pedaço da consulta, como " AND year:[{a} TO {b}]").

A Consulta vai como a tradução testada (`ambientes/traducao-consultas.json`, o parâmetro de busca do
pedido testado). Pede só os campos da linha: nada de autoria (l. 596). O título e o resumo servem à
pré-triagem (D-045) e ficam na memória; um resumo em índice invertido (OpenAlex) é remontado só para ela.
O hash é a soma SHA-256 do registro como a fonte o deu. Cursor não tem limite de profundidade: a
resposta nunca é tratada como saturada, salvo `limite_fonte` na linha.

pagina(cliente, cfg, ambiente, consulta, periodo, cursor) → {total_informado, itens, proximo, saturada}
"""
from __future__ import annotations

import hashlib
import json
import urllib.parse

from deduplicar import chave

PROTOCOLO = "api-cursor"
TIPO = "busca"
PRIMEIRO = "__primeiro__"  # o cursor do estado antes do 1º pedido (None no Recorte)


def lookfor(traducao: dict) -> str:
    pedido = traducao["pedido"].split(" ", 1)[-1]
    q = urllib.parse.parse_qs(urllib.parse.urlsplit(pedido).query)
    nome = traducao.get("param_busca")
    if nome and nome in q:
        return q[nome][0]
    for nome in ("search", "q", "query", "lookfor"):
        if nome in q:
            return q[nome][0]
    raise ValueError("a tradução não traz um pedido testado com o parâmetro de busca")


def pegar(obj, caminho: str | None):
    if not caminho:
        return None
    for parte in caminho.split("."):
        if not isinstance(obj, dict):
            return None
        obj = obj.get(parte)
    return obj


def texto(v) -> str:
    if isinstance(v, dict):  # índice invertido {palavra: [posições]} (OpenAlex)
        pos = sorted((p, w) for w, ps in v.items() for p in ps if isinstance(p, int))
        return " ".join(w for _, w in pos)
    if isinstance(v, list):
        return " ".join(str(x) for x in v if x)
    return str(v or "")


def url_pagina(cfg: dict, consulta: str, periodo: str, cursor) -> str:
    q = consulta
    params = list((cfg.get("fixos") or {}).items())
    if periodo and periodo != "todo":
        a, b = periodo.split("-")
        if cfg.get("periodo_na_busca"):
            q = q + cfg["periodo_na_busca"].format(a=a, b=b)
        elif cfg.get("filtro_periodo"):
            k, _, v = cfg["filtro_periodo"].format(a=a, b=b).partition("=")
            params.append((k, v))
    params.insert(0, (cfg["param_busca"], q))
    c = cfg.get("cursor_inicial") if cursor in (None, PRIMEIRO) else cursor
    if c is not None:
        params.append((cfg["param_cursor"], str(c)))
    return cfg["base"] + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


def pagina(cliente, cfg: dict, ambiente: str, consulta: str, periodo: str, cursor) -> dict:
    r = cliente.pedir(url_pagina(cfg, consulta, periodo, cursor))
    if r.status != 200:
        raise RuntimeError(f"HTTP {r.status} no cursor {cursor!r}")
    try:
        dados = r.json()
    except ValueError as e:
        raise RuntimeError(f"resposta não é JSON no cursor {cursor!r}: {e}") from e
    c = cfg["caminhos"]
    lista = pegar(dados, c["itens"])
    if not isinstance(lista, list):
        raise RuntimeError(f"resposta sem a lista de itens ({c['itens']}) no cursor {cursor!r}")
    total = pegar(dados, c.get("total"))
    itens = []
    for rec in lista:
        id_ = str(pegar(rec, c["id"]))
        url = pegar(rec, c.get("url")) or cfg.get("registro", "<id>").replace("<id>", urllib.parse.quote(id_, safe=":/"))
        itens.append({
            "id_fonte": id_,
            "identificador": chave(ambiente, id_, [url]),
            "url": url,
            "titulo": texto(pegar(rec, c.get("titulo"))),
            "resumo": texto(pegar(rec, c.get("resumo"))),
            "ano": pegar(rec, c.get("ano")),
            "hash": hashlib.sha256(json.dumps(rec, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest(),
        })
    proximo = pegar(dados, c.get("proximo"))
    if not itens or proximo in ("", None):
        proximo = None
    limite = cfg.get("limite_fonte")
    tam = int(cfg.get("pagina", 100))
    return {
        "total_informado": int(total) if isinstance(total, (int, float, str)) and str(total).isdigit() else None,
        "itens": itens,
        "proximo": proximo,
        "saturada": bool(limite and total and int(total) > limite),
        "curta": bool(proximo and len(itens) < tam),
    }
