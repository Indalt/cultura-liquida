"""Metadados das Entradas num cache local, fora da pasta versionada (D-045, camada 3; K-108b).

Busca na fonte o título, o ano e o resumo de cada Entrada coletada por programa e grava uma linha por
item em `<TEMP>/cultura-liquida/cache/metadados/<ambiente>.jsonl` (ou `CL_CACHE_TMP`). O cache serve à
pré-triagem por regra (`pretriagem.py`) e ao resumo da coleta; nada dele vai ao Git: o título só
entra na Entrada que passa, como metadado, e o resumo só como citação curta (padrão da F-0003).
Nunca guarda autoria (l. 596): no VuFind, só os campos id, title, publicationDates, summary e urls;
no OAI-PMH, só dc:title, dc:date e dc:description.

- **VuFind (BDTD):** refaz as buscas dos Recortes percorridos (uma por Consulta × período), com os
  campos de metadados, e casa cada item com a Entrada pela chave da deduplicação.
- **OAI-PMH (Infoteca-e):** um GetRecord por Entrada, pelo identificador OAI.
- O `hash` é a soma SHA-256 do registro de metadados como a fonte o deu (D-045, b).
- Retoma: o que já está no cache não se pede de novo. Robô identificado, robots.txt, 1 pedido por
  segundo (`_coleta.Cliente`); `--max` limita os pedidos da rodada.

Uso:
    python scripts/metadados.py --ambiente AM-0021|AM-0029 [--max 400] [--cache <pasta>]
        [--fixtures <pasta>] [--raiz <pasta>] [--simular]
Código 0 = rodou; 1 = erro de uso.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from _coleta import BloqueioAntiRobo, BloqueioRobos, Cliente, Execucao  # noqa: E402
from deduplicar import chave  # noqa: E402
import adaptador_vufind  # noqa: E402

VERSAO = "metadados-0.1"
NS = {"oai": "http://www.openarchives.org/OAI/2.0/", "dc": "http://purl.org/dc/elements/1.1/"}
CAMPOS_VUFIND = ["id", "title", "publicationDates", "summary", "urls"]


def pasta_cache(arg: Path | None = None) -> Path:
    return arg or Path(os.environ.get("CL_CACHE_TMP") or Path(tempfile.gettempdir()) / "cultura-liquida" / "cache") / "metadados"


def ler_cache(arq: Path) -> dict[str, dict]:
    if not arq.exists():
        return {}
    linhas = (json.loads(x) for x in arq.read_text(encoding="utf-8").splitlines() if x.strip())
    return {d["identificador"]: d for d in linhas}


def soma(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def entradas_do(raiz: Path, ambiente: str) -> dict[str, dict]:
    out = {}
    for f in sorted((raiz / "entrada").glob("EN-*.json")):
        d = carregar_json(f)
        if d.get("ambiente") == ambiente and d.get("identificador"):
            out[d["identificador"]] = d
    return out


def rodar_vufind(cli, cfg, raiz, ambiente, alvo, cache, ex, maximo) -> list[dict]:
    novas, pedidos = [], 0
    recortes = [carregar_json(f) for f in sorted((raiz / "ambientes" / "recortes").glob("RC-*.json"))]
    janelas = sorted({(r["consulta"], r.get("periodo", "todo")) for r in recortes
                      if r["ambiente"] == ambiente and r["estado"] == "percorrido pela busca"})
    traducoes = carregar_json(raiz / "ambientes" / "traducao-consultas.json")
    for co, periodo in janelas:
        if all(i in cache for i in alvo) or pedidos >= maximo:
            break
        consulta = adaptador_vufind.lookfor(traducoes[co][ambiente])
        p = 1
        while pedidos < maximo:
            params = [("lookfor", consulta), ("type", "AllFields"), ("limit", str(cfg.get("pagina", 100))), ("page", str(p))]
            params += [("field[]", c) for c in CAMPOS_VUFIND]
            if periodo != "todo":
                a, b = periodo.split("-")
                params.append(("filter[]", f"publishDate:[{a} TO {b}]"))
            r = cli.pedir(cfg["base"] + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote))
            pedidos += 1
            if r.status != 200:
                ex.erros.append(f"{co} {periodo} p. {p}: HTTP {r.status}")
                break
            dados = r.json()
            recs = dados.get("records", [])
            for rec in recs:
                urls = [u["url"] for u in rec.get("urls", []) if isinstance(u, dict) and u.get("url")]
                ident = chave(ambiente, rec["id"], urls)
                if ident in alvo and ident not in cache:
                    linha = {"identificador": ident, "id_fonte": rec["id"], "titulo": rec.get("title") or "",
                             "ano": (rec.get("publicationDates") or [None])[0],
                             "resumo": " ".join(rec.get("summary") or []),
                             "hash": soma(json.dumps(rec, ensure_ascii=False, sort_keys=True)),
                             "fonte": f"VuFind API v1, {co} {periodo}, página {p}"}
                    cache[ident] = linha
                    novas.append(linha)
            if not recs or p * int(cfg.get("pagina", 100)) >= int(dados.get("resultCount", 0)):
                break
            p += 1
        ex.olhado.append(f"{ambiente} × {co} ({periodo}): {p} página(s) com metadados")
    return novas


def rodar_oai(cli, cfg, ambiente, alvo, cache, ex, maximo) -> list[dict]:
    novas, pedidos = [], 0
    host = urllib.parse.urlsplit(cfg["base"]).netloc
    for ident, en in alvo.items():
        if ident in cache:
            continue
        if pedidos >= maximo:
            ex.fora.append(f"{sum(1 for i in alvo if i not in cache)} Entrada(s) além do máximo de {maximo} pedidos")
            break
        id_fonte = ident.split("/handle/", 1)[-1] if "/handle/" in ident else ident.split(":", 1)[-1]
        url = cfg["base"] + "?" + urllib.parse.urlencode({"verb": "GetRecord", "metadataPrefix": cfg.get("metadataPrefix", "oai_dc"),
                                                         "identifier": f"oai:{host}:{id_fonte}"})
        r = cli.pedir(url)
        pedidos += 1
        if r.status != 200:
            ex.erros.append(f"{en['id']}: HTTP {r.status}")
            continue
        try:
            rec = ET.fromstring(r.corpo.encode("utf-8")).find(".//oai:GetRecord/oai:record", NS)
        except ET.ParseError as e:
            ex.erros.append(f"{en['id']}: resposta não é XML ({e})")
            continue
        if rec is None:
            ex.erros.append(f"{en['id']}: GetRecord sem registro")
            continue
        campo = lambda n: [x.text or "" for x in rec.iter(f"{{{NS['dc']}}}{n}")]  # noqa: E731
        datas = [d[:4] for d in campo("date") if d[:4].isdigit()]
        linha = {"identificador": ident, "id_fonte": id_fonte, "titulo": " ".join(campo("title")),
                 "ano": min(datas) if datas else None, "resumo": " ".join(campo("description")),
                 "hash": soma(ET.tostring(rec, encoding="unicode")), "fonte": "OAI-PMH GetRecord"}
        cache[ident] = linha
        novas.append(linha)
    ex.olhado.append(f"{ambiente}: {pedidos} GetRecord")
    return novas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ambiente", required=True)
    ap.add_argument("--max", type=int, default=400)
    ap.add_argument("--cache", type=Path)
    ap.add_argument("--fixtures", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--entrada-ref", default="K-108b, metadados das Entradas no cache local (D-045)")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    cfg = carregar_json(raiz / "ambientes" / "adaptadores.json").get(a.ambiente)
    if not cfg or cfg.get("adaptador") not in ("vufind", "oai-pmh"):
        print(f"{a.ambiente}: sem adaptador VuFind ou OAI-PMH")
        return 1
    arq = pasta_cache(a.cache) / f"{a.ambiente}.jsonl"
    cache = ler_cache(arq)
    alvo = entradas_do(raiz, a.ambiente)
    ex = Execucao("metadados", a.entrada_ref, simular=a.simular)
    ex.ambientes.add(a.ambiente)
    ex.acoes.append(f"scripts/metadados.py --ambiente {a.ambiente} --max {a.max}" + (" --simular" if a.simular else ""))
    fx = (a.fixtures if a.fixtures.is_absolute() else RAIZ / a.fixtures) if a.fixtures else None
    cli = Cliente(fixtures=fx)
    try:
        if cfg["adaptador"] == "vufind":
            novas = rodar_vufind(cli, cfg, raiz, a.ambiente, alvo, cache, ex, a.max)
        else:
            novas = rodar_oai(cli, cfg, a.ambiente, alvo, cache, ex, a.max)
    except (BloqueioRobos, BloqueioAntiRobo, RuntimeError) as e:
        ex.erros.append(str(e))
        novas = []
    faltam = [i for i in alvo if i not in cache]
    if not a.simular and novas:
        arq.parent.mkdir(parents=True, exist_ok=True)
        with arq.open("a", encoding="utf-8") as f:
            for linha in novas:
                f.write(json.dumps(linha, ensure_ascii=False) + "\n")
    ex.resultados.append(f"{len(novas)} registro(s) novo(s) no cache; {len(alvo) - len(faltam)} de {len(alvo)} Entradas com metadados")
    if faltam:
        ex.fora.append(f"{len(faltam)} Entrada(s) ainda sem metadados no cache")
    ex.olhado.append(f"{cli.pedidos} pedido(s) HTTP, robots.txt incluído, robô identificado, 1 por segundo")
    print(f"{VERSAO}: {ex.id}; {ex.resultados[0]}; cache fora do Git em {arq}; {ex.gravar_log()}")
    for e in ex.erros[:10]:
        print("ERRO", e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
