"""Grava no acervo a saída de um lote do avaliador (extrair-evidencia; bloco 7; K-109). Sem IA.

O avaliador não escreve no repositório: devolve um JSON por lote (formato do pedido do K-109) e os
arquivos do `localizar_trecho.py --saida` na pasta temporária. Este script, do curador:
  - dá os IDs pela faixa da conversa (valor numeracao_id) e grava em `acervo/<tipo>/`;
  - cria a Fonte de cada Entrada (referência, link permanente, a Entrada de origem, a proteção da Entrada),
    o Trecho de cada Evidência a partir do `--saida` do script (nunca do texto que o agente escreveu),
    a Falta "trecho não verificável por máquina" quando o script não localizou, a Evidência e a
    Proposição (as Evidências com a mesma `chave` se juntam na mesma Proposição; uma Proposição já
    gravada com o mesmo atributo e valor é reaproveitada);
  - liga os lugares ditos como texto aos Lugares: "Município, UF" pela tabela do IBGE de 2024
    (`acervo/lugares/ibge/`), o nome da UF como UF; o que não casa entra como nível "outro", sem
    inferência; o lugar que a fonte não diz vira uma Falta por papel (prática, publicação, pesquisa),
    uma só, com todos os lugares onde aparece;
  - garante a CLB da cajuína (CL-0001, termo TE-0002), em "ficha em montagem", com os quatro critérios
    de prática cultural em Falta até o bloco 8 (montar-ficha), que os preenche ou mantém;
  - atualiza a Entrada: estado (eixo 1: "extraído" com Evidência, "aceito" sem, "quarentena"), valências,
    selo e motivo da quarentena, marca de aviso, saúde ou política e `gera`.
Confere o hash do Trecho contra o manifesto do `ler_fonte.py` e roda o esquema de cada registro.

Uso:
    python scripts/gravar_extracao.py <saida-do-avaliador.json> --execucao EX-nnnn [--simular]
        [--raiz <pasta>] [--manifestos <pasta>]
`--execucao` é a Execução do avaliador (o log dele, gravado antes pelo curador).
Código 0 = gravou (ou simulou) sem erro; 1 = algum registro reprova (nada se grava).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, proximo_id  # noqa: E402
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from localizar_trecho import pasta_temporaria  # noqa: E402

VERSAO = "gravar-extracao-0.1"
PASTA = {"FO": "fontes", "TR": "trechos", "EV": "evidencias", "PR": "proposicoes", "LU": "lugares",
         "CL": "clb", "F": "faltas"}
ESQ = {"FO": "fonte", "TR": "trecho", "EV": "evidencia", "PR": "proposicao", "LU": "lugar", "CL": "clb",
       "F": "falta", "EN": "entrada"}
UF = {"AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", "BA": "Bahia", "CE": "Ceará",
      "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso",
      "MS": "Mato Grosso do Sul", "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná",
      "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte",
      "RS": "Rio Grande do Sul", "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo",
      "SE": "Sergipe", "TO": "Tocantins"}
PAPEL = {"pratica": "da prática", "publicacao": "da publicação", "pesquisa": "da pesquisa"}


def chave(t: str) -> str:
    t = unicodedata.normalize("NFD", (t or "").lower().strip())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def tabela_ibge() -> dict[tuple[str, str], str]:
    arq = next((RAIZ / "acervo" / "lugares" / "ibge").glob("*.csv"))
    with arq.open(encoding="utf-8-sig", newline="") as f:
        return {(chave(l["Nome do município"]), l["Sigla da UF"]): l["Geocódigo"] for l in csv.DictReader(f, delimiter=";")}


class Gravador:
    def __init__(self, execucao: str, raiz: Path = RAIZ):
        self.raiz = raiz
        self.indice, _, erros = carregar_acervo(raiz)
        if erros:
            raise SystemExit("acervo ilegível: " + "; ".join(erros))
        self.ids = set(self.indice)
        self.novos: dict[str, dict] = {}
        self.execucao = execucao
        self.hoje = date.today().isoformat()
        self.ibge = tabela_ibge()

    def origem(self, criado_por: str = f"scripts/gravar_extracao.py ({VERSAO})") -> dict:
        return {"criado_por": criado_por, "data": self.hoje, "execucao": self.execucao}

    def novo_id(self, pref: str) -> str:
        i = proximo_id(pref, self.ids)
        self.ids.add(i)
        return i

    def por(self, pref: str, cond) -> str | None:
        for i, r in list(self.indice.items()) + list(self.novos.items()):
            if i.startswith(pref + "-") and cond(r):
                return i
        return None

    def falta_lugar(self, papel: str, onde: str) -> str:
        texto = f"lugar {PAPEL[papel]} não dito na fonte"
        i = self.por("F", lambda r: r.get("o_que_falta") == texto)
        reg = self.novos.get(i) or (dict(self.indice[i]) if i else None)
        if not reg:
            i = self.novo_id("F")
            reg = {"id": i, "tipo": "outro", "o_que_falta": texto,
                   "por_que": "A Evidência pede o lugar da prática, da publicação e da pesquisa (§6); quando a fonte não o diz, fica a Falta, dita e nunca completada por inferência (D-018).",
                   "onde_aparece": [], "criada_por": f"scripts/gravar_extracao.py ({VERSAO})", "data": self.hoje}
        if onde not in reg["onde_aparece"]:
            reg["onde_aparece"].append(onde)
        self.novos[i] = reg
        return i

    def lugar(self, texto: str | None, papel: str, onde: str, protecao: dict) -> str:
        if not texto:
            return self.falta_lugar(papel, onde)
        t = texto.strip()
        partes = [p.strip() for p in t.replace(" - ", ",").replace("/", ",").split(",")]
        nivel, mun = "outro", None
        if len(partes) == 2 and partes[1].upper() in UF and (chave(partes[0]), partes[1].upper()) in self.ibge:
            nivel, mun = "município", self.ibge[(chave(partes[0]), partes[1].upper())]
        elif chave(t) in {chave(v) for v in UF.values()} or t.upper() in UF:
            nivel = "UF"
        i = self.por("LU", lambda r: r.get("nome_na_fonte") == t and r.get("nivel") == nivel)
        if i:
            return i
        i = self.novo_id("LU")
        reg = {"id": i, "nivel": nivel, "nome_na_fonte": t,
               "protecao": {**protecao, "precisao_lugar": "município" if nivel == "município" else ("UF" if nivel == "UF" else protecao.get("precisao_lugar", "não se aplica"))},
               "origem_registro": self.origem()}
        if mun:
            reg["municipio_atual"] = {"geocodigo_ibge": mun, "ano_divisao": 2022,
                                      "validade_toponimo": "nome atual na tabela do IBGE de 2024 (Malha Municipal 2022); a época do nome na fonte não foi conferida"}
        if nivel == "outro":
            reg["nota"] = "nome como a fonte o diz, sem ligação à tabela do IBGE (não casou como 'Município, UF' nem como UF); nada inferido"
        self.novos[i] = reg
        return i

    def clb_cajuina(self) -> str:
        i = self.por("CL", lambda r: r.get("termo") == "TE-0002")
        if i:
            return i
        i = self.novo_id("CL")
        f = self.novo_id("F")
        self.novos[f] = {"id": f, "tipo": "outro", "o_que_falta": "critério de prática cultural ainda não avaliado (D-022)",
                         "por_que": "Os quatro critérios (identidade ou memória, reconhecimento pelo grupo, transmissão entre gerações, recriação) se avaliam na montagem da ficha (bloco 8, montar-ficha), com as Evidências do bloco 7; até lá, Falta dita.",
                         "onde_aparece": [f"acervo/clb/{i}.json"], "criada_por": f"scripts/gravar_extracao.py ({VERSAO})", "data": self.hoje}
        prot = {"licenca": "não conferido", "consentimento": "não se aplica", "restricao_comunitaria": "nenhuma conhecida",
                "precisao_lugar": "UF", "dado_sensivel": False, "crianca_ou_adolescente": False, "pedido_de_retirada": "nenhum"}
        self.novos[i] = {"id": i, "termo": "TE-0002", "termos": ["TE-0002"], "situacoes": [],
                         "criterios": {k: {"falta": f} for k in ("identidade_ou_memoria", "reconhecimento_pelo_grupo", "transmissao_entre_geracoes", "recriacao")},
                         "estado": "ficha em montagem", "protecao": prot,
                         "nota": "a CLB do caso-piloto (D-031), identificada pelo termo (D-039); nasce para ligar as Proposições do bloco 7; as situações e os critérios entram no bloco 8",
                         "origem_registro": self.origem()}
        return i

    def gravar_lote(self, saida: dict, manifestos: dict[str, dict]) -> list[str]:
        clb = self.clb_cajuina()
        props: dict[str, str] = {}
        for item in saida["entradas"]:
            en_id = item["entrada"]
            en = dict(carregar_json(self.raiz / "entrada" / f"{en_id}.json"))
            prot = en["protecao"]
            man = manifestos.get(en_id, {})
            fo = item.get("fonte") or {}
            fo_id = self.por("FO", lambda r: r.get("entrada") == en_id) or self.novo_id("FO")
            nota_fo = [f"lida pelo ler_fonte.py: {man.get('pdf') or man.get('pagina') or en['url_ou_arquivo']} ({man.get('tipo') or 'sem texto'})"]
            if fo.get("deriva_de"):
                nota_fo.append(f"de onde a fonte diz que tira a informação: {fo['deriva_de']}")
            fonte = {"id": fo_id,
                     "referencia": {"titulo": fo.get("titulo") or en.get("titulo", "não dito"),
                                    "instituicao": fo.get("instituicao") or "não dito",
                                    "ano": fo.get("ano") or en.get("ano") or "não dito",
                                    "tipo": fo.get("tipo_documento") or "não dito",
                                    "link_permanente": en["url_ou_arquivo"]},
                     "tipo_evidencia": fo.get("tipo_evidencia") or "escrito publicado, de arquivo ou oficial",
                     "data_fonte": str(fo.get("ano") or en.get("ano") or "não conferido"),
                     "url": en["url_ou_arquivo"], "wayback": en.get("wayback") or "não consultado (o wayback.py não passou pela Entrada)",
                     "data_acesso": self.hoje, "perspectiva": fo.get("perspectiva") or "não dito",
                     "deriva_de": [], "entrada": en_id, "protecao": prot,
                     "nota": "; ".join(nota_fo), "origem_registro": self.origem()}
            self.novos[fo_id] = fonte
            trechos, temas = [], False
            for ev in item.get("evidencias", []):
                r = json.loads(Path(ev["arquivo_trecho"]).read_text(encoding="utf-8"))
                tr = r["trecho"]
                if man.get("hash_texto") and tr.get("hash") and tr["hash"] != man["hash_texto"]:
                    raise SystemExit(f"{en_id}: hash do Trecho ≠ hash do texto lido no manifesto ({ev['arquivo_trecho']})")
                tr_id = self.novo_id("TR")
                reg_tr = {"id": tr_id, "fonte": fo_id, **{k: tr[k] for k in tr if k in (
                    "texto_exato", "antes", "depois", "localizador", "hash", "data_conferencia", "origem_texto",
                    "grau_semelhanca", "versao_normalizacao", "estado")}, "protecao": prot,
                    "origem_registro": {"criado_por": "scripts/localizar_trecho.py (pelo avaliador)", "data": self.hoje,
                                        "execucao": self.execucao, "versao_regra": tr.get("versao_normalizacao")}}
                if tr["estado"] != "localizado":
                    f_id = self.novo_id("F")
                    falta = dict(r.get("falta") or {"tipo": "trecho_nao_verificavel", "o_que_falta": "trecho não verificável por máquina",
                                                     "por_que": "abaixo do limiar", "criada_por": "scripts/localizar_trecho.py", "data": self.hoje})
                    falta.update(id=f_id, onde_aparece=[f"acervo/trechos/{tr_id}.json"])
                    self.novos[f_id] = falta
                    reg_tr["falta"] = f_id
                self.novos[tr_id] = reg_tr
                trechos.append(tr_id)
                ev_id = self.novo_id("EV")
                k = ev.get("chave") or f"{ev['atributo']}|{ev['valor']}"
                pr_id = props.get(k) or self.por("PR", lambda p: p.get("clb") == clb and chave(p.get("atributo")) == chave(ev["atributo"])
                                                 and chave(p.get("valor")) == chave(ev["valor"]))
                if not pr_id:
                    pr_id = self.novo_id("PR")
                    self.novos[pr_id] = {"id": pr_id, "clb": clb, "atributo": ev["atributo"], "valor": ev["valor"],
                                         "periodo": {"referido": ev.get("periodo_referido") or "não dito na fonte"},
                                         "evidencias": [], "mu": None, "lambda": None,
                                         "sustenta_aviso_saude_politica": False, "origem_registro": self.origem()}
                elif pr_id not in self.novos:
                    self.novos[pr_id] = dict(self.indice[pr_id])
                props[k] = pr_id
                pr = self.novos[pr_id]
                pr["evidencias"].append(ev_id)
                pr["sustenta_aviso_saude_politica"] = bool(pr["sustenta_aviso_saude_politica"] or ev.get("sustenta_aviso_saude_politica"))
                onde = f"acervo/evidencias/{ev_id}.json"
                lug = {p: self.lugar((ev.get("lugares") or {}).get(p), p, onde, prot) for p in PAPEL}
                voz = {"tipo": ev["voz"]["tipo"]}
                if ev["voz"].get("papel"):
                    voz["papel"] = ev["voz"]["papel"]
                reg_ev = {"id": ev_id, "trecho": tr_id, "proposicao": pr_id, "sentido": ev["sentido"], "voz": voz,
                          "lugares": lug, "estado": "não conferida",
                          "sustenta_aviso_saude_politica": bool(ev.get("sustenta_aviso_saude_politica")),
                          "protecao": prot, "origem_registro": self.origem()}
                if ev.get("criterio_pratica_cultural"):
                    reg_ev["criterio_pratica_cultural"] = ev["criterio_pratica_cultural"]
                self.novos[ev_id] = reg_ev
                temas = True
            en["valencias"] = item["valencias"]
            en["sustenta_aviso_saude_politica"] = bool(item.get("sustenta_aviso_saude_politica"))
            if item["estado"] == "quarentena":
                en.update(estado="quarentena", selo="PENDENTE_JULGAMENTO", motivo_quarentena=item.get("motivo_quarentena") or "critério de valência em 0")
            else:
                en["estado"] = "extraído" if temas else "aceito"
                en.pop("selo", None)
                en.pop("motivo_quarentena", None)
            en["gera"] = {"fontes": [fo_id], **({"trechos": trechos} if trechos else {})}
            en["nota"] = (en.get("nota", "").rstrip(". ") + f". Triagem do bloco 7 ({saida.get('lote')}, {self.execucao}, valencias-0.1).").strip()
            self.novos[en_id] = en
        erros = []
        for i, reg in self.novos.items():
            pref = i.split("-")[0]
            e = validar_objeto(reg, carregar_esquema(ESQ[pref]))
            erros += [f"{i}: {x}" for x in e]
        return erros

    def escrever(self) -> list[str]:
        feitos = []
        for i, reg in self.novos.items():
            pref = i.split("-")[0]
            arq = self.raiz / ("entrada" if pref == "EN" else f"acervo/{PASTA[pref]}") / f"{i}.json"
            arq.parent.mkdir(parents=True, exist_ok=True)
            arq.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            feitos.append(arq.relative_to(self.raiz).as_posix())
        return feitos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("saida")
    ap.add_argument("--execucao", required=True)
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--raiz", type=Path, default=RAIZ, help="raiz do acervo (testes)")
    ap.add_argument("--manifestos", type=Path, help="pasta dos manifestos do ler_fonte.py (padrão: a pasta temporária)")
    a = ap.parse_args()
    saida = json.loads(Path(a.saida).read_text(encoding="utf-8"))
    manifestos: dict[str, dict] = {}
    for m in sorted((a.manifestos or pasta_temporaria()).glob("lote-*.json")):
        for it in json.loads(m.read_text(encoding="utf-8"))["itens"]:
            if it.get("caracteres") or it["id"] not in manifestos:
                manifestos[it["id"]] = it
    g = Gravador(a.execucao, a.raiz)
    erros = g.gravar_lote(saida, manifestos)
    if erros:
        print("REPROVA (nada gravado):", *erros, sep="\n  ")
        return 1
    conta: dict[str, int] = {}
    for i in g.novos:
        conta[i.split("-")[0]] = conta.get(i.split("-")[0], 0) + 1
    print("registros:", ", ".join(f"{k} {v}" for k, v in sorted(conta.items())))
    if a.simular:
        print("simulado: nada gravado")
        return 0
    print(f"{len(g.escrever())} arquivo(s) gravado(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
