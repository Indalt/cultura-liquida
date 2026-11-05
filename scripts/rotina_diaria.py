"""Rotina diária sem IA (bloco 10a, camada 1; D-048): agenda, buscas, deduplicação, pegadas, feed,
checagem de links e o relatório do dia. Roda no GitHub Actions (`.github/workflows/rotinas.yml`) e,
à mão, numa conversa de trabalho; não depende de nada da máquina de Vicente (D-048).

Passos:
1. O plano do dia (`agendar.py`, agenda-0.1): que ambientes rodam, com que Consultas e teto; a porta
   nova só abre com a fila de curadoria abaixo de uma semana (l. 472).
2. Para cada ambiente do plano, `recorte.py` (busca ou colheita, deduplicação e pré-triagem por regra;
   D-045). Erro da fonte (anti-robô, robots.txt, HTTP 5xx) fica na linha da rodada e não para a rotina.
3. **Só grava com novidade (D-048):** novidade é Entrada nova, pegada nova (ID não visto) ou o cursor
   de um Recorte não terminado que avançou (o que falta ver). Sem novidade naquele ambiente, com
   `--descartar-sem-novidade` (só no workflow), o que a rodada mudou no Git volta ao estado anterior, e
   fica só a linha da rodada em `trilhas/relatorios/rodadas.jsonl`.
4. O feed de novidades por ID não visto (`feed.py`) e a checagem de uma amostra de links
   (`verificar_links.py`).
5. O relatório do dia, gravado em `trilhas/relatorios/AAAA-MM-DD.md` (`relatorio_dia.py`), sempre.
A consulta da captura no Wayback não está aqui (D-048): só o `ler_fonte.py` a usa, quando a fonte não abre.

Uso:
    python scripts/rotina_diaria.py [--data AAAA-MM-DD] [--descartar-sem-novidade] [--simular]
        [--so AM-0021[,...]] [--links 20] [--fixtures <pasta>] [--raiz <pasta>]
Código 0 = rodou (mesmo com erro de fonte, dito no relatório); 1 = a rotina quebrou (o workflow falha e
o GitHub avisa por e-mail).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
import agendar  # noqa: E402
import guarda  # noqa: E402

VERSAO = "rotina-diaria-0.1"
PY = sys.executable
CAMINHOS_DA_RODADA = ["ambientes/recortes", "ambientes/pegadas", "entrada", "acervo/faltas", "trilhas/logs"]


def fila_atual(raiz: Path) -> int | None:
    import fila_curadoria
    quadro = raiz / "trilhas" / "planejamento" / "quadro.md"
    if not quadro.exists():
        return None
    _, _, linhas = fila_curadoria.tabela_operacao(quadro.read_text(encoding="utf-8"))
    return sum(1 for x in fila_curadoria.abertos(linhas) if fila_curadoria.chama_vicente(x))


def estado_recortes(raiz: Path) -> dict[str, tuple]:
    pasta = raiz / "ambientes" / "recortes"
    saida = {}
    for arq in pasta.glob("*.json") if pasta.exists() else []:
        r = carregar_json(arq)
        saida[r["id"]] = (r.get("estado"), r.get("cursor"), r.get("total_visto"))
    return saida


def contar_entradas(raiz: Path) -> int:
    pasta = raiz / "entrada"
    return sum(1 for _ in pasta.glob("EN-*.json")) if pasta.exists() else 0


def novidade(antes: dict, depois: dict, ent0: int, ent1: int, peg0: int, peg1: int) -> dict:
    avancou = [k for k, v in depois.items()
               if v[0] not in ("percorrido pela busca", "lido por inteiro") and k in antes and v[1] != antes[k][1] and v[1]]
    return {"entradas_novas": ent1 - ent0, "pegadas_novas": peg1 - peg0, "cursores_avancados": avancou}


def git(raiz: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=raiz, capture_output=True, text=True, encoding="utf-8")


def descartar(raiz: Path) -> None:
    """Volta o que a rodada mudou nos caminhos dela (só no workflow, com a árvore limpa antes)."""
    git(raiz, "checkout", "--", *CAMINHOS_DA_RODADA)
    git(raiz, "clean", "-fdq", "--", *CAMINHOS_DA_RODADA)


def rodar_ambiente(raiz: Path, it: dict, simular: bool, fixtures: Path | None = None) -> dict:
    cmd = [PY, str(Path(__file__).resolve().parent / "recorte.py"), "--ambiente", it["ambiente"],
           "--consulta", ",".join(it["consultas"]), "--teto-chamadas", str(it["teto_chamadas"]),
           "--raiz", str(raiz), "--entrada-ref", f"rotina diária ({VERSAO}; K-112, bloco 10a)"]
    if simular:
        cmd.append("--simular")
    if fixtures:
        cmd += ["--fixtures", str(fixtures)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    saida = (r.stdout or "") + (r.stderr or "")
    erros = [x[5:] for x in saida.splitlines() if x.startswith("ERRO ")]
    pedidos = next((x for x in saida.splitlines() if x.startswith("recorte-")), "")
    return {"codigo": r.returncode, "erros": erros, "ultima_linha": pedidos.strip(), "saida": saida}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data")
    ap.add_argument("--descartar-sem-novidade", action="store_true")
    ap.add_argument("--simular", action="store_true", help="roda os Recortes sem gravar (teste)")
    ap.add_argument("--so", help="só estes ambientes (vírgula)")
    ap.add_argument("--links", type=int, default=20, help="links conferidos por dia (verificar_links.py)")
    ap.add_argument("--fixtures", type=Path, help="respostas gravadas (testes, sem rede)")
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    hoje = date.fromisoformat(a.data) if a.data else date.today()
    if a.descartar_sem_novidade and git(raiz, "status", "--porcelain", "--", *CAMINHOS_DA_RODADA).stdout.strip():
        print("a árvore tem mudança antes da rodada: --descartar-sem-novidade recusado")
        return 1
    fila = fila_atual(raiz)
    plano = agendar.plano(raiz, hoje, fila)
    if a.so:
        alvo = set(a.so.split(","))
        plano = [p for p in plano if p["ambiente"] in alvo]
    linhas = []
    quebrou = False
    for it in plano:
        print(f"{it['ambiente']}: {'RODA' if it['roda'] else 'não roda'}; {it['motivo']}")
        if not it["roda"]:
            continue
        antes, ent0, peg0 = estado_recortes(raiz), contar_entradas(raiz), guarda.Pegadas(raiz).total()
        res = rodar_ambiente(raiz, it, a.simular, a.fixtures.resolve() if a.fixtures else None)
        print(res["saida"])
        depois, ent1, peg1 = estado_recortes(raiz), contar_entradas(raiz), guarda.Pegadas(raiz).total()
        nov = novidade(antes, depois, ent0, ent1, peg0, peg1)
        tem = bool(nov["entradas_novas"] or nov["pegadas_novas"] or nov["cursores_avancados"])
        linha = {"data": hoje.isoformat(), "ambiente": it["ambiente"], "consultas": it["consultas"],
                 "motivo": it["motivo"], "intervalo_dias": it.get("intervalo"), **nov, "novidade": tem,
                 "erro": "; ".join(res["erros"])[:500] or None, "codigo": res["codigo"],
                 "gravado": tem and not a.simular, "versao": VERSAO, "regra_agenda": agendar.VERSAO}
        if res["codigo"] != 0:
            quebrou = True
            linha["erro"] = (linha["erro"] or "") + f" recorte.py saiu com código {res['codigo']}"
        if not tem and a.descartar_sem_novidade and not a.simular:
            descartar(raiz)
        linhas.append(linha)
    if not a.simular:
        arq = raiz / agendar.RODADAS
        arq.parent.mkdir(parents=True, exist_ok=True)
        with arq.open("a", encoding="utf-8", newline="\n") as f:
            for x in linhas:
                f.write(json.dumps(x, ensure_ascii=False) + "\n")
        scripts = Path(__file__).resolve().parent
        for cmd in ([PY, str(scripts / "feed.py"), "--data", hoje.isoformat(), "--raiz", str(raiz)],
                    [PY, str(scripts / "verificar_links.py"), "--max", str(a.links), "--data", hoje.isoformat(), "--raiz", str(raiz)],
                    [PY, str(scripts / "relatorio_dia.py"), "--data", hoje.isoformat(), "--raiz", str(raiz),
                     "--saida", str(raiz / "trilhas" / "relatorios" / f"{hoje.isoformat()}.md")]):
            r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
            print((r.stdout or "")[-1500:] + (r.stderr or "")[-1500:])
            if r.returncode != 0:
                quebrou = True
                print(f"FALHOU: {' '.join(Path(c).name for c in cmd[1:2])} (código {r.returncode})")
    print(f"{VERSAO}: {sum(1 for x in linhas)} ambiente(s) rodado(s), "
          f"{sum(1 for x in linhas if x['novidade'])} com novidade; fila {fila}")
    return 1 if quebrou else 0


if __name__ == "__main__":
    sys.exit(main())
