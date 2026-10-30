"""Junta a saída de um agente gravada em arquivos pequenos num JSON só (K-111; insumos 29, 71 e 74).

Os agentes sem a ferramenta Write gravam por Bash, e no Windows um comando acima de uns 8 mil caracteres
falha ("unexpected EOF"); heredoc com JSON longo e `python -c` com texto de fonte quebram aspas e barras.
O jeito pronto: um arquivo pequeno por item (`<pasta>/001.json`, `002.json`...; cada um um objeto JSON)
e, no fim, este script, que os lê em ordem de nome, monta a lista e grava um arquivo só, que o agente
valida por arquivo (`scripts/validar.py <esquema> <arquivo>`), sem heredoc.

Uso:
    python scripts/juntar_saida.py <pasta> --saida <arq.json> [--chave itens] [--base base.json] [--esquema <nome>]
--saida -  só mostra o resultado, sem gravar
--chave   o campo da lista no JSON final (padrão: "itens"); sem --base, o JSON final é {chave: [...]}
--base    um JSON pequeno com os outros campos (ex.: o arquivo, a data, o verificador); a lista entra nele
--esquema valida o resultado pelo esquema (esquemas/<nome>.schema.json) antes de gravar
Código 0 = gravado; 1 = arquivo ilegível ou resultado fora do esquema (nada se grava).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import carregar_esquema, validar_objeto  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pasta", type=Path)
    ap.add_argument("--saida", type=Path, required=True)
    ap.add_argument("--chave", default="itens")
    ap.add_argument("--base", type=Path)
    ap.add_argument("--esquema")
    a = ap.parse_args()
    itens, erros = [], []
    for arq in sorted(p for p in a.pasta.glob("*.json") if p.resolve() != a.saida.resolve() and p != a.base):
        try:
            itens.append(json.loads(arq.read_text(encoding="utf-8")))
        except Exception as e:
            erros.append(f"{arq.name}: JSON ilegível ({e})")
    if erros:
        print("REPROVA (nada gravado):", *erros, sep="\n  ")
        return 1
    final = json.loads(a.base.read_text(encoding="utf-8")) if a.base else {}
    final[a.chave] = itens
    if a.esquema:
        erros = validar_objeto(final, carregar_esquema(a.esquema))
        if erros:
            print("REPROVA (nada gravado):", *erros[:10], sep="\n  ")
            return 1
    a.saida.write_text(json.dumps(final, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(itens)} item(ns) em {a.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
