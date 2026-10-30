"""Monta os casos reais da rodada B (bloco 9; K-111) nos exemplos de cada habilidade.

Cada caso é um JSON pequeno que o `testes/rodada-b/caso_real.py` roda sobre uma cópia do acervo do
momento: o par real que passa e a cópia do real com o erro injetado (padrão da rodada A; brief, l. 348).
Grava `.claude/skills/<h>/exemplos/real-*.json` e a lista `exemplos/casos-rodada-b.json` de cada
habilidade, que o `rodar_testes.py` lê com `--rodada B`. Rodar de novo regrava tudo:
    python testes/rodada-b/montar_casos.py
O que o piloto não deu não se inventa (brief, seção 6C, item 7): fica dito no LEIA-ME da habilidade.
"""
from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RODAR = "testes/rodada-b/caso_real.py"
VALIDAR = ["scripts/validar_acervo.py", "--raiz", "{raiz}"]
MU_LAMBDA = ["scripts/calcular_mu_lambda.py", "--raiz", "{raiz}", "--conferir", "--sem-grafo"]

CASOS: dict[str, list[dict]] = {
    "registrar-termo": [
        {"arq": "real-te0002", "nome": "TE-0002 cajuína, atestado, com o termo ambíguo marcado (e o TE-0004 que divide a forma)",
         "espera": "passa", "caso": {"sementes": ["TE-0002", "TE-0004"],
                                     "validadores": [VALIDAR, ["scripts/gerar_termo.py", "--raiz", "{raiz}"]]},
         "criterio": "Termo real do piloto (K-110): atestado por abonações de Trecho localizado; os booleanos saem do Termo; 'mocororó' marcado como termo ambíguo nos dois Termos (D-039)"},
        {"arq": "erro-te0002-ocr-variante", "nome": "TE-0002 com a forma de busca 'cajuyna' registrada como variante de OCR",
         "espera": "reprova", "caso": {"sementes": ["TE-0002", "TE-0004"], "validadores": [VALIDAR],
                                       "mudancas": [{"registro": "TE-0002", "op": "anexar", "caminho": ["variantes"],
                                                     "valor": {"forma": "cajuina", "tipo_variacao": "grafia sem acento vinda do OCR das bases"}}]},
         "criterio": "erro do brief (l. 348): forma de OCR nunca é variante, só forma de busca"},
        {"arq": "erro-te0002-ambiguo-sem-marca", "nome": "TE-0002 com 'mocororó' como designação local, sem a marca de termo ambíguo",
         "espera": "reprova", "caso": {"sementes": ["TE-0002", "TE-0004"], "validadores": [VALIDAR],
                                       "mudancas": [{"registro": "TE-0002", "op": "set", "caminho": ["variantes", 1, "tipo_variacao"],
                                                     "valor": "designação local, de alguns produtores do Piauí, para a cajuína crua, no período das fontes (2009–2014)"}]},
         "criterio": "insumos 26 e 88 (D-039): a forma que nomeia mais de um Termo é termo ambíguo e se marca nos dois; o erro do K-110 foi tratar 'mocororó' como nome de uma CLB só"},
    ],
    "extrair-evidencia": [
        {"arq": "real-tr0001", "nome": "TR-0001 (EV-0001, conferida pelo auditor) relocalizado na janela de citação",
         "espera": "passa", "caso": {"modo": "trecho", "trecho": "TR-0001"},
         "criterio": "Trecho real do piloto (K-109), localizado pelo script, nunca pela IA; a fonte é reduzida à janela de citação que já está no Git (o texto integral nunca entra, l. 100)"},
        {"arq": "erro-tr0034-palavra-de-outro-trecho", "nome": "TR-0034 com 'fresco', palavra de outro trecho, marcado como localizado",
         "espera": "reprova", "caso": {"modo": "trecho", "trecho": "TR-0034",
                                       "mudancas": [{"op": "set", "caminho": ["texto_exato"],
                                                     "valor": "A cajuína é o suco do caju fresco e puro, clarificado, sem adição de açúcar e conservantes, acondicionado em garrafas que são colocadas por um período de cozimento em banho-maria para o líquido adquirir uma coloração âmbar e um sabor característico"}]},
         "criterio": "erro do brief (l. 348): trecho não localizado marcado como localizado; o erro injetado é o do achado A5 do K-109 (insumo 72): 'fresco' veio de outro trecho"},
        {"arq": "real-tr0101-ligadura", "nome": "TR-0101 com a ligadura 'ﬁ' no texto exato e o grau gravado da leitura com 'fi' (0,9746)",
         "espera": "passa", "caso": {"modo": "trecho", "trecho": "TR-0101",
                                     "mudancas": [{"op": "set", "caminho": ["grau_semelhanca"], "valor": 0.9746}]},
         "criterio": "insumo 83 (achado A6 do K-110): o texto exato é literal na fonte (relido 1.0) e o grau gravado é o da leitura do agente; o conferir não acusa diferença falsa"},
        {"arq": "real-pr0001", "nome": "PR-0001 com a EV-0004 (leitura divergente) fora da conta de μ e λ",
         "espera": "passa", "caso": {"sementes": ["PR-0001"], "validadores": [MU_LAMBDA]},
         "criterio": "par real do achado A1 do K-109 (insumo 72): a Evidência ligada a Proposição que diz mais que o trecho fica visível e fora da conta (D-041)"},
        {"arq": "erro-pr0001-divergente-contada", "nome": "PR-0001 gravada sem a EV-0004 em fora_da_conta (a leitura divergente contada)",
         "espera": "reprova", "caso": {"sementes": ["PR-0001"], "validadores": [MU_LAMBDA],
                                       "mudancas": [{"registro": "PR-0001", "op": "set", "caminho": ["fora_da_conta"], "valor": {}}]},
         "criterio": "insumo 72, A1: a leitura divergente nunca pesa; o recálculo reprova a Proposição gravada que a conta"},
        {"arq": "real-pr0002", "nome": "PR-0002 com a marca de saúde da EV-0002",
         "espera": "passa", "caso": {"sementes": ["PR-0002"], "validadores": [VALIDAR]},
         "criterio": "par real do achado A3 do K-109 (insumo 72): a marca de aviso, saúde ou política da Evidência vai à Proposição (acervo-0.4, item 13)"},
        {"arq": "erro-pr0002-marca-perdida", "nome": "PR-0002 sem a marca de saúde que a EV-0002 tem",
         "espera": "reprova", "caso": {"sementes": ["PR-0002"], "validadores": [VALIDAR],
                                       "mudancas": [{"registro": "PR-0002", "op": "set", "caminho": ["sustenta_aviso_saude_politica"], "valor": False}]},
         "criterio": "insumo 72, A3: a marca faltando numa Proposição de composição (o erro real do K-109, antes do lote de correção)"},
        {"arq": "erro-tr0505-rotulo-sem-palavra", "nome": "'mocororó' declarado num trecho da p. 100 que não traz a palavra",
         "espera": "reprova", "comando": ["scripts/mencoes_incidentais.py", "--separadas",
                                          ".claude/skills/extrair-evidencia/exemplos/erro-tr0505-separadas.json", "--simular"],
         "criterio": "insumo 88: o rótulo de uma menção usa só a palavra que o trecho traz; o erro real do K-110 (a p. 100 do dossiê rotulada 'mocororó')"},
    ],
    "montar-ficha": [
        {"arq": "real-cl0001", "nome": "ficha CL-0001 (cajuína) com as Proposições que ela marca",
         "espera": "passa", "caso": {"fichas": ["CL-0001.md"], "validadores": [VALIDAR]},
         "criterio": "ficha real do piloto (K-110): toda frase factual com a marca [PR-nnnn] de uma Proposição que existe"},
        {"arq": "erro-cl0001-frase-sem-proposicao", "nome": "ficha CL-0001 com uma frase factual sem a marca da Proposição",
         "espera": "reprova", "caso": {"fichas": ["CL-0001.md"], "validadores": [VALIDAR],
                                       "mudancas": [{"arquivo": "acervo/fichas/CL-0001.md", "op": "texto",
                                                     "de": "enquanto a bebida fermentada ficou nos cantos recônditos (μ 0,5, intermediário) [PR-0402].",
                                                     "para": "enquanto a bebida fermentada ficou nos cantos recônditos (μ 0,5, intermediário)."}]},
         "criterio": "erro do brief (l. 348): frase factual sem Proposição"},
        {"arq": "real-educacao-cl0001", "nome": "camada Educação da CL-0001 (K-110), com as marcas e as habilidades da BNCC",
         "espera": "passa", "caso": {"fichas": ["educacao/CL-0001.md"], "validadores": [VALIDAR]},
         "criterio": "insumo 80 (regra educacao-0.1, acervo-0.4, item 14): cada item sobre a CLB com a marca; cada habilidade com código, texto literal e página do PDF oficial"},
        {"arq": "erro-educacao-bncc-sem-pagina", "nome": "camada Educação com uma habilidade da BNCC sem a página do PDF",
         "espera": "reprova", "caso": {"fichas": ["educacao/CL-0001.md"], "validadores": [VALIDAR],
                                       "mudancas": [{"arquivo": "acervo/fichas/educacao/CL-0001.md", "op": "texto",
                                                     "de": "| p. 82 |", "para": "| não conferida |"}]},
         "criterio": "insumo 80: a habilidade da BNCC cita a página do PDF do MEC, e não uma Proposição"},
    ],
    "gerar-grafo": [
        {"arq": "real-pr0016", "nome": "PR-0016 com duas linhagens a favor (FO-0008 e FO-0009), μ 1,0",
         "espera": "passa", "caso": {"sementes": ["PR-0016"], "validadores": [MU_LAMBDA]},
         "criterio": "Proposição real do piloto: μ e λ gravados batem com o recálculo por linhagens independentes"},
        {"arq": "erro-pr0016-mesma-linhagem", "nome": "PR-0016 com a FO-0009 derivada da FO-0008 e o μ gravado contando duas",
         "espera": "reprova", "caso": {"sementes": ["PR-0016"], "validadores": [MU_LAMBDA],
                                       "mudancas": [{"registro": "FO-0009", "op": "set", "caminho": ["deriva_de"], "valor": ["FO-0008"]}]},
         "criterio": "erro do brief (l. 348): duas fontes da mesma linhagem contadas como duas"},
        {"arq": "real-pr0065", "nome": "PR-0065 com tensão interna de linhagem (FO-0032 e FO-0034), fora de μ e λ",
         "espera": "passa", "caso": {"sementes": ["PR-0065"], "validadores": [MU_LAMBDA]},
         "criterio": "par real da D-041: a linhagem com Evidência a favor e divergente fica sinalizada e não pesa em nenhum lado"},
        {"arq": "erro-pr0065-tensao-apagada", "nome": "PR-0065 gravada sem a tensão interna sinalizada",
         "espera": "reprova", "caso": {"sementes": ["PR-0065"], "validadores": [MU_LAMBDA],
                                       "mudancas": [{"registro": "PR-0065", "op": "set", "caminho": ["tensao_interna"], "valor": []}]},
         "criterio": "D-041: a tensão interna é sinalizada, nunca escondida"},
    ],
    "ficha-de-acesso": [
        {"arq": "real-am0001", "nome": "ficha da Hemeroteca (AM-0001) do K-106: 403 e via humana",
         "espera": "passa", "caso": {"modo": "registro", "registro": "AM-0001", "caminho": ["ficha_de_acesso"], "esquema": "ficha-acesso"},
         "criterio": "ficha real do piloto (teste de 23/10/2026): bloqueio registrado e não contornado; decisão = falta com via humana"},
        {"arq": "erro-am0001-403-aceito", "nome": "ficha da Hemeroteca com o 403 e a decisão 'aceito'",
         "espera": "reprova", "caso": {"modo": "registro", "registro": "AM-0001", "caminho": ["ficha_de_acesso"], "esquema": "ficha-acesso",
                                       "mudancas": [{"op": "set", "caminho": ["decisao"], "valor": "aceito como via automática"}]},
         "criterio": "erro do brief (l. 348): 403 com decisão 'aceito'"},
    ],
    "consulta": [
        {"arq": "real-rc0010", "nome": "Recorte RC-0010 da primeira coleta real (K-108)",
         "espera": "passa", "caso": {"modo": "registro", "registro": "RC-0010", "esquema": "recorte"},
         "criterio": "Recorte real: total informado, total visto, saturação e próxima ação"},
        {"arq": "erro-rc0010-visto-maior", "nome": "Recorte RC-0010 com o total visto acima do informado, sem explicação",
         "espera": "reprova", "caso": {"modo": "registro", "registro": "RC-0010", "esquema": "recorte",
                                       "mudancas": [{"op": "set", "caminho": ["total_visto"], "valor": 999999}]},
         "criterio": "erro do brief (l. 348): total visto acima do informado, sem explicação"},
    ],
    "triagem-juridica": [
        {"arq": "real-f0033", "nome": "F-0033 (mocororó dos Tremembé, só para publicar), do K-110",
         "espera": "passa", "caso": {"modo": "registro", "registro": "F-0033", "esquema": "falta"},
         "criterio": "Falta jurídica real: norma com trecho e URL oficial, vale_para e caminho de liberação"},
        {"arq": "real-f0024", "nome": "F-0024 (dúvida de conhecimento tradicional, só para publicar), do K-109",
         "espera": "passa", "caso": {"modo": "registro", "registro": "F-0024", "esquema": "falta"},
         "criterio": "Falta jurídica real, relida no K-110 e no K-111"},
        {"arq": "erro-f0033-sem-caminho", "nome": "F-0033 sem o caminho de liberação",
         "espera": "reprova", "caso": {"modo": "registro", "registro": "F-0033", "esquema": "falta",
                                       "mudancas": [{"op": "apagar", "caminho": ["caminho_de_liberacao"]}]},
         "criterio": "caso do bloco 3: toda barreira jurídica traz porquê e caminho de liberação (D-025)"},
        {"arq": "erro-f0024-completada", "nome": "F-0024 completada por inferência",
         "espera": "reprova", "caso": {"modo": "registro", "registro": "F-0024", "esquema": "falta",
                                       "mudancas": [{"op": "set", "caminho": ["valor_inferido"], "valor": "não é conhecimento tradicional"}]},
         "criterio": "caso do bloco 3: a Falta é dita, nunca completada (D-018); o Jurídico nunca autoriza (D-020)"},
        {"arq": "real-en0009-ler", "nome": "regra fixa: ler, localizar, linkar e citar a Entrada real EN-0009 (BDTD)",
         "espera": "passa", "comando": ["scripts/triagem_fixa.py", "entrada/EN-0009.json", "--portao"],
         "criterio": "D-042: ler e citar trecho curto de informação pública não gera Falta"},
        {"arq": "erro-en0009-copiar", "nome": "regra fixa: copiar além da citação a Entrada real EN-0009 barra agora",
         "espera": "reprova", "comando": ["scripts/triagem_fixa.py", "entrada/EN-0009.json", "--ato", "copiar", "--portao"],
         "criterio": "D-042: cópia além da citação barra agora (a regra fixa do Jurídico reprova o caso de teste)"},
    ],
    "guia-de-liberacao": [
        {"arq": "real-guia-9610", "nome": "guia da licença de uso (Lei 9.610), rascunho do K-109",
         "espera": "passa", "caso": {"modo": "registro", "arquivo": "trilhas/2026-10-29_K-109/guias/G-licenca-lei-9610.json", "esquema": "guia-liberacao"},
         "criterio": "guia real do piloto: porquê, passos com nível e URL, documentos e limites"},
        {"arq": "erro-guia-9610-sem-limites", "nome": "guia da Lei 9.610 sem os limites",
         "espera": "reprova", "caso": {"modo": "registro", "arquivo": "trilhas/2026-10-29_K-109/guias/G-licenca-lei-9610.json", "esquema": "guia-liberacao",
                                       "mudancas": [{"op": "apagar", "caminho": ["limites"]}]},
         "criterio": "caso do bloco 3: o guia diz o que não faz (nunca autoriza, não protocola; D-020)"},
        {"arq": "erro-guia-9610-oficial-sem-url", "nome": "guia da Lei 9.610 com passo 'oficial' sem URL",
         "espera": "reprova", "caso": {"modo": "registro", "arquivo": "trilhas/2026-10-29_K-109/guias/G-licenca-lei-9610.json", "esquema": "guia-liberacao",
                                       "mudancas": [{"op": "apagar", "caminho": ["passos", 0, "url"]}]},
         "criterio": "caso do bloco 3: 'oficial' só com a página oficial aberta, com URL"},
    ],
}

# o erro que cada caso que reprova tem de nomear (achado A2 do auditor no K-111)
ESPERADO = {
 "erro-te0002-ocr-variante": "forma de OCR",
 "erro-te0002-ambiguo-sem-marca": "termo ambíguo",
 "erro-tr0034-palavra-de-outro-trecho": "NÃO SE SUSTENTA",
 "erro-pr0001-divergente-contada": "NÃO BATE: PR-0001",
 "erro-pr0002-marca-perdida": "Proposição sem a marca",
 "erro-tr0505-rotulo-sem-palavra": "não está no texto exato",
 "erro-cl0001-frase-sem-proposicao": "sem marcação de Proposição",
 "erro-educacao-bncc-sem-pagina": "sem a página do PDF",
 "erro-pr0016-mesma-linhagem": "NÃO BATE: PR-0016",
 "erro-pr0065-tensao-apagada": "NÃO BATE: PR-0065",
 "erro-am0001-403-aceito": "decisao",
 "erro-rc0010-visto-maior": "maior que total_informado",
 "erro-f0033-sem-caminho": "caminho_de_liberacao",
 "erro-f0024-completada": "['valor_inferido']}]}",
 "erro-en0009-copiar": "BARRA",
 "erro-guia-9610-sem-limites": "limites",
 "erro-guia-9610-oficial-sem-url": "url"
}

SEPARADAS_TR0505 = {
    "lote": "caso que reprova da rodada B (K-111, insumo 88): cópia do erro real do K-110",
    "nota": "O K-110 rotulou 'mocororó' um trecho da p. 100 do dossiê que não traz a palavra; aqui, o TR-0505 (p. 100, real) declarado como abonação da forma. A regra mencoes-0.1 reprova: a forma tem de estar no texto exato.",
    "termos_declarados": [{"forma": "mocororó", "sentido": "caso de teste", "abonado_em": ["TR-0505"], "ambiguo_com": "TE-0002"}],
}


def main() -> None:
    for hab, casos in CASOS.items():
        pasta = RAIZ / ".claude" / "skills" / hab / "exemplos"
        lista = []
        for c in casos:
            item = {"nome": c["nome"], "espera": c["espera"], "criterio": c["criterio"]}
            if c["arq"] in ESPERADO:
                item["saida_contem"] = ESPERADO[c["arq"]]
            if "caso" in c:
                arq = pasta / f"{c['arq']}.json"
                arq.write_text(json.dumps({"habilidade": hab, "nome": c["nome"], **c["caso"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                item["comando"] = [RODAR, arq.relative_to(RAIZ).as_posix()]
            else:
                item["comando"] = c["comando"]
            lista.append(item)
        (pasta / "casos-rodada-b.json").write_text(json.dumps({"habilidade": hab, "rodada": "B", "casos": lista},
                                                              ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{hab}: {len(lista)} caso(s)")
    sep = RAIZ / ".claude" / "skills" / "extrair-evidencia" / "exemplos" / "erro-tr0505-separadas.json"
    sep.write_text(json.dumps(SEPARADAS_TR0505, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
