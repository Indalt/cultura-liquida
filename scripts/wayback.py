"""Cópia no Wayback (l. 509): pede a captura das Entradas sem cópia pelo Save Page Now 2 (SPN2) do
Internet Archive, em ritmo baixo, e grava o endereço da cópia na Entrada.

- Sem chave, no ritmo anônimo (Parada (c) do bloco 5, pelo padrão de Vicente). Os limites do
  anônimo vêm de documentação de comunidade, nível secundária (Fundação l. 509: 3 capturas por
  minuto, 200 por dia, no máximo 5 por URL por dia; a página oficial não foi conferida). O ritmo
  daqui fica bem abaixo: 1 captura a cada 30 s e no máximo `--max` por rodada (padrão 5).
- Não captura página de ambiente cuja ficha registra 403, captcha ou verificação de navegador: a
  Entrada fica com o link permanente, e a dúvida vai ao juridico (l. 419). O robots.txt do
  web.archive.org é respeitado como o de qualquer host.
- Nunca captura sem a triagem do juridico sobre a política de cópias arquivadas (Lei 9.610; l. 740):
  a triagem é feita uma vez, antes da primeira captura, e o `--triagem` aponta o arquivo dela.
- Barreira que valha para a captura em si deixa o item sem cópia, com a Falta, o porquê e o caminho
  (D-025). A Falta é do juridico; este script a cumpre: com uma Falta `impedimento_juridico` aberta
  (caminho não liberado) que aponte `scripts/wayback.py` e não valha só para publicar, nada se
  captura, e as Entradas ficam com o link permanente (F-0004, triagem de 23/10/2026, K-107).

Uso:
    python scripts/wayback.py --triagem <arquivo da triagem> [--entrada EN-0001,...] [--max 5]
        [--fixtures <pasta>] [--raiz <pasta>] [--simular]
Código 0 = rodou; 1 = sem triagem ou erro de uso.
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from _coleta import BloqueioAntiRobo, BloqueioRobos, Cliente, Execucao, gravar_json  # noqa: E402

VERSAO = "wayback-0.1"
SPN = "https://web.archive.org/save/"
INTERVALO_S = 30.0
BARREIRAS = re.compile(r"\b403\b|captcha|cloudflare|verificação de navegador", re.I)
RE_COPIA = re.compile(r"/web/(\d{14})/")


def triagem_valida(tri: Path | None) -> bool:
    """A triagem do juridico sobre esta política: JSON com o item que cita o wayback.py e as oito perguntas (A-010)."""
    if not tri or not tri.is_file():
        return False
    try:
        t = carregar_json(tri)
    except Exception:
        return False
    return "wayback.py" in str(t.get("item", "")) and len(t.get("perguntas", [])) == 8


def _ficha(raiz: Path, ambiente: str) -> dict:
    arq = raiz / "ambientes" / f"{ambiente}.json"
    return carregar_json(arq).get("ficha_de_acesso", {}) if arq.exists() else {}


def _motivo(ficha: dict) -> str | None:
    texto = " ".join(str(ficha.get(k, "")) for k in ("acesso", "robots", "como_buscar", "decisao"))
    m = BARREIRAS.search(texto)
    return m.group(0) if m else None


def barrado(raiz: Path, ambiente: str | None, url: str = "") -> str | None:
    """O motivo, se a ficha do ambiente registra 403, captcha ou verificação de navegador; sem ambiente,
    pelo host do link, contra os hosts das fichas com barreira (A-012)."""
    if ambiente and (m := _motivo(_ficha(raiz, ambiente))):
        return f"a ficha de {ambiente} registra {m!r}"
    host = (urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")
    if not host:
        return None
    for arq in sorted((raiz / "ambientes").glob("AM-*.json")) if (raiz / "ambientes").exists() else []:
        ficha = carregar_json(arq).get("ficha_de_acesso", {})
        if (m := _motivo(ficha)) and host in {(urllib.parse.urlsplit(u).hostname or "").removeprefix("www.")
                                              for u in re.findall(r"https?://[^\s)<>\"']+", json.dumps(
                                                  [ficha.get(k, "") for k in ("endpoint", "link_permanente", "acesso", "como_buscar")],
                                                  ensure_ascii=False))}:  # só os campos de via, não o robô nem as notas
            return f"o link é do host de {arq.stem}, cuja ficha registra {m!r}"
    return None


def falta_que_barra(raiz: Path) -> str | None:
    """A Falta jurídica aberta que barra a captura em si, se houver."""
    pasta = raiz / "acervo" / "faltas"
    for arq in sorted(pasta.glob("*.json")) if pasta.exists() else []:
        f = carregar_json(arq)
        if (f.get("tipo") == "impedimento_juridico" and "scripts/wayback.py" in f.get("onde_aparece", [])
                and f.get("vale_para") != "publicar" and f.get("caminho_de_liberacao", {}).get("estado") != "liberado"):
            return f["id"]
    return None


def capturar(cli: Cliente, url: str) -> str:
    r = cli.pedir(SPN + url)
    if not 200 <= r.status < 300:  # 429 ou 5xx nunca viram cópia (A-011)
        raise RuntimeError(f"HTTP {r.status}: o SPN2 não fez a cópia")
    for onde in (r.url, r.headers.get("Content-Location", ""), r.headers.get("Location", ""), r.corpo[:20000]):
        m = RE_COPIA.search(onde or "")
        if m:
            return f"https://web.archive.org/web/{m.group(1)}/{url}"
    raise RuntimeError(f"HTTP {r.status}: o SPN2 não devolveu o endereço da cópia")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--triagem", type=Path)
    ap.add_argument("--entrada", help="uma ou mais, separadas por vírgula; sem ela, as Entradas sem cópia")
    ap.add_argument("--max", type=int, default=5)
    ap.add_argument("--fixtures", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    tri = (a.triagem if a.triagem.is_absolute() else RAIZ / a.triagem) if a.triagem else None
    if not triagem_valida(tri):
        print("REPROVA: sem a triagem do juridico sobre a política de cópias arquivadas (Lei 9.610; l. 740): "
              "o arquivo tem de ser a triagem do wayback.py, com as oito perguntas")
        return 1
    if barra := falta_que_barra(raiz):
        print(f"BARRADO: a Falta jurídica {barra} está aberta e vale para a captura em si; nada se captura, "
              "e as Entradas ficam com o link permanente (D-020, D-025)")
        return 0
    fx = (a.fixtures if a.fixtures.is_absolute() else RAIZ / a.fixtures) if a.fixtures else None
    cli = Cliente(fixtures=fx, intervalo_s=INTERVALO_S)
    ex = Execucao("wayback", f"cópia no Wayback (SPN2 anônimo), triagem {tri.relative_to(RAIZ).as_posix() if tri.is_relative_to(RAIZ) else tri.name}", simular=a.simular)
    pasta = raiz / "entrada"
    alvos = [x.strip() for x in (a.entrada or "").split(",") if x.strip()]
    entradas = []
    for arq in sorted(pasta.glob("*.json")) if pasta.exists() else []:
        e = carregar_json(arq)
        if e.get("retirado") or e.get("wayback") or not e.get("url_ou_arquivo", "").startswith("http"):
            continue
        if alvos and e["id"] not in alvos:
            continue
        entradas.append((arq, e))
    feitas = puladas = 0
    for arq, e in entradas:
        if feitas >= a.max:
            ex.fora.append(f"{len(entradas) - feitas - puladas} Entrada(s) sem cópia além do máximo de {a.max} por rodada")
            break
        if motivo := barrado(raiz, e.get("ambiente"), e["url_ou_arquivo"]):
            puladas += 1
            ex.fora.append(f"{e['id']}: não captura: {motivo}; fica o link permanente (l. 419)")
            continue
        try:
            copia = capturar(cli, e["url_ou_arquivo"])
        except (BloqueioRobos, BloqueioAntiRobo, RuntimeError) as err:
            ex.erros.append(f"{e['id']}: {err}")
            ex.fora.append(f"{e['id']}: sem cópia ({err})")
            puladas += 1
            continue
        e["wayback"] = copia
        feitas += 1
        if not a.simular:
            gravar_json(arq, e)
        ex.saidas.append(f"entrada/{e['id']}.json")
        ex.resultados.append(f"{e['id']}: cópia {copia}")
    ex.acoes.append(f"scripts/wayback.py --max {a.max}" + (" (fixtures)" if fx else "") + (" --simular" if a.simular else ""))
    ex.olhado.append(f"{len(entradas)} Entrada(s) sem cópia; {feitas} capturada(s), {puladas} pulada(s) ou com erro; "
                     f"{cli.pedidos} pedido(s) HTTP, robots.txt incluído, 1 a cada {int(INTERVALO_S)} s")
    for x in ex.resultados + ex.fora:
        print(x)
    for x in ex.erros:
        print("ERRO", x)
    print(f"{VERSAO}: {ex.id}; {feitas} cópia(s); {ex.gravar_log()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
