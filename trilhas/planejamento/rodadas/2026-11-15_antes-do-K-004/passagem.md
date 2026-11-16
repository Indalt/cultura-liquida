# Passagem para a próxima sessão (15/11/2026)

Escrita para uma sessão nova, em Opus 5.5, que não viu a conversa de 14 e 15/11. A conversa foi de planejamento, começou em Opus 5.5 (esforço máximo) e terminou em Fable 5.2, por troca de modelo feita por Vicente; esse modelo não estará mais disponível. **Nada aqui é decisão.** Decisão é só o que está em `trilhas/decisoes/` (a última é a D-056). O que está aqui são medidas, leituras e perguntas em aberto, para não se refazer o caminho.

## 1. O que ficou gravado
- **Insumo 140** (o alcance da Consulta geral). Ler junto a linha de correção no log `trilhas/logs/2026-11-14_curador.jsonl`: as contagens do insumo são de todas as 2.578 Entradas; só na Consulta geral (CO-0008, 567 Entradas) ficam cerveja 56, suco 46, refrigerante 22, bebida láctea 19, cachaça 18, vinho 15, água de coco 13, caldo de cana 11, néctar 10, hidromel 8.
- **Insumo 141** (o custo de escala por bebida e a dependência de IA, não medidos por parte).
- **Falas de Vicente e essências pendentes:** `trilhas/2026-11-14_piloto-outras-bebidas/falas-vicente.md`; a lista das 199 Entradas em `escopo-proposto.json`, na mesma pasta.
- **Nada mudou na ferramenta:** nenhum script, esquema, rotina ou registro do acervo.

## 2. O que espera Vicente, na ordem em que ele pôs
1. **Entender o gasto e a dependência de IA (fala 4).** Ele estranhou o custo previsto e disse que deseja uma ferramenta quase independente de IA, sem saber se isso foi dito expressamente. Devolvido a ele: "IA só onde é preciso ler texto; todo o resto por regra e script". Pergunta em aberto: a leitura também deve dispensar IA? **Não registrar como decisão sem a resposta dele** (habilidade `registrar-decisao`).
2. **A D-057 (piloto com outras bebidas) está pendente e em dúvida.** A essência v2 está no arquivo de falas. Depois dela veio a fala 4, que questiona o custo: a confirmação anterior não vale mais sozinha. Também ficou sem resposta o sentido de "o que falta vem na próxima semana".
3. **O K-004 espera.** Vicente disse que antes quer ver o piloto funcionando em outras bebidas. A divisão do K-004 em etapas está na seção 5.
4. **A rotina do Claude não foi tocada.** Segue configurada para a segunda leitura (D-055), sem ninguém propondo (D-056). Para as 199, Vicente disse "sem rotina".

## 3. O que a ferramenta achou até 14/11 (medido)
- **Do bruto à ficha:** só a cajuína (CL-0001): 520 Evidências, 427 Proposições, 34 Fontes, ficha, Educação, grafo (72 nós, 24 arestas). Restam brutos 20 documentos do BCR sobre ela (EN-1729 a EN-1748).
- **Candidatas:** vinho de caju (CL-0002), mocororó (CL-0003), caoi (CL-0004); só Termo candidato; 7 Entradas brutas citam as duas primeiras.
- **Bruto:** 2.544 Entradas sem leitura; 1.977 das Consultas de caju e cajuína e 567 da Consulta geral (CO-0008: "bebida" com os descritores do processo da cajuína). Nomes de bebidas nativas testados como exemplo (cauim, caxiri, aluá, chicha, tarubá, jurema) não aparecem em nenhuma Entrada; tiquira, uma vez.
- **Fila da rotina com IA** (`scripts/fila_ia.py --resumo`): faixa 1, 49; faixa 2, 56; faixa 3, 1.405; faixa 4, 521; faixa 5, 513. A rotina só faz extrair-evidencia; Termo, ficha e grafo de CLB nova ficam fora dela (`ambientes/rotinas-ia/rotina-semanal.md`).
- **Como se contou:** script avulso, não gravado; título e `citacao_resumo` de `entrada/EN-*.json`, sem acento, palavra inteira, plural com "s"; a Consulta pelo motivo da pré-triagem.

## 4. Onde está o custo (medido em `trilhas/2026-11-14_relatorio-piloto/dados.json`)
- **Sem IA:** coleta diária, deduplicação, pré-triagem, localização do trecho, validador, μ e λ, fila, portão, relatório do dia, wiki.
- **Com IA:** ler a fonte e extrair Evidências e Proposições (avaliador); Termo, ficha e pontos do grafo (arquivista); Educação (redator).
- **Cajuína:** avaliador 1.212.590 tokens para 520 Evidências (perto de 2.300 por Evidência); registrar-termo 149.782 (3 execuções), montar-ficha 111.618, gerar-grafo 104.796. Conteúdo: 1,6 milhão, 23% dos 6.912.130 do piloto. Auditor e escrita da Fundação: 51%. Juridico: 18%.
- **Previsão para as 199 Entradas e umas dez bebidas, sem verificação:** extração em 14 lotes de 15, 180 a 260 mil tokens por lote em Haiku (insumo 132), 2,5 a 3,6 milhões; por bebida, perto de 270 mil mais a Educação, 2,5 a 3,6 milhões; total de 5 a 7 milhões, 80 a 110 pp pela taxa do `orcamento.py` (medida com Sonnet e Opus; Haiku sem medida). É teto: usa os custos da cajuína.
- **Não medido:** quanto de um lote é leitura da fonte e quanto é peso do agente (instruções, exemplos, 26 a 35 chamadas). **Não testado:** montar a ficha e os pontos do grafo por script, a partir das Proposições. Sem isso não se sabe quanto do custo é da tarefa e quanto é do jeito de construir.
- **Sem IA, já possível para as 199:** a lista por bebida com título, ano, fonte, link e trecho do resumo.

## 5. O K-004 em sete etapas (proposta de Vicente; conferida, não decidida)
A divisão cabe sem decisão nova, se forem etapas do mesmo cartão (quadro, l. 18), com o estado em `rodadas/AAAA-MM-DD_K-004/`. Vicente escreveu quatro; as três últimas foram lidas do destino do cartão e ele não as confirmou.
1. **Juntar o material.** Dos 139 insumos de então, 57 fechados (52 pelo cartão concluído, 5 por decisão) e 82 abertos: 38 apontam para cartão aberto ou item V, 44 estão "a definir pelo planejamento" (só esses pedem leitura). A conferir, porque o cartão só os levou ao relatório ou respondeu em parte: 81, 95, 110, 117, 120 e 114. A coluna "Vira" está no mapa das três frentes, seção 6. Hoje há 141 insumos.
2. **Estacionados (K-125, K-115b, K-115c).** As habilidades do K-115c somaram 49% dos tokens de agentes do piloto (3.408.189) e são as da etapa 6 (escrever e verificar a Fundação); as do K-115b, 11%. O K-125 só volta com cota paga e decisão nova (D-056).
3. **3ª passada do K-005.** O `dados.json` tem o consumo por agente e habilidade, os pp por semana e frente e o acervo por estado; não tem o resultado das amostras, a fila por semana nem as notas de valência. Usar o piso e dizer (insumos 136 e 139). O registro manda calibrar a fila "com as horas medidas no bloco 13", que não existem (insumo 138).
4. **K-006.** Três habilidades dele correspondem às etapas 1 (consolidar-para-planejamento), 3 (medir-custo) e 5 (preparar-tarefa).
5. **Cartões novos e destino de cada insumo aberto, de uma vez** (D-046).
6. **Escrever a Fundação** (V-01 a V-38 e o que vier). A v0.2 custou 1.227.342 tokens de agentes (insumo 6); com o teto de 300 mil por rodada, uns quatro lotes.
7. **Conferir e fechar** (aprovação de Vicente; V-35, V-03, V-34).
Medida das rodadas de planejamento: 8 a 17 pp por cartão; 2 a 6 pp por conversa sem agentes.

## 6. Por onde a próxima sessão começa
1. Ler `AGENTS.md`, `RETOMAR.md` e este arquivo. Conferir o modelo (Opus 5.5).
2. Perguntar a Vicente só o item 1 da seção 2 e, com a resposta, o item 2. Uma pergunta por vez, para compreender.
3. Só então: registrar decisão, se houver; ou medir o que a seção 4 diz que não foi medido, se ele pedir. Nenhum agente antes de dizer quantos são e quanto gastam.
