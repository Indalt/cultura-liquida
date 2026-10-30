"""Menções incidentais a outras CLB (K-102; brief, l. 338-344; D-037, diretriz 4; D-039), sem IA.
Regra mencoes-0.1.

Dois atos e uma conferência:
- **Candidatas** (`--separadas <arq.json>`): as Evidências que um lote separou como de outra CLB
  (brief, l. 419 b). O arquivo traz `termos_declarados`: a forma, o sentido, os Trechos do acervo em
  que a forma está (`abonado_em`) e, para o termo ambíguo, o Termo com que ele divide a forma
  (`ambiguo_com`). Pela regra: a forma tem de estar no texto exato de um Trecho localizado (eixo 3),
  senão nada se grava (código 1); a forma que o registro não tem nasce como Termo candidato e CLB
  candidata; a forma que o registro já tem num Termo declarado ambíguo (`ambiguo_com`) se desdobra
  (D-039) em Termo candidato e CLB candidata novos, com a relação ao Termo de origem; a forma que o
  registro já tem, sem desdobramento declarado, não gera nada. A CLB candidata nasce com os quatro
  critérios em Falta (F-0020), sem situação, e com a origem na nota, que o `fila_curadoria.py` põe
  na linha do cartão de lista das CLB candidatas (um só cartão; D-039). Atestar fica com o arquivista.
- **Varredura** (`--textos <pasta>`): compara o texto que o processamento leu (a pasta temporária
  das fontes, fora do Git) com o registro de Termos do momento: as designações e as variantes de
  todo Termo não retirado (as formas de busca ficam fora: são de busca, não do termo). Cada texto
  EN-nnnn.txt é da CLB das Proposições ligadas às Fontes dessa Entrada. Para cada forma achada
  (a mais longa, sem distinguir maiúscula): termo ambíguo (a forma está em mais de um Termo, ou a
  variante diz "ambíguo") → menção marcada, sem ligação automática (D-039); termo de uma CLB que não é
  a do texto → ligação no grafo (`grafo/mencoes-incidentais.json`); a própria CLB, Termo sem CLB
  (caju, que é insumo) ou texto sem CLB de origem → só contagem. Grava só IDs, a forma, contagens e localizadores (página e
  caracteres do texto normalizado): nunca o texto da fonte.
- `--conferir`: refaz a varredura em memória e reprova (código 1) se uma menção a outra CLB não tem
  ligação no arquivo (`--arquivo`), se uma ligação aponta para CLB que não existe, se um termo
  ambíguo aparece ligado, se uma CLB candidata não tem linha com a menção de origem no cartão de lista
  (`--lista`) ou se o quadro (`--quadro`) tem cartão por CLB no lugar da linha, ou mais de um cartão
  de lista aberto.
Alcance (D-030): o script só vê as CLB cujo termo está no registro de Termos do momento; o log diz
quantos Termos e textos olhou e que o que não está registrado ficou fora.

Uso:
    python scripts/mencoes_incidentais.py --separadas <arq.json> [--raiz <pasta>] [--simular]
    python scripts/mencoes_incidentais.py --textos <pasta> [--raiz <pasta>] [--saida <arq.json>] [--simular]
    python scripts/mencoes_incidentais.py --textos <pasta> --conferir [--arquivo <arq.json>]
        [--lista <clb-candidatas.md>] [--quadro <quadro.md>] [--raiz <pasta>]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, prefixo, proximo_id  # noqa: E402
from _coleta import Execucao, gravar_json  # noqa: E402
from _comum import RAIZ, carregar_esquema, validar_objeto  # noqa: E402
from localizar_trecho import VERSAO as NORMALIZACAO, normalizar  # noqa: E402

VERSAO = "mencoes-0.1"
CRITERIOS = ("identidade_ou_memoria", "reconhecimento_pelo_grupo", "transmissao_entre_geracoes", "recriacao")
FALTA_CRITERIO = "F-0020"
PROTECAO = {"licenca": "não conferido", "consentimento": "não se aplica", "restricao_comunitaria": "nenhuma conhecida",
            "precisao_lugar": "não se aplica", "dado_sensivel": False, "crianca_ou_adolescente": False,
            "pedido_de_retirada": "nenhum"}
RE_PAG = re.compile(r"\[\[p\. ?(\d+)\]\]")
MARCA_AMBIGUA = "termo ambíguo (D-039): sem ligação automática"


def rel(p: Path) -> str:
    return p.relative_to(RAIZ).as_posix() if p.is_relative_to(RAIZ) else p.as_posix()


def chave(forma: str) -> str:
    return normalizar(forma).casefold()


def padrao(formas) -> re.Pattern:
    alt = "|".join(re.escape(f) for f in sorted(formas, key=len, reverse=True))
    return re.compile(rf"(?<!\w)(?:{alt})(?!\w)", re.IGNORECASE)


class Registro:
    """O acervo do momento: Termos, CLB e o caminho Entrada → Fonte → Trecho → Evidência → Proposição → CLB."""

    def __init__(self, raiz: Path):
        self.raiz = raiz
        self.indice, _, self.erros = carregar_acervo(raiz)
        vivos = {i: r for i, r in self.indice.items() if not r.get("retirado")}
        self.termos = {i: r for i, r in vivos.items() if prefixo(i) == "TE"}
        self.clbs = {i: r for i, r in vivos.items() if prefixo(i) == "CL"}
        self.formas: dict[str, set[str]] = {}       # chave da forma → Termos
        self.ambiguas: set[str] = set()              # chaves declaradas ambíguas no registro
        for te, t in self.termos.items():
            for d in t.get("designacoes", []):
                self.formas.setdefault(chave(d["forma"]), set()).add(te)
            for v in t.get("variantes", []):
                self.formas.setdefault(chave(v["forma"]), set()).add(te)
                if "ambígu" in v.get("tipo_variacao", "").casefold():
                    self.ambiguas.add(chave(v["forma"]))
        self.clb_do_termo: dict[str, set[str]] = {}
        for cl, c in self.clbs.items():
            for te in set(c.get("termos", [])) | ({c["termo"]} if c.get("termo") else set()):
                self.clb_do_termo.setdefault(te, set()).add(cl)
        trecho_fonte = {i: r.get("fonte") for i, r in vivos.items() if prefixo(i) == "TR"}
        prop_clb = {i: r.get("clb") for i, r in vivos.items() if prefixo(i) == "PR"}
        self.clbs_da_fonte: dict[str, set[str]] = {}
        for i, ev in vivos.items():
            if prefixo(i) == "EV" and (fo := trecho_fonte.get(ev.get("trecho"))) and (cl := prop_clb.get(ev.get("proposicao"))):
                self.clbs_da_fonte.setdefault(fo, set()).add(cl)
        self.fontes_da_entrada: dict[str, set[str]] = {}
        for i, fo in vivos.items():
            if prefixo(i) == "FO" and fo.get("entrada"):
                self.fontes_da_entrada.setdefault(fo["entrada"], set()).add(i)

    def ambigua(self, k: str) -> bool:
        return len(self.formas.get(k, ())) > 1 or k in self.ambiguas

    def clbs_do_texto(self, entrada: str) -> set[str]:
        return set().union(*[self.clbs_da_fonte.get(fo, set()) for fo in self.fontes_da_entrada.get(entrada, ())])


# --- varredura ----------------------------------------------------------------------------------

def varrer(reg: Registro, pasta: Path) -> dict:
    formas_orig = {}
    for t in reg.termos.values():
        for f in [d["forma"] for d in t.get("designacoes", [])] + [v["forma"] for v in t.get("variantes", [])]:
            formas_orig.setdefault(chave(f), normalizar(f))
    pat = padrao(formas_orig.values()) if formas_orig else None
    ligacoes, ambiguas, propria, sem_clb, sem_origem, textos = {}, {}, {}, {}, {}, []
    for arq in sorted(pasta.glob("*.txt")):
        entrada = arq.stem if re.fullmatch(r"EN-\d{4,}", arq.stem) else None
        de = sorted(reg.clbs_do_texto(entrada)) if entrada else []
        textos.append({"arquivo": arq.name, "entrada": entrada, "clbs": de})
        if not pat:
            continue
        texto = normalizar(arq.read_text(encoding="utf-8", errors="replace"))
        pags = [(m.start(), m.group(1)) for m in RE_PAG.finditer(texto)]
        for m in pat.finditer(texto):
            k = m.group(0).casefold()
            pag = next((n for s, n in reversed(pags) if s <= m.start()), None)
            loc = (f"p. {pag}; " if pag else "") + f"car. {m.start()}-{m.end()} do texto normalizado ({NORMALIZACAO})"
            termos = sorted(reg.formas.get(k, ()))
            if reg.ambigua(k):
                r = ambiguas.setdefault((entrada or arq.name, k), {"forma": formas_orig[k], "termos": termos, "texto": arq.name,
                                                                      "entrada": entrada, "de": de, "marca": MARCA_AMBIGUA,
                                                                      "ocorrencias": 0, "localizadores": []})
                r["ocorrencias"] += 1
                r["localizadores"].append(loc)
                continue
            te = termos[0]
            para = reg.clb_do_termo.get(te, set())
            if not para:
                sem_clb[te] = sem_clb.get(te, 0) + 1
                continue
            if not de:
                sem_origem[te] = sem_origem.get(te, 0) + 1
                continue
            for cl in sorted(para):
                if cl in de:
                    propria[cl] = propria.get(cl, 0) + 1
                    continue
                r = ligacoes.setdefault((entrada or arq.name, cl, te), {"de": de, "para": cl, "termo": te, "forma": formas_orig[k],
                                                                         "texto": arq.name, "entrada": entrada,
                                                                         "ocorrencias": 0, "localizadores": []})
                r["ocorrencias"] += 1
                r["localizadores"].append(loc)
    return {"versao_regra": VERSAO, "normalizacao": NORMALIZACAO,
            "dicionario": {"termos": sorted(reg.termos), "formas": sorted(formas_orig.values()),
                           "ambiguas": sorted(formas_orig[k] for k in formas_orig if reg.ambigua(k))},
            "textos": textos, "ligacoes": list(ligacoes.values()), "ambiguas": list(ambiguas.values()),
            "contagens": {"propria_clb": propria, "termo_sem_clb": sem_clb, "texto_sem_clb_de_origem": sem_origem,
                          "textos_sem_clb": sum(1 for t in textos if not t["clbs"])}}


def chaves_ligacoes(v: dict) -> set:
    return {(l["texto"], l["para"], l["termo"]) for l in v.get("ligacoes", [])}


# --- candidatas ---------------------------------------------------------------------------------

def candidatas(reg: Registro, arq: Path, ex: Execucao) -> tuple[list[dict], list[str]]:
    sep = json.loads(arq.read_text(encoding="utf-8"))
    novos, erros, ids = [], [], set(reg.indice)
    esq_te, esq_cl = carregar_esquema("termo"), carregar_esquema("clb")
    for d in sep.get("termos_declarados", []):
        forma, k = d["forma"], chave(d["forma"])
        achados = [tr for tr in d.get("abonado_em", [])
                   if (t := reg.indice.get(tr)) and t.get("estado") == "localizado"
                   and padrao([normalizar(forma)]).search(normalizar(t.get("texto_exato", "")))]
        if not achados:
            erros.append(f"{forma!r}: a forma não está no texto exato de nenhum Trecho localizado de {d.get('abonado_em')} (eixo 3)")
            continue
        no_registro = reg.formas.get(k, set())
        origem_amb = d.get("ambiguo_com")
        if no_registro and not origem_amb:
            ex.decisoes.append({"item": forma, "decisao": "descartado", "automatica": True, "versao_regra": VERSAO,
                                "motivo": f"já no registro ({', '.join(sorted(no_registro))}): CLB já registrada, nada nasce"})
            continue
        if origem_amb:
            if origem_amb not in no_registro or not reg.ambigua(k):
                erros.append(f"{forma!r}: desdobramento declarado de {origem_amb}, mas a forma não está nele como termo ambíguo (D-039)")
                continue
            if len(no_registro) > 1:
                ex.decisoes.append({"item": forma, "decisao": "descartado", "automatica": True, "versao_regra": VERSAO,
                                    "motivo": f"já desdobrado ({', '.join(sorted(no_registro))})"})
                continue
        te, cl = proximo_id("TE", ids), None
        ids.add(te)
        cl = proximo_id("CL", ids)
        ids.add(cl)
        separadas = ", ".join(d.get("evidencias_separadas", [])) or "nenhuma com a forma no trecho"
        origem = (f"Evidências separadas como outra CLB em {rel(arq)} ({separadas}); a forma no texto exato de "
                  f"{', '.join(achados)}" + (f"; desdobramento do termo ambíguo de {origem_amb} (D-039)" if origem_amb else ""))
        termo = {"id": te, "conceito": d["sentido"], "designacoes": [{"forma": forma}], "estado": "candidato",
                 "nota": f"Nasce candidato pela regra {VERSAO} (brief, l. 419 b; D-039; K-102): {origem}. Atestar fica com o "
                         "arquivista (registrar-termo), fora do K-102. Sem língua: nenhuma fonte a dá (insumo 30).",
                 "protecao": d.get("protecao", PROTECAO),
                 "origem_registro": ex.origem(f"scripts/mencoes_incidentais.py ({VERSAO})", VERSAO)}
        if origem_amb:
            termo["relacoes"] = [{"tipo": "relacionado", "termo": origem_amb}]
        clb = {"id": cl, "termo": te, "termos": [te], "situacoes": [],
               "criterios": {c: {"falta": FALTA_CRITERIO} for c in CRITERIOS}, "estado": "candidata",
               "protecao": d.get("protecao", PROTECAO),
               "nota": f"origem: {origem}. CLB de outro termo pela regra {VERSAO} (D-039); os critérios esperam a triagem "
                       "(F-0020); a situação, as Evidências gravadas no acervo.",
               "origem_registro": ex.origem(f"scripts/mencoes_incidentais.py ({VERSAO})", VERSAO)}
        if origem_amb:
            clb["desdobrada_de"] = origem_amb
        for obj, esq in ((termo, esq_te), (clb, esq_cl)):
            erros += [f"{obj['id']}: {e}" for e in validar_objeto(obj, esq)]
        novos += [termo, clb]
        ex.decisoes.append({"item": f"{forma} ({d['sentido'][:60]})", "decisao": "aceito", "automatica": True, "versao_regra": VERSAO,
                            "motivo": f"nasce {te} (Termo candidato) e {cl} (CLB candidata)" + (f", desdobrada de {origem_amb}" if origem_amb else "")})
    return novos, erros


# --- conferência --------------------------------------------------------------------------------

def conferir(reg: Registro, atual: dict, salvo: dict, lista: Path | None, quadro: Path | None) -> list[str]:
    p = []
    for falta in sorted(chaves_ligacoes(atual) - chaves_ligacoes(salvo)):
        p.append(f"menção sem ligação: {falta[0]} → {falta[1]} ({falta[2]})")
    for l in salvo.get("ligacoes", []):
        if l["para"] not in reg.clbs or any(c not in reg.clbs for c in l.get("de", [])):
            p.append(f"ligação para CLB que não existe: {l.get('de')} → {l['para']}")
        if reg.ambigua(chave(l["forma"])):
            p.append(f"termo ambíguo ligado automaticamente: {l['forma']} → {l['para']} (D-039)")
    candidatas_ = [c for c in reg.clbs.values() if c.get("estado") == "candidata"]
    linhas = lista.read_text(encoding="utf-8").splitlines() if lista and lista.exists() else []
    for c in candidatas_:
        ln = next((x for x in linhas if re.search(rf"(?<![\w-]){re.escape(c['id'])}(?![\w-])", x)), None)
        if ln is None:
            p.append(f"CLB candidata {c['id']} sem linha no cartão de lista")
        elif "origem" not in ln:
            p.append(f"linha de {c['id']} no cartão de lista sem a menção de origem")
    if quadro and quadro.exists():
        abertos = [x for x in quadro.read_text(encoding="utf-8").splitlines() if x.startswith(("| A fazer", "| Fazendo"))]
        listas = [x for x in abertos if "Lista das CLB candidatas" in x]
        if len(listas) > 1:
            p.append(f"{len(listas)} cartões de lista das CLB candidatas abertos (D-039: um só)")
        for c in candidatas_:
            if any(re.search(rf"(?<![\w-]){re.escape(c['id'])}(?![\w-])", x) for x in abertos if x not in listas):
                p.append(f"cartão por CLB para {c['id']} no lugar da linha no cartão de lista (D-039)")
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--separadas", type=Path)
    ap.add_argument("--textos", type=Path)
    ap.add_argument("--saida", type=Path)
    ap.add_argument("--arquivo", type=Path)
    ap.add_argument("--lista", type=Path)
    ap.add_argument("--quadro", type=Path)
    ap.add_argument("--conferir", action="store_true")
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    absol = lambda p: p if p is None or p.is_absolute() else RAIZ / p  # noqa: E731
    raiz = absol(a.raiz)
    reg = Registro(raiz)
    if reg.erros:
        print("REPROVA: acervo ilegível: " + "; ".join(reg.erros[:3]))
        return 1

    if a.separadas:
        sep = absol(a.separadas)
        ex = Execucao("mencoes-incidentais", f"CLB candidatas das Evidências separadas ({rel(sep)})", simular=a.simular)
        novos, erros = candidatas(reg, sep, ex)
        for e in erros:
            print("REPROVA", e)
        if erros:
            print(f"{VERSAO}: nada gravado")
            return 1
        for obj in novos:
            pasta = "termos" if obj["id"].startswith("TE") else "clb"
            alvo = raiz / "acervo" / pasta / f"{obj['id']}.json"
            print(f"{'simulado' if a.simular else 'gravado'}: {rel(alvo)} ({'Termo candidato' if pasta == 'termos' else 'CLB candidata'}"
                  f"{', desdobra ' + obj['desdobrada_de'] if obj.get('desdobrada_de') else ''})")
            if not a.simular:
                gravar_json(alvo, obj)
                ex.saidas.append(rel(alvo))
        ex.acoes.append(f"scripts/mencoes_incidentais.py --separadas {rel(sep)}")
        ex.resultados.append(f"{len(novos) // 2} Termo(s) candidato(s) e CLB candidata(s)")
        ex.olhado += [f"{len(reg.termos)} Termo(s) do registro", f"os termos declarados de {rel(sep)}"]
        ex.fora += ["as Evidências separadas sem termo no trecho (o nome não se infere)",
                    "atestar os Termos candidatos (arquivista, fora do K-102)"]
        if not a.simular:
            print(f"log: {ex.gravar_log()}")
        print(f"{VERSAO}: {len(novos) // 2} candidata(s) {'simulada(s)' if a.simular else 'gravada(s)'}")
        if not a.textos:
            return 0
        reg = Registro(raiz)

    if not a.textos:
        ap.error("--textos ou --separadas")
    pasta = absol(a.textos)
    atual = varrer(reg, pasta)
    n_lig, n_amb = len(atual["ligacoes"]), len(atual["ambiguas"])
    resumo = (f"{len(atual['textos'])} texto(s), {len(reg.termos)} Termo(s), {len(atual['dicionario']['formas'])} forma(s); "
              f"{n_lig} ligação(ões); {n_amb} menção(ões) ambígua(s)")
    if a.conferir:
        arq = absol(a.arquivo) or raiz / "grafo" / "mencoes-incidentais.json"
        salvo = json.loads(arq.read_text(encoding="utf-8")) if arq.exists() else {}
        lista = absol(a.lista) or raiz / "trilhas" / "planejamento" / "clb-candidatas.md"
        quadro = absol(a.quadro) or raiz / "trilhas" / "planejamento" / "quadro.md"
        probs = conferir(reg, atual, salvo, lista, quadro)
        for x in probs:
            print("PROBLEMA", x)
        print(f"{VERSAO}: {resumo}; {'conferido' if not probs else f'{len(probs)} problema(s)'}")
        return 1 if probs else 0
    ex = Execucao("mencoes-incidentais", f"varredura de menções incidentais ({pasta.name}, fora do Git)", simular=a.simular)
    saida = absol(a.saida) or raiz / "grafo" / "mencoes-incidentais.json"
    atual = {"execucao": ex.id, "data": date.today().isoformat(), **atual}
    ex.acoes.append(f"scripts/mencoes_incidentais.py --textos <pasta temporária das fontes> ({len(atual['textos'])} textos)")
    ex.resultados += [resumo] + [f"{l['texto']}: {l['de']} → {l['para']} ({l['forma']}, {l['ocorrencias']}×)" for l in atual["ligacoes"]] \
        + [f"{m['texto']}: '{m['forma']}' {m['ocorrencias']}× marcada ({MARCA_AMBIGUA})" for m in atual["ambiguas"]]
    ex.decisoes += [{"item": f"{l['texto']} → {l['para']}", "decisao": "aceito", "automatica": True, "versao_regra": VERSAO,
                     "motivo": f"menção a '{l['forma']}' ({l['termo']}), de CLB que não é a do texto: ligação"} for l in atual["ligacoes"]]
    ex.olhado += [f"{len(atual['textos'])} texto(s) da pasta temporária das fontes", f"{len(reg.termos)} Termo(s) do registro "
                  f"({', '.join(atual['dicionario']['termos'])}) e {len(atual['dicionario']['formas'])} forma(s) (designações e variantes)"]
    ex.fora += ["toda CLB cujo termo não está no registro de Termos do momento (D-030)", "as formas de busca (OCR, grafia)",
                "a flexão (plural) das formas, que só bate se estiver no registro",
                f"{atual['contagens']['textos_sem_clb']} texto(s) sem CLB de origem (sem Entrada ou sem Proposição): as menções contam, sem ligação"]
    if not a.simular:
        gravar_json(saida, atual)
        ex.saidas.append(rel(saida))
        print(f"log: {ex.gravar_log()}")
    print(f"{VERSAO}: {resumo}{'' if not a.simular else ' (simulado)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
