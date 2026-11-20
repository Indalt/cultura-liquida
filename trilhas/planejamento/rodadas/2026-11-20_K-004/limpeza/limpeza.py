"""K-004, etapa 1 (D-058): a limpeza dos insumos abertos, por script e sem IA, em volta da proposta e da releitura.

Subcomandos:
- validar <arquivo.json>  confere a forma de uma proposta ou de um resultado: os 82 abertos de
                          lista_abertos.json, cada um uma vez; ação conhecida; alvo que existe (insumo
                          que fica, cartão do quadro, V do proxima-versao.md, decisão, Falta); sem cadeia
                          (junta a insumo que também sai). Código 1 se algo falha.
- pacotes                 monta pacote-R1.json, pacote-R2.json e pacote-R3.json para a releitura (D-038):
                          cada saída e cada junção com o texto inteiro do insumo, a linha do mapa §6, o
                          texto do alvo, o motivo e a prova da proposta.
- resultado               junta proposta.json, releitura-R*.json e ajustes.json (se houver) em
                          resultado.json e resultado.md: o que a releitura confirmou vale; o que ela
                          refutou fica, salvo ajuste aprovado por quem não o propôs.

Nada aqui altera insumo, mapa ou quadro (D-058: nada se apaga). Uso: python limpeza.py <subcomando> (PYTHONUTF8=1).
"""
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

PASTA = pathlib.Path(__file__).resolve().parent
RODADA = PASTA.parent
RAIZ = pathlib.Path(__file__).resolve().parents[5]
INSUMOS = RAIZ / "trilhas" / "insumos-planejamento.md"
MAPA = RAIZ / "trilhas" / "planejamento" / "mapa-tres-frentes.md"
QUADRO = RAIZ / "trilhas" / "planejamento" / "quadro.md"
PROXIMA = RAIZ / "trilhas" / "planejamento" / "proxima-versao.md"
AGENTS = RAIZ / "AGENTS.md"
LISTA = RODADA / "lista_abertos.json"

ACOES = {"fica", "junta", "sai_resolvido", "sai_fora_da_promessa"}
RE_K = re.compile(r"^K-\d{3}[a-c]?$")
RE_V = re.compile(r"^V-\d{2}$")
RE_D = re.compile(r"^D-\d{3}$")
RE_F = re.compile(r"^F-\d{4}$")


def ler_insumos():
    itens = {}
    for linha in INSUMOS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (\d+) \| ([^|]*)\| ([^|]*)\| (.*)\| (.*) \|\s*$", linha)
        if m:
            itens[int(m.group(1))] = {"data": m.group(2).strip(), "origem": m.group(3).strip(),
                                      "insumo": m.group(4).strip(), "aonde": m.group(5).strip()}
    return itens


def ler_mapa():
    dentro, vira = False, {}
    for linha in MAPA.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## 6."):
            dentro = True
            continue
        if dentro and linha.startswith("## 7."):
            break
        m = re.match(r"^\| (\d+), (.*?) \| ([^|]*)\| (.*) \|\s*$", linha) if dentro else None
        if m:
            vira[int(m.group(1))] = m.group(4).strip()
    return vira


def ler_quadro():
    cartoes = {}
    for linha in QUADRO.read_text(encoding="utf-8").splitlines():
        m = re.search(r"\*\*(K-\d{3}[a-c]?)\*\*", linha)
        if linha.startswith("| ") and m:
            col = [c.strip() for c in linha.split("|")[1:-1]]
            cartoes[m.group(1)] = {"coluna": col[0], "texto": " | ".join(col[1:])[:1800]}
    return cartoes


def ler_proxima():
    vs = {}
    for linha in PROXIMA.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (V-\d{2}) \|", linha)
        if m:
            vs[m.group(1)] = linha[:1500]
    return vs


def ler_decisoes():
    ds = {}
    for linha in AGENTS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- \*\*(D-\d{3})", linha)
        if m:
            ds[m.group(1)] = linha[:1500]
    return ds


def alvos(item):
    a = item.get("alvo") or "—"
    return [t.strip() for t in a.split(";") if t.strip() and t.strip() != "—"]


def validar(arq):
    dados = json.loads(pathlib.Path(arq).read_text(encoding="utf-8"))
    lista = json.loads(LISTA.read_text(encoding="utf-8"))
    abertos = {r["insumo"] for r in lista["itens"] if not r["classe"].startswith("fechado")}
    itens = dados["itens"]
    erros = []
    ns = [i["n"] for i in itens]
    for n, c in Counter(ns).items():
        if c > 1:
            erros.append(f"insumo {n} aparece {c} vezes")
    if set(ns) != abertos:
        erros.append(f"faltam {sorted(abertos - set(ns))}; sobram {sorted(set(ns) - abertos)}")
    acao = {i["n"]: i["acao"] for i in itens}
    cartoes, vs, ds = ler_quadro(), ler_proxima(), ler_decisoes()
    for i in itens:
        n, a = i["n"], i["acao"]
        if a not in ACOES:
            erros.append(f"{n}: ação desconhecida {a}")
        if not i.get("motivo") or not i.get("evidencia"):
            erros.append(f"{n}: sem motivo ou sem prova")
        if a == "fica" and not i.get("problema"):
            erros.append(f"{n}: fica sem problema escrito")
        if a != "fica" and dados.get("tipo", "proposta") == "proposta" and not i.get("lote"):
            erros.append(f"{n}: sem lote de releitura")
        if a == "junta" and not alvos(i):
            erros.append(f"{n}: junta sem alvo")
        for t in alvos(i):
            if t.isdigit():
                if a != "junta":
                    erros.append(f"{n}: só a junção aponta insumo ({t})")
                elif acao.get(int(t)) != "fica":
                    erros.append(f"{n}: junta ao {t}, que não fica ({acao.get(int(t))}): cadeia")
            elif RE_K.match(t):
                if t not in cartoes:
                    erros.append(f"{n}: cartão {t} não está no quadro")
            elif RE_V.match(t):
                if t not in vs:
                    erros.append(f"{n}: {t} não está no proxima-versao.md")
            elif RE_D.match(t):
                if t not in ds:
                    erros.append(f"{n}: {t} não está no AGENTS.md")
            elif RE_F.match(t):
                if not (RAIZ / "acervo" / "faltas" / f"{t}.json").exists():
                    erros.append(f"{n}: {t} não existe em acervo/faltas")
            elif t != "proxima-versao.md":
                erros.append(f"{n}: alvo não reconhecido '{t}'")
    contagem = Counter(acao.values())
    print(json.dumps({"itens": len(itens), "contagem": dict(contagem), "erros": len(erros)}, ensure_ascii=False))
    for e in erros:
        print("ERRO:", e)
    return 1 if erros else 0


def pacotes():
    prop = json.loads((PASTA / "proposta.json").read_text(encoding="utf-8"))
    ins, vira, cartoes, vs, ds = ler_insumos(), ler_mapa(), ler_quadro(), ler_proxima(), ler_decisoes()
    por_n = {i["n"]: i for i in prop["itens"]}
    lotes = defaultdict(list)
    for i in prop["itens"]:
        if i["acao"] == "fica":
            continue
        textos = []
        for t in alvos(i):
            if t.isdigit():
                alvo = por_n[int(t)]
                textos.append({"alvo": t, "insumo": ins[int(t)],
                               "na_proposta": {"acao": alvo["acao"], "problema": alvo.get("problema")}})
            elif RE_K.match(t):
                textos.append({"alvo": t, "quadro": cartoes.get(t)})
            elif RE_V.match(t):
                textos.append({"alvo": t, "proxima_versao": vs.get(t)})
            elif RE_D.match(t):
                textos.append({"alvo": t, "agents_md": ds.get(t)})
            else:
                textos.append({"alvo": t})
        lotes[i["lote"]].append({
            "n": i["n"], "insumo": ins[i["n"]], "vira_no_mapa": vira.get(i["n"]),
            "proposta": {"acao": i["acao"], "alvo": i.get("alvo"), "motivo": i["motivo"],
                         "evidencia": i["evidencia"]},
            "texto_do_alvo": textos})
    for lote, itens in sorted(lotes.items()):
        saida = {"lote": lote, "regra": prop["regra"], "acoes": prop["acoes"], "itens": itens}
        (PASTA / f"pacote-{lote}.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1),
                                                   encoding="utf-8")
        print(f"pacote-{lote}.json: {len(itens)} itens ({', '.join(str(x['n']) for x in itens)})")


def resultado():
    prop = json.loads((PASTA / "proposta.json").read_text(encoding="utf-8"))
    rel = {}
    for arq in sorted(PASTA.glob("releitura-R*.json")):
        for r in json.loads(arq.read_text(encoding="utf-8"))["itens"]:
            rel[r["insumo"]] = {**r, "arquivo": arq.name}
    ajustes, extra = {}, {}
    if (PASTA / "ajustes.json").exists():
        extra = json.loads((PASTA / "ajustes.json").read_text(encoding="utf-8"))
        for a in extra["itens"]:
            ajustes[a["n"]] = a
    itens, sem_releitura = [], []
    for i in prop["itens"]:
        n = i["n"]
        final = {k: i[k] for k in ("n", "acao", "alvo", "familia", "problema", "motivo", "evidencia") if k in i}
        final["proposto"] = i["acao"]
        if i["acao"] != "fica":
            r = rel.get(n)
            if r is None:
                sem_releitura.append(n)
                final.update({"acao": "fica", "estado": "sem releitura: fica até ser relido"})
            else:
                final["releitura"] = {k: r.get(k) for k in ("veredito", "motivo", "parte_nao_coberta",
                                                            "acao_sugerida", "conferido", "arquivo")}
                if r["veredito"] == "refuta":
                    final.update({"acao": "fica", "estado": "refutado na releitura: fica"})
                else:
                    final["estado"] = "confirmado na releitura" if r["veredito"] == "confirma" \
                        else "confirmado em parte na releitura"
        if n in ajustes:
            a = ajustes[n]
            final.update({"acao": a["acao"], "alvo": a.get("alvo", final.get("alvo")),
                          "estado": a["estado"], "ajuste": a})
            for k in ("problema", "familia"):
                if a.get(k):
                    final[k] = a[k]
        if final["acao"] == "fica" and "alvo" in final:
            final["alvo_proposto"] = final.pop("alvo")
        itens.append(final)
    cont = Counter(x["acao"] for x in itens)
    fica = [x for x in itens if x["acao"] == "fica"]
    saida = {"versao": "limpeza-0.1", "tipo": "resultado", "data": prop["data"], "regra": prop["regra"],
             "acoes": prop["acoes"], "familias": prop["familias"], "contagem": dict(cont),
             "ficam": len(fica), "sem_releitura": sem_releitura, "itens": itens}
    saida["notas_cruzamento"] = {c["insumo"]: c["decisao"] for c in extra.get("cruzamento", [])}
    saida["leitura"] = extra.get("leitura", [])
    cego = None
    if (PASTA / "cruzamento-cego.json").exists():
        cego = json.loads((PASTA / "cruzamento-cego.json").read_text(encoding="utf-8"))
        saida["cruzamento_cego"] = comparar_cego(cego, itens)
    (PASTA / "resultado.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    (PASTA / "resultado.md").write_text(escrever_md(saida, ajustes, cego), encoding="utf-8")
    print(json.dumps({"contagem": dict(cont), "ficam": len(fica), "sem_releitura": sem_releitura,
                      "divergencias_cego": len(saida.get("cruzamento_cego", {}).get("divergencias", []))},
                     ensure_ascii=False))


def destino(x):
    """Onde o insumo acaba: ele mesmo (fica), o alvo da junção, ou a saída."""
    if x["acao"] == "fica":
        return str(x["n"])
    if x["acao"] == "junta":
        return x.get("alvo") or "?"
    return x["acao"]


def comparar_cego(cego, itens):
    """Pares que o agrupador cego viu como o mesmo problema e que o resultado não pôs no mesmo lugar."""
    por_n = {x["n"]: x for x in itens}
    div = []
    for tema in cego.get("temas", []):
        for g in tema.get("mesmo_problema", []):
            membros = [m for m in g["insumos"] if m in por_n]
            dest = {m: destino(por_n[m]) for m in membros}
            mae = g.get("mae")
            alvo_mae = dest.get(mae, str(mae))
            for m in membros:
                if m == mae:
                    continue
                if dest[m] not in (alvo_mae, str(mae)) and not dest[m].startswith("sai"):
                    div.append({"tema": tema["nome"], "insumo": m, "mae_no_cego": mae,
                                "no_resultado": dest[m], "mae_no_resultado": alvo_mae, "porque": g["porque"]})
    fora = [{"insumo": f["insumo"], "no_resultado": destino(por_n[f["insumo"]]), "porque": f["porque"]}
            for f in cego.get("parece_fora_da_promessa", []) if f["insumo"] in por_n
            and por_n[f["insumo"]]["acao"] == "fica"]
    return {"divergencias": div, "fora_no_cego_e_fica_no_resultado": fora,
            "repete_fechado": cego.get("repete_fechado", [])}


def escrever_md(s, ajustes, cego):
    itens = s["itens"]
    por_n = {x["n"]: x for x in itens}
    fam = s["familias"]
    cont = s["contagem"]
    L = ["# Limpeza dos insumos abertos (K-004, etapa 1, D-058)", "",
         f"Gerado por `limpeza.py resultado` ({s['versao']}), sem IA, de `proposta.json`, `releitura-R*.json`"
         f"{', `ajustes.json`' if ajustes else ''} e `cruzamento-cego.json`. Nenhum insumo foi alterado nem apagado.", "",
         f"- Abertos antes da limpeza: {len(itens)} (de 142; os outros 60 já saíram por script na etapa 1).",
         f"- **Ficam: {s['ficam']}**. Juntados a outro insumo, a um cartão ou a um V: {cont.get('junta', 0)}. "
         f"Saem resolvidos: {cont.get('sai_resolvido', 0)}. Saem por não serem problema da promessa: "
         f"{cont.get('sai_fora_da_promessa', 0)}.",
         f"- Regra: {s['regra']}", ""]
    refutados = [x for x in itens if x.get("estado", "").startswith("refutado")]
    if refutados:
        L.append(f"- Refutados na releitura e de volta à fila: {', '.join(str(x['n']) for x in refutados)}.")
    if s.get("sem_releitura"):
        L.append(f"- Sem releitura (ficam): {', '.join(map(str, s['sem_releitura']))}.")
    if s.get("leitura"):
        L += ["", "## Leitura do curador: como os problemas se acumularam", ""]
        L += [f"- {t}" for t in s["leitura"]]
    L += ["", "## O que fica, por família", ""]
    juntos = defaultdict(list)
    for x in itens:
        if x["acao"] == "junta":
            for t in alvos(x):
                if t.isdigit():
                    juntos[int(t)].append(x["n"])
    for f in sorted(fam):
        fica = [x for x in itens if x["acao"] == "fica" and x.get("familia") == f]
        if not fica:
            continue
        L.append(f"### {f}. {fam[f]} ({len(fica)})")
        L.append("")
        for x in sorted(fica, key=lambda y: y["n"]):
            j = juntos.get(x["n"])
            L.append(f"- **{x['n']}**{' (com ' + ', '.join(map(str, j)) + ')' if j else ''}: {x.get('problema', '')}")
        L.append("")
    L += ["## O que se juntou", "", "| Insumo | Junta a | Motivo | Releitura |", "|---|---|---|---|"]
    for x in itens:
        if x["acao"] == "junta":
            r = x.get("releitura") or {}
            L.append(f"| {x['n']} | {x.get('alvo', '')} | {x['motivo'].replace('|', '/')} | "
                     f"{(r.get('veredito') or x.get('estado', '')).replace('|', '/')} |")
    L += ["", "## O que saiu", "", "| Insumo | Como | Onde segue | Motivo | Releitura |", "|---|---|---|---|---|"]
    for x in itens:
        if x["acao"].startswith("sai"):
            r = x.get("releitura") or {}
            como = "resolvido" if x["acao"] == "sai_resolvido" else "fora da promessa"
            L.append(f"| {x['n']} | {como} | {x.get('alvo', '—')} | {x['motivo'].replace('|', '/')} | "
                     f"{(r.get('veredito') or x.get('estado', '')).replace('|', '/')} |")
    if refutados:
        L += ["", "## Refutados na releitura (voltam à fila)", "", "| Insumo | Proposto | Motivo da releitura |",
              "|---|---|---|"]
        for x in refutados:
            L.append(f"| {x['n']} | {x['proposto']} | {x['releitura']['motivo'].replace('|', '/')} |")
    parciais = [x for x in itens if (x.get("releitura") or {}).get("veredito") == "confirma_em_parte"]
    if parciais:
        L += ["", "## Confirmados em parte: o que escrever no alvo na etapa 5", "",
              "A parte que o alvo não cobre não se perde: vai escrita no alvo quando a etapa 5 der o destino "
              "de tudo de uma vez (D-046, D-058).", "",
              "| Insumo | Alvo | Parte não coberta | Onde escrever (sugestão do releitor) |", "|---|---|---|---|"]
        for x in parciais:
            r = x["releitura"]
            L.append(f"| {x['n']} | {x.get('alvo', '—')} | {(r.get('parte_nao_coberta') or '').replace('|', '/')} | "
                     f"{(r.get('acao_sugerida') or '').replace('|', '/')} |")
    if ajustes:
        L += ["", "## Ajustes depois da releitura", "", "| Insumo | Fica como | Proposto por | Aprovado por | Motivo |",
              "|---|---|---|---|---|"]
        for n, a in sorted(ajustes.items()):
            L.append(f"| {n} | {a['acao']}{' ' + a['alvo'] if a.get('alvo') else ''} | {a['proposto_por']} | "
                     f"{a['aprovado_por']} | {a['motivo'].replace('|', '/')} |")
    cc = s.get("cruzamento_cego")
    if cc:
        L += ["", "## Cruzamento cego (agrupador que não viu a proposta)", ""]
        if cego:
            L.append(f"Temas: {len(cego.get('temas', []))}. Isolados: {', '.join(map(str, cego.get('isolados', []))) or 'nenhum'}.")
            L.append("")
            for t in cego.get("temas", []):
                L.append(f"- **{t['nome']}** ({', '.join(map(str, t['abertos']))}): {t['problema_de_fundo']}")
            L.append("")
        notas = s.get("notas_cruzamento", {})
        L += ["### Pares que o cego viu como o mesmo problema e o resultado deixou em lugares diferentes", "",
              "| Insumo | Mãe no cego | No resultado | Mãe no resultado | Por que o cego os junta | Decisão |",
              "|---|---|---|---|---|---|"]
        for d in cc["divergencias"]:
            L.append(f"| {d['insumo']} | {d['mae_no_cego']} | {d['no_resultado']} | {d['mae_no_resultado']} | "
                     f"{d['porque'].replace('|', '/')} | {notas.get(d['insumo'], notas.get(str(d['insumo']), '—')).replace('|', '/')} |")
        L += ["", "### Abertos que o cego marcou como fora da promessa e o resultado mantém", "",
              "| Insumo | Por que o cego os marcou |", "|---|---|"]
        for f in cc["fora_no_cego_e_fica_no_resultado"]:
            L.append(f"| {f['insumo']} | {f['porque'].replace('|', '/')} |")
        L += ["", "### Abertos que repetem um fechado", "", "| Aberto | Fechado | Cartão do fechado | O problema continuou? | Por quê |",
              "|---|---|---|---|---|"]
        for r in cc["repete_fechado"]:
            L.append(f"| {r['aberto']} | {r['fechado']} | {r.get('cartao_do_fechado', '')} | {r['problema_continuou']} | "
                     f"{r['porque'].replace('|', '/')} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "validar":
        sys.exit(validar(sys.argv[2]))
    elif cmd == "pacotes":
        pacotes()
    elif cmd == "resultado":
        resultado()
    else:
        print(__doc__)
        sys.exit(2)
