"""Lê o texto das Fontes de um lote na pasta temporária, fora do repositório (bloco 7; l. 100; K-109).

Para cada Entrada pedida, abre a página do item (o `url_ou_arquivo` da Entrada) pelo cliente da coleta
(robô identificado, robots.txt de cada host, 1 pedido por segundo; proteção anti-robô nunca se contorna),
acha o PDF do item pela meta `citation_pdf_url` (DSpace e repositórios que seguem a convenção do Google
Acadêmico) ou, sem ela, pelo primeiro link de `bitstream` terminado em `.pdf`, e baixa o PDF. Sem PDF,
fica a página. Grava na pasta temporária das fontes (a mesma do `localizar_trecho.py`;
`<TEMP>/cultura-liquida/fontes/` ou `CL_FONTES_TMP`):
  - `<EN>.pdf` ou `<EN>.html`, os bytes lidos (é deles que o `localizar_trecho.py` relê o trecho);
  - `<EN>.txt`, o texto normalizado pela mesma regra do `localizar_trecho.py`, com a marca
    `[[p. n]]` no começo de cada página do PDF, para o avaliador ler por `grep -n` e faixas;
  - `lote-<rotulo>.json`, o manifesto: por Entrada, a página, o PDF, o tipo, as páginas, o tamanho do
    texto, o SHA-256 do texto lido (o mesmo `hash` do Trecho) e o erro, se houver.
Nada disso entra no Git: a pasta temporária fica fora do repositório, e o script recusa o contrário.
Ao fim do lote, `--apagar <rotulo>` apaga os arquivos do lote (o texto integral não fica).

O que não faz: não cria Fonte nem Trecho (é o avaliador, com o `localizar_trecho.py`, e o curador
grava); não lê página vedada pelo robots.txt nem com desafio anti-robô (vira erro no manifesto e no
log, e a Entrada fica para a via humana); não baixa PDF acima de `--max-mb` (padrão 60).

Uso:
    python scripts/ler_fonte.py --rotulo K109-L1 --entrada EN-1155,EN-1543 [--url URL ...] [--max-mb 60]
    python scripts/ler_fonte.py --apagar K109-L1
Código 0 = leu todas; 2 = alguma Entrada sem texto (dita no manifesto e no log); 1 = erro de uso.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from _coleta import BloqueioAntiRobo, BloqueioRobos, Cliente, Execucao  # noqa: E402
from localizar_trecho import extrair_texto, pasta_temporaria, sha256  # noqa: E402

VERSAO = "ler-fonte-0.1"


class _Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pdf_meta: str | None = None
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "meta" and (d.get("name") or "").lower() == "citation_pdf_url" and d.get("content"):
            self.pdf_meta = self.pdf_meta or d["content"]
        if tag == "a" and d.get("href"):
            self.links.append(d["href"])


def achar_pdf(html_texto: str, base: str) -> str | None:
    p = _Links()
    p.feed(html_texto)
    if p.pdf_meta:
        return urllib.parse.urljoin(base, p.pdf_meta)
    for h in p.links:
        if "bitstream" in h and re.search(r"\.pdf(\?|$)", h, re.I):
            return urllib.parse.urljoin(base, h)
    return None


def texto_com_paginas(texto: str, inicios: list[int]) -> str:
    if not inicios:
        return texto
    partes = []
    for k, ini in enumerate(inicios):
        fim = inicios[k + 1] - 1 if k + 1 < len(inicios) else len(texto)
        partes.append(f"[[p. {k + 1}]] {texto[ini:fim]}")
    return "\n".join(partes)


def ler(cli: Cliente, rotulo: str, url: str, pasta: Path, max_mb: int) -> dict:
    item = {"id": rotulo, "pagina": url, "pdf": None, "tipo": None, "paginas": 0, "caracteres": 0,
            "hash_texto": None, "arquivo": None, "erro": None}
    try:
        r = cli.pedir(url)
        if r.status >= 400:
            item["erro"] = f"HTTP {r.status} na página"
            return item
        dados, tipo, ctype = r.bruto, "html", (r.headers.get("Content-Type") or "").lower()
        if dados[:5] == b"%PDF-" or "pdf" in ctype:
            tipo = "pdf"
        else:
            pdf = achar_pdf(r.corpo, r.url)
            if pdf:
                item["pdf"] = pdf
                rp = cli.pedir(pdf)
                if rp.status < 400 and len(rp.bruto) <= max_mb * 1024 * 1024 and rp.bruto[:5] == b"%PDF-":
                    dados, tipo = rp.bruto, "pdf"
                else:
                    item["erro"] = (f"PDF não lido (HTTP {rp.status}, {len(rp.bruto)} bytes); fica a página")
        texto, inicios = extrair_texto(dados, tipo)
        arq = pasta / f"{rotulo}.{tipo}"
        arq.write_bytes(dados)
        (pasta / f"{rotulo}.txt").write_text(texto_com_paginas(texto, inicios), encoding="utf-8", errors="replace")
        item.update(tipo=tipo, paginas=len(inicios), caracteres=len(texto), hash_texto=sha256(texto),
                    arquivo=str(arq))
    except (BloqueioRobos, BloqueioAntiRobo, RuntimeError) as e:
        item["erro"] = str(e)
    except Exception as e:  # rede, PDF ilegível: dito, nunca completado
        item["erro"] = f"{type(e).__name__}: {e}"
    return item


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rotulo", help="nome do lote (ex.: K109-L1)")
    ap.add_argument("--entrada", default="", help="EN-nnnn separados por vírgula")
    ap.add_argument("--url", action="append", default=[], help="ROTULO=URL de item ainda sem Entrada")
    ap.add_argument("--max-mb", type=int, default=60)
    ap.add_argument("--apagar", help="apaga os arquivos do lote dado")
    ap.add_argument("--fixtures", type=Path, help="respostas gravadas (testes, sem rede)")
    a = ap.parse_args()
    pasta = pasta_temporaria()
    if a.apagar:
        man = pasta / f"lote-{a.apagar}.json"
        if not man.exists():
            raise SystemExit(f"sem manifesto {man}")
        n = 0
        for it in json.loads(man.read_text(encoding="utf-8"))["itens"]:
            for ext in ("pdf", "html", "txt"):
                f = pasta / f"{it['id']}.{ext}"
                if f.exists():
                    f.unlink()
                    n += 1
        man.unlink()
        print(f"{n} arquivo(s) do lote {a.apagar} apagado(s) da pasta temporária")
        return 0
    if not a.rotulo or not (a.entrada or a.url):
        ap.error("--rotulo e --entrada ou --url")
    alvos: list[tuple[str, str]] = []
    for en in filter(None, a.entrada.split(",")):
        e = carregar_json(RAIZ / "entrada" / f"{en.strip()}.json")
        alvos.append((e["id"], e["url_ou_arquivo"]))
    for u in a.url:
        rot, _, url = u.partition("=")
        alvos.append((rot, url))
    ex = Execucao("script", f"leitura das Fontes do lote {a.rotulo} ({VERSAO})", simular=bool(a.fixtures))
    cli = Cliente(fixtures=a.fixtures)
    itens = [ler(cli, rot, url, pasta, a.max_mb) for rot, url in alvos]
    (pasta / f"lote-{a.rotulo}.json").write_text(json.dumps(
        {"lote": a.rotulo, "versao": VERSAO, "execucao": ex.id, "itens": itens}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    sem = [i for i in itens if not i["caracteres"]]
    ex.acoes.append(f"leu {len(itens)} item(ns) pelo cliente da coleta (robots.txt, robô identificado, 1 pedido/s)")
    ex.resultados.append(f"{len(itens) - len(sem)} com texto ({sum(1 for i in itens if i['tipo'] == 'pdf')} PDF); "
                         f"{len(sem)} sem texto; pasta temporária fora do Git")
    ex.olhado = [f"{i['id']}: {i['pdf'] or i['pagina']} ({i['tipo'] or 'sem texto'}, {i['paginas']} p.)" for i in itens]
    ex.fora = [f"{i['id']}: {i['erro']}" for i in itens if i["erro"]] + [
        f"{cli.pedidos} pedidos HTTP no total, robots.txt incluídos; o texto integral não entra no Git"]
    ex.erros = [f"{i['id']}: {i['erro']}" for i in sem]
    print(ex.gravar_log() if not a.fixtures else "teste com respostas gravadas: log não gravado")
    for i in itens:
        print(f"{i['id']}\t{i['tipo']}\t{i['paginas']} p.\t{i['caracteres']} car.\t{i['erro'] or ''}")
    print(f"manifesto: {pasta / ('lote-' + a.rotulo + '.json')}")
    return 2 if sem else 0


if __name__ == "__main__":
    sys.exit(main())
