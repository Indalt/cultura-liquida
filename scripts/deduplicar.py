"""Uma Entrada por item (l. 435): a deduplicação de `entrada/` pelo identificador do item.

A chave é o identificador: DOI, handle ou o ID na fonte, nessa ordem (doi:<DOI>, hdl:<handle>,
<ambiente>:<ID>). Um handle só vale como chave global quando é resolvível no hdl.handle.net, ou
quando tem prefixo numérico diferente do 123456789 (o prefixo de exemplo do DSpace, que muitos
repositórios mantêm); senão, a chave é a do ambiente. Quando várias Consultas acham o mesmo item, a
Entrada é uma só, com todos os Recortes de origem; o rendimento de cada Consulta (itens achados e
descobertas, isto é, itens que ela achou primeiro) sai das Entradas. A Entrada não guarda autoria
(l. 596).

Uso como biblioteca (recorte.py, assistido.py, entrada_link.py): chave(), Indice, registrar().
Uso como script:
    python scripts/deduplicar.py --conferir [--raiz <pasta>]   # reprova (código 1) se houver duplicata
    python scripts/deduplicar.py --rendimento [--raiz <pasta>]  # itens e descobertas por Consulta
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from _acervo import proximo_id  # noqa: E402
from _coleta import gravar_json  # noqa: E402

VERSAO = "deduplicacao-0.1"
PROTECAO_PADRAO = {
    "licenca": "não conferido", "consentimento": "não se aplica", "restricao_comunitaria": "nenhuma conhecida",
    "precisao_lugar": "não se aplica", "dado_sensivel": False, "crianca_ou_adolescente": False,
    "pedido_de_retirada": "nenhum",
}
RE_DOI = re.compile(r"(10\.\d{4,9}/\S+)", re.I)
RE_HANDLE = re.compile(r"(?:hdl\.handle\.net/|/handle/)([^/?#\s]+/[^/?#\s]+)")


def chave(ambiente: str, id_fonte: str, urls: list[str] = (), doi: str | None = None) -> str:
    """O identificador do item: doi:, hdl: ou <ambiente>:<ID na fonte>."""
    if doi and (m := RE_DOI.search(doi)):
        return "doi:" + m.group(1).rstrip(".").lower()
    for u in urls:
        if "doi.org/" in u and (m := RE_DOI.search(urllib.parse.unquote(u))):
            return "doi:" + m.group(1).rstrip(".").lower()
    for u in urls:
        m = RE_HANDLE.search(u)
        if not m:
            continue
        h = m.group(1)
        prefixo_h = h.split("/")[0]
        if "hdl.handle.net/" in u or (prefixo_h.replace(".", "").isdigit() and prefixo_h != "123456789"):
            return "hdl:" + h
    return f"{ambiente}:{id_fonte}"


def normalizar_url(u: str) -> str:
    return u.strip().rstrip("/").replace("http://", "https://", 1).lower()


class Indice:
    """As Entradas de `entrada/`, por identificador e, sem ele, pelo link (normalizado)."""

    def __init__(self, raiz: Path = RAIZ):
        self.pasta = raiz / "entrada"
        self.por_chave: dict[str, tuple[Path, dict]] = {}
        self.por_url: dict[str, tuple[Path, dict]] = {}
        self.ids: set[str] = set()
        self.duplicatas: list[str] = []
        if self.pasta.exists():
            for arq in sorted(self.pasta.glob("*.json")):
                self._por(arq, carregar_json(arq))

    def _por(self, arq: Path, e: dict) -> None:
        self.ids.add(e["id"])
        if e.get("retirado"):
            return
        k = e.get("identificador")
        if k:
            if k in self.por_chave:
                self.duplicatas.append(f"{k}: {self.por_chave[k][1]['id']} e {e['id']}")
            else:
                self.por_chave[k] = (arq, e)
        self.por_url.setdefault(normalizar_url(e["url_ou_arquivo"]), (arq, e))

    def achar(self, identificador: str | None, url: str) -> tuple[Path, dict] | None:
        if identificador and identificador in self.por_chave:
            return self.por_chave[identificador]
        if not identificador:
            return self.por_url.get(normalizar_url(url))
        return None


def registrar(ind: Indice, *, identificador: str | None, url: str, canal: str, origem: dict,
              ambiente: str | None = None, recorte: str | None = None, localizador: str | None = None,
              nota: str | None = None, gravar: bool = True) -> tuple[str, bool]:
    """Grava a Entrada do item ou acrescenta o Recorte à que já existe. Devolve (id, nova?).
    Sem identificador (link trazido sem DOI, handle nem ambiente), a chave é o próprio link."""
    if achada := ind.achar(identificador, url):
        arq, e = achada
        if recorte and recorte not in e.setdefault("recortes", []):
            e["recortes"].append(recorte)
            if gravar:
                gravar_json(arq, e)
        return e["id"], False
    e = {"id": proximo_id("EN", ind.ids), "canal": canal}
    if ambiente:
        e["ambiente"] = ambiente
    if recorte:
        e["recortes"] = [recorte]
    e.update(data_entrada=date.today().isoformat(), url_ou_arquivo=url)
    if identificador:
        e["identificador"] = identificador
    if localizador:
        e["localizador"] = localizador
    e.update(estado="bruto", sustenta_aviso_saude_politica=False, protecao=dict(PROTECAO_PADRAO))
    e["nota"] = nota or ("a marca de aviso, saúde ou política é posta na triagem (bloco 7); "
                         "licença e proteção a conferir na triagem")
    e["origem_registro"] = origem
    erros = validar_objeto(e, carregar_esquema("entrada"))
    if erros:
        raise ValueError(f"Entrada inválida: {'; '.join(erros)}")
    arq = ind.pasta / f"{e['id']}.json"
    if gravar:
        gravar_json(arq, e)
    ind._por(arq, e)
    return e["id"], True


def rendimento(raiz: Path) -> dict[str, dict[str, int]]:
    """Por Consulta: itens achados e descobertas (o primeiro Recorte da Entrada é o da descoberta)."""
    consulta_do = {}
    pasta = raiz / "ambientes" / "recortes"
    if pasta.exists():
        for arq in pasta.glob("*.json"):
            r = carregar_json(arq)
            consulta_do[r["id"]] = r.get("consulta", "?")
    saida: dict[str, dict[str, int]] = {}
    for _, e in Indice(raiz).por_chave.values():
        cons = [consulta_do.get(r, "?") for r in e.get("recortes", [])]
        for i, c in enumerate(dict.fromkeys(cons)):
            d = saida.setdefault(c, {"itens": 0, "descobertas": 0})
            d["itens"] += 1
            d["descobertas"] += 1 if i == 0 else 0
    return saida


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--conferir", action="store_true")
    ap.add_argument("--rendimento", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    ind = Indice(raiz)
    if a.rendimento:
        for c, d in sorted(rendimento(raiz).items()):
            print(f"{c}: {d['itens']} itens, {d['descobertas']} descobertas")
    for d in ind.duplicatas:
        print("DUPLICATA", d)
    print(f"{VERSAO}: {len(ind.por_chave)} Entradas com identificador; "
          f"{'sem duplicata' if not ind.duplicatas else f'{len(ind.duplicatas)} duplicata(s)'}")
    return 1 if a.conferir and ind.duplicatas else 0


if __name__ == "__main__":
    sys.exit(main())
