"""Sorteia a amostra da segunda leitura, com semente registrada (bloco 3; D-026; padrão A-04,
D-038; valor amostra_sorteada de esquemas/valores-provisorios.json). Regra amostra-0.2.

Universo: o que a ferramenta produziu desde a amostra anterior, em entrada/ e acervo/ (por
exemplo Entradas, Trechos, Evidências, Faltas e CLB situadas; D-017): os registros que
nenhuma amostra anterior de <raiz>/trilhas/amostras/ teve no universo (regra amostra-0.2;
achado A-013 do K-105). Retirados ficam fora. O item marcado por sustentar aviso, saúde
ou política sai do sorteio e vai à lista "lidos todos, fora da amostra" (D-038).
Sorteio: random.Random(semente).sample(universo em ordem, min(itens, tamanho)). A amostra
audita a ferramenta (D-037, diretriz 2) e é lida pelo auditor, fora da cota de Vicente.

Uso:
    python scripts/sortear_amostra.py [--raiz <pasta>] [--semente N] [--gravar]
    python scripts/sortear_amostra.py --conferir <amostra.json>
--gravar grava <raiz>/trilhas/amostras/<data>_amostra.json.
--conferir refaz o sorteio pela semente e pelo universo gravados; código 1 se não bate.
"""
from __future__ import annotations

import argparse
import json
import random
import secrets
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, onde_esta_no_layout  # noqa: E402
from _comum import RAIZ, carregar_json, carregar_valores  # noqa: E402

VERSAO = "amostra-0.2"
ITENS = carregar_valores()["valores"]["amostra_sorteada"]["valor"]["itens"]


def sortear(universo: list[str], semente: int) -> list[str]:
    return sorted(random.Random(semente).sample(sorted(universo), min(ITENS, len(universo))))


def ja_vistos(raiz: Path) -> tuple[str | None, set[str]]:
    """A data da última amostra e os IDs que já entraram no universo (ou na leitura de todos)
    de alguma amostra anterior: o novo universo é o resto (achado A-013 do K-105)."""
    pasta = raiz / "trilhas" / "amostras"
    ams = [carregar_json(p) for p in sorted(pasta.glob("*_amostra*.json"))] if pasta.exists() else []
    vistos = {i for a in ams for i in a.get("universo", []) + a.get("lidos_todos_fora_da_amostra", [])}
    return max((a["data"] for a in ams if a.get("data")), default=None), vistos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--semente", type=int)
    ap.add_argument("--gravar", action="store_true")
    ap.add_argument("--conferir", type=Path)
    a = ap.parse_args()
    if a.conferir:
        am = carregar_json(a.conferir if a.conferir.is_absolute() else RAIZ / a.conferir)
        refeito = sortear(am["universo"], am["semente"])
        if refeito != sorted(am["itens"]):
            print(f"NÃO BATE: a semente {am['semente']} sobre o universo gravado dá {refeito}, e a amostra diz {sorted(am['itens'])}")
            return 1
        print(f"a amostra bate com a semente {am['semente']} ({len(refeito)} itens de {len(am['universo'])})")
        return 0
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    indice, onde, _ = carregar_acervo(raiz)
    corte, vistos = ja_vistos(raiz)
    universo, marcados = [], []
    for i, r in sorted(indice.items()):
        if r.get("retirado") or i in vistos or not onde_esta_no_layout(onde[i][0], raiz, ("entrada", "acervo")):
            continue
        (marcados if r.get("sustenta_aviso_saude_politica") else universo).append(i)
    semente = a.semente if a.semente is not None else secrets.randbits(32)
    itens = sortear(universo, semente)
    am = {"data": date.today().isoformat(), "versao_regra": VERSAO, "semente": semente, "corte": corte,
          "tamanho_regra": ITENS, "universo": universo, "itens": itens,
          "lidos_todos_fora_da_amostra": marcados,
          "nota": "lida pelo auditor depois dos scripts; audita a ferramenta (D-037, diretriz 2); sem achado também vira linha de log"}
    print(json.dumps(am, ensure_ascii=False, indent=2))
    if a.gravar:
        pasta = raiz / "trilhas" / "amostras"
        pasta.mkdir(parents=True, exist_ok=True)
        (pasta / f"{am['data']}_amostra.json").write_text(json.dumps(am, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{VERSAO}: semente {semente}; {len(itens)} de {len(universo)} sorteados; {len(marcados)} marcados lidos fora da amostra")
    return 0


if __name__ == "__main__":
    sys.exit(main())
