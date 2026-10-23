"""Conta do ritmo do piloto (cartão K-005), sem IA.

Lê dados-ritmo.json (leituras do uso da conta informadas por Vicente, as conversas entre elas
e as chamadas que o brief prevê no resto do piloto) e os logs de trilhas/logs/, e imprime em
Markdown:
  1. os pontos percentuais (pp) da conta por intervalo entre duas leituras e por frente;
  2. o ajuste, por mínimos quadrados, das conversas de desenvolvimento: pp = m x conversas +
     k x (tokens de agentes / 100 mil). É estimativa com 3 pontos e leituras inteiras; a medida
     é só o pp de cada intervalo;
  3. a estimativa de tokens por agente e habilidade, tirada dos logs (a última medida do mesmo
     agente com a mesma habilidade; sem medida, a média dos lotes de agentes Sonnet);
  4. a previsão do resto do piloto em pp (baixa, central, alta) e as semanas de pp por meta.

Uso:
    python calcular_ritmo.py            # imprime as tabelas
    python calcular_ritmo.py --json     # imprime os números em JSON
"""
from __future__ import annotations

import argparse
import json
import math
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
LOGS = RAIZ / "trilhas" / "logs"


def br(x: float, casas: int = 0) -> str:
    """Número no formato brasileiro: 1.234,5."""
    s = f"{x:,.{casas}f}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".")


def carregar_dados() -> dict:
    return json.loads((AQUI / "dados-ritmo.json").read_text(encoding="utf-8"))


def medidas_dos_logs() -> list[dict]:
    """Lotes de agente com tokens, gravados pelo curador (o número do retorno do Agent)."""
    lotes = []
    for f in sorted(LOGS.glob("*.jsonl")):
        for n, linha in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if not linha.strip():
                continue
            d = json.loads(linha)
            if d.get("fonte_do_registro") != "curador" or d.get("agente") == "curador":
                continue
            if not isinstance(d.get("tokens"), int) or d["tokens"] <= 0:
                continue
            lotes.append({
                "agente": d["agente"], "habilidade": d.get("habilidade"), "modelo": d.get("modelo"),
                "tokens": d["tokens"], "chamadas": d.get("chamadas"), "data_hora": d.get("data_hora"),
                "arquivo": f"trilhas/logs/{f.name}, l. {n}",
            })
    lotes.sort(key=lambda x: x["data_hora"] or "")
    return lotes


def estimativas(lotes: list[dict]) -> tuple[dict, float]:
    por_chave: dict[tuple[str, str], list[dict]] = {}
    for l in lotes:
        por_chave.setdefault((l["agente"], l["habilidade"]), []).append(l)
    tabela = {}
    for chave, ls in por_chave.items():
        t = [x["tokens"] for x in ls]
        tabela[chave] = {"n": len(t), "ultima": ls[-1]["tokens"], "min": min(t), "max": max(t),
                         "media": sum(t) / len(t), "modelo": ls[-1]["modelo"]}
    sonnet = [l["tokens"] for l in lotes if (l["modelo"] or "").startswith("claude-sonnet")]
    return tabela, sum(sonnet) / len(sonnet)


def tokens_da_chamada(ag: dict, tabela: dict, media_sonnet: float) -> tuple[float, str]:
    hab = ag.get("proxy") if ag.get("proxy") not in (None, "media_sonnet") else ag["habilidade"]
    if ag.get("proxy") == "media_sonnet":
        return media_sonnet, "média Sonnet"
    chave = (ag["agente"], hab)
    if chave in tabela:
        return float(tabela[chave]["ultima"]), f"última de {ag['agente']}/{hab}"
    return media_sonnet, "sem medida: média Sonnet"


def ajuste(intervalos: list[dict]) -> dict:
    """Mínimos quadrados sem intercepto: pp = m * conversas + k * tokens/100 mil."""
    X = [(i["n_conversas"], i["tokens_agentes"] / 100_000) for i in intervalos]
    y = [i["pp"] for i in intervalos]
    s11 = sum(a * a for a, _ in X)
    s12 = sum(a * b for a, b in X)
    s22 = sum(b * b for _, b in X)
    t1 = sum(a * v for (a, _), v in zip(X, y))
    t2 = sum(b * v for (_, b), v in zip(X, y))
    det = s11 * s22 - s12 * s12
    m = (t1 * s22 - t2 * s12) / det
    k = (s11 * t2 - s12 * t1) / det
    resid = [v - (m * a + k * b) for (a, b), v in zip(X, y)]
    gl = len(y) - 2
    s2 = sum(r * r for r in resid) / gl if gl > 0 else float("nan")
    return {"m": m, "k": k, "ep_m": math.sqrt(s2 * s22 / det), "ep_k": math.sqrt(s2 * s11 / det),
            "residuos": resid, "graus_de_liberdade": gl}


def prever(resto: list[dict], tabela: dict, media_sonnet: float, m: float, k: float,
           cenario: str) -> list[dict]:
    linhas = []
    for c in resto:
        conv = c["conversas"][0] if cenario == "baixa" else (
            c["conversas"][1] if cenario == "alta" else sum(c["conversas"]) / 2)
        chamadas = 0.0
        tokens = 0.0
        for ag in c["agentes"]:
            n = ag["min"] if cenario == "baixa" else (ag["max"] if cenario == "alta" else (ag["min"] + ag["max"]) / 2)
            t, _ = tokens_da_chamada(ag, tabela, media_sonnet)
            chamadas += n
            tokens += n * t
        linhas.append({"cartao": c["cartao"], "bloco": c["bloco"], "conversas": conv,
                       "chamadas": chamadas, "tokens": tokens,
                       "pp": m * conv + k * tokens / 100_000})
    return linhas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    dados = carregar_dados()
    leit = {l["id"]: l["valor"] for l in dados["leituras"]}
    for i in dados["intervalos"]:
        i["pp"] = leit[i["ate"]] - leit[i["de"]]
    dev = [i for i in dados["intervalos"] if i["frente"] == "D"]
    plan = [i for i in dados["intervalos"] if i["frente"] == "P"]
    aj = ajuste(dev)
    m, k = aj["m"], aj["k"]

    lotes = medidas_dos_logs()
    tabela, media_sonnet = estimativas(lotes)

    cen = {
        "baixa": prever(dados["resto_do_piloto"], tabela, media_sonnet,
                        max(m - aj["ep_m"], 0), max(k - aj["ep_k"], 0), "baixa"),
        "central": prever(dados["resto_do_piloto"], tabela, media_sonnet, m, k, "central"),
        "alta": prever(dados["resto_do_piloto"], tabela, media_sonnet, m + aj["ep_m"], k + aj["ep_k"], "alta"),
    }
    tot = {c: sum(x["pp"] for x in v) for c, v in cen.items()}
    tok_total = sum(i["tokens_agentes"] for i in dados["intervalos"])
    pp_total = sum(i["pp"] for i in dados["intervalos"])
    pp_agentes = k * tok_total / 100_000
    antiga = dados["regra_antiga"]["teto_tokens_semana"]

    if a.json:
        print(json.dumps({"ajuste": aj, "media_sonnet": media_sonnet, "total_resto": tot,
                          "pp_total_medido": pp_total, "pp_agentes_estimado": pp_agentes},
                         ensure_ascii=False, indent=2))
        return 0

    print("## 1. Uso da conta por intervalo (medida: leituras de Vicente)\n")
    print("| Intervalo | Conversas | Frente | Configuração | pp | Tokens de agentes |")
    print("|---|---|---|---|---|---|")
    for i in dados["intervalos"]:
        print(f"| {i['de']} ({leit[i['de']]}%) → {i['ate']} ({leit[i['ate']]}%) | {', '.join(i['conversas'])} "
              f"| {i['frente']} | {i['configuracao']} | {i['pp']} | {br(i['tokens_agentes'])} |")
    print(f"| **Planejamento** | | P | | **{sum(i['pp'] for i in plan)}** | **{br(sum(i['tokens_agentes'] for i in plan))}** |")
    print(f"| **Desenvolvimento** | | D | | **{sum(i['pp'] for i in dev)}** | **{br(sum(i['tokens_agentes'] for i in dev))}** |")
    print(f"| **Total** | | | | **{pp_total}** | **{br(tok_total)}** |\n")

    print("## 2. Ajuste das conversas de desenvolvimento (estimativa)\n")
    print(f"- pp = m × conversas + k × (tokens de agentes / 100 mil), mínimos quadrados em {len(dev)} intervalos "
          f"({aj['graus_de_liberdade']} grau de liberdade; leituras inteiras, ±1 pp em cada diferença).")
    print(f"- m (conversa principal, Opus 5.5 médio) = {br(m, 2)} pp por conversa; erro-padrão {br(aj['ep_m'], 2)}.")
    print(f"- k (agentes Sonnet 5.5 alto) = {br(k, 2)} pp por 100 mil tokens do retorno do Agent; erro-padrão {br(aj['ep_k'], 2)}.")
    print("- resíduos: " + "; ".join(f"{'+'.join(i['conversas'])} {br(r, 2)}" for i, r in zip(dev, aj["residuos"])))
    print(f"- na semana medida, os agentes dariam {br(pp_agentes, 1)} dos {pp_total} pp, e as conversas principais, "
          f"{br(pp_total - pp_agentes, 1)}.")
    print(f"- os {br(antiga)} tokens de agentes por semana da regra antiga equivalem a {br(k * antiga / 100_000, 1)} pp.")
    for i in plan:
        print(f"- planejamento, {', '.join(i['conversas'])}: {i['pp']} pp, dos quais {br(k * i['tokens_agentes'] / 100_000, 1)} "
              f"seriam de agentes pelo k (se o k dos agentes de workflow for o mesmo).")
    print()

    print("## 3. Estimativa por agente e habilidade (logs de trilhas/logs/)\n")
    print("| Agente | Habilidade | Modelo | Lotes | Última | Mín. | Máx. | Média | pp da última (k) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for (ag, hab), v in sorted(tabela.items()):
        print(f"| {ag} | {hab} | {v['modelo']} | {v['n']} | {br(v['ultima'])} | {br(v['min'])} | {br(v['max'])} "
              f"| {br(v['media'])} | {br(k * v['ultima'] / 100_000, 1)} |")
    print(f"\nSem medida do mesmo agente e habilidade: a média dos {sum(1 for l in lotes if (l['modelo'] or '').startswith('claude-sonnet'))} "
          f"lotes Sonnet dos logs, {br(media_sonnet)} tokens ({br(k * media_sonnet / 100_000, 1)} pp).\n")

    print("## 4. Resto do piloto (K-106 a K-116 e K-102), em pp da conta (estimativa)\n")
    print("| Cartão | Bloco | Chamadas (mín.–máx.) | Tokens centrais | pp baixa | pp central | pp alta |")
    print("|---|---|---|---|---|---|---|")
    for b, c, h in zip(cen["baixa"], cen["central"], cen["alta"]):
        print(f"| {c['cartao']} | {c['bloco']} | {br(b['chamadas'])}–{br(h['chamadas'])} | {br(c['tokens'])} "
              f"| {br(b['pp'], 1)} | {br(c['pp'], 1)} | {br(h['pp'], 1)} |")
    print(f"| **Total** | | {br(sum(x['chamadas'] for x in cen['baixa']))}–{br(sum(x['chamadas'] for x in cen['alta']))} "
          f"| {br(sum(x['tokens'] for x in cen['central']))} | **{br(tot['baixa'], 1)}** | **{br(tot['central'], 1)}** "
          f"| **{br(tot['alta'], 1)}** |")
    print("\nBaixa: menos conversas e chamadas, com m e k um erro-padrão abaixo; alta: mais conversas e chamadas, "
          "com m e k um erro-padrão acima. Fora da conta: a rotina de teste da 10b, a diferença de custo do redator "
          "(Opus) e a das rodadas em Haiku do bloco 12.\n")

    cal = dados["calendario"]
    inicio = date.fromisoformat(cal["proxima_renovacao_suposta"])
    espera = cal["semanas_de_espera"]

    def fim(semanas: float) -> str:
        return (inicio + timedelta(days=round(semanas * 7))).strftime("%d/%m")

    print("## 5. Semanas do desenvolvimento, por meta\n")
    print(f"Semanas da conta a partir da próxima renovação: o consumo dividido pela meta, mais {espera} de espera "
          f"(os 7 dias da 10a). Datas pela suposição de {inicio.strftime('%d/%m/%Y')} ({cal['nota']}).\n")
    print("| Meta (pp por semana) | Semanas, baixa | Semanas, central | Semanas, alta | Fim (baixa · central · alta) |")
    print("|---|---|---|---|---|")
    for meta in dados["metas_testadas"]:
        s = [tot[c] / meta + espera for c in ("baixa", "central", "alta")]
        print(f"| {meta} | {br(s[0], 1)} | {br(s[1], 1)} | {br(s[2], 1)} | {fim(s[0])} · {fim(s[1])} · {fim(s[2])} |")
    print(f"\nFora da conta: {cal['espera'].split('; ', 1)[1]}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
