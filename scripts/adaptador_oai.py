"""Adaptador OAI-PMH (l. 430, 431): a colheita de um repositório pelo protocolo OAI-PMH (no piloto,
a Infoteca-e, AM-0029, cuja busca por texto o robots.txt veda ao robô).

O OAI-PMH não busca por texto: a colheita traz a lista inteira (ListRecords, oai_dc, página a página
pelo resumptionToken), e o filtro das Consultas é local, nos campos título, assunto e descrição,
que ficam só na memória (o texto não vai ao Git). Uma colheita serve a todas as Consultas da rodada.
O total informado é o completeListSize da lista, e o total visto, os registros colhidos.
Registros apagados (status="deleted") contam como vistos e não geram Entrada.

pagina(cliente, cfg, cursor) → {total_informado, itens, proximo, saturada}
casa(texto, consulta) → a Consulta acha o registro?
"""
from __future__ import annotations

import re
import unicodedata
import urllib.parse
import xml.etree.ElementTree as ET

from deduplicar import chave

PROTOCOLO = "oai-pmh"
TIPO = "colheita"  # uma colheita para todas as Consultas
NS = {"oai": "http://www.openarchives.org/OAI/2.0/", "dc": "http://purl.org/dc/elements/1.1/"}


def url_pagina(cfg: dict, cursor) -> str:
    if cursor:
        q = {"verb": "ListRecords", "resumptionToken": cursor}
    else:
        q = {"verb": "ListRecords", "metadataPrefix": cfg.get("metadataPrefix", "oai_dc")}
        if cfg.get("set"):
            q["set"] = cfg["set"]
    return cfg["base"] + "?" + urllib.parse.urlencode(q)


def pagina(cliente, cfg: dict, ambiente: str, cursor) -> dict:
    r = cliente.pedir(url_pagina(cfg, cursor))
    if r.status != 200:
        raise RuntimeError(f"HTTP {r.status} no cursor {cursor!r}")
    raiz = ET.fromstring(r.corpo.encode("utf-8"))
    erro = raiz.find("oai:error", NS)
    if erro is not None:
        if erro.get("code") == "noRecordsMatch":
            return {"total_informado": 0, "itens": [], "vistos": 0, "proximo": None, "saturada": False}
        raise RuntimeError(f"OAI-PMH {erro.get('code')}: {(erro.text or '').strip()}")
    itens, vistos = [], 0
    for rec in raiz.iterfind(".//oai:ListRecords/oai:record", NS):
        vistos += 1
        cab = rec.find("oai:header", NS)
        if cab is None or cab.get("status") == "deleted":
            continue
        oai_id = cab.findtext("oai:identifier", "", NS)
        dc = rec.find("oai:metadata", NS)
        campo = (lambda n: [x.text or "" for x in dc.iter(f"{{{NS['dc']}}}{n}")]) if dc is not None else (lambda n: [])
        urls = [u for u in campo("identifier") if u.startswith("http")]
        id_fonte = oai_id.split(":", 2)[-1] if oai_id.count(":") >= 2 else oai_id
        itens.append({
            "id_fonte": id_fonte,
            "identificador": chave(ambiente, id_fonte, urls),
            "url": next((u for u in urls if "/handle/" in u), urls[0] if urls else cfg["registro"].replace("<id>", id_fonte.split("/")[-1])),
            "texto": " ".join(campo("title") + campo("subject") + campo("description")),
        })
    tok = raiz.find(".//oai:ListRecords/oai:resumptionToken", NS)
    total = int(tok.get("completeListSize")) if tok is not None and tok.get("completeListSize") else None
    proximo = (tok.text or "").strip() if tok is not None else ""
    if total is None and not proximo:
        total = None  # lista de uma página só, sem completeListSize: o total fica desconhecido
    return {"total_informado": total, "itens": itens, "vistos": vistos, "proximo": proximo or None, "saturada": False}


def _norm(s: str) -> str:
    return unicodedata.normalize("NFC", s).casefold()


def _acha(texto: str, formas: list[str]) -> bool:
    t = _norm(texto)
    return any(re.search(rf"(?<!\w){re.escape(_norm(f))}(?!\w)", t) for f in formas)


def casa(texto: str, formas: list[str], descritores: list[str], tipo: str) -> bool:
    """termo: uma forma; mista: uma forma E um descritor; só descritores: um descritor."""
    if tipo == "termo":
        return _acha(texto, formas)
    if tipo == "mista":
        return _acha(texto, formas) and _acha(texto, descritores)
    return _acha(texto, descritores)
