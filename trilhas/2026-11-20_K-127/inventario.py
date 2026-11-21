"""K-127 (D-059): inventário por script, sem IA — quem usa cada script, esquema e habilidade.

Uso vivo = citado pelo nome em: .github/workflows, .githooks, scripts/ (outro script), testes/ e os
casos das habilidades, .claude/ (agentes e habilidades), ambientes/rotinas.json, AGENTS.md, CLAUDE.md,
README. A trilha (trilhas/, logs) não conta como uso vivo: é registro do caminho, que não se limpa.
Saída: lista.md nesta pasta (uma linha por item: usado por; proposta fica / olhar). Não muda nada.
Uso: python trilhas/2026-11-20_K-127/inventario.py   (PYTHONUTF8=1)
"""
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parents[2]
PASTA = pathlib.Path(__file__).resolve().parent
LUGARES = {
    "workflows": list((RAIZ / ".github" / "workflows").glob("*.yml")),
    "gancho": list((RAIZ / ".githooks").glob("*")),
    "scripts": list((RAIZ / "scripts").glob("*.py")),
    "testes": [p for p in (RAIZ / "testes").rglob("*") if p.is_file() and p.suffix in (".json", ".py", ".md")
               and "fixtures" not in p.parts],
    "harness": [p for p in (RAIZ / ".claude").rglob("*") if p.is_file() and p.suffix in (".md", ".json", ".py")],
    "esquemas": list((RAIZ / "esquemas").glob("*.json")),
    "rotinas": [RAIZ / "ambientes" / "rotinas.json", RAIZ / "ambientes" / "adaptadores.json"],
    "regras": [RAIZ / x for x in ("AGENTS.md", "CLAUDE.md", "README.md") if (RAIZ / x).exists()],
}
TEXTO = {k: [(p, p.read_text(encoding="utf-8", errors="ignore")) for p in v if p.exists()] for k, v in LUGARES.items()}


def usos(alvo: pathlib.Path, nome: str) -> list[str]:
    if nome.endswith(".schema.json"):  # esquema: citado pelo nome inteiro, por "x.schema" ou pela chave "x" entre aspas
        b = re.escape(nome[: -len(".schema.json")])
        pad = re.compile(rf"{b}\.schema|[\"']{b}[\"']")
    else:
        pad = re.compile(r"(?<![\w-])" + re.escape(nome) + r"(?![\w-])")
    achados = []
    for lugar, arqs in TEXTO.items():
        n = sum(1 for p, t in arqs if p.resolve() != alvo.resolve() and pad.search(t))
        if n:
            achados.append(f"{lugar} {n}")
    return achados


def main():
    linhas = ["# Inventário do K-127 (D-059), por script, sem IA", "",
              "Gerado por `inventario.py`. 'Usado por' conta arquivos que citam o nome fora da trilha. "
              "Sem uso vivo = candidato a sair (fica no histórico do Git); a decisão de cada linha vai na lista do lote.", ""]
    grupos = [("Scripts", sorted((RAIZ / "scripts").glob("*.py")), lambda p: p.stem),
              ("Esquemas", sorted((RAIZ / "esquemas").glob("*.json")), lambda p: p.name),
              ("Habilidades", sorted(p for p in (RAIZ / ".claude" / "skills").iterdir() if p.is_dir()), lambda p: p.name),
              ("Agentes", sorted((RAIZ / ".claude" / "agents").glob("*.md")), lambda p: p.stem)]
    sem_uso = []
    for titulo, itens, nome in grupos:
        linhas += [f"## {titulo}", "", "| Item | Usado por | Proposta |", "|---|---|---|"]
        for p in itens:
            if p.name.startswith("_") and p.suffix == ".py":
                u = usos(p, p.stem) or ["(módulo interno)"]
            else:
                u = usos(p, nome(p))
            prop = "fica" if u else "olhar: sem uso vivo"
            if not u:
                sem_uso.append(f"{titulo}: {p.relative_to(RAIZ).as_posix()}")
            linhas.append(f"| `{p.relative_to(RAIZ).as_posix()}` | {', '.join(u) or '—'} | {prop} |")
        linhas.append("")
    linhas += ["## Sem uso vivo", ""] + [f"- {s}" for s in sem_uso]
    (PASTA / "lista.md").write_text("\n".join(linhas) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(sem_uso)} sem uso vivo"); print("\n".join(sem_uso))


if __name__ == "__main__":
    main()
