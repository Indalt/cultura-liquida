"""Casos da manutenção da casa (`scripts/manutencao.py`), rodados por `scripts/rodar_testes.py`.

Cada caso monta uma casa pequena numa pasta temporária (com `git init`), roda a vistoria com `--raiz`
e confere o que ela disse. Nada se grava na pasta real.

Uso: python testes/manutencao/teste_manutencao.py <caso>
Casos: casa-limpa | casa-suja | nao-muda-nada | estrito-suja
Código 0 = o caso se comportou como o critério diz; 1 = não. O caso `estrito-suja` devolve o código da
própria vistoria com `--estrito` (1, de propósito: é o caso que reprova).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SCRIPT = RAIZ / "scripts" / "manutencao.py"

AGENTS = """# AGENTS.md
## Decisões vigentes
- **D-001:** uma decisão.
## Passo corrente
- **Em curso:** K-002.{historia}
## Agentes e habilidades
| Agente | Papel | Habilidades | Modelo inicial |
|---|---|---|---|
| avaliador | triagem | extrair-evidencia | {modelo}, alto |
"""
QUADRO = """# Quadro
## Desenvolvimento
| Coluna | Cartão | Origem | Destino |
|---|---|---|---|
| Concluído | **K-001** um | x | y |
| Fazendo | **K-002** dois | x | y |
{extra}"""


def git(pasta: Path, *args: str) -> None:
    subprocess.run(["git", "-c", "user.name=teste", "-c", "user.email=teste",*args],
                   cwd=pasta, capture_output=True, check=True)


def montar(pasta: Path, suja: bool) -> None:
    def escrever(nome: str, texto: str) -> None:
        p = pasta / nome
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(texto, encoding="utf-8")

    escrever("AGENTS.md", AGENTS.format(modelo="Sonnet 5.5" if suja else "Haiku 5.5",
                                        historia=" Antes: " + "histórico " * 600 if suja else ""))
    escrever("CLAUDE.md", "@AGENTS.md\n")
    escrever("README.md", "Leia `scripts/usado.py`." + (" E `scripts/sumiu.py`." if suja else "") + "\n")
    escrever("RETOMAR.md", "# RETOMAR — " + ("K-001" if suja else "K-002") + "\n")
    escrever("trilhas/planejamento/quadro.md", QUADRO.format(extra="| Fazendo | **K-003** três | x | y |\n" if suja else ""))
    escrever("trilhas/decisoes/D-001.json", "{}\n")
    escrever(".claude/agents/avaliador.md", "---\nmodel: claude-haiku-5-5\neffort: high\n---\n")
    escrever(".claude/skills/extrair-evidencia/SKILL.md", "habilidade\n")
    escrever(".claude/skills/extrair-evidencia/exemplos/casos.json", "{}\n")
    escrever("scripts/usado.py", "print('ok')\n")
    if suja:
        escrever("-", "saída de comando\n")
        escrever("trilhas/decisoes/D-002.json", "{}\n")
        escrever("scripts/orfao.py", "print('ninguém chama')\n")
    git(pasta, "init", "-q")
    git(pasta, "add", "-A")
    git(pasta, "commit", "-q", "-m", "casa")
    if suja:
        (pasta / "solto.txt").write_text("fora do Git\n", encoding="utf-8")


def vistoria(pasta: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), "--raiz", str(pasta), *args],
                          capture_output=True, text=True, encoding="utf-8")


def achados(pasta: Path) -> list[dict]:
    return json.loads(vistoria(pasta, "--json").stdout)["achados"]


def digest(pasta: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(x for x in pasta.rglob("*") if x.is_file() and ".git" not in x.parts):
        h.update(str(p.relative_to(pasta)).encode() + p.read_bytes())
    return h.hexdigest()


def main() -> int:
    caso = sys.argv[1] if len(sys.argv) > 1 else ""
    with tempfile.TemporaryDirectory() as tmp:
        pasta = Path(tmp) / "casa"
        pasta.mkdir()
        montar(pasta, suja=caso != "casa-limpa")
        if caso == "casa-limpa":
            ruins = [a for a in achados(pasta) if a["grau"] != "nota"]
            print(f"casa limpa: {len(ruins)} achado(s)" + "".join(f"\n  {a['olhar']}: {a['o_que']}" for a in ruins))
            return 0 if not ruins else 1
        if caso == "casa-suja":
            vistos = {(a["olhar"], a["grau"]) for a in achados(pasta)}
            esperados = {("raiz", "arrumar"), ("sobras", "arrumar"), ("contexto", "arrumar"), ("decisoes", "arrumar"),
                         ("quadro", "arrumar"), ("retomar", "arrumar"), ("harness", "arrumar"),
                         ("referencias", "olhar"), ("scripts", "olhar"), ("git", "arrumar")}
            faltam = sorted(esperados - vistos)
            print(f"casa suja: {len(esperados) - len(faltam)} de {len(esperados)} sujeiras vistas" + (f"; faltam {faltam}" if faltam else ""))
            return 0 if not faltam else 1
        if caso == "nao-muda-nada":
            antes = digest(pasta)
            vistoria(pasta)
            vistoria(pasta, "--json")
            igual = digest(pasta) == antes
            print("a vistoria não mudou nada" if igual else "a vistoria mudou a pasta")
            return 0 if igual else 1
        if caso == "estrito-suja":
            r = vistoria(pasta, "--estrito")
            print(r.stdout.strip().splitlines()[-1])
            return r.returncode
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
