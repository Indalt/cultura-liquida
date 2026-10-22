"""Grava um insumo para o planejamento de melhorias (habilidade registrar-melhoria; K-103).

O insumo vem num objeto no formato de esquemas/insumo.schema.json. O script dá o número
seguinte e grava duas linhas: uma na tabela de trilhas/insumos-planejamento.md e outra na
seção 6 do mapa das três frentes (trilhas/planejamento/mapa-tres-frentes.md), que diz o
cartão que leva o insumo. Não usa IA: serve à sessão e à rotina.

Uso:
    python scripts/registrar_melhoria.py <arquivo.json>              # grava
    python scripts/registrar_melhoria.py -                           # o objeto vem pela entrada padrão
    python scripts/registrar_melhoria.py <arquivo.json> --simular    # confere e mostra, sem gravar

Reprova (código 1, sem gravar nada) se:
  - o objeto não passa no esquema de insumo;
  - aparece dado pessoal de terceiros (scripts/procurar_dado_pessoal.py);
  - um campo tem "|" ou quebra de linha (quebraria a tabela);
  - o mesmo texto de insumo já está anotado;
  - a tabela de insumos e a seção 6 do mapa não terminam no mesmo número.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, validar_objeto  # noqa: E402
from procurar_dado_pessoal import achar  # noqa: E402

INSUMOS = RAIZ / "trilhas" / "insumos-planejamento.md"
MAPA = RAIZ / "trilhas" / "planejamento" / "mapa-tres-frentes.md"
LINHA_INSUMO = re.compile(r"^\| (\d+) \|")
TITULO_MAPA = re.compile(r"^## 6\. Insumos 1 a (\d+)")
LINHA_MAPA = re.compile(r"^\| (\d+), ")
CAMPOS_TEXTO = ("origem", "insumo", "aonde", "rotulo", "vira")


def ultimo_numero(linhas: list[str], rx: re.Pattern) -> tuple[int, int]:
    """Devolve (maior número, índice da última linha que casa); (0, -1) se nenhuma casa."""
    num, idx = 0, -1
    for i, l in enumerate(linhas):
        m = rx.match(l)
        if m:
            num, idx = max(num, int(m.group(1))), i
    return num, idx


def secao_6(linhas: list[str]) -> tuple[int, int]:
    """Devolve (índice do título da seção 6, índice da última linha de tabela dela)."""
    ini = next((i for i, l in enumerate(linhas) if TITULO_MAPA.match(l)), -1)
    if ini < 0:
        return -1, -1
    fim = ini
    for i in range(ini + 1, len(linhas)):
        if linhas[i].startswith("## "):
            break
        if linhas[i].startswith("|"):
            fim = i
    return ini, fim


def conferir(e: dict, txt_ins: str, txt_mapa: str) -> list[str]:
    erros = [f"esquema: {x}" for x in validar_objeto(e, carregar_esquema("insumo"))]
    texto = json.dumps(e, ensure_ascii=False, indent=0)
    erros += [f"dado pessoal de terceiros: {tipo}: {s}" for _, tipo, s in achar(texto)]
    for c in CAMPOS_TEXTO:
        v = e.get(c)
        if isinstance(v, str) and ("|" in v or "\n" in v):
            erros.append(f"{c}: tem '|' ou quebra de linha, que quebrariam a tabela")
    if isinstance(e.get("insumo"), str) and len(e["insumo"]) >= 20 and e["insumo"] in txt_ins:
        erros.append("insumo: o mesmo texto já está anotado em trilhas/insumos-planejamento.md")
    n_ins, idx_ins = ultimo_numero(txt_ins.splitlines(), LINHA_INSUMO)
    linhas_mapa = txt_mapa.splitlines()
    ini, _ = secao_6(linhas_mapa)
    if idx_ins < 0:
        erros.append("insumos-planejamento.md: tabela de insumos não encontrada")
    if ini < 0:
        erros.append("mapa-tres-frentes.md: seção '## 6. Insumos 1 a N' não encontrada")
    else:
        n_tit = int(TITULO_MAPA.match(linhas_mapa[ini]).group(1))
        n_tab, _ = ultimo_numero(linhas_mapa[ini:], LINHA_MAPA)
        if not (n_ins == n_tit == n_tab):
            erros.append(f"fora de sincronia: tabela de insumos até {n_ins}, título da seção 6 do mapa até {n_tit}, "
                         f"linhas da seção 6 até {n_tab}; acertar antes de anotar")
    return erros


def montar(e: dict, n: int) -> tuple[str, str]:
    a, m, d = e["data"].split("-")
    linha_ins = f"| {n} | {d}/{m}/{a} | {e['origem']} | {e['insumo']} | {e['aonde']} |"
    linha_mapa = f"| {n}, {e['rotulo']} | {'; '.join(e['frente'])} | {e['vira']} |"
    return linha_ins, linha_mapa


def inserir(caminho: Path, nova: str, apos: int, titulo: tuple[int, str] | None = None) -> None:
    bruto = caminho.read_text(encoding="utf-8")
    fim_linha = "\r\n" if "\r\n" in bruto else "\n"
    linhas = bruto.splitlines()
    if titulo:
        linhas[titulo[0]] = titulo[1]
    linhas.insert(apos + 1, nova)
    caminho.write_text(fim_linha.join(linhas) + (fim_linha if bruto.endswith(("\n", "\r\n")) else ""),
                       encoding="utf-8", newline="")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo", help="JSON com o insumo, ou - para a entrada padrão")
    ap.add_argument("--simular", action="store_true", help="confere e mostra, sem gravar")
    a = ap.parse_args()
    bruto = sys.stdin.read() if a.arquivo == "-" else Path(a.arquivo).read_text(encoding="utf-8")
    e = json.loads(bruto)
    txt_ins = INSUMOS.read_text(encoding="utf-8")
    txt_mapa = MAPA.read_text(encoding="utf-8")
    erros = conferir(e, txt_ins, txt_mapa)
    if erros:
        print("REPROVA: nada foi gravado.")
        for x in erros:
            print(f"    - {x}")
        return 1
    n_ant, idx_ins = ultimo_numero(txt_ins.splitlines(), LINHA_INSUMO)
    n = n_ant + 1
    linha_ins, linha_mapa = montar(e, n)
    if a.simular:
        print(f"PASSA (simulação, nada gravado): seria o insumo {n}")
        print(f"    insumos-planejamento.md: {linha_ins}")
        print(f"    mapa-tres-frentes.md, seção 6: {linha_mapa}")
        return 0
    linhas_mapa = txt_mapa.splitlines()
    ini, fim = secao_6(linhas_mapa)
    titulo = TITULO_MAPA.sub(f"## 6. Insumos 1 a {n}", linhas_mapa[ini], count=1)
    inserir(INSUMOS, linha_ins, idx_ins)
    inserir(MAPA, linha_mapa, fim, (ini, titulo))
    print(f"PASSA: insumo {n} gravado em trilhas/insumos-planejamento.md e na seção 6 do mapa das três frentes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
