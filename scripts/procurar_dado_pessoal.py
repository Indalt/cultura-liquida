"""Procura dado pessoal de terceiros em arquivos de texto (regra 5 do brief; D-021).

Procura: e-mail, telefone brasileiro, CPF, @perfil e links de perfil em redes sociais.
Permitidos (não são de terceiros, ou são institucionais): ver PERMITIDOS abaixo.
Cada novo permitido precisa de motivo no comentário.

Uso:
    python scripts/procurar_dado_pessoal.py <arquivo-ou-pasta> [...]
    python scripts/procurar_dado_pessoal.py --git          # arquivos rastreados + preparados no Git
    python scripts/procurar_dado_pessoal.py --texto "..."  # confere um texto
Código 0 = nada achado; 1 = achou (lista arquivo:linha: tipo: trecho).

Também é importado por registrar_log.py (função achar).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402

PERMITIDOS = {
    "vicente@dacaatinga.com.br",       # Vicente, autor e responsável (regra 5 do brief)
    "noreply@anthropic.com",           # linha de atribuição dos commits
    "atendimento@cinemateca.org.br",   # e-mail institucional, mantido no Bloco 1
    # JSON-LD e notação técnica, não são perfis:
    "@context", "@id", "@type", "@graph", "@value", "@language", "@vocab",
    # sintaxe de importação do CLAUDE.md citada nos textos:
    "@caminho", "@path",
    # a própria palavra usada nas regras ("@perfil"):
    "@perfil",
    # notação técnica citada da documentação oficial do Claude Code (mapa de hospedagem, 17/10):
    # versão de uma ação do GitHub ("@v1", "@beta"), menção ao bot da ação ("@claude")
    # e escopo de pacote npm ("@anthropic"); não são perfis de pessoas:
    "@v1", "@beta", "@claude", "@anthropic",
}

# Páginas institucionais das plataformas (termos, políticas, documentação), não perfis:
PAGINAS_INSTITUCIONAIS = re.compile(
    r"/(terms|legal|products|docs|policies|policy|privacy|help|about|business|developers|"
    r"community-guidelines|support|safety|transparency|research|watch|results|feed|hashtag|explore)(?![\w-])", re.I)

PADROES = [
    ("e-mail", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("telefone", re.compile(r"(?:\+55\s?)?\(\d{2}\)\s?9?\d{4}[-\s]?\d{4}\b|\+55\s?\d{2}\s?9?\d{4}[-\s]?\d{4}\b")),
    ("CPF", re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|CPF[:\s]*\d{11}\b")),
    ("@perfil", re.compile(r"(?<![\w.@/\\`])@[A-Za-z0-9_][A-Za-z0-9_.]{1,29}(?![\w/])")),
    ("perfil em rede social", re.compile(
        r"(?:instagram\.com|facebook\.com|fb\.com|tiktok\.com|twitter\.com|x\.com|linkedin\.com/in|threads\.net)"
        r"/@?[A-Za-z0-9_.-]{2,}|youtube\.com/(?:@|c/|channel/|user/)[A-Za-z0-9_.-]+", re.I)),
]

# Casos de teste que DEVEM conter um dado pessoal fictício para provar que o registrar_log.py o recusa.
# Só a varredura de arquivos os pula; a função achar() (usada pelo registrar_log.py) continua acusando.
FIXTURES_COM_DADO_FICTICIO = {
    ".claude/skills/executar-brief/exemplos/erro-log-com-email.json",
    ".claude/skills/registrar-melhoria/exemplos/erro-dado-pessoal.json",
}

EXT_ARQUIVO = re.compile(r"\.(md|json|jsonl|py|txt|csv|yml|yaml|html)$", re.I)
IGNORAR_PASTAS = {".git", ".venv", "legado", "__pycache__", "node_modules"}
EXT_TEXTO = {".md", ".json", ".jsonl", ".py", ".txt", ".csv", ".yml", ".yaml", ".html", ".gitignore", ""}


def achar(texto: str) -> list[tuple[int, str, str]]:
    """Devolve (linha, tipo, trecho) para cada ocorrência não permitida."""
    achados = []
    for n, linha in enumerate(texto.splitlines(), 1):
        for tipo, rx in PADROES:
            for m in rx.finditer(linha):
                s = m.group(0).rstrip(".")
                if s.lower() in PERMITIDOS or s in PERMITIDOS:
                    continue
                if tipo == "@perfil":
                    # e-mail já é tratado; arquivos citados (@AGENTS.md) não são perfil
                    if EXT_ARQUIVO.search(s) or linha[m.end():m.end() + 1] == "@":
                        continue
                if tipo == "perfil em rede social" and PAGINAS_INSTITUCIONAIS.search(s):
                    continue
                if tipo == "e-mail" and s.lower().endswith((".png", ".jpg", ".svg")):
                    continue
                achados.append((n, tipo, s))
    return achados


def arquivos_de(caminhos: list[str]) -> list[Path]:
    saida = []
    for c in caminhos:
        p = Path(c)
        if p.is_dir():
            for f in p.rglob("*"):
                if f.is_file() and not (set(f.relative_to(p).parts) & IGNORAR_PASTAS) and f.suffix.lower() in EXT_TEXTO:
                    saida.append(f)
        elif p.is_file():
            saida.append(p)
    return saida


def arquivos_git() -> list[Path]:
    def ls(*args):
        r = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
        return [x for x in r.stdout.splitlines() if x]
    nomes = set(ls("ls-files")) | set(ls("diff", "--cached", "--name-only")) | set(ls("ls-files", "--others", "--exclude-standard"))
    return [RAIZ / n for n in sorted(nomes) if (RAIZ / n).is_file() and (RAIZ / n).suffix.lower() in EXT_TEXTO]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("caminhos", nargs="*")
    ap.add_argument("--git", action="store_true", help="arquivos rastreados, preparados e novos não ignorados")
    ap.add_argument("--texto")
    a = ap.parse_args()
    total = 0
    if a.texto is not None:
        for n, tipo, s in achar(a.texto):
            print(f"(texto):{n}: {tipo}: {s}")
            total += 1
    arqs = arquivos_git() if a.git else arquivos_de(a.caminhos)
    for f in arqs:
        try:
            if f.resolve().relative_to(RAIZ).as_posix() in FIXTURES_COM_DADO_FICTICIO:
                continue
        except ValueError:
            pass
        try:
            texto = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for n, tipo, s in achar(texto):
            try:
                nome = f.relative_to(RAIZ)
            except ValueError:
                nome = f
            print(f"{nome}:{n}: {tipo}: {s}")
            total += 1
    print(f"{total} ocorrência(s) em {len(arqs)} arquivo(s).", file=sys.stderr)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
