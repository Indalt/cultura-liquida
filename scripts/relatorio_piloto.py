"""Números do relatório do piloto (K-116; brief de execuções, bloco 14, "Antes da v0.3"), sem IA.

Lê o acervo, as Entradas, os ambientes, os Recortes, as pegadas, o grafo, as Faltas, os logs e as tabelas
do checklist do piloto, e grava os números num JSON e num Markdown, para o redator escrever e o auditor
conferir. Não muda nada fora da pasta de saída.

Regras da conta:
  - tokens e chamadas de agente: só as linhas com tokens que não vêm do hook SubagentStop (o hook grava
    só uma linha mínima de segurança; o número oficial é o do curador, CLAUDE.md);
  - os registros de teste de modelo (entrada_ref com "[teste de modelo]", D-051) ficam à parte, fora da
    medida de produção;
  - pp por frente: a soma da coluna pp da tabela "Semana da conta" do checklist; "não lido" e "—" não somam.

Uso:
    python scripts/relatorio_piloto.py [--saida trilhas/2026-11-14_relatorio-piloto]
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

VERSAO = "relatorio-piloto-0.1"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKLIST = "trilhas/2026-10-17_execucao-piloto.md"


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as f:
        return json.load(f)


def arquivos(padrao):
    return sorted(glob.glob(os.path.join(RAIZ, padrao)))


def contar(itens, chave):
    c = collections.Counter()
    for d in itens:
        v = d.get(chave)
        if isinstance(v, dict):
            v = v.get("estado", json.dumps(v, ensure_ascii=False))
        c[str(v) if v is not None else "(sem campo)"] += 1
    return dict(c.most_common())


def json_dir(padrao):
    out = []
    for f in arquivos(padrao):
        try:
            with open(f, encoding="utf-8") as h:
                out.append(json.load(h))
        except (json.JSONDecodeError, UnicodeDecodeError):
            out.append({"_erro": os.path.basename(f)})
    return out


def numero(s):
    s = (s or "").strip().replace(".", "").replace(",", ".")
    m = re.match(r"^-?\d+(\.\d+)?", s)
    return float(m.group(0)) if m else None


def tabela_md(texto, cabecalho_inicio):
    """Linhas da primeira tabela cujo cabeçalho começa com cabecalho_inicio."""
    linhas = texto.splitlines()
    for i, l in enumerate(linhas):
        if l.startswith(cabecalho_inicio):
            cab = [c.strip() for c in l.strip("|").split("|")]
            rows = []
            for l2 in linhas[i + 2:]:
                if not l2.startswith("|"):
                    break
                cel = [c.strip() for c in l2.strip("|").split("|")]
                rows.append(dict(zip(cab, cel)))
            return rows
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--saida", default="trilhas/2026-11-14_relatorio-piloto")
    a = ap.parse_args()
    r = {"versao": VERSAO, "alcance": {"olhado": [], "fora": []}}

    # Acervo
    acervo = {}
    for d in sorted(os.listdir(os.path.join(RAIZ, "acervo"))):
        p = os.path.join(RAIZ, "acervo", d)
        if os.path.isdir(p):
            acervo[d] = len([x for x in os.listdir(p) if not x.startswith(".")])
    r["acervo_arquivos"] = acervo
    props = json_dir("acervo/proposicoes/*.json")
    r["proposicoes"] = {
        "total": len(props),
        "por_estado": contar(props, "estado"),
        "por_atributo": contar(props, "atributo"),
        "sustentam_aviso_saude_politica": sum(1 for p in props if p.get("sustenta_aviso_saude_politica") is True),
        "com_evidencia_fora_da_conta": sum(1 for p in props if p.get("fora_da_conta")),
        "com_tensao_interna": sum(1 for p in props if p.get("tensao_interna")),
        "versao_regra": contar(props, "versao_regra"),
    }
    evs = json_dir("acervo/evidencias/*.json")
    r["evidencias"] = {"total": len(evs), "por_tipo_de_voz": collections.Counter(
        (e.get("voz") or {}).get("tipo", "(sem voz)") if isinstance(e.get("voz"), dict) else str(e.get("voz"))
        for e in evs).most_common()}
    trs = json_dir("acervo/trechos/*.json")
    r["trechos"] = {"total": len(trs)}
    for campo in ("localizacao", "estado", "metodo"):
        if trs and any(campo in t for t in trs):
            r["trechos"]["por_" + campo] = contar(trs, campo)
    r["clb"] = {"total": len(json_dir("acervo/clb/*.json")), "por_estado": contar(json_dir("acervo/clb/*.json"), "estado")}
    r["termos"] = {"total": len(json_dir("acervo/termos/*.json")), "por_estado": contar(json_dir("acervo/termos/*.json"), "estado")}
    r["fontes"] = {"total": len(json_dir("acervo/fontes/*.json")), "por_tipo_de_evidencia": contar(json_dir("acervo/fontes/*.json"), "tipo_evidencia")}
    fichas = [os.path.relpath(f, RAIZ).replace("\\", "/") for f in arquivos("acervo/fichas/**/*.md")]
    r["fichas"] = fichas
    r["alcance"]["olhado"].append("acervo/ (todas as pastas, contagem de arquivos; Proposições, Evidências, Trechos, CLB, Termos e Fontes lidos por inteiro)")

    # Faltas
    fal = json_dir("acervo/faltas/*.json")
    r["faltas"] = {
        "total": len(fal),
        "por_tipo": contar(fal, "tipo"),
        "por_subtipo_juridico": contar([f for f in fal if f.get("subtipo_juridico")], "subtipo_juridico"),
        "por_vale_para": contar(fal, "vale_para"),
        "caminho_de_liberacao_estado": contar(fal, "caminho_de_liberacao"),
    }

    # Entradas e pegadas
    ens = json_dir("entrada/EN-*.json")
    r["entradas"] = {
        "total": len(ens),
        "por_estado": contar(ens, "estado"),
        "por_ambiente": contar(ens, "ambiente"),
        "por_pretriagem": contar(ens, "pretriagem"),
        "por_mes_de_entrada": dict(sorted(collections.Counter((e.get("data_entrada") or "")[:7] for e in ens).items())),
    }
    peg_linhas = 0
    for f in arquivos("ambientes/pegadas/*.jsonl"):
        with open(f, encoding="utf-8") as h:
            peg_linhas += sum(1 for l in h if l.strip())
    r["pegadas"] = {"arquivos": len(arquivos("ambientes/pegadas/*.jsonl")), "itens_vistos": peg_linhas}
    r["alcance"]["olhado"].append("entrada/EN-*.json e ambientes/pegadas/*.jsonl (contagem)")
    r["alcance"]["fora"].append("o bruto fora do Git (D-045) e o wiki local")

    # Ambientes e Recortes
    ams = json_dir("ambientes/AM-*.json")
    via = collections.Counter()
    for m in ams:
        v = (m.get("via_protocolo") or "(sem via)").split(":")[0].strip()
        via[v] += 1
    r["ambientes"] = {
        "total": len(ams),
        "por_estado_monitoramento": contar(ams, "estado_monitoramento"),
        "por_estado_escavacao": contar(ams, "estado_escavacao"),
        "por_via": dict(via.most_common()),
        "por_tipo": contar(ams, "tipo"),
    }
    rcs = json_dir("ambientes/recortes/*.json")
    inf = [numero(str(x.get("total_informado"))) for x in rcs]
    vis = [numero(str(x.get("total_visto"))) for x in rcs]
    r["recortes"] = {
        "total": len(rcs),
        "por_estado": contar(rcs, "estado"),
        "por_ambiente": contar(rcs, "ambiente"),
        "soma_total_informado": sum(x for x in inf if x is not None),
        "soma_total_visto": sum(x for x in vis if x is not None),
        "sem_total_informado": sum(1 for x in inf if x is None),
    }
    r["consultas"] = len(arquivos("ambientes/consultas/*.json"))
    try:
        rot = ler("ambientes/rotinas.json")
        r["rotinas"] = {"versao": rot.get("versao"), "chaves": list(rot.keys())[:20]}
    except Exception as e:  # noqa: BLE001
        r["rotinas"] = {"erro": str(e)}

    # Grafo
    nos = ler("grafo/nos.json")
    ar = ler("grafo/arestas.json")
    r["grafo"] = {
        "versao_regra": nos.get("versao_regra"),
        "nos": len(nos.get("nos", [])),
        "arestas": len(ar.get("arestas", [])),
        "nos_por_tipo": contar(nos.get("nos", []), "tipo"),
        "arestas_por_estado": contar(ar.get("arestas", []), "estado"),
    }

    # Logs
    linhas = []
    for f in arquivos("trilhas/logs/*.jsonl"):
        with open(f, encoding="utf-8") as h:
            for l in h:
                l = l.strip()
                if l:
                    try:
                        linhas.append(json.loads(l))
                    except json.JSONDecodeError:
                        pass
    prod = collections.defaultdict(lambda: {"execucoes": 0, "tokens": 0, "chamadas": 0, "modelos": set()})
    teste = collections.defaultdict(lambda: {"execucoes": 0, "tokens": 0, "chamadas": 0, "modelos": set()})
    por_fonte = collections.Counter()
    for d in linhas:
        por_fonte[d.get("fonte_do_registro", "(sem campo)")] += 1
        if d.get("fonte_do_registro") == "hook-SubagentStop" or not isinstance(d.get("tokens"), int):
            continue
        alvo = teste if "[teste de modelo]" in str(d.get("entrada_ref", "")) else prod
        k = f'{d.get("agente")} / {d.get("habilidade")}'
        alvo[k]["execucoes"] += 1
        alvo[k]["tokens"] += d["tokens"]
        alvo[k]["chamadas"] += d.get("chamadas") or 0
        alvo[k]["modelos"].add(str(d.get("modelo")))

    def fechar(t):
        return {k: {**v, "modelos": sorted(v["modelos"])} for k, v in sorted(t.items(), key=lambda x: -x[1]["tokens"])}

    r["logs"] = {
        "linhas": len(linhas),
        "por_fonte_do_registro": dict(por_fonte.most_common()),
        "producao_por_agente_habilidade": fechar(prod),
        "producao_total_tokens": sum(v["tokens"] for v in prod.values()),
        "producao_total_chamadas": sum(v["chamadas"] for v in prod.values()),
        "teste_de_modelo_por_agente_habilidade": fechar(teste),
        "teste_total_tokens": sum(v["tokens"] for v in teste.values()),
        "primeira_data": min((str(d.get("data_hora", ""))[:10] for d in linhas if d.get("data_hora")), default=None),
        "ultima_data": max((str(d.get("data_hora", ""))[:10] for d in linhas if d.get("data_hora")), default=None),
    }
    r["alcance"]["olhado"].append("trilhas/logs/*.jsonl (todas as linhas)")
    r["alcance"]["fora"].append("tokens da conversa principal (não registrados por linha; só os pp da tabela) e o consumo do Gemini (contador próprio do K-125)")

    # Checklist: Semana da conta e horas
    with open(os.path.join(RAIZ, CHECKLIST), encoding="utf-8") as h:
        ck = h.read()
    sem = tabela_md(ck, "| Semana da conta |")
    pp = collections.defaultdict(float)
    sem_pp = 0
    for l in sem:
        v = numero(l.get("pp", ""))
        if v is None:
            sem_pp += 1
            continue
        pp[(l.get("Semana da conta"), l.get("Frente"))] += v
    r["semana_da_conta"] = {
        "linhas": len(sem),
        "linhas_sem_pp": sem_pp,
        "pp_por_semana_e_frente": {f"{s} | {fr}": round(v, 2) for (s, fr), v in pp.items()},
        "pp_por_frente": {fr: round(sum(v for (s2, f2), v in pp.items() if f2 == fr), 2) for fr in sorted({f for _, f in pp})},
    }
    r["horas_de_vicente"] = tabela_md(ck, "| Semana | Revisões (h)")
    r["alcance"]["olhado"].append(f"{CHECKLIST}: tabelas 'Semana da conta' e 'Horas de Vicente'")

    # Gatilho da fase 2 (Fundação, l. 676-679): só os dados; a avaliação é do relatório
    cl1 = next((c for c in json_dir("acervo/clb/*.json") if c.get("id") == "CL-0001"), {})
    r["gatilho_fase2_dados"] = {
        "1_caso_piloto_do_bruto_a_ficha": {"CL-0001_estado": cl1.get("estado"), "ficha": cl1.get("ficha")},
        "2_horas_reais_4_semanas": {"semanas_com_linha": len(r["horas_de_vicente"]),
                                     "valores": [l.get("Revisões (h)") for l in r["horas_de_vicente"]]},
        "3_decisoes_degrau_2": "sem campo no acervo; conferir no §5.4 e nas decisões (licença, aviso de privacidade, canal com o titular)",
    }

    out = os.path.join(RAIZ, a.saida)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "dados.json"), "w", encoding="utf-8") as h:
        json.dump(r, h, ensure_ascii=False, indent=2)
        h.write("\n")
    print(f"{VERSAO}: {len(props)} Proposições, {len(evs)} Evidências, {len(ens)} Entradas, {peg_linhas} pegadas, "
          f"{len(ams)} ambientes, {len(rcs)} Recortes, {len(fal)} Faltas; tokens de produção {r['logs']['producao_total_tokens']}; "
          f"gravado em {a.saida}/dados.json")


if __name__ == "__main__":
    sys.exit(main())
