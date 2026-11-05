"""Casos das rotinas sem IA (K-112, bloco 10a), rodados por `scripts/rodar_testes.py`.

Cada caso monta uma cópia de `testes/coleta/raiz` numa pasta temporária (com `git init`, para o
descarte sem novidade), roda o script com as respostas gravadas da BDTD (`testes/coleta/fixtures/bdtd`,
sem autoria) e confere o resultado. Os logs vão a uma pasta temporária (CL_PASTA_LOGS): nada se grava
no acervo real nem em trilhas/logs.

Uso: python testes/rotinas/teste_rotinas.py <caso>
Casos: agenda | agenda-fila-cheia | duas-rodadas | feed | erro-agenda-sem-regra | copia-na-falha |
       sem-copia-no-bloqueio
Código 0 = o caso se comportou como o critério diz; 1 = não.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
import agendar  # noqa: E402

PY = sys.executable
FIX = RAIZ / "testes" / "coleta" / "fixtures" / "bdtd"


def montar(tmp: Path) -> Path:
    r = tmp / "raiz"
    shutil.copytree(RAIZ / "testes" / "coleta" / "raiz", r)
    (r / "ambientes").mkdir(exist_ok=True)
    (r / "ambientes" / "rotinas.json").write_text(json.dumps({
        "versao": "rotinas-0.1",
        "AM-0021": {"ligado": True, "consultas": ["CO-0005"], "teto_chamadas": 10, "cadencia_min_dias": 1, "cadencia_max_dias": 8},
        "AM-0029": {"ligado": False, "consultas": [], "motivo": "teste"}}), encoding="utf-8")
    for c in (["init", "-q"], ["config", "user.email", "teste.example.org"], ["config", "user.name", "teste"],
              ["add", "-A"], ["commit", "-qm", "base"]):
        subprocess.run(["git", *c], cwd=r, check=True, capture_output=True)
    return r


def rodar(r: Path, data: str, logs: Path) -> str:
    env = dict(os.environ, CL_PASTA_LOGS=str(logs), PYTHONUTF8="1", CL_GRAVADOR="rotina")
    p = subprocess.run([PY, str(RAIZ / "scripts" / "rotina_diaria.py"), "--raiz", str(r), "--data", data,
                        "--descartar-sem-novidade", "--links", "0", "--fixtures", str(FIX)],
                       capture_output=True, text=True, encoding="utf-8", env=env)
    if p.returncode != 0:
        raise SystemExit(f"rotina_diaria saiu com {p.returncode}: {(p.stdout + p.stderr)[-800:]}")
    subprocess.run(["git", "add", "-A"], cwd=r, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-qm", data], cwd=r, capture_output=True)
    return p.stdout


def caso_agenda() -> str:
    linha = {"cadencia_min_dias": 1, "cadencia_max_dias": 8}
    sem = {"entradas_novas": 0, "pegadas_novas": 0}
    com = {"entradas_novas": 2, "pegadas_novas": 3}
    seq = [agendar.intervalo(linha, h) for h in ([], [sem], [sem, sem], [sem] * 5, [sem, sem, com], [sem, {"erro": "HTTP 500"}])]
    assert seq == [1, 2, 4, 8, 1, 2], seq
    return f"agenda-0.1: intervalos {seq} (mínimo, dobra sem novidade até o máximo, volta ao mínimo com novidade, erro não mede)"


def caso_agenda_fila_cheia() -> str:
    with tempfile.TemporaryDirectory() as t:
        r = montar(Path(t))
        p = agendar.plano(r, date(2026, 11, 5), fila=16)
        it = next(x for x in p if x["ambiente"] == "AM-0021")
        assert not it["roda"] and "fila cheia" in it["motivo"], it
        return f"porta nova fechada: {it['motivo']}"


def caso_duas_rodadas() -> str:
    with tempfile.TemporaryDirectory() as t:
        r, logs = montar(Path(t)), Path(t) / "logs"
        base = {p.name for p in (r / "entrada").glob("EN-*.json")}
        rodar(r, "2026-11-05", logs)
        rod = [json.loads(x) for x in (r / agendar.RODADAS).read_text(encoding="utf-8").splitlines()]
        assert rod[-1]["entradas_novas"] > 0 and rod[-1]["gravado"], rod[-1]
        ents1 = sorted(p.name for p in (r / "entrada").glob("EN-*.json"))
        novas = [n for n in ents1 if n not in base]
        assert novas and all(50000 <= int(n[3:-5]) <= 89999 for n in novas), novas
        # segunda rodada no dia seguinte: nada novo; só a linha da rodada
        rodar(r, "2026-11-06", logs)
        rod = [json.loads(x) for x in (r / agendar.RODADAS).read_text(encoding="utf-8").splitlines()]
        ents2 = sorted(p.name for p in (r / "entrada").glob("EN-*.json"))
        st = subprocess.run(["git", "show", "--stat", "--format=", "HEAD"], cwd=r, capture_output=True, text=True).stdout
        assert rod[-1]["entradas_novas"] == 0 and rod[-1]["pegadas_novas"] == 0 and not rod[-1]["gravado"], rod[-1]
        assert ents1 == ents2, (ents1, ents2)
        mudou = [x.split("|")[0].strip() for x in st.splitlines() if "|" in x]
        assert all(m.startswith("trilhas/relatorios") for m in mudou), mudou
        # a agenda dobra o intervalo: no dia 07 o ambiente não roda
        p = agendar.plano(r, date(2026, 11, 7))
        assert not next(x for x in p if x["ambiente"] == "AM-0021")["roda"]
        return (f"1ª rodada: {rod[0]['entradas_novas']} Entrada(s) nova(s), gravada(s) na faixa da rotina; 2ª: só o não visto "
                f"(nenhum), nada gravado além de {', '.join(sorted(set(mudou)))}; intervalo dobrado")


def caso_feed() -> str:
    with tempfile.TemporaryDirectory() as t:
        r, logs = montar(Path(t)), Path(t) / "logs"
        rodar(r, "2026-11-05", logs)
        xml = (r / "entrada" / "feed.xml").read_text(encoding="utf-8")
        assert "Consulta de origem: CO-0005" in xml and "<entry>" in xml, xml[:400]
        antes = xml
        rodar(r, "2026-11-06", logs)
        assert (r / "entrada" / "feed.xml").read_text(encoding="utf-8") == antes
        return "feed com a Consulta de origem de cada Entrada; sem Entrada nova, o feed não muda"


def caso_erro_agenda_sem_regra() -> str:
    linha = {"cadencia_min_dias": 1, "cadencia_max_dias": 8}
    # erro esperado: uma regra que não dobrasse daria intervalo 1 depois de três rodadas sem novidade
    n = agendar.intervalo(linha, [{"entradas_novas": 0, "pegadas_novas": 0}] * 3)
    if n == 1:
        return "a regra não dobrou"
    raise SystemExit(f"REPROVA como esperado: três rodadas sem novidade dão intervalo {n}, não 1 (a regra dobra)")


def fixtures_copia(pasta: Path, status_pagina: int) -> None:
    """Respostas sintéticas (hosts .example e o Wayback), sem dado real."""
    sys.path.insert(0, str(RAIZ / "scripts"))
    from _coleta import _nome_fixture
    url = "https://repositorio.example/handle/123"
    snap = "https://web.archive.org/web/20250101000000/" + url
    corpo_pagina = "registro de teste (K-112), sintético: Forbidden" if status_pagina == 403 else "Not Found"
    resp = {
        "https://repositorio.example/robots.txt": (404, ""),
        url: (status_pagina, corpo_pagina),
        "https://archive.org/robots.txt": (404, ""),
        "https://archive.org/wayback/available?url=" + __import__("urllib.parse").parse.quote(url, safe=""):
            (200, json.dumps({"archived_snapshots": {"closest": {"available": True, "status": "200", "url": snap}}})),
        "https://web.archive.org/robots.txt": (404, ""),
        "https://web.archive.org/web/20250101000000id_/" + url:
            (200, "<html><body><p>registro de teste (K-112), sintético: o modo de fazer a bebida na cópia arquivada.</p></body></html>"),
    }
    pasta.mkdir(parents=True, exist_ok=True)
    for u, (st, corpo) in resp.items():
        (pasta / _nome_fixture("GET", u)).write_text(json.dumps({"url": u, "status": st, "headers": {}, "corpo": corpo}), encoding="utf-8")


def ler_com_copia(status_pagina: int, raiz_real: bool = False) -> str:
    with tempfile.TemporaryDirectory() as t:
        fx = Path(t) / "fx"
        fixtures_copia(fx, status_pagina)
        (Path(t) / "sem-barreiras").mkdir()
        env = dict(os.environ, CL_FONTES_TMP=str(Path(t) / "fontes"), PYTHONUTF8="1")
        p = subprocess.run([PY, str(RAIZ / "scripts" / "ler_fonte.py"), "--rotulo", "teste-copia", "--url",
                            "T1=https://repositorio.example/handle/123", "--fixtures", str(fx)]
                           + ([] if raiz_real else ["--raiz-barreiras", str(Path(t) / "sem-barreiras")]),
                           capture_output=True, text=True, encoding="utf-8", env=env)
        return p.stdout + p.stderr


def caso_copia_na_falha() -> str:
    out = ler_com_copia(404)
    linha = next(x for x in out.splitlines() if x.startswith("T1	"))
    assert "cópia arquivada https://web.archive.org/web/20250101000000/" in linha and "html" in linha, out[-600:]
    return "página com HTTP 404: lida pela cópia arquivada que já existe (" + linha.split("	")[4] + ")"


def caso_sem_copia_no_bloqueio() -> str:
    out = ler_com_copia(403)
    linha = next(x for x in out.splitlines() if x.startswith("T1	"))
    if "cópia arquivada https" in linha:
        return "leu a cópia num bloqueio"
    raise SystemExit("REPROVA como esperado: 403 é bloqueio contra robô; a cópia não se consulta (D-044): " + linha.split("	")[-1])


def caso_geral_classe_e_descritor() -> str:
    import adaptador_oai
    ds = ["clarificação", "filtração"]
    assert adaptador_oai.casa("Clarificação de bebida de frutas", ["bebida"], ds, "só descritores")
    assert not adaptador_oai.casa("Filtração de água para irrigação", ["bebida"], ds, "só descritores")
    assert adaptador_oai.casa("Filtração de água", [], ds, "só descritores")  # sem classe: a regra antiga
    return "Consulta geral: a colheita acha a classe E um descritor (consultas-gerais-0.1); sem classe, um descritor basta"


class _Resp:
    def __init__(self, corpo, headers=None, status=200):
        self.corpo, self.headers, self.status = json.dumps(corpo), headers or {}, status

    def json(self):
        return json.loads(self.corpo)


class _Cli:
    """Cliente sintético: devolve as respostas na ordem e guarda os pedidos."""
    def __init__(self, resps):
        self.resps, self.urls = list(resps), []

    def pedir(self, url):
        self.urls.append(url)
        return self.resps.pop(0)


def caso_cursor_dois_formatos() -> str:
    import adaptador_cursor as ac
    oa = {"adaptador": "api-cursor", "base": "https://api.example/works", "param_busca": "search", "param_cursor": "cursor",
          "cursor_inicial": "*", "fixos": {"per-page": "2"}, "pagina": 2, "filtro_periodo": "filter=publication_year:{a}-{b}",
          "caminhos": {"itens": "results", "total": "meta.count", "proximo": "meta.next_cursor", "id": "id", "titulo": "title",
                       "ano": "publication_year", "resumo": "abstract_inverted_index", "url": "doi"}}
    cli = _Cli([_Resp({"meta": {"count": 3, "next_cursor": "abc"}, "results": [
        {"id": "W1", "title": "registro sintético", "publication_year": 2001, "abstract_inverted_index": {"bebida": [0], "clarificada": [1]}},
        {"id": "W2", "title": "outro registro sintético", "doi": "https://doi.org/10.0/x"}]})])
    p = ac.pagina(cli, oa, "AM-9", '"bebida" AND clarificação', "1990-2000", None)
    assert "cursor=%2A" in cli.urls[0] and "filter=publication_year%3A1990-2000" in cli.urls[0], cli.urls
    assert p["total_informado"] == 3 and p["proximo"] == "abc" and p["itens"][0]["resumo"] == "bebida clarificada", p
    assert p["itens"][1]["url"] == "https://doi.org/10.0/x"
    ia = {"adaptador": "api-cursor", "base": "https://arquivo.example/scrape", "param_busca": "q", "param_cursor": "cursor",
          "cursor_inicial": None, "fixos": {"count": "100"}, "pagina": 100, "periodo_na_busca": " AND year:[{a} TO {b}]",
          "registro": "https://arquivo.example/details/<id>",
          "caminhos": {"itens": "items", "total": "total", "proximo": "cursor", "id": "identifier", "titulo": "title", "ano": "year"}}
    cli = _Cli([_Resp({"items": [{"identifier": "item1", "title": "registro sintético"}], "count": 1, "total": 1})])
    p = ac.pagina(cli, ia, "AM-9", "cajuína", "1900-1950", None)
    assert "cursor" not in cli.urls[0] and "year%3A%5B1900%20TO%201950%5D" in cli.urls[0], cli.urls
    assert p["proximo"] is None and p["itens"][0]["url"] == "https://arquivo.example/details/item1", p
    return "api-cursor: a mesma regra lê a forma da OpenAlex (cursor inicial, filtro de período, resumo remontado) e a da Scrape API (período na busca, fim sem cursor)"


def caso_tainacan_buscas() -> str:
    import adaptador_tainacan as at
    cfg = {"adaptador": "tainacan", "base": "https://acervo.example/wp-json/tainacan/v2/items", "pagina": 2}
    cli = _Cli([_Resp([{"id": 1, "title": "registro sintético", "url": "https://acervo.example/a/1"}, {"id": 2, "title": "b"}],
                      {"X-WP-Total": "3"}),
                _Resp([{"id": 9, "title": "c"}], {"X-WP-Total": "1"})])
    p = at.pagina(cli, cfg, "AM-9", ["cajuina", "cajuína"], "todo", None)
    assert p["total_informado"] == 4 and p["proximo"] == "0:2" and "perpage=1" in cli.urls[1], (p, cli.urls)
    cli = _Cli([_Resp([{"id": 3, "title": "d"}], {"X-WP-Total": "3"})])
    p = at.pagina(cli, cfg, "AM-9", ["cajuina", "cajuína"], "todo", "0:2")
    assert p["proximo"] == "1:1" and p["total_informado"] is None, p
    cli = _Cli([_Resp([{"id": 1, "title": "registro sintético"}], {"X-WP-Total": "1"})])
    p = at.pagina(cli, cfg, "AM-9", ["cajuina", "cajuína"], "todo", "1:1")
    assert p["proximo"] is None and p["reinicio"], p
    return "tainacan: uma busca por forma, o total somado na 1ª página, o cursor 'busca:página' e a 1ª página da outra busca marcada (não é repetição)"


def caso_erro_tainacan_sem_buscas() -> str:
    import adaptador_tainacan as at
    try:
        at.lookfor({"pedido": "GET https://acervo.example/wp-json/tainacan/v2/items?search=cajuina"})
    except ValueError as e:
        raise SystemExit(f"REPROVA como esperado: {e}")
    return "aceitou tradução sem a lista de buscas"


def caso_copia_barrada_pela_falta() -> str:
    out = ler_com_copia(404, raiz_real=True)
    linha = next(x for x in out.splitlines() if x.startswith("T1	"))
    assert "Falta F-0034 barra a consulta" in linha, linha
    return "com a F-0034 aberta (termos do Internet Archive não lidos), a cópia não se consulta: " + linha.split("	")[-1]


CASOS = {"copia-barrada-pela-falta": caso_copia_barrada_pela_falta, "cursor-dois-formatos": caso_cursor_dois_formatos, "tainacan-buscas": caso_tainacan_buscas,
         "erro-tainacan-sem-buscas": caso_erro_tainacan_sem_buscas, "geral-classe-e-descritor": caso_geral_classe_e_descritor, "copia-na-falha": caso_copia_na_falha, "sem-copia-no-bloqueio": caso_sem_copia_no_bloqueio,
         "agenda": caso_agenda, "agenda-fila-cheia": caso_agenda_fila_cheia, "duas-rodadas": caso_duas_rodadas,
         "feed": caso_feed, "erro-agenda-sem-regra": caso_erro_agenda_sem_regra}

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(CASOS[sys.argv[1]]())
