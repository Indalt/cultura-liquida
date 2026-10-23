"""Conta da conversa antes de abrir um agente, em pontos percentuais (pp) do limite semanal
da conta (D-040; brief de execuções, seção 0; valor orcamento de esquemas/valores-provisorios.json).

Folga da conversa (desenvolvimento):
    H = o menor entre (teto_desenvolvimento_pp − o que o desenvolvimento já usou na semana),
        (teto_projeto_pp − o que o projeto já usou na semana) e (linha_conta_pct − A0).
No planejamento, sem o primeiro termo (o planejamento usa o resto do teto do projeto).
Abre-se o lote se
    conversa_principal_pp + pp_por_100mil_tokens × (tokens dos agentes já rodados na conversa ÷ 100 mil)
    + pp_por_100mil_tokens × (estimativa do lote ÷ 100 mil) ≤ H,
sem folga de 2× nem margem: a conversa não para antes do teto. Se não couber, é a Parada (b).

De onde vem cada número:
- A0 e a janela de 5 h: a leitura de Vicente ao abrir (--a0, --janela).
- O que o desenvolvimento já usou na semana: a soma da coluna pp das linhas da frente
  "desenvolvimento" na tabela "Semana da conta" do checklist do piloto, na semana da última linha
  (ou --semana). O que o projeto já usou: A0, menos as linhas "fora do projeto" da semana; todo
  uso sem linha conta como do projeto, como no K-005. --dev-usado e --projeto-usado substituem.
- A estimativa do lote: a última medida do mesmo agente com a mesma habilidade nos logs
  (trilhas/logs/*.jsonl, tokens do retorno do Agent); sem medida, estimativa_sem_medida. --estimativa substitui.
- Com a janela de 5 h acima de janela_5h_lote_unico_pct: só um lote, e a conversa fecha com o estado salvo.

Uso:
    python scripts/orcamento.py --a0 51 --janela 48 --agente auditor --habilidade verificar-fundacao
        [--frente desenvolvimento|planejamento] [--medidos-conversa 120000 ...] [--estimativa N]
        [--semana 21/10-28/10] [--dev-usado X] [--projeto-usado Y] [--checklist <md>] [--logs <pasta>]
Código 0 = PODE abrir o agente; 1 = PARAR (Parada b, com o estado salvo).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_valores  # noqa: E402

ORC = carregar_valores()["valores"]["orcamento"]["valor"]
VERSAO = ORC["versao_regra"]
CHECKLIST = RAIZ / "trilhas" / "2026-10-17_execucao-piloto.md"
LOGS = RAIZ / "trilhas" / "logs"
CABECALHO = "| Semana da conta |"


def numero(cel: str) -> float | None:
    m = re.fullmatch(r"\s*~?\s*(-?\d+(?:[.,]\d+)?)\s*", cel)
    return float(m.group(1).replace(",", ".")) if m else None


def linhas_semana(checklist: Path) -> list[dict]:
    """As linhas da tabela "Semana da conta" do checklist: semana, frente, cartão, pp."""
    linhas, dentro = [], False
    for l in checklist.read_text(encoding="utf-8").splitlines():
        if l.startswith(CABECALHO):
            dentro, cols = True, [c.strip().lower() for c in l.strip("|").split("|")]
            continue
        if dentro:
            if not l.startswith("|"):
                break
            cel = [c.strip() for c in l.strip().strip("|").split("|")]
            if set(cel[0]) <= set("-: "):
                continue
            r = dict(zip(cols, cel))
            linhas.append({"semana": r.get("semana da conta", ""), "frente": r.get("frente", "").lower(),
                           "cartao": r.get("cartão", ""), "pp": numero(r.get("pp", ""))})
    return linhas


def usado_na_semana(checklist: Path, semana: str | None) -> tuple[str, float, float, list[str]]:
    """(semana, pp do desenvolvimento, pp fora do projeto, avisos)."""
    linhas = linhas_semana(checklist)
    if not linhas:
        raise SystemExit(f"sem a tabela '{CABECALHO.strip('| ')}' em {checklist}: informe --dev-usado e --projeto-usado")
    semana = semana or linhas[-1]["semana"]
    da = [l for l in linhas if l["semana"] == semana]
    avisos = [f"linha sem pp ({l['cartao'] or l['frente']}): não entra na soma" for l in da if l["pp"] is None]
    dev = sum(l["pp"] or 0 for l in da if l["frente"].startswith("desenvolvimento"))
    fora = sum(l["pp"] or 0 for l in da if l["frente"].startswith("fora"))
    return semana, dev, fora, avisos


def estimativa_dos_logs(logs: Path, agente: str, habilidade: str) -> tuple[int, str]:
    """A última medida do mesmo agente com a mesma habilidade; sem medida, a do registro."""
    ultima = None
    for arq in sorted(logs.glob("*.jsonl")):
        for l in arq.read_text(encoding="utf-8").splitlines():
            if not l.strip():
                continue
            d = json.loads(l)
            if d.get("agente") == agente and d.get("habilidade") == habilidade and isinstance(d.get("tokens"), int):
                if ultima is None or d.get("data_hora", "") >= ultima.get("data_hora", ""):
                    ultima = d
    if ultima:
        return ultima["tokens"], f"última medida de {agente}/{habilidade} ({ultima.get('data_hora', '')[:16]})"
    return ORC["estimativa_sem_medida"], f"{agente}/{habilidade} sem medida: estimativa_sem_medida"


def milhar(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def fmt(x: float) -> str:
    return f"{x:.2f}".replace(".", ",")


def conta(a0: float, dev_usado: float, projeto_usado: float, medidos: list[int], estimativa: int,
          frente: str) -> tuple[bool, float, float, list[str]]:
    k, m = ORC["pp_por_100mil_tokens"], ORC["conversa_principal_pp"]
    termos = {"teto do projeto": ORC["teto_projeto_pp"] - projeto_usado, "linha da conta": ORC["linha_conta_pct"] - a0}
    if frente == "desenvolvimento":
        termos = {"teto do desenvolvimento": ORC["teto_desenvolvimento_pp"] - dev_usado, **termos}
    h = min(termos.values())
    gasto = m + k * sum(medidos) / 1e5 + k * estimativa / 1e5
    linhas = [f"H = o menor entre " + ", ".join(f"{n} {fmt(v)}" for n, v in termos.items()) + f" = {fmt(h)} pp",
              f"conta = {fmt(m)} (conversa principal) + {fmt(k * sum(medidos) / 1e5)} ({milhar(sum(medidos))} tokens"
              f" já rodados) + {fmt(k * estimativa / 1e5)} (lote de {milhar(estimativa)} tokens) = {fmt(gasto)} pp"]
    return gasto <= h + 1e-9, h, gasto, linhas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--a0", type=float, required=True, help="uso semanal da conta ao abrir (%%), lido por Vicente")
    ap.add_argument("--janela", type=float, help="uso da janela de 5 h ao abrir (%%), lido por Vicente")
    ap.add_argument("--frente", choices=["desenvolvimento", "planejamento"], default="desenvolvimento")
    ap.add_argument("--agente")
    ap.add_argument("--habilidade")
    ap.add_argument("--estimativa", type=int)
    ap.add_argument("--medidos-conversa", type=int, nargs="*", default=[],
                    help="tokens de cada agente já rodado nesta conversa (retorno do Agent)")
    ap.add_argument("--semana")
    ap.add_argument("--dev-usado", type=float)
    ap.add_argument("--projeto-usado", type=float)
    ap.add_argument("--checklist", type=Path, default=CHECKLIST)
    ap.add_argument("--logs", type=Path, default=LOGS)
    a = ap.parse_args()
    chk = a.checklist if a.checklist.is_absolute() else RAIZ / a.checklist
    logs = a.logs if a.logs.is_absolute() else RAIZ / a.logs

    avisos: list[str] = []
    if a.dev_usado is None or a.projeto_usado is None:
        semana, dev, fora, avisos = usado_na_semana(chk, a.semana)
        print(f"semana da conta {semana}: desenvolvimento {fmt(dev)} pp; fora do projeto {fmt(fora)} pp (checklist)")
    dev_usado = a.dev_usado if a.dev_usado is not None else dev
    projeto_usado = a.projeto_usado if a.projeto_usado is not None else a.a0 - fora

    if a.estimativa is not None:
        estimativa, origem = a.estimativa, "informada (--estimativa)"
    elif a.agente and a.habilidade:
        estimativa, origem = estimativa_dos_logs(logs, a.agente, a.habilidade)
    else:
        raise SystemExit("informe --agente e --habilidade (estimativa pelos logs) ou --estimativa")
    print(f"estimativa do lote: {milhar(estimativa)} tokens, {origem}")

    pode, h, gasto, linhas = conta(a.a0, dev_usado, projeto_usado, a.medidos_conversa, estimativa, a.frente)
    for l in avisos + linhas:
        print(l)
    if a.janela is not None and a.janela > ORC["janela_5h_lote_unico_pct"]:
        print(f"janela de 5 h em {fmt(a.janela)}% (acima de {ORC['janela_5h_lote_unico_pct']}%): "
              "só um lote, e a conversa fecha com o estado salvo")
    print(f"{VERSAO}: " + ("PODE abrir o agente" if pode else
                          "PARAR (Parada b): o lote não cabe na folga; salvar o estado, commit e push"))
    return 0 if pode else 1


if __name__ == "__main__":
    sys.exit(main())
