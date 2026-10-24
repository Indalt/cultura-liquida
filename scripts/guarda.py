"""A guarda das Entradas em escala (D-045; K-108b): as pegadas por Recorte e o alarme de tamanho.

Três camadas (D-045, item 1):
- **a pegada**, sempre e compacta: uma linha por item visto, num arquivo por Recorte
  (`ambientes/pegadas/RC-nnnn.jsonl`; esquemas/pegada.schema.json), com o ID na fonte, o link, a data,
  o hash do registro de metadados da fonte, o estado da pré-triagem, o motivo e a versão da regra, e a
  Entrada (EN-nnnn) quando há uma, ou quando o item a teve antes da migração;
- **a Entrada de trabalho** (`entrada/`), só do que segue na pré-triagem ou fica em quarentena;
- **o bruto** fora do Git: a fonte o guarda e o Recorte o refaz; o cache local de `metadados.py` fica
  fora da pasta versionada durante o processamento.

O alarme (D-045, item 4): conta os arquivos e soma o tamanho do que o Git versiona ou vai versionar
(`git ls-files -co --exclude-standard`) e avisa acima dos valores do registro (`guarda_alarme`:
20 mil arquivos ou 200 MB, provisórios). A compressão das pegadas de Recortes fechados há muito é
permitida pela D-045 e não está feita: o alarme diz quando ela passa a valer a pena.

Uso como biblioteca: Pegadas, indice_pegadas(), medir().
Uso como script:
    python scripts/guarda.py --medir [--raiz <pasta>] [--limite-arquivos N] [--limite-mb M]   # contagem, tamanho e alarme
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, carregar_valores, validar_objeto  # noqa: E402

VERSAO = "guarda-0.1"
PASTA = Path("ambientes") / "pegadas"


def ler(arq: Path) -> list[dict]:
    if not arq.exists():
        return []
    return [json.loads(x) for x in arq.read_text(encoding="utf-8").splitlines() if x.strip()]


class Pegadas:
    """As pegadas de todos os Recortes: por Recorte, por identificador e os EN-nnnn que elas guardam."""

    def __init__(self, raiz: Path = RAIZ):
        self.pasta = raiz / PASTA
        self.por_recorte: dict[str, list[dict]] = {}
        self.ids_por_recorte: dict[str, set[str]] = {}  # A-004: busca constante, não linear
        self.en_por_identificador: dict[str, str] = {}
        self.ens: set[str] = set()
        self.esquema = carregar_esquema("pegada")
        if self.pasta.exists():
            for arq in sorted(self.pasta.glob("RC-*.jsonl")):
                self.por_recorte[arq.stem] = ler(arq)
        for rc, linhas in self.por_recorte.items():
            self.ids_por_recorte[rc] = {p["identificador"] for p in linhas}
            for p in linhas:
                if p.get("entrada"):
                    self.ens.add(p["entrada"])
                    self.en_por_identificador.setdefault(p["identificador"], p["entrada"])

    def tem(self, recorte: str, identificador: str) -> bool:
        return identificador in self.ids_por_recorte.get(recorte, set())

    def acrescentar(self, recorte: str, linha: dict, gravar: bool = True) -> bool:
        """Grava a linha do item no arquivo do Recorte (uma por identificador). Devolve se era nova."""
        erros = validar_objeto(linha, self.esquema)
        if erros:
            raise ValueError(f"pegada inválida ({recorte}): {'; '.join(erros)}")
        if self.tem(recorte, linha["identificador"]):
            return False
        self.por_recorte.setdefault(recorte, []).append(linha)
        self.ids_por_recorte.setdefault(recorte, set()).add(linha["identificador"])
        if linha.get("entrada"):
            self.ens.add(linha["entrada"])
            self.en_por_identificador.setdefault(linha["identificador"], linha["entrada"])
        if gravar:
            self.pasta.mkdir(parents=True, exist_ok=True)
            with (self.pasta / f"{recorte}.jsonl").open("a", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(linha, ensure_ascii=False) + "\n")
        return True

    def ligar(self, identificador: str, en: str, gravar: bool = True) -> list[str]:
        """Põe o EN-nnnn nas pegadas do identificador que ainda não o têm (o item que ficou fora num
        Recorte e seguiu por outra Consulta; S-001). A triagem de cada Recorte não muda."""
        mudados = []
        for rc, linhas in self.por_recorte.items():
            if identificador not in self.ids_por_recorte.get(rc, set()):
                continue
            for p in linhas:
                if p["identificador"] == identificador and not p.get("entrada"):
                    p["entrada"] = en
                    mudados.append(rc)
        self.ens.add(en)
        self.en_por_identificador.setdefault(identificador, en)
        if gravar:
            for rc in dict.fromkeys(mudados):
                self.reescrever(rc)
        return mudados

    def reescrever(self, recorte: str) -> None:
        self.pasta.mkdir(parents=True, exist_ok=True)
        (self.pasta / f"{recorte}.jsonl").write_text(
            "".join(json.dumps(p, ensure_ascii=False) + "\n" for p in self.por_recorte[recorte]), encoding="utf-8", newline="\n")

    def total(self) -> int:
        return sum(len(v) for v in self.por_recorte.values())


def medir(raiz: Path = RAIZ, limite: dict | None = None) -> dict:
    """Arquivos e MB do que o Git versiona ou vai versionar, contra o alarme do registro."""
    lim = dict(carregar_valores()["valores"]["guarda_alarme"]["valor"], **(limite or {}))
    try:
        saida = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "-z"], cwd=raiz,
                               capture_output=True, check=True).stdout.decode("utf-8")
        arqs = [raiz / p for p in saida.split("\0") if p]
    except (subprocess.CalledProcessError, FileNotFoundError):
        arqs = [p for p in raiz.rglob("*") if p.is_file() and ".git" not in p.parts]
    existentes = [p for p in arqs if p.is_file()]
    mb = sum(p.stat().st_size for p in existentes) / 1024 / 1024
    avisos = []
    if len(existentes) > lim["arquivos"]:
        avisos.append(f"{len(existentes)} arquivos, acima de {lim['arquivos']}")
    if mb > lim["mb"]:
        avisos.append(f"{mb:.1f} MB, acima de {lim['mb']} MB")
    por_pasta: dict[str, int] = {}
    for p in existentes:
        topo = p.relative_to(raiz).parts[0]
        por_pasta[topo] = por_pasta.get(topo, 0) + 1
    return {"arquivos": len(existentes), "mb": round(mb, 1), "limite": lim, "avisos": avisos, "por_pasta": por_pasta}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--medir", action="store_true")
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--limite-arquivos", type=int)
    ap.add_argument("--limite-mb", type=float)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    lim = {k: v for k, v in (("arquivos", a.limite_arquivos), ("mb", a.limite_mb)) if v is not None}
    m = medir(raiz, lim)
    peg = Pegadas(raiz)
    print(f"{VERSAO}: {m['arquivos']} arquivos, {m['mb']} MB (alarme: {m['limite']['arquivos']} arquivos ou {m['limite']['mb']} MB); "
          f"{peg.total()} pegada(s) em {len(peg.por_recorte)} Recorte(s)")
    for av in m["avisos"]:
        print("ALARME", av)
    return 0


if __name__ == "__main__":
    sys.exit(main())
