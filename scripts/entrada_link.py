"""Entrada por link ou documento trazido por Vicente (§5.4, canal da fase 1, l. 449; D-035).

Mesmo fluxo das outras Entradas: uma Entrada por item (deduplicação pelo DOI ou handle do link, e,
sem eles, pelo próprio link), em `entrada/`, com canal, data, origem e "pessoa" como executor, e o
localizador (onde, no item, está o que se trouxe). Documento: só o nome do arquivo e a soma SHA-256 do
conteúdo (a chave da deduplicação), e o arquivo fica fora da pasta versionada (texto integral fora do Git, l. 100); nunca o conteúdo.
Reprova (código 1, nada gravado) sem localizador, ou sem link nem arquivo.

Uso:
    python scripts/entrada_link.py --url https://... --localizador "p. 12" [--ambiente AM-0061]
        [--nota "..."] [--raiz <pasta>] [--simular]
    python scripts/entrada_link.py --arquivo nome-do-arquivo.pdf --localizador "folha 3" [...]
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402
from _coleta import Execucao  # noqa: E402
import deduplicar  # noqa: E402

VERSAO = "entrada-link-0.1"
CANAL = "link ou documento trazido por Vicente"
EXECUTOR = "Vicente (pessoa), link ou documento trazido"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url")
    ap.add_argument("--arquivo")
    ap.add_argument("--localizador", default="")
    ap.add_argument("--ambiente")
    ap.add_argument("--nota")
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    erros = []
    if not (a.url or a.arquivo):
        erros.append("sem link nem arquivo")
    if a.url and not a.url.startswith("http"):
        erros.append("o link não começa por http")
    if not a.localizador.strip():
        erros.append("sem localizador (l. 449: registro com localizador)")
    if erros:
        print("REPROVA: nada gravado.")
        for e in erros:
            print("    -", e)
        return 1
    if a.arquivo:
        doc = Path(a.arquivo)
        if not doc.is_file():
            print(f"REPROVA: o arquivo {doc.name} não existe na máquina; nada gravado.")
            return 1
        soma = hashlib.sha256(doc.read_bytes()).hexdigest()
    # o documento se identifica pelo conteúdo, não pelo nome: dois arquivos homônimos são dois itens (A-008)
    alvo = a.url or f"arquivo: {Path(a.arquivo).name} (sha256 {soma}; fora da pasta versionada)"
    ex = Execucao("entrada-link", f"{CANAL}: {alvo}", simular=a.simular)
    ind = deduplicar.Indice(raiz)
    ident = None
    if a.url:
        k = deduplicar.chave(a.ambiente or "AM-0000", a.url.strip(), [a.url])
        if k.startswith(("doi:", "hdl:")):
            ident = k
        elif a.ambiente:
            ident = f"{a.ambiente}:{a.url.strip()}"
    id_, nova = deduplicar.registrar(
        ind, identificador=ident, url=alvo, canal=CANAL, origem=ex.origem(EXECUTOR, VERSAO),
        ambiente=a.ambiente, localizador=a.localizador.strip(), nota=a.nota, gravar=not a.simular)
    if nova:
        ex.saidas.append(f"entrada/{id_}.json")
        ex.resultados.append(f"{id_}: Entrada nova, canal {CANAL}, localizador {a.localizador.strip()!r}")
    else:
        ex.resultados.append(f"{id_}: o item já tem Entrada; nada novo (uma Entrada por item, l. 435)")
    ex.acoes.append("scripts/entrada_link.py" + (" --simular" if a.simular else ""))
    ex.olhado.append(f"o item trazido por Vicente ({alvo}) e as Entradas de entrada/, para a deduplicação")
    ex.fora.append("o conteúdo do item: nada se abriu nem se baixou; a triagem é do bloco 7")
    for x in ex.resultados:
        print(x)
    print(f"{VERSAO}: {ex.id}; {ex.gravar_log(fonte='pessoa')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
