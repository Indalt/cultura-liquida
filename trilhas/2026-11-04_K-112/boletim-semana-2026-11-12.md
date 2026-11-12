# Boletim da semana: rotina diária sem IA, 05 a 12/11/2026

Primeiro boletim, escrito uma vez para testar o papel do redator (cartão K-112, bloco 10a do brief de execuções). Não é publicação: fica no repositório (D-032). Fala só do que a rotina viu nesses dias (D-030); o que ela não olhou está no fim.

**Como ler.** A *rotina* é um programa que roda sozinho na nuvem (GitHub Actions), sem IA, uma vez por dia. Cada fonte de busca é um *ambiente* (AM-nnnn); cada pergunta feita a ela é uma *Consulta* (CO-nnnn). Um item achado que passa na *pré-triagem* (uma regra fixa, sem IA, que procura a palavra da Consulta no título ou no resumo) vira uma *Entrada* (EN-nnnn); o que não passa fica só como *pegada*, um registro curto de que foi visto (D-045). Antes de gravar, um *portão* (a bateria de testes) tem de passar; se reprova, nada se grava.

## 1. O que entrou

**1.398 Entradas novas** na semana (o acervo tinha 1.006 antes do dia 05 e 2.404 no fim do dia 12). Dias com rodada gravada: 05, 06, 07, 08 e 12/11. Nos dias 09, 10 e 11 nada se gravou (ver seção 3).

| Fonte | 05/11 | 06/11 | 07/11 | 08/11 | 12/11 | Semana |
|---|---|---|---|---|---|---|
| BDTD (AM-0021) | 1 | 15 | 0 | — | 0 | 16 |
| Infoteca-e (AM-0029) | 4 | — | — | — | 1 | 5 |
| Oasisbr (AM-0022) | — | — | — | 1.008 | 349 | 1.357 |
| BCR (AM-0061) | — | — | — | 20 | — | 20 |
| **Total do dia** | 5 | 15 | 0 | 1.028 | 350 | **1.398** |

"—" = a fonte não rodou nesse dia (cada fonte tem o seu intervalo). Fonte de cada coluna: `trilhas/relatorios/2026-11-05.md`, `2026-11-06.md`, `2026-11-07.md`, `2026-11-08.md` e `2026-11-12.md`, bloco "Entradas".

**Por Consulta** (bloco "Rotina do dia" dos mesmos relatórios). Uma Entrada pode vir de mais de uma Consulta, por isso a soma passa do total.

| Consulta | 05/11 | 06/11 | 07/11 | 08/11 | 12/11 |
|---|---|---|---|---|---|
| CO-0001 | 1 | 14 | 0 | 678 | 55 |
| CO-0002 | 0 | 15 | 0 | 648 | 34 |
| CO-0003 | 0 | 1 | 0 | 76 | 0 |
| CO-0004 | 0 | 1 | 0 | 84 | 0 |
| CO-0005 | 0 | 0 | 0 | 4 | 0 |
| CO-0008 (geral) | 4 | 0 | 0 | 269 | 295 |

**Pegadas:** de 9.845 para 20.706 (em 48 Recortes); 5.884 delas ficaram fora pela regra da pré-triagem (eram 3.222 no dia 05). O tamanho em disco ficou em 5.569 arquivos e 19,1 MB, abaixo do alarme (20 mil arquivos ou 200 MB). Fonte: bloco "Guarda das Entradas" de `2026-11-05.md` e `2026-11-12.md`.

**Uma diferença que fica dita.** Em 08/11 o bloco "Entradas" dá 1.008 do Oasisbr e 20 do BCR, mas a linha da rodada dá 1.004 e 0. Houve várias execuções nesse dia (seção 3); a diferença não foi medida.

## 2. O que é novo de fato

A Consulta geral **CO-0008** não pergunta por caju nem por cajuína: usa só descritores de processo (como "bebida"). Ela abre a porta para outras bebidas brasileiras.

- **Quantas:** 565 Entradas, pela conta do curador. Nesta leitura do boletim (arquivos `entrada/EN-*.json` cujo motivo de pré-triagem cita CO-0008), 567: 563 do Oasisbr e 4 da Infoteca-e; a soma das linhas diárias dá 568. A diferença de 2 a 3 não foi explicada.
- **Sem caju:** 563 dessas 567 não têm "caju" no título nem no trecho do resumo.
- **Por que entraram:** descritor no resumo, 250; forma no resumo, 155; descritor no título, 106; forma no título, 56. A forma que mais aparece é "bebida" (211).
- **O que aparece nos títulos** (contagem crua de palavras, sem leitura): cerveja 53, suco 25, "fermentad-" 22, cachaça 18, refrigerante 18, vinho 9, hidromel 6, néctar 5, umbu 5, "destilad-" 5, licor 4, aguardente 3, açaí 2, kefir 2. Exemplos de Entradas: um fermentado de jabuticaba (EN-51263), extratos de baru e pequi (EN-51304), água de coco (EN-51202), espumantes (EN-50000).
- **Ruído:** a regra também deixa passar o que não é bebida. Numa amostra de 15 títulos, cerca de metade não trata de bebida: concreto, aço, tratamento de água, saúde de animais (por exemplo, EN-50885, EN-51191, EN-50868). Para a pré-triagem sem IA isso já era esperado; a triagem é que decide, e a regra não foi mudada aqui.

Nenhuma dessas Entradas foi lida nem extraída: todas estão no estado "bruto". Não são CLB candidatas, são só itens a triar.

## 3. Os dias de erro e o que ensinaram

Fonte: `trilhas/2026-11-04_K-112/dias-da-rotina.md` (as execuções do GitHub Actions, lidas em 12/11).

| Dia | O que falhou | Conserto |
|---|---|---|
| 05/11 | O registro dizia "passa" quando o portão tinha reprovado: o resultado dos testes se perdia no caminho até o registro. | Corrigido (commit bffd3b4). |
| 05/11 | Um teste não conhecia a faixa de números que a rotina usa para as Entradas. | Corrigido (467d9b5). |
| 05/11 | O portão passou, mas a regra do repositório exigia aprovação para juntar. | Vicente mudou a proteção do `main`; a junção seguinte deu certo (1c9df40). |
| 05/11 | Falha provocada de propósito. | O aviso por e-mail chegou a Vicente, como pedia o cartão. |
| 08/11 | O Oasisbr reúne itens de outros repositórios; o teste das pegadas não aceitava o item ligado pelo link. | Corrigido (93540aa). |
| 08/11 | O número de um item do Oasisbr tinha um espaço. | Corrigido (1fcb938). |
| 09 a 11/11 | (1) O mesmo item do Oasisbr chegou por dois caminhos em dias diferentes, e a rotina parou dizendo que a Entrada "já era de outro item"; (2) com a rodada interrompida, um teste que lê um Recorte real (RC-0010) reprovou o portão. Nada se gravou nos três dias. | (1) Corrigido em 12/11 (6dd5d99): a rodada achou 349 Entradas novas. |
| 12/11 | Persistia a causa (2): a rotina grava uma explicação no RC-0010 real, e o teste não esperava. | O teste passou a ignorar esse campo (ff8fd66); a execução seguinte gravou com o portão passando (commit 063d2a1). |

**O que se aprende:**
- Um teste que lê registros reais quebra quando a rotina muda esses registros; ele deve conferir só o que importa.
- Um agregador como o Oasisbr traz o mesmo item por chaves e links diferentes; a ferramenta tem de reconhecer que é o mesmo, mesmo quando chega em dias diferentes.
- A falha funcionou como planejado: rodada com erro não grava nada e avisa por e-mail. O custo foi perder três dias de coleta, recuperados na rodada de 12/11, que repetiu o Oasisbr.

## 4. O que ficou de fora e por quê

- **OpenAlex:** fora da rotina. Sem chave (o projeto não abre cadastro, D-049) e com respostas de recusa e de indisponibilidade (códigos 429 e 503).
- **Internet Archive:** fechado pela Falta F-0034, que espera Vicente no cartão K-208.
- **Hemeroteca Digital:** segue na via humana; não passou no teste de acesso automático (D-044).
- **Recortes interrompidos pelo teto:** 6 em 12/11 (eram 0 no dia 05 e 2 no dia 06). A busca parou no limite do dia; o que faltou não foi visto.
- **Faltas:** de 31 para 40 na semana. O tipo de cada Falta nova não foi medido aqui.
- **Links quebrados:** 22 no total em 12/11 (1 em 05/11). Não foi medido quais são.

## 5. O que não se olhou

- Nenhuma Entrada da semana foi lida, extraída ou triada: o boletim conta itens, não diz o que eles afirmam.
- A divisão entre bebida e ruído vem de uma amostra de 15 títulos e de uma contagem crua de palavras, não de leitura.
- Não se mediu quantas das 1.398 Entradas repetem itens que já estavam no acervo por outro caminho.
- O relatório da última execução de 12/11 (43203545917) não foi lido; o resultado vem só da mensagem do commit 063d2a1.
- As fontes fora da rotina (seção 4) não foram consultadas: o que elas teriam não se sabe.
