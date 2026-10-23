"""Monta os acervos de teste dos scripts do núcleo (K-105, bloco 3).

EXEMPLO DE ESQUEMA: dados sintéticos, na faixa de IDs 900000-999999 (valor numeracao_id),
sem fonte real e sem pessoa real. Não contam como par real (brief, bloco 2).

acervo-ok/ passa no validar_acervo.py e no calcular_mu_lambda.py --conferir. acervo-d041/ é o
acervo-ok com os casos da D-041 (K-123, mu-lambda-0.2): a linhagem mista e as Evidências fora da
conta. Cada erro-*/ é uma cópia com uma só mudança, que deve reprovar. Rodar de novo regrava tudo:
    python testes/nucleo/montar_acervos.py
"""
from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ORIGEM = {"criado_por": "curador (exemplo de esquema, K-105)", "data": "2026-10-22", "execucao": "EX-900001"}
PROT = {"licenca": "não conferido", "consentimento": "não se aplica", "restricao_comunitaria": "nenhuma conhecida",
        "precisao_lugar": "UF", "dado_sensivel": False, "crianca_ou_adolescente": False, "pedido_de_retirada": "nenhum"}
NOTA = "exemplo de esquema (K-105): dado sintético"


def fonte(n, deriva=()):
    return {"id": f"FO-90000{n}", "referencia": {"titulo": f"Fonte sintética {n}", "instituicao": "exemplo de esquema",
            "ano": 2026, "tipo": "exemplo", "link_permanente": f"https://example.org/fonte-{n}"},
            "tipo_evidencia": "escrito publicado, de arquivo ou oficial", "data_fonte": "2026",
            "url": f"https://example.org/fonte-{n}", "wayback": "não feita", "data_acesso": "2026-10-22",
            "perspectiva": "pesquisador", "deriva_de": list(deriva), "protecao": PROT, "origem_registro": ORIGEM, "nota": NOTA}


def trecho(n, fo, texto):
    return {"id": f"TR-90000{n}", "fonte": fo, "texto_exato": texto, "antes": "", "depois": "",
            "localizador": "car. 0-60 do texto normalizado (normalizacao-0.2)", "hash": "0" * 64,
            "data_conferencia": "2026-10-22", "origem_texto": "fonte", "grau_semelhanca": 1.0,
            "versao_normalizacao": "normalizacao-0.2", "estado": "localizado", "protecao": PROT,
            "origem_registro": ORIGEM, "nota": NOTA}


def evid(n, tr, pr, voz=None, sentido="a favor"):
    return {"id": f"EV-90000{n}", "trecho": tr, "proposicao": pr, "sentido": sentido,
            "voz": voz or {"tipo": "autor"}, "lugares": {"pratica": "LU-900001", "publicacao": "LU-900001",
            "pesquisa": "LU-900001"}, "estado": "conferida", "protecao": PROT, "origem_registro": ORIGEM, "nota": NOTA}


def prop(n, evs, mu, lam, estado, detalhe=None, atributo="processo", **extra):
    r = {"id": f"PR-90000{n}", "clb": "CL-900001", "atributo": atributo, "valor": f"valor sintético {n}",
         "periodo": {"referido": "2026"}, "evidencias": evs, "mu": mu, "lambda": lam, "estado": estado,
         "sustenta_aviso_saude_politica": False, "versao_regra": "mu-lambda-0.2", "protecao": PROT,
         "origem_registro": ORIGEM, "nota": NOTA}
    if detalhe:
        r["estado_detalhe"] = detalhe
    r.update(extra)
    return r


def base() -> dict[str, dict]:
    r = [
        fonte(1), fonte(2, ["FO-900001"]), fonte(3),
        trecho(1, "FO-900001", "o suco era coado em pano e clarificado"),
        trecho(2, "FO-900002", "o suco era coado em pano e clarificado com resina"),
        trecho(3, "FO-900003", "clarificava-se o suco antes de engarrafar"),
        trecho(4, "FO-900003", "a gente sabe o ponto pela cor"),
        evid(1, "TR-900001", "PR-900001"), evid(2, "TR-900002", "PR-900001"), evid(3, "TR-900003", "PR-900001"),
        evid(4, "TR-900004", "PR-900002", {"tipo": "pessoa citada em fala direta", "pessoa": "P-900001"}),
        # PR-900001: FO-900001 e FO-900002 são uma linhagem, FO-900003 outra → μ = 2/2 = 1
        prop(1, ["EV-900001", "EV-900002", "EV-900003"], 1.0, 0.0, "verdadeiro"),
        # PR-900002: uma linhagem → μ = 0,5; Dc = 0,5; Dct = -0,5 → intermediário
        prop(2, ["EV-900004"], 0.5, 0.0, "intermediário", "quase-verdadeiro tendendo ao paracompleto", "ponto"),
        {"id": "TE-900001", "conceito": "conceito sintético", "designacoes": [{"forma": "bebida-exemplo"}],
         "variantes": [{"forma": "bebida exemplo", "tipo_variacao": "grafia sem hífen", "abonacoes": ["EV-900001"]}],
         "formas_de_busca": ["bebida-ezemplo"], "abonacoes": ["EV-900001"], "estado": "atestado",
         "relacoes": [], "protecao": PROT, "origem_registro": ORIGEM, "nota": NOTA},
        {"codigo": "P-900001", "papeis": ["detentor ou mestre", "quem fala no trecho"], "forma_atribuicao": "anônimo",
         "nivel_colaborador": "anônimo", "consentimento": "referência fora do Git (exemplo)", "protecao": PROT,
         "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "CP-900001", "designacao_local": "o ponto", "lugar": "LU-900001", "comunidade": "exemplo",
         "periodo": "2026", "evidencias": ["EV-900004"], "atestada_pratica_comum": True, "protecao": PROT,
         "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "LU-900001", "nivel": "UF", "nome_na_fonte": "UF sintética", "protecao": PROT, "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "F-900001", "tipo": "compreensao_local_nao_captada", "o_que_falta": "a W do elemento 2",
         "por_que": "nenhuma voz de quem pratica no exemplo", "onde_aparece": ["EL-900002"],
         "criada_por": "curador (exemplo de esquema, K-105)", "data": "2026-10-22", "nota": NOTA},
        {"id": "IN-900001", "nome": "fruto sintético", "tipo": "fruto", "status_botanico_cultural": "nativo", "proposicoes": ["PR-900001"], "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "PC-900001", "nome": "clarificação", "tipo": "separação", "proposicoes": ["PR-900001"], "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "PC-900002", "nome": "cozimento", "tipo": "calor", "proposicoes": ["PR-900002"], "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "EL-900001", "clb": "CL-900001", "x": ["IN-900001"], "y": ["PC-900001"], "z": "2026", "w": "CP-900001",
         "proposicoes": ["PR-900001"], "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "EL-900002", "clb": "CL-900001", "x": ["IN-900001"], "y": ["PC-900002"], "z": "2026", "w": "F-900001",
         "proposicoes": ["PR-900002"], "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "AR-900001", "de": "EL-900001", "para": "EL-900002", "tipo": "antecede", "tensao": False,
         "proposicoes": ["PR-900001"], "z": "2026", "w": "F-900001", "mu": 1.0, "lambda": 0.0, "estado": "verdadeiro",
         "versao_regra": "mu-lambda-0.2", "origem_registro": ORIGEM, "nota": NOTA},
        {"id": "CL-900001", "termo": "TE-900001", "termos": ["TE-900001"],
         "situacoes": [{"lugares": ["LU-900001"], "periodo": "2026", "evidencias": ["EV-900001"]}],
         "criterios": {"identidade_ou_memoria": {"evidencias": ["EV-900001"]}, "reconhecimento_pelo_grupo": {"falta": "F-900001"},
                       "transmissao_entre_geracoes": {"falta": "F-900001"}, "recriacao": {"falta": "F-900001"}},
         "estado": "admitida", "protecao": PROT, "origem_registro": ORIGEM, "nota": NOTA},
    ]
    return {(x.get("id") or x["codigo"]): x for x in r}


PASTA = {"AM": "ambientes", "EN": "entrada", "FO": "acervo/fontes", "TR": "acervo/trechos", "EV": "acervo/evidencias",
         "PR": "acervo/proposicoes", "TE": "acervo/termos", "P": "acervo/pessoas", "CP": "acervo/compreensoes",
         "LU": "acervo/lugares", "F": "acervo/faltas", "IN": "acervo/insumos", "PC": "acervo/processos",
         "EL": "acervo/elementos", "AR": "acervo/arestas", "CL": "acervo/clb"}
FICHA = """# CL-900001 (exemplo de esquema, K-105)

## Modo de fazer
O suco é coado em pano e clarificado [PR-900001]. Quem faz diz que conhece o ponto pela cor [PR-900002].

## Faltas
- F-900001: a W do elemento 2 não foi captada.

## Fontes
- FO-900001, FO-900002, FO-900003 (sintéticas).
"""


def gravar(nome: str, regs: dict[str, dict], ficha: str = FICHA, extra: dict[str, dict] | None = None):
    raiz = AQUI / nome
    if raiz.exists():
        shutil.rmtree(raiz)
    for id_, r in regs.items():
        p = raiz / PASTA[id_.split("-")[0]] / f"{id_}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for rel, r in (extra or {}).items():
        (raiz / rel).write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (raiz / "acervo" / "fichas").mkdir(parents=True, exist_ok=True)
    (raiz / "acervo" / "fichas" / "CL-900001.md").write_text(ficha, encoding="utf-8")


def main():
    ok = base()
    gravar("acervo-ok", ok)

    r = copy.deepcopy(ok)
    r["FO-900003"]["deriva_de"] = ["FO-900001"]  # agora as três fontes são uma linhagem só
    gravar("erro-mesma-linhagem", r)

    r = copy.deepcopy(ok)
    r["TE-900001"]["variantes"].append({"forma": "bebida-cxemplo", "tipo_variacao": "forma de OCR"})
    gravar("erro-ocr-variante", r)

    r = copy.deepcopy(ok)
    t = r["TR-900001"]
    for k in ("hash", "data_conferencia", "grau_semelhanca", "versao_normalizacao"):
        t.pop(k)
    t["estado"] = "não localizado"
    gravar("erro-atestado-sem-localizado", r)

    r = copy.deepcopy(ok)
    r["P-900001"]["papeis"] = ["autor de fonte"]
    gravar("erro-w-sem-pratica", r)

    gravar("erro-ficha-sem-marca", ok, FICHA.replace(" [PR-900002].", "."))

    r = copy.deepcopy(ok)
    r["EV-900001"]["trecho"] = "TR-900099"
    gravar("erro-evidencia-sem-trecho", r)

    # achados do auditor no K-105: marca no meio da frase (A-003), fato após comentário (A-005), ciclo (A-014)
    gravar("erro-ficha-marca-no-meio", ok, FICHA.replace("O suco é coado em pano e clarificado [PR-900001].",
                                                        "O suco [PR-900001] é coado em pano e clarificado."))
    gravar("erro-ficha-fato-apos-comentario", ok, FICHA.replace("## Faltas", "<!-- nota --> O caju era coado em pano.\n\n## Faltas"))
    r = copy.deepcopy(ok)
    r["FO-900001"]["deriva_de"] = ["FO-900002"]  # FO-900002 já deriva de FO-900001
    gravar("erro-deriva-ciclo", r)

    gravar("erro-colisao", ok, extra={"acervo/fontes/FO-900001-copia.json": ok["FO-900001"]})

    # D-041 (K-123, mu-lambda-0.2): os casos A-009 e A-010 do auditor no K-105
    d = copy.deepcopy(ok)
    t = trecho(5, "FO-900002", "o suco nunca era clarificado")
    t6 = trecho(6, "FO-900003", "o caju era cozido em tacho de cobre")
    for k in ("hash", "data_conferencia", "grau_semelhanca", "versao_normalizacao"):
        t6.pop(k)
    t6.update(estado="não verificável por máquina", falta="F-900002")
    e9 = evid(9, "TR-900003", "PR-900004")
    e9["estado"] = "leitura divergente"
    novos = [
        t, t6,
        # PR-900003 (A-010): FO-900001 e FO-900002 são uma linhagem, com Evidência a favor e divergente:
        # tensão interna, fora de μ e λ → μ = 0, λ = 0, Dct = −1 → paracompleto
        evid(5, "TR-900001", "PR-900003"), evid(6, "TR-900005", "PR-900003", sentido="divergente"),
        prop(3, ["EV-900005", "EV-900006"], 0.0, 0.0, "paracompleto", tensao_interna=["FO-900001"]),
        # PR-900004 (A-009): o trecho não verificável e a leitura divergente ficam fora da conta;
        # só a EV-900007 conta → μ = 0,5
        evid(8, "TR-900006", "PR-900004"), e9, evid(7, "TR-900001", "PR-900004"),
        prop(4, ["EV-900007", "EV-900008", "EV-900009"], 0.5, 0.0, "intermediário",
             "quase-verdadeiro tendendo ao paracompleto",
             fora_da_conta={"EV-900008": "trecho não verificável por máquina", "EV-900009": "leitura divergente"}),
        {"id": "F-900002", "tipo": "trecho_nao_verificavel", "o_que_falta": "trecho não verificável por máquina",
         "por_que": "semelhança abaixo do limiar (exemplo)", "onde_aparece": ["TR-900006"],
         "criada_por": "scripts/localizar_trecho.py (normalizacao-0.2)", "data": "2026-10-23", "nota": NOTA},
    ]
    d.update({(x.get("id") or x["codigo"]): x for x in novos})
    gravar("acervo-d041", d)

    r = copy.deepcopy(d)
    r["PR-900003"].update(mu=0.5, **{"lambda": 0.5}, estado="intermediário",
                          estado_detalhe="quase-verdadeiro tendendo ao inconsistente")
    r["PR-900003"].pop("tensao_interna")
    gravar("erro-linhagem-mista-dois-lados", r)  # como a regra mu-lambda-0.1 contava (A-010)

    r = copy.deepcopy(d)
    r["PR-900004"].update(mu=1.0, estado="verdadeiro")
    r["PR-900004"].pop("estado_detalhe")
    r["PR-900004"].pop("fora_da_conta")
    gravar("erro-fora-da-conta-contado", r)  # o trecho não verificável e a leitura divergente contados (A-009)

    r = copy.deepcopy(ok)
    r["PR-900001"]["versao_regra"] = "mu-lambda-0.1"
    gravar("erro-regra-antiga", r)
    print("acervos de teste montados em", AQUI)


if __name__ == "__main__":
    main()
