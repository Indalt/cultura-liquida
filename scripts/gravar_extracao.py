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
Pessoas (K-110; padrão do K-104, valor tabela_codigo_nome): a voz de pessoa citada vem do avaliador
só por rótulo local (`voz.rotulo_pessoa`, ex.: "V01"); o nome fica no arquivo de rótulos que o
avaliador grava fora do Git (`--pessoas`). O script dá o código opaco P-nnnn (o mesmo nome reaproveita
o código), grava a Pessoa em `acervo/pessoas/` só com código e papéis, e a tabela código → nome na
pasta privada (`CL_PRIVADO` ou o caminho padrão do registro), nunca no repositório. Um Trecho cujo
texto exato traz um nome da tabela reprova; no "antes" e no "depois", o contexto é cortado no nome
e também num tratamento seguido de nome próprio ("Dona", "D.", "seu", "tia"...), que pega a pessoa
que a fonte nomeia sem falar (sem rótulo). `--recortar-contextos` aplica o corte aos Trechos já
gravados (o contexto é só seletor de citação: o hash e o localizador não mudam).

Uso:
    python scripts/gravar_extracao.py <saida-do-avaliador.json> --execucao EX-nnnn [--simular]
        [--raiz <pasta>] [--manifestos <pasta>] [--pessoas <rótulos fora do Git> ...] [--privado <pasta>] [--clb CL-nnnn]
`--execucao` é a Execução do avaliador (o log dele, gravado antes pelo curador).
`--clb CL-nnnn` (0.3, K-111, insumo 92): as Evidências que um lote separou como de outra CLB (D-039) vão
à CLB candidata dada, que já existe (nasce pela regra das menções); a Fonte já gravada fica como está, e a
Entrada só ganha os Trechos novos. O que a Falta de conhecimento tradicional marca não entra no arquivo
de saída: fica na pasta local (D-043, 3).
Código 0 = gravou (ou simulou) sem erro; 1 = algum registro reprova (nada se grava).
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, proximo_id  # noqa: E402
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from localizar_trecho import pasta_temporaria  # noqa: E402
from nomes_provaveis import lugares as lugares_ibge, provaveis  # noqa: E402

VERSAO = "gravar-extracao-0.3"
PASTA = {"FO": "fontes", "TR": "trechos", "EV": "evidencias", "PR": "proposicoes", "LU": "lugares",
         "CL": "clb", "F": "faltas", "P": "pessoas"}
ESQ = {"FO": "fonte", "TR": "trecho", "EV": "evidencia", "PR": "proposicao", "LU": "lugar", "CL": "clb",
       "F": "falta", "EN": "entrada", "P": "pessoa"}
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


def pasta_privada() -> Path:
    """A pasta da tabela código → nome (valor tabela_codigo_nome), fora do repositório."""
    return Path(os.environ.get("CL_PRIVADO") or "C:/Antigravity/Cultura Liquida - privado") / "pessoas"


def fora_do_repositorio(p: Path) -> bool:
    """Fora do repositório, ou nos casos de teste (`testes/`, com nomes fictícios)."""
    try:
        rel = p.resolve().relative_to(RAIZ.resolve())
    except ValueError:
        return True
    return rel.parts[:1] == ("testes",)


def formas_do_nome(info: dict) -> list[str]:
    return [f for f in [info.get("nome"), *info.get("outras_formas", [])] if f and len(f.strip()) >= 4]


RE_TRATAMENTO = re.compile(r"(?<!\w)(Dona|D\.|Seu|seu|Sr\.?|Sra\.?|Dr\.?|Dra\.?|Mestre|Tia|tia|Tio|tio|Vó|vó|Vovó|Padre|Frei)"
                           r"\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ]+")


_LUGS: set[str] = set()


def cortar_nome(contexto: str, formas: list[str], lado: str) -> str:
    """Corta o "antes" depois do último nome achado e o "depois" antes do primeiro (o contexto é só seletor).
    Desde a 0.3 (K-111, insumo 76), corta também no nome provável da regra nomes-0.1, que não depende da
    leitura: o contexto perde só o pedaço, e o hash e o localizador do Trecho não mudam."""
    for f in formas:
        baixo = contexto.lower()
        k = baixo.rfind(f.lower()) if lado == "antes" else baixo.find(f.lower())
        if k >= 0:
            contexto = contexto[k + len(f):] if lado == "antes" else contexto[:k]
    achados = list(RE_TRATAMENTO.finditer(contexto))
    if achados:
        contexto = contexto[achados[-1].end():] if lado == "antes" else contexto[:achados[0].start()]
    if not _LUGS:
        _LUGS.update(lugares_ibge())
    for seq in provaveis(contexto, _LUGS):
        k = contexto.rfind(seq) if lado == "antes" else contexto.find(seq)
        if k >= 0:
            contexto = contexto[k + len(seq):] if lado == "antes" else contexto[:k]
    return contexto


def recortar_contextos(raiz: Path, formas: list[str], simular: bool) -> list[str]:
    """Aplica o corte aos Trechos já gravados; devolve os que mudaram."""
    mudados = []
    for arq in sorted((raiz / "acervo" / "trechos").glob("TR-*.json")):
        reg = json.loads(arq.read_text(encoding="utf-8"))
        novo = {**reg, "antes": cortar_nome(reg.get("antes", ""), formas, "antes"),
                "depois": cortar_nome(reg.get("depois", ""), formas, "depois")}
        if novo != reg:
            mudados.append(reg["id"])
            if not simular:
                arq.write_text(json.dumps(novo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mudados


class Gravador:
    def __init__(self, execucao: str, raiz: Path = RAIZ, rotulos: dict | None = None, privado: Path | None = None):
        self.raiz = raiz
        self.indice, _, erros = carregar_acervo(raiz)
        if erros:
            raise SystemExit("acervo ilegível: " + "; ".join(erros))
        self.ids = set(self.indice)
        self.novos: dict[str, dict] = {}
        self.execucao = execucao
        self.hoje = date.today().isoformat()
        self.ibge = tabela_ibge()
        self.rotulos = rotulos or {}
        self.privado = privado or pasta_privada()
        arq_tab = self.privado / "tabela.json"
        self.tabela: dict[str, dict] = json.loads(arq_tab.read_text(encoding="utf-8")) if arq_tab.exists() else {}
        self.formas = sorted({f for info in [*self.tabela.values(), *self.rotulos.values()] for f in formas_do_nome(info)},
                             key=len, reverse=True)

    def pessoa(self, rotulo: str, onde: str) -> str:
        """O código opaco da pessoa do rótulo local; o nome só na tabela privada."""
        info = self.rotulos.get(rotulo)
        if not info or not info.get("nome"):
            raise SystemExit(f"{onde}: rótulo de pessoa {rotulo} sem nome no arquivo de rótulos (--pessoas)")
        cod = next((c for c, t in self.tabela.items() if chave(t["nome"]) == chave(info["nome"])), None)
        if not cod:
            cod = self.novo_id("P")
            self.tabela[cod] = {"nome": info["nome"], "outras_formas": info.get("outras_formas", []), "onde": []}
        if onde not in self.tabela[cod]["onde"]:
            self.tabela[cod]["onde"].append(onde)
        reg = self.novos.get(cod) or (dict(self.indice[cod]) if cod in self.indice else {
            "codigo": cod, "papeis": [], "forma_atribuicao": "nome", "nivel_colaborador": "identificado",
            "nota": "pessoa nomeada na fonte; no Git, só o código e os papéis (a tabela código → nome fica fora do repositório)",
            "consentimento": "não se aplica (fala publicada em fonte de terceiro; o projeto não colheu a fala)",
            "protecao": {"licenca": "não conferido", "consentimento": "não se aplica", "restricao_comunitaria": "nenhuma conhecida",
                         "precisao_lugar": "não se aplica", "dado_sensivel": False, "crianca_ou_adolescente": False,
                         "pedido_de_retirada": "nenhum"},
            "origem_registro": self.origem()})
        reg["papeis"] = list(dict.fromkeys([*reg.get("papeis", []), *info.get("papeis", ["quem fala no trecho"])]))
        self.novos[cod] = reg
        return cod

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

    def gravar_lote(self, saida: dict, manifestos: dict[str, dict], clb_destino: str | None = None) -> list[str]:
        if clb_destino and clb_destino not in self.indice:
            raise SystemExit(f"--clb {clb_destino}: a CLB não existe no acervo (nasce pela regra das menções, mencoes_incidentais.py)")
        clb = clb_destino or self.clb_cajuina()
        props: dict[str, str] = {}
        for item in saida["entradas"]:
            en_id = item["entrada"]
            en = dict(carregar_json(self.raiz / "entrada" / f"{en_id}.json"))
            prot = en["protecao"]
            man = manifestos.get(en_id, {})
            fo = item.get("fonte") or {}
            fo_id = self.por("FO", lambda r: r.get("entrada") == en_id) or self.novo_id("FO")
            separadas = bool(clb_destino)
            if separadas and fo_id not in self.indice:
                raise SystemExit(f"--clb: {en_id} sem Fonte no acervo; as Evidências separadas vêm de uma fonte já extraída")
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
            if not separadas:  # com --clb, a Fonte já gravada fica como está
                self.novos[fo_id] = fonte
            trechos, temas = [], False
            for ev in item.get("evidencias", []):
                r = json.loads(Path(ev["arquivo_trecho"]).read_text(encoding="utf-8"))
                tr = r["trecho"]
                if man.get("hash_texto") and tr.get("hash") and tr["hash"] != man["hash_texto"]:
                    raise SystemExit(f"{en_id}: hash do Trecho ≠ hash do texto lido no manifesto ({ev['arquivo_trecho']})")
                baixo = tr["texto_exato"].lower()
                if any(f.lower() in baixo for f in self.formas):
                    raise SystemExit(f"{en_id}: o texto exato de {ev['arquivo_trecho']} traz um nome da tabela de pessoas; "
                                     "o avaliador escolhe outro trecho (o nome só entra por código opaco)")
                tr = {**tr, "antes": cortar_nome(tr.get("antes", ""), self.formas, "antes"),
                      "depois": cortar_nome(tr.get("depois", ""), self.formas, "depois")}
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
                if ev["voz"].get("rotulo_pessoa"):
                    voz["pessoa"] = self.pessoa(ev["voz"]["rotulo_pessoa"], onde)
                reg_ev = {"id": ev_id, "trecho": tr_id, "proposicao": pr_id, "sentido": ev["sentido"], "voz": voz,
                          "lugares": lug, "estado": "não conferida",
                          "sustenta_aviso_saude_politica": bool(ev.get("sustenta_aviso_saude_politica")),
                          "protecao": prot, "origem_registro": self.origem()}
                if ev.get("criterio_pratica_cultural"):
                    reg_ev["criterio_pratica_cultural"] = ev["criterio_pratica_cultural"]
                self.novos[ev_id] = reg_ev
                temas = True
            if separadas:  # a Entrada só ganha os Trechos novos; a triagem dela é a do lote de origem
                en["gera"] = {**(en.get("gera") or {}), "trechos": list(dict.fromkeys([*(en.get("gera") or {}).get("trechos", []), *trechos]))}
                en["nota"] = (en.get("nota", "").rstrip(". ") + f". Evidências separadas gravadas na {clb} ({saida.get('lote')}, {VERSAO}).").strip()
                self.novos[en_id] = en
                continue
            en["valencias"] = item["valencias"]
            en["sustenta_aviso_saude_politica"] = bool(item.get("sustenta_aviso_saude_politica"))
            if item["estado"] == "quarentena":
                en.update(estado="quarentena", selo="PENDENTE_JULGAMENTO", motivo_quarentena=item.get("motivo_quarentena") or "critério de valência em 0")
            else:
                en["estado"] = "extraído" if temas or en.get("estado") == "extraído" else "aceito"
                en.pop("selo", None)
                en.pop("motivo_quarentena", None)
            # uma fonte longa se lê em mais de um lote (K-110, o dossiê do IPHAN): os Trechos se somam
            trechos = list(dict.fromkeys([*(en.get("gera") or {}).get("trechos", []), *trechos]))
            en["gera"] = {"fontes": [fo_id], **({"trechos": trechos} if trechos else {})}
            en["nota"] = (en.get("nota", "").rstrip(". ") + f". Triagem pela extrair-evidencia ({saida.get('lote')}, {self.execucao}, valencias-0.1).").strip()
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
        if any(i.startswith("P-") for i in self.novos):
            self.privado.mkdir(parents=True, exist_ok=True)
            (self.privado / "tabela.json").write_text(json.dumps(self.tabela, ensure_ascii=False, indent=2), encoding="utf-8")
        return feitos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("saida", nargs="?")
    ap.add_argument("--recortar-contextos", action="store_true",
                    help="corta nomes no antes e no depois dos Trechos já gravados (sem saída do avaliador)")
    ap.add_argument("--execucao")
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--raiz", type=Path, default=RAIZ, help="raiz do acervo (testes)")
    ap.add_argument("--manifestos", type=Path, help="pasta dos manifestos do ler_fonte.py (padrão: a pasta temporária)")
    ap.add_argument("--pessoas", type=Path, nargs="+", default=[],
                    help="rótulos locais → nome, gravados pelo avaliador fora do Git (vários lotes: os rótulos se somam)")
    ap.add_argument("--privado", type=Path, help="pasta da tabela código → nome (padrão: CL_PRIVADO ou o caminho do registro)")
    ap.add_argument("--clb", help="CLB candidata de destino das Evidências separadas como outra CLB (insumo 92; K-111)")
    a = ap.parse_args()
    rotulos = {}
    for arq in a.pessoas:
        if not fora_do_repositorio(arq):
            print("REPROVA: o arquivo de rótulos de pessoas está dentro do repositório; nada gravado.")
            return 1
        rotulos.update(json.loads(arq.read_text(encoding="utf-8")))
    if a.privado and not fora_do_repositorio(a.privado):
        print("REPROVA: a pasta privada está dentro do repositório; nada gravado.")
        return 1
    if a.recortar_contextos:
        g = Gravador(a.execucao or "EX-0000", a.raiz, rotulos, a.privado)
        mud = recortar_contextos(a.raiz, g.formas, a.simular)
        print(f"{len(mud)} Trecho(s) com o contexto cortado{' (simulado)' if a.simular else ''}: {', '.join(mud)}")
        return 0
    if not (a.saida and a.execucao):
        ap.error("a saída do avaliador e --execucao")
    saida = json.loads(Path(a.saida).read_text(encoding="utf-8"))
    manifestos: dict[str, dict] = {}
    for m in sorted((a.manifestos or pasta_temporaria()).glob("lote-*.json")):
        for it in json.loads(m.read_text(encoding="utf-8"))["itens"]:
            if it.get("caracteres") or it["id"] not in manifestos:
                manifestos[it["id"]] = it
    g = Gravador(a.execucao, a.raiz, rotulos, a.privado)
    erros = g.gravar_lote(saida, manifestos, a.clb)
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
