# Relatório da rodada K-005 (23/10/2026)

**Cartão:** K-005, "Ritmo do piloto: o teto semanal da execução e a regra de folga calibrados pela medida, com estimativas por agente e habilidade". **Frente:** planejamento de melhorias. **Estado:** a 1ª passada fechou em 23/10/2026: Vicente aceitou o ritmo com outros valores (D-040) e decidiu as regras dos insumos 34 e 36 (D-041), o que dispensou a 2ª passada; o K-005 voltou a "A fazer" para a 3ª, depois do K-110. O fechamento está na seção "Fechamento", no fim; as seções até "Próximo" contam a primeira conversa, como estava antes da aceitação.
**Pedido de Vicente (fala original, para a trilha):** "Rodada de planejamento de melhorias: cartão K-005 (ritmo do piloto) de trilhas/planejamento/quadro.md, com os blocos 1 a 3 medidos. Siga trilhas/planejamento/estado-planejamento.md, sem agentes: use as medidas do checklist do piloto e os usos da conta informados. Quero o ritmo dado em pontos percentuais da conta por semana, com a meta. Opus 5.5, esforço máximo, thinking. Uso atual: 43%."
**Sessão:** `claude-opus-5-5` (conferido), esforço máximo e thinking, sem ultracode e sem agentes, como Vicente pediu. **Uso da conta:** 43% no início, lido por Vicente; no fim, a informar. **Ordem:** o quadro põe o K-002 antes do K-005, e Vicente pegou o K-005. O K-005 só pede os blocos 1 a 3 medidos (quadro; mapa, seção 8). O que é do K-002 (o teto do planejamento, a IA da operação) entra aqui como suposição dita, e não como decisão.

**Como ler.** "pp" é o ponto percentual do limite semanal da conta, na página claude.ai/settings/usage, que só Vicente lê. "Semana da conta" vai de uma renovação desse limite à seguinte. "Meta" é o que se planeja gastar por semana no desenvolvimento do piloto; "teto" é o que não se passa. "Medida" é número lido por Vicente ou informado pela ferramenta Agent; "estimativa" é conta feita sobre as medidas, sempre marcada como tal (P96). As tabelas numeradas saem de `calcular_ritmo.py`, nesta pasta, que lê `dados-ritmo.json` e os logs de `trilhas/logs/`, sem IA.

## O ritmo proposto

| | Proposta | De onde vem |
|---|---|---|
| Unidade | pp do limite semanal da conta. Os tokens de agentes seguem medidos e registrados, como estimativa e teto de cada lote, mas deixam de parar a semana | o limite que trava tudo é o da conta. Na semana medida, as conversas principais deram cerca de 24 dos 39 pp (estimativa, tabela 2), e a regra de 300 mil tokens não as via |
| Semana | a semana da conta, de uma renovação à seguinte (Vicente diz uma vez o dia e a hora que a página mostra) | o pp zera na renovação. Pela fala "tokens renovados" de 21/10, a semana em curso começou na quarta, 21/10 (não conferido na página) |
| Teto do projeto | **50 pp por semana**, somadas as três frentes | o limite que Vicente deu nesta semana, na autorização do K-105: "pare com o estado salvo antes de 50%" |
| **Meta do piloto** | **35 pp por semana no desenvolvimento**, com teto de 40 | o resto do piloto custa cerca de 106 pp (estimativa central; faixa de 48 a 183, tabela 4) |
| Planejamento | o que sobra dos 50 pp depois do desenvolvimento (15 pp, com a meta), até o K-002 fixar o teto e a cadência dele | rodadas medidas: 8 pp no K-001; 17 pp no K-003, com o fechamento |
| Linha da conta | o projeto não leva a conta acima de 90% | guarda o uso de Vicente fora do projeto e o fechamento com estado salvo |
| Folga (Parada b) | antes de cada agente, o gasto estimado da conversa + 2 × o lote + 1 pp cabe na folga da conversa (regra abaixo) | a folga de 2× da D-023 fica, mas sobre o próprio lote e em pp; o 1 pp cobre o fechamento e o arredondamento da leitura |
| Estimativa do lote | a última medida do mesmo agente com a mesma habilidade, tirada dos logs; sem medida, **96.520 tokens** (a média dos 10 lotes Sonnet dos logs), e não 60 mil | brief, l. 40; insumo 16 (o lote do K-001 veio 49% acima com os 60 mil) |
| Conversão | m = 2 pp por conversa principal; k = 1,6 pp por 100 mil tokens de agente; refeitos a cada conversa de desenvolvimento medida | ajuste de 3 conversas de desenvolvimento: m = 1,80 e k = 1,58 (estimativa, tabela 2) |
| **Previsão** | **fim do piloto (K-116) por volta de 25/11/2026**, se a conta renovar em 28/10; faixa de 14/11 a 11/12 | tabela 5: o consumo dividido pela meta, mais uma semana de espera nos 7 dias da 10a |

**A conta de cada conversa de desenvolvimento** (substitui `orcamento.py --teto 300000`):
1. Ao abrir, Vicente informa o uso da conta (A0), como já faz. Na conversa de desenvolvimento, m = 2 pp e k = 1,6 pp por 100 mil tokens, até a próxima recalibração.
2. Folga da conversa: **H = o menor entre (40 − o que o desenvolvimento já usou na semana), (50 − o que o projeto já usou na semana) e (90 − A0)**. O "já usou" vem da tabela da semana da conta no checklist, uma linha por conversa (A0, A1, pp, tokens de agentes, chamadas).
3. Antes de cada agente: **2 + k × (tokens dos agentes já rodados na conversa) + 2 × k × (estimativa do lote) + 1 ≤ H**, com os tokens em centenas de milhares. Se não couber, é a Parada (b): estado salvo, commit e push; o bloco retoma na semana seguinte (D-035).
4. Ao fechar, Vicente informa o uso (A1). Sem A1, a leitura da abertura seguinte fecha a conversa, sabendo que ela pode misturar uso de fora do projeto.
5. Vicente pode subir a linha de uma conversa, como fez nesta semana; a subida fica no checklist.

**Exemplo com uma conversa já feita (K-105, 22/10).** A0 = 37%; os 37 pp da semana contam todos como do projeto (os 4% de antes do K-001 incluídos), e o desenvolvimento tinha usado 8 (K-103 e K-101, 5; K-104, 3). H = o menor entre 32, 13 e 53 = 13 pp. Juridico, sem medida na época (96.520 tokens, 1,5 pp): 2 + 0 + 3,1 + 1 = 6,1 ≤ 13, pode. Auditor (última medida de auditor/verificar-fundacao, 143.833 tokens, 2,3 pp): 2 + 1,1 + 4,6 + 1 = 8,7 ≤ 13, pode. A conversa mediu 6 pp, e a conta fechou em 43%, abaixo dos 50%. Pela regra antiga, já o juridico teria dado PARAR (a folga de 82.703 tokens ficava abaixo de 2 × 143.833); Vicente a suspendeu nesta semana, na autorização do K-105.

## 1. O que foi medido: o uso da conta por conversa

| Intervalo | Conversas | Frente | Configuração | pp | Tokens de agentes |
|---|---|---|---|---|---|
| L1 (4%) → L2 (12%) | K-001 | P | Opus 5.5, esforço máximo, ultracode | 8 | 299.042 |
| L2 (12%) → L3 (23%) | K-003 (rodada e releitura do brief) | P | Opus 5.5, esforço máximo, ultracode | 11 | 214.004 |
| L3 (23%) → L4 (29%) | K-003 (fechamento) | P | Opus 5.5, esforço máximo | 6 | 0 |
| L4 (29%) → L5 (34%) | K-103, K-101 | D | Opus 5.5, esforço médio | 5 | 73.464 |
| L5 (34%) → L6 (37%) | K-104 | D | Opus 5.5, esforço médio | 3 | 143.833 |
| L6 (37%) → L7 (43%) | K-105 | D | Opus 5.5, esforço médio | 6 | 227.477 |
| **Planejamento** | | P | | **25** | **513.046** |
| **Desenvolvimento** | | D | | **14** | **444.774** |
| **Total** | | | | **39** | **957.820** |

- As fontes de cada leitura e de cada número de tokens estão em `dados-ritmo.json`. A leitura do início do K-101 veio em branco, e por isso o K-103 e o K-101 ficam juntos.
- Cada leitura é inteira: cada diferença tem ±1 pp. Cada intervalo inclui o que Vicente tenha usado fora do projeto, o que não está registrado; para o projeto, é um teto.
- Em cerca de um dia (de 21/10, por volta das 23h30, a 22/10, 23h49, pelos commits), o projeto usou 39 pp, 64% deles no planejamento. Nesse passo, a conta inteira duraria uns dois dias e meio.

## 2. O que se tira das medidas (estimativa)

- **Ajuste.** pp = m × conversas + k × (tokens de agentes ÷ 100 mil), por mínimos quadrados nas 3 conversas de desenvolvimento: **m = 1,80 pp por conversa principal** (Opus 5.5 médio; erro-padrão 0,79) e **k = 1,58 pp por 100 mil tokens** do retorno do Agent (Sonnet 5.5 alto; erro-padrão 0,69). Os resíduos (0,24; −1,07; 0,60) cabem no ±1 das leituras. São 3 pontos e 1 grau de liberdade: é uma estimativa fraca, que se refaz a cada conversa medida.
- **A conversa principal pesa mais que os agentes.** Pelo k, os agentes dariam 15,1 dos 39 pp da semana, e as conversas principais, 23,9. No planejamento, em esforço máximo, a conversa principal daria cerca de 17 dos 25 pp: o fechamento do K-003, sem agente, mediu 6 pp sozinho.
- **A regra antiga media o que pesa menos.** Os 300 mil tokens de agentes por semana equivalem a 4,7 pp, e a conversa principal ficava fora da soma (brief, seção 0). Por ela, só os tokens de agentes do resto do piloto (4,8 milhões, estimativa central, tabela 4) pediriam 16 semanas ou mais, e a folga de 2× o maior lote já deixava 1 a 2 agentes por semana (insumo 4).

## 3. Estimativa por agente e habilidade (logs)

| Agente | Habilidade | Modelo | Lotes | Última | Mín. | Máx. | Média | pp da última (k) |
|---|---|---|---|---|---|---|---|---|
| auditor | conferir-fato | claude-sonnet-5-5 | 1 | 31.342 | 31.342 | 31.342 | 31.342 | 0,5 |
| auditor | verificar-fundacao | claude-sonnet-5-5 | 7 | 159.897 | 46.051 | 159.897 | 102.906 | 2,5 |
| juridico | conferir-fato | claude-sonnet-5-5 | 1 | 67.580 | 67.580 | 67.580 | 67.580 | 1,1 |
| juridico | conferir-fato + triagem-juridica | claude-sonnet-5-5 | 1 | 145.933 | 145.933 | 145.933 | 145.933 | 2,3 |
| redator | escrever-secao-fundacao | claude-opus-5-5 | 9 | 50.232 | 50.232 | 140.860 | 87.145 | 0,8 |

- **Sem medida** (rastreador, avaliador, arquivista, campo-de-acao, juridico em triagem-juridica sozinha ou em guia-de-liberacao): 96.520 tokens, a média dos 10 lotes Sonnet dos logs, cerca de 1,5 pp. A referência de 60 mil vinha dos agentes de 15/10 com teto de 15 a 18 consultas (Fundação, l. 921); os lotes do projeto desde então vão de 31 a 160 mil.
- **O k é de agentes Sonnet.** O redator é Opus, as rodadas em Haiku do bloco 12 devem custar menos, e a rotina de teste da 10b gasta a cota da assinatura sem passar pelo Agent: nenhum deles tem pp medido. A primeira chamada de cada um mede, com a leitura de Vicente antes e depois, se ele puder.
- O auditor que lê a amostra (blocos 7, 8 e 10b) não tem medida própria; a previsão usa a dele em verificar-fundacao.

## 4. O resto do piloto em pp (estimativa)

As chamadas de cada bloco são as que o brief prevê (blocos 4 a 14), repartidas por agente e habilidade em `dados-ritmo.json`. Nos blocos 1 a 3, o brief previu 1, 1 a 2 e 2 a 3 chamadas, e vieram 1, 1 e 2.

| Cartão | Bloco | Chamadas (mín.–máx.) | Tokens centrais | pp baixa | pp central | pp alta |
|---|---|---|---|---|---|---|
| K-106 | 4 | 3–4 | 272.642 | 3,0 | 6,1 | 9,9 |
| K-107 | 5 | 2–2 | 256.417 | 3,3 | 6,8 | 11,0 |
| K-108 | 6 | 1–2 | 144.780 | 1,9 | 4,1 | 7,0 |
| K-109 | 7 | 8–11 | 983.066 | 8,2 | 18,2 | 31,5 |
| K-110 | 8 | 5–7 | 651.042 | 5,9 | 13,0 | 22,3 |
| K-102 | entre 8 e 9 | 0–0 | 0 | 1,0 | 1,8 | 2,6 |
| K-111 | 9 | 1–2 | 239.846 | 3,5 | 7,4 | 12,4 |
| K-112 | 10a | 3–4 | 226.354 | 3,6 | 8,1 | 14,0 |
| K-113 | 10b | 1–2 | 239.846 | 2,4 | 6,5 | 12,4 |
| K-114 | 11 | 1–2 | 144.780 | 1,9 | 4,1 | 7,0 |
| K-115 | 12 | 10–15 | 1.301.566 | 10,2 | 23,3 | 40,9 |
| K-116 | 14 | 2–4 | 315.194 | 2,9 | 6,8 | 12,1 |
| **Total** | | 37–55 | 4.775.530 | **47,7** | **106,1** | **183,2** |

Baixa: menos conversas e chamadas, com m e k um erro-padrão abaixo. Alta: mais conversas e chamadas, com m e k um erro-padrão acima. Fora da conta: a rotina de teste da 10b, a diferença de custo do redator (Opus) e a das rodadas em Haiku.

## 5. A meta e o calendário

| Meta (pp por semana) | Semanas, baixa | Semanas, central | Semanas, alta | Fim (baixa · central · alta) |
|---|---|---|---|---|
| 25 | 2,9 | 5,2 | 8,3 | 17/11 · 04/12 · 25/12 |
| **35** | 2,4 | **4,0** | 6,2 | 14/11 · **25/11** · 11/12 |
| 45 | 2,1 | 3,4 | 5,1 | 11/11 · 21/11 · 02/12 |

- As semanas contam a partir da próxima renovação: o consumo dividido pela meta, mais uma semana de espera nos 7 dias seguidos de relatório do dia da 10a (K-112), porque o desenvolvimento pega um cartão por vez (D-035). As datas supõem a renovação às quartas, com a próxima em 28/10.
- Não entram as esperas por Vicente (a aprovação do harness no bloco 9, a revisão do kit no bloco 11) nem o K-002, que tem de vir antes do K-113 (quadro).
- **Por que 35:** subir para 45 adianta o fim em cerca de 4 dias, porque a espera da 10a não encolhe; descer para 25 atrasa cerca de 9. Com 35, o planejamento fica com 15 pp por semana dentro dos 50 do projeto, e a conta fica com a metade livre para Vicente.
- **Semana a semana, pela estimativa central** (indicativo): 1ª semana, K-106 a K-109 (cerca de 35 pp); 2ª, K-110, K-102, K-111 e a montagem da 10a (cerca de 26 pp), e começam os 7 dias; 3ª, o fechamento da 10a, o K-113 e o K-114 (cerca de 15 pp); 4ª, o K-115 e o K-116 (cerca de 30 pp). No planejamento: a 2ª passada do K-005 antes do K-109 (abaixo) e o K-002 antes do K-113.
- **Nesta semana da conta** o projeto já usou 43 pp antes desta rodada. Pelo padrão, o piloto retoma na próxima renovação, salvo se Vicente liberar mais.

## O que o K-005 não calibra agora

- **Sem medida ainda:** os números que a D-038 deixou "provisórios até o K-005" (os 15 itens da amostra e os 15 cartões da fila) e os outros valores do registro que dizem "K-005" na calibração (`esquemas/valores-provisorios.json`: lote de máquina de 15, escala de valências e saída da quarentena, fila, amostra, normalização e limiar). Nenhuma amostra foi sorteada, nenhum lote de máquina rodou, nenhuma Entrada foi triada, nenhum cartão de conflito ou de Falta foi aberto, e as horas só se medem desde o bloco 6. Pela confirmação da D-038, eles valem "até o K-005 calibrá-los pela medida"; sem medida, ficam como estão, e a D-038 não muda.
- **Regras, não números: os insumos 34 e 36.** O 36 é uma falha conhecida do `localizar_trecho.py`: um trecho com um "nunca" inserido passa por semelhança (0,955 contra o limiar de 0,9; achado A-010 do auditor no K-105). O bloco 7 (K-109) usa esse script para localizar o trecho de toda Evidência. O 34 (que Evidências contam em μ e λ) entra no bloco 8 (K-110). As regras são de Vicente (D-038).
- **Padrão proposto:** o K-005 volta a "A fazer", com o estado salvo, para mais duas passadas. A 2ª, antes do K-109 e sem agentes, leva a Vicente as regras dos insumos 34 e 36, com os casos A-010 e A-015 do auditor. A 3ª, depois do K-110 e com as horas do bloco 13, calibra os números e refaz o ritmo com as medidas novas. O K-109 ganha no quadro "*Depois da 2ª passada do K-005*".

## O que muda se Vicente aceitar (fechamento, sem agentes)

1. **D-040**, pela registrar-decisao: a essência do ritmo e as palavras conferidas ("meta", "teto do projeto", "semana da conta").
2. **Brief de execuções:** a seção 0 ("Orçamento") com a conta em pp no lugar dos 300 mil tokens, e uma linha no quadro de ajustes do início. Até o K-123, o brief vale sobre o `executar-brief`, que ainda diz 300 mil, e sobre o `curador.md`, que lista as decisões até a D-039.
3. **Registro de valores provisórios:** `orcamento` (unidade, semana da conta, teto do projeto, meta e teto do desenvolvimento, linha da conta, m, k, a estimativa sem medida de 96.520) e `parada_conversa_principal` (a conta da conversa); os demais ficam.
4. **Quadro:** o K-005 volta a "A fazer", com as duas passadas; o K-109 ganha a dependência; nasce o **K-123** no desenvolvimento, antes do K-106. O K-123 leva o ritmo para a ferramenta: o `orcamento.py` em pp (a folga da conversa pela leitura de Vicente, m e k lidos do registro, a estimativa por agente e habilidade tirada dos logs), a tabela da semana da conta no checklist do piloto e o `executar-brief` e o `curador.md` em dia. Sem agentes, como o K-103, com casos que passam e que reprovam.
5. **Em dia:** `AGENTS.md` (orçamento, D-040, passo corrente), o mapa das três frentes (seções 7 e 8), `proxima-versao.md` (V-30 com a unidade em pp e a D-040) e o estado do planejamento.

## Como se fez

- **Kit de leitura:** `AGENTS.md`, `estado-planejamento.md`, o quadro; os insumos abertos do cartão (3, item 1; 4; 6; 16; 34; 36); a D-038 (`trilhas/decisoes/`) e a D-023 (`AGENTS.md`; Fundação, l. 511 e 904); a Fundação, l. 505-512 e 898-930; o brief, l. 1-60, 125-175, 259-413 e 430-470; o checklist do piloto inteiro; o registro de valores provisórios (o `orcamento` e os valores que dizem K-005); os relatórios do K-001 e do K-003 (as leituras da conta); o mapa, seções 1, 6, 7 e 8; `proxima-versao.md` (V-20, V-24, V-30); `orcamento.py`; os logs, por script; `git log`.
- **Conta sem IA:** `calcular_ritmo.py` lê `dados-ritmo.json` e `trilhas/logs/*.jsonl` e imprime as tabelas 1 a 5. Para refazer: `python trilhas/planejamento/rodadas/2026-10-23_K-005/calcular_ritmo.py`.
- **Correção de passagem:** o checklist do piloto dava 22/10/2026 como quarta-feira em quatro títulos; foi quinta (a quarta foi 21/10, o dia da renovação). Corrigido.

## Consumo

Nenhum agente, a pedido de Vicente: 0 tokens de agentes, dentro do teto da rodada. A conversa principal é a medida da conta: 43% no início; no fim, a informar.

## Insumos novos

- **37 (K-002):** o planejamento em pp. Na semana da conta de 21/10, as rodadas usaram 25 dos 39 pp medidos, e o ajuste atribui cerca de 17 deles às conversas principais em esforço máximo; o teto de 300 mil tokens de agentes por rodada não vê esse consumo.
- **38 (K-002):** a leitura da conta só existe quando Vicente a informa. O fim de cada conversa vem da abertura seguinte e pode misturar uso de fora do projeto, e a do K-101 veio em branco; se o Claude Code mostra o uso da conta à sessão não foi conferido. A medida das rotinas (10b) tem o mesmo limite.

## Alcance

- **Olhado:** o kit de leitura acima; as 7 leituras da conta (6 intervalos) e os 10 lotes de agente com tokens dos logs.
- **Fora:** os transcripts das conversas (somar o consumo da sessão pelo registro dela é "não conferido", pelo registro de valores, e Vicente pediu só o checklist e as leituras da conta); o preço de cada modelo e o peso de cada um no limite da conta, que a página não mostra; a web; os agentes; os Anexos; o roteiro; `legado/`. As previsões falam só das chamadas que o brief prevê; o que o piloto pedir além disso aparece na medida.

## Próximo

Vicente aceita o ritmo como está ou muda os números (a meta, o teto do projeto, a linha da conta, a reserva). Com a aceitação, o fechamento faz o que a seção "O que muda" lista, e o K-005 volta a "A fazer" para a 2ª passada. Pela ordem: no planejamento, o K-002 e a 2ª passada do K-005, as duas antes dos cartões que dependem delas (K-113 e K-109); no desenvolvimento, o K-123 e depois o K-106, na próxima semana da conta.

## Fechamento (23/10/2026, conversa sem agentes)

**Pedido de Vicente, em resumo fiel:** fechar o K-005 pela seção "O que muda se Vicente aceitar", sem agentes; registrar a D-040 e a D-041 pela registrar-decisao, com as essências dadas na mensagem e a fala original na trilha da rodada; depois, o K-123 no quadro, antes do K-106; o `AGENTS.md`, o mapa e o estado em dia; o uso da conta no fim; commit e push. **Uso da conta ao abrir, lido por Vicente:** 49% (semanal) e 36% (janela de 5 h). **Sessão:** `claude-opus-5-5` (conferido), esforço máximo, sem agentes.

**Falas originais de Vicente (23/10/2026)**
- Para a D-040: "Apos as medicoes eu autorizo o uso de até 60% do maximo de tokens semanais por semana para este projeto. podemos assumir que fui aumentando devagar os limites de cada ação para que elas nao parem antes do limite seja antigido. podemos aumentar os limites por sessao desde que nao tenhamos trabalho perdido tb por limites de 5h em 5h em uma sessao. nao precisa criar novo insumo para a proxima versao, basta alterar as regras atuais. ao final do desenvolvimento e inicio da execucao autonoma estes limites podem voltar a ser bem menores porque seria apenas manutencao." Confirmação da essência: "ritmo ok".
- Para a D-041: "trecho exato ok" (a regra do insumo 36) e "Aprovo" (a regra do insumo 34).

**As decisões** (`trilhas/decisoes/D-040.json` e `D-041.json`, as duas aprovadas por `validar.py decisao`):
- **D-040:** o ritmo em pontos percentuais (pp) do limite semanal da conta. O projeto usa até 60 pp por semana, somadas as três frentes; o desenvolvimento, até 50; o planejamento, o resto; a conta nunca passa de 90%. A conversa não para antes do teto: sai a folga de 2× e a margem de 1 pp da proposta. A guarda é não perder trabalho: commit e push a cada lote, e a janela de 5 h informada ao abrir; acima de 70% dela, só um lote e a conversa fecha. No fim do K-113, o teto de manutenção do K-002. Muda só o que está em vigor; nada novo em `proxima-versao.md` nem em insumos.
- **D-041:** no `localizar_trecho.py`, negação e sentido contrário batem exatamente, e a semelhança tolera só OCR e grafia. Em μ e λ só conta a Evidência com trecho localizado e leitura fiel; cada linhagem conta uma vez, e a linhagem com Evidência a favor e divergente vira tensão interna sinalizada, sem pesar dos dois lados. As regras têm versão e recalculam por script.
- **Duas leituras do curador, ditas a Vicente no fim desta conversa:** o "acima de 70%" da D-040 é o da janela de 5 h, porque a frase vem logo depois dela e a fala fala dos limites de 5 h; e o "sem pesar dos dois lados" da D-041 ficou como está escrito, porque não diz se a linhagem mista pesa num lado só ou em nenhum. O K-123 confirma esse ponto com Vicente antes de gravar o script.

**O que mudou**

| Arquivo | Mudança |
|---|---|
| `trilhas/decisoes/D-040.json`, `D-041.json` | as duas decisões |
| `esquemas/valores-provisorios.json` | versão 0.2.0: `orcamento` (orcamento-0.2: pp, semana da conta, 60 e 50 pp, linha de 90%, janela de 5 h a 70%, 2 pp e 1,6 pp por 100 mil tokens, estimativa sem medida de 96.520, teto de manutenção no K-002) e `parada_conversa_principal`. A chave `teto_semanal` (300 mil) fica, marcada como fora de uso, porque o `orcamento.py` a lê até o K-123 |
| brief de execuções | o cabeçalho; no quadro de ajustes, a linha das decisões (até a D-041), a do orçamento (D-040, que supera a leitura A-13) e uma linha nova para o trecho e μ e λ (D-041); a seção 0 ("Orçamento") reescrita; a seção 2 com as D-040 e D-041 e a nota na D-023; a camada 2 da seção 3b e a operação depois do bloco 14; a trilha |
| quadro | o K-005 em "A fazer", depois do K-006, só para a 3ª passada; o K-002 com o teto do planejamento dentro dos 60 pp, o teto de manutenção (D-040) e os insumos 37 e 38; o K-123 novo, antes do K-106 |
| mapa das três frentes | seção 1 (teto de cada frente; cartões até o K-123); seção 6 (insumos 34 e 36: regra pela D-041, script no K-123); seção 7 (D-040 e D-041; a D-023 com o número substituído); seção 8 (as ordens, com o K-123 e as passadas do K-005) |
| `AGENTS.md` | D-040 e D-041; a nota na D-023; o passo corrente; o orçamento |
| estado do planejamento | o K-005, as decisões até a D-041, o consumo e a próxima rodada |
| `dados-ritmo.json` | a leitura L8 (49%, ao abrir o fechamento) e a meta de 50 pp na tabela 5 |

**O que ficou de fora, de propósito**
- **`proxima-versao.md` e insumos:** nada novo, pela D-040.
- **A D-041 no registro e nos scripts:** o `localizar_trecho.py` e o `calcular_mu_lambda.py` gravam em cada saída a versão da regra que leem do registro (`versao_regra`). Subir a versão no registro sem mudar o código daria saída com uma regra que o script não aplica. Os dois mudam juntos no K-123, antes do K-106, e por isso os blocos 7 e 8 já rodam com elas.
- **O `orcamento.py`, o `executar-brief`, o `curador.md` e o checklist do piloto:** vão ao K-123. Até lá, a conta se faz pela seção 0 do brief, que vale sobre o `executar-brief` (ainda com 300 mil).
- **A dependência do K-109 na 2ª passada:** não entrou, porque a D-041 dispensou essa passada e o K-123 vem antes do K-106.

**Previsão com a D-040** (estimativa, tabela 5 refeita): com o desenvolvimento a 50 pp por semana, o piloto termina por volta de 19/11/2026, se a conta renovar em 28/10; a faixa vai de 11/11 a 30/11. Os 7 dias da 10a e as esperas por Vicente seguem fora da conta de pp. Nesta semana da conta, o projeto estava em 49 pp ao abrir o fechamento, com todo o uso contado como do projeto; pela D-040, ele pode chegar a 60.

**Checagens, sem IA:** `validar.py decisao` nas duas decisões e `validar.py valores-provisorios` no registro: PASSA; `checar_mapa.py` do K-001: sem problemas (36 cartões, 38 V, 13 atritos); `orcamento.py` segue rodando com o registro novo; `rodar_testes.py` e `procurar_dado_pessoal.py --git` antes do commit (resultado no log).

**Consumo:** nenhum agente (0 tokens de agentes). A primeira conversa do K-005 mediu 6 pp (de 43% a 49%, pela leitura da abertura desta), como o fechamento do K-003; esta conversa abriu em 49% (semanal) e 36% (janela de 5 h), e o fim fica a informar.

**Alcance do fechamento**
- **Olhado:** a mensagem de Vicente; o relatório e os dados desta rodada; a habilidade registrar-decisao e o esquema de decisão; a D-039 (forma); o registro de valores provisórios e o esquema dele; os usos do registro no `orcamento.py`, no `localizar_trecho.py` e no `calcular_mu_lambda.py` (por `grep`); os casos do `executar-brief`; no brief, o cabeçalho, o quadro de ajustes, a seção 0, a seção 2, a 3b, a operação e a trilha; o quadro; o mapa (seções 1, 6, 7 e 8); o `AGENTS.md`.
- **Fora:** a web; os agentes; a Fundação, que não muda na execução (D-035); o corpo dos scripts, que o K-123 muda; a conversa em que Vicente confirmou as essências, que não está nesta sessão (vale a mensagem dele, com as falas originais).

**Próximo:** no desenvolvimento, o K-123 (as D-040 e D-041 na ferramenta) e depois o K-106 (bloco 4), quando Vicente autorizar; no planejamento, o K-002 (antes do K-113) e o K-006; o K-005 volta para a 3ª passada depois do K-110. O uso da conta que Vicente der ao abrir a próxima conversa fecha a conta desta.
