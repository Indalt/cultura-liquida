# Piloto com outras bebidas: falas de Vicente e essência à espera de confirmação (14/11/2026)

Conversa de planejamento depois da entrega do piloto (D-056), Opus 5.5, esforço máximo. As falas ficam aqui só por rastreabilidade: o texto de trabalho usa a essência confirmada (habilidade `registrar-decisao`), nunca a transcrição.

## Falas
1. "antes preciso ver o piloto funcionando para as clbs que se pode ter com o que foi construido como teste piloto. o que conseguimos encontrar?"
2. Depois do levantamento (o que a ferramenta achou; insumo 140): "adicione estas entradas liberando o filtro e sinalizando que elas fazem parte do piloto. nao precisa coletar dados sobre elas ou fazer verificacao juridica. precisamos olhar o que conseguimos fazer com com o cultura liquida"

## Essência devolvida (pendente; vira a D-057 só depois da confirmação)
Para ver o que a ferramenta consegue fazer além da cajuína, as Entradas de outras bebidas que as rotinas já coletaram entram no piloto, cada uma com a marca de que entrou por esta decisão. Elas passam à frente na fila da rotina com IA e seguem a ferramenta como a cajuína seguiu (Evidências e Proposições; depois Termo, CLB, ficha e grafo de cada bebida), em vez de parar em candidata (D-039). Nada novo se coleta sobre elas, e o juridico não faz a triagem delas. Segue o resto da ferramenta: trecho localizado, validador, portão, segunda leitura do auditor, o filtro de pessoa citada e a busca de dado pessoal antes do commit; e a Falta F-0024, já aberta para as outras bebidas de caju. Para elas serem lidas, a rotina do Claude volta a propor e reler (o primeiro ato da D-056).

Muda, só para estas Entradas: a D-039 (no piloto, só a cajuína ia até a ficha), a ordem da fila (`fila-ia-0.1`) e a triagem jurídica da lista de rigor da D-056.

## Palavras a conferir
- **"estas entradas":** as 199 da Consulta geral (CO-0008) com um dos 10 nomes listados na conversa (cerveja, suco, refrigerante, bebida láctea, cachaça, vinho, água de coco, caldo de cana, néctar, hidromel) e as 7 das CLB candidatas (vinho de caju, mocororó); não as 567 da Consulta geral inteiras, nem bebidas que as rotinas não trouxeram. Lista em `escopo-proposto.json`.
- **"o filtro":** a ordem da fila (que lê primeiro a cajuína) e o limite da D-039; não o filtro de pessoa citada nem o portão.
- **"fazem parte do piloto":** uma marca em cada Entrada (a decisão e a data), para os relatórios separarem o que veio daqui.
- **"verificação jurídica":** a triagem do juridico (triagem-juridica, Faltas novas, guias); não os scripts da ferramenta.
- **"coletar dados":** nenhuma Consulta ou Recorte novo para essas bebidas; a rotina diária segue como está.

## Resposta de Vicente à essência devolvida
3. "199. sem rotina. apenas com flag de piloto para que saim antes da nova versao. porem, com tudo o que conseguimos oferecer enquanto cultura liquida. nao vai passar por verificacoes, testes etc. o que falta vem na proxima semana"

## Essência v2 (pendente; vira a D-057 com a confirmação)
Antes da nova versão da Fundação (K-004), as 199 Entradas da Consulta geral que nomeiam uma das dez bebidas entram no piloto, com a marca de piloto, e saem com tudo o que a ferramenta oferece: Evidências e Proposições, Termo e CLB de cada bebida (pelas regras de termo da D-039), ficha, camada Educação, grafo 4D e página no wiki local. O trabalho se faz em conversas de trabalho, não pela rotina. Elas não passam por verificação nem por teste (sem triagem do juridico, sem segunda leitura do auditor, sem amostra, sem teste de modelo); por isso saem como proposta marcada de piloto, e não como conhecimento aprovado da base (quem propõe não aprova, D-038). O que falta vem na semana seguinte.

Leituras a conferir: (a) ficam, porque fazem a Evidência existir ou são regra do Git público: o trecho localizado por script, μ e λ por script, o validador do pre-commit e a busca de dado pessoal antes de cada commit; (b) "o que falta vem na próxima semana" foi lido como: o processamento, que não cabe nesta semana da conta, começa depois de 18/11, 23h; (c) o trabalho entra no quadro como cartão próprio (seria o K-126), exceção à D-046 por esta decisão. Muda, só para as 199: a D-039, a segunda leitura e a leitura pelo auditor de tudo o que sustenta aviso, saúde ou política (D-038), a triagem jurídica e a segunda leitura da lista de rigor da D-056.

Custo previsto: extração em 14 lotes de 15, de 180 a 260 mil tokens por lote no avaliador em Haiku (insumo 132), de 2,5 a 3,6 milhões; por CLB, os números da cajuína (registrar-termo perto de 50 mil, montar-ficha 112 mil, gerar-grafo 105 mil, mais a Educação), de 2,5 a 3,6 milhões para umas dez CLB. Total de 5 a 7 milhões de tokens: de 80 a 110 pp pela taxa do `orcamento.py` (medida com Sonnet e Opus; o Haiku deve pesar menos, sem medida).

## Falas de 15/11 (depois da essência v2; a sessão já em Fable 5.2)
4. "Eu nao entendi o porque de ter todo esse gasto para: 'Evidências e Proposições; o Termo e a CLB de cada bebida, pelas regras de termo da D-039; a ficha, a camada Educação, o grafo 4D e a página no wiki local.' Gastamos bastante para ter uma ferramenta automatizavel, eficiente. com rigor, mas nao me parece que estamos criando uma ferramenta quase independente de IA que é algo desejavel, mas que nao sei se foi dito expressamente. Parece que apos todos os criterios desenhados e criados e executados ainda gastar essa quantidade de tokens para definir se uma atividade da cultura alimentar com bebidas/liquidos produzidos sao uma clb? quero entender mais que criticar. nao me parece muito complicado e caro fazer o que nos propomos no sentido de tanto gasto de token. me explica o porque. criamos diversos scripts, esquemas, regras e cuidados para que as logicas funcionem e eu nao estava ciente de que ainda falta tanto depois do piloto. O imaginei mais afil também."
5. "temos apenas 5% de tokens semanais usando o fable para este projeto e nao teremos mais acesso ao modelo. como organizar o que fizemos sem perder o que ganhamos usando o modelo para que as proximas sessoes possam ser aplicadas em modelos como o opus 5.5"

Devolvido a Vicente sobre a fala 4, sem confirmação ainda: "IA só onde é preciso ler texto; todo o resto por regra e script"; pergunta em aberto: a leitura também deve dispensar IA? Com a fala 4, a essência v2 acima deixa de estar confirmada por si. O que se respondeu e o que fica para a próxima sessão estão em `trilhas/planejamento/rodadas/2026-11-15_antes-do-K-004/passagem.md`.

## Falas de 19/11 (sessão nova, Opus 5.5, seção 6 da passagem)
Na sessão, a explicação do gasto foi devolvida com os números de `dados.json` (conteúdo 23% dos 6.912.130 tokens; Fundação e fatos 51%; juridico 18%; o que não foi medido) e a pergunta aberta foi como Vicente vê a leitura da fonte numa ferramenta quase independente de IA.
6. "no momento eu prefiro continuar para finalizar o piloto para falar dos aprimoramentos depois. este ja esta anotado?"

Resposta: a questão está no insumo 141 (custo por bebida e por parte, IA só onde regra e script não alcançam; essência da fala 4 não confirmada). A pergunta sobre a leitura sem IA fica para a conversa dos aprimoramentos (K-004), sem resposta e sem decisão. A essência v3 da D-057, abaixo, foi devolvida a Vicente.

## Essência v3 (pendente; vira a D-057 com a confirmação)
A essência v2, com a fala 6: o piloto termina com a ferramenta como ela está hoje, agentes com IA incluídos; o enxugamento (menos IA, custo medido por parte) é aprimoramento para depois do piloto, no K-004 (insumo 141). [ABERTO]: o que é "o que falta" em "o que falta vem na próxima semana" (fala 3); a leitura (b) da v2, só de data, perdeu o sentido depois de 18/11.

## Fala de 20/11 (mesma sessão, Opus 5.5)
Devolvida a essência v3 com os dez nomes por extenso e o custo, Vicente respondeu:
7. "Sucos, refrescos, bebidas lacteas e hidromel podem ser consideradas bebidas brasileiras se são parte da cultura. Falamos de culturas líquidas. de onde veio cerveja, refrigerantes etc.? eu nao lembro de ter incluido isso."

**Conferido na trilha:** os dez nomes não vieram de Vicente; nenhuma das falas 1 a 6 nomeia bebida. Vieram (1) da Consulta geral CO-0008 (`scripts/gerar_termo.py --gerais`, 05/11, regra consultas-gerais-0.1: "bebida" e um descritor do processo da cajuína: extração do suco, clarificação, filtração, envase, tratamento térmico, higienização), que trouxe sobretudo tecnologia de alimentos; e (2) da conversa de 14/11, que escolheu os nomes a contar no levantamento e leu "estas entradas" (fala 2) e "199" (fala 3) como as Entradas com os dez nomes mais frequentes. Os nomes estavam nas palavras a conferir, mas não foram discutidos como critério: uma contagem de frequência virou escopo, sem regra. Nada foi aplicado: nenhuma marca, nenhuma leitura.

**Medido em 20/11** (script avulso, não gravado; título e `citacao_resumo` de `entrada/EN-*.json`, sem acento, palavra inteira): as 199 tratam quase todas de processo industrial (higienização e clarificação na cervejaria, linha de envase de refrigerante, bebida láctea UHT, filtração de cachaça). Das 567 Entradas da CO-0008, 31 têm ao menos uma de 28 palavras ligadas a cultura (tradicional, artesanal, cultura, comunidade, indígena, quilombola, patrimônio, memória, história, festa, ritual, saber, regional, etnobotânica, etnografia e variações); a maioria por "artesanal", quase toda cerveja artesanal como produto, e várias por acaso ("cultura microbiana"); "refresco" não aparece. Entre as 7 Entradas das CLB candidatas, que ficaram fora com o "199", estão os únicos estudos sobre cultura deste material: EN-1066 e EN-50910 (mocororó e o povo Kanindé de Aratuba) e EN-1069 (o Torém, dos Tremembé). Alcance: só título e trecho do resumo; o resumo inteiro e o bruto fora do Git não foram lidos.

**Leitura, sem decisão:** o critério da fala 7, "se são parte da cultura", já é a regra da ferramenta (D-022: os quatro critérios de prática cultural na CLB, cada um com Evidência ou Falta; a Falta nunca recusa; nenhuma bebida entra ou sai pelo nome); não se registra de novo. O escopo por dez nomes sai da essência v3; o escopo da D-057 fica [ABERTO], perguntado a Vicente. Segue [ABERTO] "o que falta vem na próxima semana".

## Fala de 20/11, seguinte
Perguntado o que quer ver passar pela ferramenta para dar o piloto por terminado, Vicente respondeu:
8. "nao entendi o porque de ter saido 7 entradas das 3 bebidas que achou pela regra. é cultura liquida. caoi é um nome nunca lido por mim e esse precisaria de desambiguacao para entender se é erro de digitacao ou compreensao. As os terminaram?"

**Conferido na trilha:** as 7 Entradas das CLB candidatas estavam na essência devolvida em 14/11 ("e as 7 das CLB candidatas"); a conversa leu o "199" da fala 3 como "só as 199" e as tirou, sem perguntar (`escopo-proposto.json`, campo `candidatas_fora`). Foi leitura da conversa, não regra nem fala de Vicente. Nada se perdeu: as 7 seguem brutas no acervo, e as três CLB seguem candidatas.

**Caoi:** a forma está na fonte, não é erro da ferramenta. Embrapa 2009 (FO-0006, Infoteca-e, handle doc/697354), p. 1, trecho TR-0018 localizado por script com semelhança 1,0: "como bebida fermentada (o caoi ou caoim), a qual era utilizada em comemorações e em ocasiões especiais". A fonte dá duas formas. No acervo, só o dossiê do Iphan (FO-0034) fala de cauim, no contexto de dois trechos (a etimologia de cajuína, com "cauinagem", e "as beberagens do cauim"), sem ligar a caoi. O TE-0005 segue candidato; atestar e ver as variantes é da regra de termos (registrar-termo, do arquivista), que não completa por inferência: com uma fonte só e sem coleta nova, a dúvida tende a ficar como Falta dita.

## Essência v4 (pendente; vira a D-057 com a confirmação)
Antes da nova versão da Fundação, o piloto termina com as CLB que a ferramenta achou pela regra além da cajuína: vinho de caju (CL-0002), mocororó (CL-0003) e caoi (CL-0004), com as 7 Entradas que as citam e o que o acervo já tem delas. Passam por tudo o que a ferramenta oferece hoje, agentes com IA incluídos: Evidências e Proposições, Termo (o caoi pela regra de termos), CLB, ficha com os quatro critérios de prática cultural, Educação, grafo 4D e página no wiki local. Em conversas de trabalho, sem rotina, com a marca de piloto, sem verificação nem teste; saem como proposta, não como conhecimento aprovado. Ficam o trecho localizado, μ e λ, o validador, a busca de dado pessoal e o detalhe de conhecimento tradicional na pasta local, fora do Git (D-043, como já está o do mocororó). Custo, teto pelos números da cajuína: um lote de extração (180 a 260 mil tokens) e perto de 270 mil por CLB mais a Educação; de 1 a 1,4 milhão de tokens, de 16 a 22 pp. [ABERTO]: o que mais entra (a busca geral, pelo critério de ser parte da cultura, fala 7); "o que falta vem na próxima semana".

## Estado
Nada mudou na ferramenta. Custo previsto: 14 lotes de 15 Entradas; um lote da rotina com IA custou de 270 a 350 mil tokens em 13/11 (insumo 132). Nada roda antes de 18/11, 23h: a semana da conta está em 88% (estimada), e o limite é 90%.
