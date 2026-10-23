"""K-106 (bloco 4): grava as fichas de acesso testadas em ambientes/<id>.json e a tradução de cada
Consulta em ambientes/traducao-consultas.json, a partir da saída do rastreador (EX-0016), sem IA.

Uso: python trilhas/2026-10-23_K-106/gravar_fichas_traducoes.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]
AQUI = Path(__file__).resolve().parent
EX = "EX-0016"
DATA = "2026-10-23"
UA = "CulturaLiquida-rastreador/0.1 (+https://github.com/Indalt/cultura-liquida)"
BDTD = "https://bdtd.ibict.br/vufind/api/v1/search?type=AllFields&limit=0&lookfor="

fichas = json.loads((AQUI / "fichas.json").read_text(encoding="utf-8"))
VIA = {
    "AM-0061": ("proposto", "via automática não testada: o nome não resolveu na rede da sessão em 23/10/2026; via humana até o reteste"),
    "AM-0029": ("proposto", "OAI-PMH em https://www.infoteca.cnptia.embrapa.br/oai/request (colheita e filtro local); a busca por texto do site é vedada ao robô pelo robots.txt e fica na via humana"),
    "AM-0021": ("proposto", "API VuFind v1 em JSON (https://bdtd.ibict.br/vufind/api/v1/search), lookfor em UTF-8 percent-encoded; o RSS de busca é vedado pelo robots.txt"),
    "AM-0001": ("proposto", "via humana: o leitor automático recebeu 403 com desafio do Cloudflare em 15/10 e em 23/10/2026; nunca se contorna"),
}
for am, (est, via) in VIA.items():
    p = R / "ambientes" / f"{am}.json"
    a = json.loads(p.read_text(encoding="utf-8"))
    a["ficha_de_acesso"] = fichas[am]
    a["via_protocolo"] = via
    a["estado_escavacao"] = est
    a["ultima_visita"] = DATA
    marca = f" Ficha de acesso testada em {DATA} pelo rastreador ({EX}, K-106); trilha em trilhas/2026-10-23_K-106/."
    a["nota"] = a.get("nota", "").split(" Ficha de acesso testada em ")[0] + marca  # idempotente
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

NAO_BCR = {"sintaxe": "não testada: o nome bcr.iphan.gov.br não resolveu na rede da sessão; hipóteses na ficha (WordPress ?s=, API REST do WordPress ou do Tainacan), sem saber se há OR", "pedido": "não feito", "data": DATA, "resposta": "sem resposta HTTP (curl 6, Could not resolve host)", "total_informado": "não informado", "perda": "não conferida", "estado": "não testada (falta: reteste)"}
NAO_INFOTECA = {"pedido": "não feito: o robots.txt veda /simple-search e /discover ao robô; o OAI-PMH não busca por texto", "data": DATA, "resposta": "não aplicável", "total_informado": "não informado", "perda": "a consulta inteira na via automática: colher o OAI-PMH (59.357 registros em 23/10) e filtrar localmente; a sintaxe dada é a da busca humana", "estado": "não testada: via humana para a busca por texto"}
HUMANA = {"pedido": "digitação humana na busca da Hemeroteca; nenhum pedido do robô", "data": DATA, "resposta": "não testada: via humana (403 em 23/10/2026)", "total_informado": "não informado", "perda": "nenhuma prevista pela sintaxe do Anexo E (aspas, + para e, / para ou, parênteses; acento indiferente); não conferida na prática", "estado": "não testada: via humana"}
SEM_HIFEN = ("Para usar na BDTD: a mesma Consulta sem as formas de hífen de quebra de linha, que são de texto lido por OCR e não de metadado digitado; no teste variante por variante de 23/10, \"cajuí-na\" deu 1305 (quase o total de \"caju\", 1306) e \"ca-juína\" 128, contra 25 de \"cajuína\". "
             "As formas continuam no Termo e nas fontes de OCR; o ruído fica anotado, sem apagar (insumo novo sobre a regra das formas por tipo de ambiente).")


def bdtd(sintaxe, cod, total, perda, extra=None):
    d = {"sintaxe": sintaxe, "pedido": "GET " + BDTD + cod, "data": DATA, "resposta": f"HTTP 200 {{\"resultCount\":{total},\"status\":\"OK\"}}", "total_informado": total, "perda": perda, "estado": "testada"}
    if extra:
        d.update(extra)
    return d


TERMO1 = '("caju" OR "cajú" OR "ca-ju")'
TERMO2 = '("cajuína" OR "cajuina" OR "caju-ína" OR "cajuí-na" OR "ca-juína" OR "cajuyna")'
DESCR = '("processamento do pedúnculo" OR "etapas de produção" OR colheita OR descastanhamento)'
C_T1 = "%28%22caju%22+OR+%22caj%C3%BA%22+OR+%22ca-ju%22%29"
C_T2 = "%28%22caju%C3%ADna%22+OR+%22cajuina%22+OR+%22caju-%C3%ADna%22+OR+%22caju%C3%AD-na%22+OR+%22ca-ju%C3%ADna%22+OR+%22cajuyna%22%29"
C_D = "%28%22processamento+do+ped%C3%BAnculo%22+OR+%22etapas+de+produ%C3%A7%C3%A3o%22+OR+colheita+OR+descastanhamento%29"
VARS = {"cajuína": ("%22caju%C3%ADna%22", 25), "cajuina": ("%22cajuina%22", 25), "caju-ína": ("%22caju-%C3%ADna%22", 0),
        "cajuí-na": ("%22caju%C3%AD-na%22", 1305), "ca-juína": ("%22ca-ju%C3%ADna%22", 128), "cajuyna": ("%22cajuyna%22", 0)}

trad = {
    "nota": f"Tradução de cada Consulta (ambientes/consultas/) para a sintaxe de cada fonte do piloto, testada e datada pelo rastreador em {DATA} ({EX}, K-106; brief, bloco 4; Fundação l. 426). Um pedido por fonte e Consulta, só o total informado (limit=0), nada coletado; robô identificado ({UA}). Seis pedidos da BDTD mandados antes em Latin-1 devolveram a base inteira (1.167.710) e foram descartados como inválidos (trilha: trilhas/2026-10-23_K-106/).",
    "regra": "termo-0.2",
    "CO-0001": {
        "AM-0021": bdtd(f"VuFind AllFields: {TERMO1}", C_T1, 1306, "nenhuma de sintaxe (aspas, OR, parênteses aceitos)"),
        "AM-0029": dict(NAO_INFOTECA, sintaxe="busca humana: caju OR cajú OR \"ca-ju\""),
        "AM-0061": NAO_BCR,
        "AM-0001": dict(HUMANA, sintaxe="(caju/\"ca-ju\") (acento indiferente: cajú já coberto)"),
    },
    "CO-0002": {
        "AM-0021": bdtd(f"VuFind AllFields: {TERMO2}", C_T2, 1441, "nenhuma de sintaxe; o total sobe pelas formas de hífen (ver variantes)",
                        {"variantes": {f: {"pedido": "GET " + BDTD + c, "total_informado": n} for f, (c, n) in VARS.items()},
                         "uso": SEM_HIFEN}),
        "AM-0029": dict(NAO_INFOTECA, sintaxe="busca humana: cajuína OR cajuina OR \"caju-ína\" OR \"cajuí-na\" OR \"ca-juína\" OR cajuyna"),
        "AM-0061": NAO_BCR,
        "AM-0001": dict(HUMANA, sintaxe="(cajuína/\"caju-ína\"/\"cajuí-na\"/\"ca-juína\"/cajuyna) (acento indiferente: cajuina já coberta)"),
    },
    "CO-0003": {
        "AM-0021": bdtd(f"VuFind AllFields: {TERMO1} AND {DESCR}", C_T1 + "+AND+" + C_D, 80, "nenhuma de sintaxe (AND aceito)"),
        "AM-0029": dict(NAO_INFOTECA, sintaxe=f"busca humana: (caju OR \"ca-ju\") AND {DESCR}"),
        "AM-0061": NAO_BCR,
        "AM-0001": dict(HUMANA, sintaxe="(caju/\"ca-ju\")+(\"processamento do pedúnculo\"/\"etapas de produção\"/colheita/descastanhamento)"),
    },
    "CO-0004": {
        "AM-0021": bdtd(f"VuFind AllFields: {TERMO2} AND {DESCR}", C_T2 + "+AND+" + C_D, 83, "nenhuma de sintaxe (AND aceito); as formas de hífen pesam como em CO-0002", {"uso": SEM_HIFEN}),
        "AM-0029": dict(NAO_INFOTECA, sintaxe=f"busca humana: {TERMO2} AND {DESCR}"),
        "AM-0061": NAO_BCR,
        "AM-0001": dict(HUMANA, sintaxe="(cajuína/\"caju-ína\"/\"cajuí-na\"/\"ca-juína\"/cajuyna)+(\"processamento do pedúnculo\"/\"etapas de produção\"/colheita/descastanhamento)"),
    },
    "CO-0005": {
        "AM-0021": bdtd("VuFind AllFields: (\"processamento do pedúnculo\" OR descastanhamento)", "%28%22processamento+do+ped%C3%BAnculo%22+OR+descastanhamento%29", 10, "nenhuma de sintaxe"),
        "AM-0029": dict(NAO_INFOTECA, sintaxe="busca humana: \"processamento do pedúnculo\" OR descastanhamento (caso de controle: o item 748513, 'Processamento do pedúnculo do caju: cajuína')"),
        "AM-0061": NAO_BCR,
        "AM-0001": dict(HUMANA, sintaxe="\"processamento do pedúnculo\"/descastanhamento"),
    },
}
(R / "ambientes" / "traducao-consultas.json").write_text(json.dumps(trad, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("fichas: 4; traduções: 5 Consultas × 4 fontes")
