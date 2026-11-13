"""Gera testes/modelos/../relatorio-modelos.md a partir dos logs (bloco 12; K-115a). relatorio-modelos-0.1.

Lê os registros de teste de modelo em trilhas/logs/*.jsonl (entrada_ref começando por "[teste de modelo]",
com "prova <nome>" na entrada_ref) e o resultado de cada rodada em testes/modelos/resultados/ (gravado pelo
`banco.py avaliar --resumo`). Monta a tabela habilidade × agente × modelo × aprovação × tokens × chamadas,
e, por habilidade, o modelo mais barato que passa (regra da Fundação, l. 698: fica o mais barato que passa
nos validadores). A ordem de custo é a do preço por token conferido no C115 (Haiku 5.5 < Sonnet 5.5 < Opus 5.5).
Os registros de teste não são medida de produção (D-051, D-053; orcamento.py).

Uso:
    python testes/modelos/relatorio.py [--saida testes/relatorio-modelos.md] [--conferir]
--conferir  não grava; código 1 se o arquivo gravado difere da tabela calculada agora.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MARCA = "[teste de modelo]"
ORDEM = {"claude-haiku-5-5": 0, "claude-sonnet-5-5": 1, "claude-opus-5-5": 2}
INICIO = "<!-- tabela gerada por testes/modelos/relatorio.py: não editar à mão -->"
FIM = "<!-- fim da tabela gerada -->"


def registros() -> list[dict]:
    saida = []
    for arq in sorted((RAIZ / "trilhas" / "logs").glob("*.jsonl")):
        for l in arq.read_text(encoding="utf-8").splitlines():
            if not l.strip():
                continue
            d = json.loads(l)
            if str(d.get("entrada_ref", "")).startswith(MARCA) and isinstance(d.get("tokens"), int):
                saida.append(d)
    return saida


def resultado(prova: str, modelo: str) -> dict | None:
    achados = sorted((RAIZ / "testes" / "modelos" / "resultados").glob(f"{prova}__{modelo}__*.json"))
    return json.loads(achados[-1].read_text(encoding="utf-8")) if achados else None


def milhar(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def tabela() -> str:
    linhas = ["| Habilidade | Agente | Modelo | Esforço | Prova | Aprovação | Tokens | Chamadas | Execução |",
              "|---|---|---|---|---|---|---|---|---|"]
    por_hab: dict[str, list[tuple[str, bool]]] = {}
    for d in sorted(registros(), key=lambda x: (x["habilidade"], ORDEM.get(x.get("modelo"), 9), x["data_hora"])):
        m = re.search(r"prova ([a-z0-9-]+)", d["entrada_ref"])
        prova = m.group(1) if m else "?"
        r = resultado(prova, d.get("modelo", ""))
        passa = bool(r and r["passa"])
        aprov = "passa" if passa else ("reprova" if r else "sem resultado")
        if r and not passa:
            motivos = [c["texto"] for c in r["checagens"] if not c["ok"]]
            aprov += f" ({len(motivos)} checagem(ns): {motivos[0][:90]})"
        linhas.append(f"| {d['habilidade']} | {d['agente']} | {d.get('modelo')} | {d.get('esforco')} | {prova} | {aprov} | "
                      f"{milhar(d['tokens'])} | {d.get('chamadas')} | {d.get('id', '—')} |")
        por_hab.setdefault(d["habilidade"], []).append((d.get("modelo"), passa))
    linhas += ["", "| Habilidade | Modelo mais barato que passa |", "|---|---|"]
    for h, rodadas in sorted(por_hab.items()):
        passam = sorted({m for m, p in rodadas if p}, key=lambda m: ORDEM.get(m, 9))
        linhas.append(f"| {h} | {passam[0] if passam else 'nenhum dos testados: reforçar o harness antes de subir (l. 698)'} |")
    return "\n".join([INICIO, *linhas, FIM])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--saida", type=Path, default=RAIZ / "testes" / "relatorio-modelos.md")
    ap.add_argument("--conferir", action="store_true")
    a = ap.parse_args()
    t = tabela()
    atual = a.saida.read_text(encoding="utf-8") if a.saida.exists() else ""
    if INICIO in atual and FIM in atual:
        novo = atual[:atual.index(INICIO)] + t + atual[atual.index(FIM) + len(FIM):]
    else:
        novo = atual + ("\n" if atual else "") + t + "\n"
    if a.conferir:
        ok = novo == atual
        print("relatorio-modelos-0.1: " + ("a tabela gravada bate com os logs" if ok else "a tabela gravada NÃO BATE com os logs"))
        return 0 if ok else 1
    a.saida.write_text(novo, encoding="utf-8")
    print(f"relatorio-modelos-0.1: {len(t.splitlines()) - 2} linha(s) de tabela em {a.saida.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
