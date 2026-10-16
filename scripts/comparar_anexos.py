"""Confere que os Anexos A e B da Fundação não mudaram desde o commit 1 (e868a98).

Compara o trecho que vai da linha "## Anexo A" até a linha "## Anexo C" (exclusive) no
arquivo atual com o mesmo trecho em `git show <commit>:<arquivo>`. Normaliza os fins de
linha (CRLF -> LF), porque a cópia de trabalho usa CRLF.

Uso:
    python scripts/comparar_anexos.py [--arquivo 00_Fundacao_Cultura_Liquida.md] [--commit e868a98]
Código 0 = idêntico; 1 = diferente ou trecho não encontrado (mostra as primeiras diferenças).
"""
from __future__ import annotations

import argparse
import difflib
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402

COMMIT_BASE = "e868a98"
ARQUIVO = "00_Fundacao_Cultura_Liquida.md"


def trecho_anexos(texto: str) -> list[str] | None:
    linhas = texto.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    ini = next((i for i, l in enumerate(linhas) if l.startswith("## Anexo A")), None)
    fim = next((i for i, l in enumerate(linhas) if l.startswith("## Anexo C")), None)
    if ini is None or fim is None or fim <= ini:
        return None
    return linhas[ini:fim]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--arquivo", default=ARQUIVO)
    ap.add_argument("--commit", default=COMMIT_BASE)
    a = ap.parse_args()
    atual = (RAIZ / a.arquivo).read_text(encoding="utf-8")
    r = subprocess.run(["git", "show", f"{a.commit}:{a.arquivo}"], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        print(f"ERRO: git show {a.commit}:{a.arquivo} falhou: {r.stderr.decode('utf-8', 'replace').strip()}")
        return 1
    base = r.stdout.decode("utf-8")
    ta, tb = trecho_anexos(atual), trecho_anexos(base)
    if ta is None or tb is None:
        print(f"DIFERENTE: trecho '## Anexo A' .. '## Anexo C' não encontrado em {'atual' if ta is None else a.commit}")
        return 1
    if ta == tb:
        print(f"IDÊNTICO: Anexos A e B ({len(ta)} linhas) iguais ao commit {a.commit} (fins de linha normalizados)")
        return 0
    diff = list(difflib.unified_diff(tb, ta, f"{a.commit}", "atual", lineterm="", n=0))
    print(f"DIFERENTE: {sum(1 for d in diff if d[:1] in '+-' and d[:3] not in ('+++', '---'))} linhas alteradas")
    for d in diff[:40]:
        print("    " + d)
    return 1


if __name__ == "__main__":
    sys.exit(main())
