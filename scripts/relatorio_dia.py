"""Relatório calculado do dia e das frentes de trabalho da l. 512 (as linhas de coleta e de
processamento: a CLB do piloto, os vácuos por região e período; não são as três frentes da D-036).
Abre cada conversa de trabalho a partir do bloco 5 e, a partir do bloco 10, cada rotina (l. 505, 512).

Calcula, sem IA: as Entradas novas do dia (por canal e ambiente) e o total; os Recortes por estado;
as Faltas (abertas e novas do dia); a fila de curadoria (cartões que esperam Vicente, contra 15 por
semana); as propostas das rotinas à espera de junção, com o resultado do portão (ramificações
`claude/`; A-10, D-038); a Matriz de Pegadas e Vácuos (vácuos de busca); o consumo da semana da conta
(tabela do checklist do piloto; D-040); a guarda das Entradas (D-045): as pegadas por estado da
pré-triagem e o alarme de tamanho (arquivos e MB do que o Git versiona, contra `guarda_alarme`). Vácuos por região e período do conhecimento são do grafo
(bloco 8): aqui, só o que a coleta mostra.

Uso:
    python scripts/relatorio_dia.py [--data AAAA-MM-DD] [--saida <arquivo.md>] [--raiz <pasta>]
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
import fila_curadoria  # noqa: E402
import orcamento  # noqa: E402
import guarda  # noqa: E402
import pegadas  # noqa: E402

VERSAO = "relatorio-dia-0.2"


def ramificacoes_claude(raiz: Path) -> list[str]:
    try:
        r = subprocess.run(["git", "branch", "-a", "--list", "*claude/*"], cwd=raiz, capture_output=True,
                           text=True, encoding="utf-8", timeout=30)
        return [x.strip(" *") for x in r.stdout.splitlines() if x.strip()]
    except Exception:
        return []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data")
    ap.add_argument("--saida", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    hoje = a.data or date.today().isoformat()
    ents = fila_curadoria.registros(raiz, "entrada")
    novas = [e for e in ents if e.get("data_entrada") == hoje]
    rcs, vacuos = pegadas.matriz(raiz)
    faltas = fila_curadoria.registros(raiz, "acervo/faltas")
    ls = [f"# Relatório do dia {hoje}", "", f"Calculado por `scripts/relatorio_dia.py` ({VERSAO}), sem IA (l. 512).", ""]
    ls.append(f"## Entradas: {len(novas)} nova(s) hoje, {len(ents)} no total")
    por = Counter(f"{e.get('canal')} · {e.get('ambiente', 'sem ambiente')}" for e in novas)
    ls += [f"- {k}: {v}" for k, v in sorted(por.items())] or ["- nenhuma"]
    estados = Counter(e.get("estado") for e in ents)
    if ents:
        ls.append("- por estado (todas): " + ", ".join(f"{k} {v}" for k, v in sorted(estados.items())))
        ls.append(f"- sem cópia no Wayback: {sum(1 for e in ents if not e.get('wayback') and str(e.get('url_ou_arquivo', '')).startswith('http'))}")
    peg = guarda.Pegadas(raiz)
    tri = Counter(p["triagem"] for v in peg.por_recorte.values() for p in v)
    m = guarda.medir(raiz)
    ls += ["", f"## Guarda das Entradas (D-045): {peg.total()} pegada(s) em {len(peg.por_recorte)} Recorte(s)",
           "- por pré-triagem: " + (", ".join(f"{k} {v}" for k, v in sorted(tri.items())) or "nenhuma"),
           f"- hoje: {sum(1 for v in peg.por_recorte.values() for p in v if p['data'] == hoje)} pegada(s) nova(s)",
           f"- tamanho: {m['arquivos']} arquivos, {m['mb']} MB (alarme acima de {m['limite']['arquivos']} arquivos ou {m['limite']['mb']} MB)"]
    ls += [f"- **ALARME:** {av}; as pegadas de Recortes fechados há muito podem ser comprimidas (D-045, item 4)" for av in m["avisos"]]
    ls += ["", f"## Recortes: {len(rcs)}"]
    ls += [f"- {k}: {v}" for k, v in sorted(Counter(r["estado"] for r in rcs).items())] or ["- nenhum"]
    ls += ["", f"## Faltas no acervo: {len(faltas)} ({sum(1 for f in faltas if f.get('data') == hoje)} nova(s) hoje)"]
    ls += [f"- {k}: {v}" for k, v in sorted(Counter(f.get("tipo") for f in faltas).items())] or ["- nenhuma"]
    quadro = raiz / "trilhas" / "planejamento" / "quadro.md"
    if quadro.exists():
        _, _, linhas = fila_curadoria.tabela_operacao(quadro.read_text(encoding="utf-8"))
        fila = [x for x in fila_curadoria.abertos(linhas) if fila_curadoria.chama_vicente(x)]
        ls += ["", f"## Fila de curadoria: {len(fila)} cartão(ões) à espera de Vicente, para {fila_curadoria.LIMITE} por semana"
               + (" — a fila passa de uma semana" if len(fila) > fila_curadoria.LIMITE else "")]
        ls += [f"- {x.split('|')[2].strip()[:140]}" for x in fila]
        pend = len(fila_curadoria.pendencias(raiz, fila_curadoria.TERMOS_PILOTO))
        ls.append(f"- itens no acervo que pedem cartão: {pend} (os novos se abrem com `fila_curadoria.py --abrir-cartoes`)")
    ram = ramificacoes_claude(raiz)
    ls += ["", f"## Propostas das rotinas à espera de junção: {len(ram)}"]
    ls += [f"- {x}: portão não rodado (o portão é do bloco 10)" for x in ram] or ["- nenhuma (as rotinas são do bloco 10)"]
    ls += ["", f"## Vácuos de busca: {len(vacuos)} (Matriz de Pegadas e Vácuos, `scripts/pegadas.py`)"]
    ls += [f"- {v}" for v in vacuos[:20]] + ([f"- … mais {len(vacuos) - 20}"] if len(vacuos) > 20 else [])
    ck = raiz / "trilhas" / "2026-10-17_execucao-piloto.md"
    ls += ["", "## Consumo da semana da conta (D-040)"]
    if ck.exists():
        try:
            semana, dev, fora, avisos = orcamento.usado_na_semana(ck, None)
            ls.append(f"- semana {semana}: desenvolvimento {dev:.0f} pp de {orcamento.ORC['teto_desenvolvimento_pp']}; fora do projeto {fora:.0f} pp")
            ls += [f"- {x}" for x in avisos]
        except SystemExit as e:
            ls.append(f"- {e}")
    else:
        ls.append("- sem o checklist do piloto")
    t = "\n".join(ls) + "\n"
    if a.saida:
        s = a.saida if a.saida.is_absolute() else RAIZ / a.saida
        s.parent.mkdir(parents=True, exist_ok=True)
        s.write_text(t, encoding="utf-8")
    print(t)
    print(f"{VERSAO}: {len(novas)} Entrada(s) nova(s), {len(rcs)} Recorte(s), {len(faltas)} Falta(s), {len(vacuos)} vácuo(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
