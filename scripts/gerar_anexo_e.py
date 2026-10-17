"""Gera a tabela do Anexo E da Fundação (ambientes candidatos) a partir do catálogo da pesquisa de 15/10.

Lê as fontes ("sources") de:
  - trilhas/2026-10-15_pesquisa/w16qvy0xk.output.json (frentes FH, PA e MO; o mesmo resultado do
    registro wf_89a76895-c9b.journal.jsonl);
  - trilhas/2026-10-15_pesquisa/wviefxn3h.output.json (lote A).
Junta as repetidas pelo nome (a primeira ocorrência vale) e escreve uma tabela em Markdown:
ambiente, tipo, via de acesso, como buscar (sintaxe), uso, nível, link e termos de uso.

Uso:
    python scripts/gerar_anexo_e.py [--saida arquivo.md]
O texto de cada célula é o do catálogo, sem resumo: só as quebras de linha e as barras verticais
são trocadas, para não quebrar a tabela.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402

PASTA = RAIZ / "trilhas" / "2026-10-15_pesquisa"
ARQUIVOS = [("w16qvy0xk.output.json", "frentes FH, PA e MO"), ("wviefxn3h.output.json", "lote A")]


def fontes(obj, achadas: list[dict]) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "sources" and isinstance(v, list):
                achadas.extend(x for x in v if isinstance(x, dict))
            else:
                fontes(v, achadas)
    elif isinstance(obj, list):
        for v in obj:
            fontes(v, achadas)


def celula(v) -> str:
    if v is None or v == "":
        return "—"
    if isinstance(v, (list, dict)):
        v = json.dumps(v, ensure_ascii=False)
    return str(v).replace("\r", " ").replace("\n", " ").replace("|", "/").strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--saida")
    args = ap.parse_args()

    linhas, vistos = [], set()
    for nome, origem in ARQUIVOS:
        achadas: list[dict] = []
        fontes(json.loads((PASTA / nome).read_text(encoding="utf-8")), achadas)
        for f in achadas:
            chave = celula(f.get("name")).lower()
            if chave in vistos:
                continue
            vistos.add(chave)
            link = f.get("url") or f.get("permalink") or f.get("endpoint")
            linhas.append("| " + " | ".join([
                celula(f.get("name")), celula(f.get("kind")), celula(f.get("access")),
                celula(f.get("how_to_search")), celula(f.get("use")), celula(f.get("level")),
                celula(link), celula(f.get("terms")), origem,
            ]) + " |")

    cab = ("| Ambiente | Tipo | Via de acesso | Como buscar | Uso | Nível | Link | Termos de uso | Origem |\n"
           "|---|---|---|---|---|---|---|---|---|")
    texto = cab + "\n" + "\n".join(linhas) + "\n"
    if args.saida:
        Path(args.saida).write_text(texto, encoding="utf-8")
        print(f"{len(linhas)} ambientes gravados em {args.saida}")
    else:
        sys.stdout.write(texto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
