"""Cabeçalhos de agentes e habilidades (cabecalhos-0.1; sem IA): reprova o que o Claude Code não carregaria.

Por quê (insumo 105; D-059, K-127): em 30/10 as descrições do rastreador e da guia-de-liberacao ganharam
dois-pontos sem aspas no cabeçalho YAML, o Claude Code deixou de carregá-los, e a suíte não viu. Esta
checagem roda na suíte (rodar_testes.py), logo no pre-commit, na validação do GitHub e no portão da rotina.

O que confere, em .claude/agents/*.md e .claude/skills/*/SKILL.md, sem biblioteca de YAML:
- o arquivo começa por '---' e o cabeçalho fecha com outro '---';
- 'name' e 'description' existem, e o 'name' é o nome do arquivo (agente) ou da pasta (habilidade);
- valor sem aspas não traz ': ' nem ' #', não termina em ':' e não começa por caractere reservado do YAML
  (o que faria o cabeçalho não carregar ou mudar de sentido).

Uso: python scripts/checar_cabecalhos.py [--claude <pasta com agents/ e skills/>]  (padrão: a .claude do projeto; os
     casos de teste usam pastas sem ponto, para o Claude Code não as ler como habilidades)   (código 1 se algum cabeçalho reprova)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VERSAO = "cabecalhos-0.1"
RESERVADOS = tuple("&*!|>%@`{[")


def checar(arq: Path, esperado: str) -> list[str]:
    linhas = arq.read_text(encoding="utf-8").splitlines()
    if not linhas or linhas[0].strip() != "---":
        return [f"{arq}: não começa por '---'"]
    try:
        fim = next(i for i, x in enumerate(linhas[1:], 1) if x.strip() == "---")
    except StopIteration:
        return [f"{arq}: o cabeçalho não fecha com '---'"]
    erros, chaves = [], {}
    for n, x in enumerate(linhas[1:fim], 2):
        m = re.match(r"^([A-Za-z_][\w-]*):(.*)$", x)
        if not m:
            continue  # item de lista ou continuação
        chave, valor = m.group(1), m.group(2).strip()
        chaves[chave] = valor.strip("\"'")
        if not valor or valor[0] in "\"'":
            continue
        if ": " in valor or " #" in valor or valor.endswith(":") or valor.startswith(RESERVADOS):
            erros.append(f"{arq}, l. {n}: valor de '{chave}' sem aspas com caractere que quebra o YAML")
    for c in ("name", "description"):
        if c not in chaves:
            erros.append(f"{arq}: falta '{c}' no cabeçalho")
    if chaves.get("name") and chaves["name"] != esperado:
        erros.append(f"{arq}: name '{chaves['name']}' diferente de '{esperado}'")
    return erros


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--claude", type=Path, default=Path(__file__).resolve().parent.parent / ".claude")
    base = ap.parse_args().claude
    erros, n = [], 0
    for a in sorted((base / "agents").glob("*.md")):
        erros += checar(a, a.stem); n += 1
    for s in sorted((base / "skills").glob("*/SKILL.md")):
        erros += checar(s, s.parent.name); n += 1
    for e in erros:
        print("CABEÇALHO:", e)
    print(f"{VERSAO}: {n} cabeçalhos; " + (f"{len(erros)} reprovado(s)" if erros else "em ordem"))
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
