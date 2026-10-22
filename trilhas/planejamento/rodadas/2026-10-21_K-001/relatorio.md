# Relatório da rodada K-001 (21 e 22/10/2026)

**Cartão:** K-001, "Reunir tudo nas três frentes" (D-036). **Frente:** planejamento de melhorias.
**Pedido de Vicente (fala original, para a trilha):** "Rodada de planejamento de melhorias: cartão K-001 de trilhas/planejamento/quadro.md. Siga trilhas/planejamento/estado-planejamento.md (kit de leitura, teto de 300 mil tokens de agentes, essência e não transcrição). Opus 5.5, esforço máximo, thinking. Uso atual:4%."
**Sessão:** `claude-opus-5-5` (conferido), esforço máximo, thinking e ultracode (`estado-planejamento.md`, passo 1). **Uso da conta:** 4% no início, informado por Vicente; no fim, 12%, informado por Vicente em 22/10/2026 ao abrir a rodada K-003, como resposta ao pedido deste relatório. Nenhuma sessão está registrada entre o fim do K-001 e essa leitura; se a janela de uso renovou nesse intervalo, não está registrado.

## Entregas

| Arquivo | O que é |
|---|---|
| `trilhas/planejamento/mapa-tres-frentes.md` | o mapa: cada parte da Fundação v0.2, do roteiro e do brief, cada insumo (1 a 14) e cada decisão (D-001 a D-037) com frente, estado e destino; 13 atritos das D-036 e D-037 com o texto em vigor (A-01 a A-13); a ordem dos cartões; onde o quadro mora |
| `trilhas/planejamento/quadro.md` | o quadro completo: 35 cartões (planejamento K-000 a K-010; desenvolvimento K-100 a K-122; operação K-201), em ordem |
| `trilhas/planejamento/proxima-versao.md` | o que entra na próxima versão da Fundação: V-01 a V-36, para o K-004, depois do relatório do piloto |
| `rodadas/2026-10-21_K-001/` | este relatório; o lote C3 (`lote-C3.json`); a verificação (`verificacao.json`); a checagem mecânica (`checar_mapa.py`) |

## Conclusões

- **Onde o quadro mora:** no arquivo, na fase 1. O plano responde (D-034): princípio 11 (tudo na pasta e no repositório, reconstituível por qualquer IA), princípio 16 com o fato do lote C3 de que o `GITHUB_TOKEN` não acessa o Projects (a rotina precisaria de um token pessoal da conta de Vicente), e a D-026 (a fase 1 não recebe contribuições). A porta de contribuição da fase 2 é o K-008, com os fatos que ficaram "não conferido". Detalhe: mapa, seção 9.
- **Ordem:** o K-003 (acertar o brief às D-036 e D-037) vem antes do bloco 1; no desenvolvimento, o K-103 (registrar-melhoria) vem antes do K-101 (bloco 1), e o K-102 (script de menções) entre o K-110 (bloco 8) e o K-111 (bloco 9). O porquê está no mapa, seção 8.
- **Próxima versão:** depois do relatório do piloto (D-035; insumo 1). Até lá, as decisões valem pelos registros e a 6A do brief vale sobre o texto.
- **Atritos:** as D-036 e D-037 ainda não estão no brief, no roteiro nem em `.claude/`. A maior parte se resolve pelo texto das decisões; quatro pontos não, e vão a Vicente pelo K-003: quem lê a amostra que audita a ferramenta e se ela entra na cota (A-04); quem tira um item da quarentena (A-05); a CLB nova vinda de Entrada de rotina (A-09, b); a junção da ramificação das rotinas à versão principal (A-10). A configuração de cada frente e o sentido de "operação" na D-023 vão ao K-002 (A-12, A-13).

## Como se fez

1. Kit de leitura do `estado-planejamento.md`; K-001 movido para "Fazendo".
2. Lote C3 (auditor, conferir-fato, teto de 10 chamadas) sobre Issues e Projects do GitHub (insumo 14). Gravado em `lote-C3.json`, que valida no esquema de conferência, com log próprio.
3. Rascunho dos três arquivos pela sessão principal, a partir da leitura das fontes.
4. Checagem mecânica sem IA (`checar_mapa.py`): cada decisão, insumo, bloco, subseção da Fundação, linha do §8, pergunta do §10 e linha da 6A tem destino; os cartões, os V e os A citados existem. Passou, depois de uma correção (o K-000 não era citado).
5. Verificação independente (D-026) por três auditores, Sonnet 5.5 alto, um por fatia, no workflow `wf_beec673c-cdd`: (A) brief e quadro; (B) Fundação e próxima versão; (C) decisões, insumos, atritos e a casa do quadro. Cada achado com a linha e o trecho da fonte.
6. Correções nos três arquivos; checagem mecânica de novo; este relatório; insumos 15 a 19; estado do planejamento, quadro e `AGENTS.md` em dia; logs; busca de dado pessoal; commit e push.

## Verificação: 30 achados, 29 aceitos, 1 descartado

| Achado | Gravidade | O que mudou |
|---|---|---|
| A-01 | média | o quadro passa a trazer as paradas dos blocos 2 (c), 5 (c) e 10a (a, fornecedor pela D-033); o mapa anota que o brief se contradiz no bloco 2 (l. 136 e 216 contra l. 212) |
| A-02 | baixa | a 6A tem 17 linhas, não 16 |
| A-03 | baixa | faixas do bloco 10: 10a, l. 314-328 e 332-335; 10b, l. 329-331, 332-333 e 336-337 |
| A-04 | baixa | agentes do bloco 0 (redator e auditor previstos, nenhum rodou) e do 10b (auditor) |
| A-05 | baixa | o destino do K-101 e do K-104 segue o "Pronto quando" do bloco |
| A-06 | baixa | o porquê do K-102 antes do K-111 reescrito: o brief só pede par real para habilidades; a posição vem da D-037 |
| A-07 | baixa | a l. 392 do brief ("mudar a Fundação fora dos blocos 0 e 14") está superada pela D-035; entra no A-11 (o curador conferiu: o auditor não confirmou) |
| A-08 | baixa | as linhas dos blocos 2 e 13 apontam para os atritos da fila, da amostra e das horas (o curador conferiu) |
| B-01, B-02 | média | as l. 741, 742 e 744 entram nos V-12, V-16 e V-22; o Passo 4 aponta para eles |
| B-03 | média | as l. 76, 200, 376, 396, 667, 795 e 861 (a amostra como segunda leitura) entram no V-24 e no A-04 |
| B-04 | baixa | V-04 cita as l. 56 e 59-64 |
| B-05 | média | V-21 traz as l. 130-131 e 707 (validador e localização do trecho no Passo 1); o Passo 2 aponta para o V-21 |
| B-06 | baixa | V-20 cita as l. 100, 407, 426, 696 e 723 |
| B-07 | baixa | V-27 reescrito: saem as l. 807 e 821; "modelos" não está no §8 |
| B-08 | baixa | V-07: a frase está na l. 133; o selo, nas l. 372 e 635 |
| B-09 | baixa | o cabeçalho da Fundação (l. 1-43) entra no mapa e no V-01, com "quem escreveu esta versão" |
| B-10 | baixa | **descartado:** o quadro já leva as origens do §8 e do §10 no K-010; a dúvida veio de um grep truncado |
| C-01 | **alta** | o A-04 deixa de ser "leitura dada" e fica "em aberto": a D-037 dá à cota a auditoria da ferramenta ("substitui") e diz que nada mais chama Vicente (diretriz 1); quem lê a amostra e se ela entra na cota vão a Vicente pelo K-003 |
| C-02 | média | o A-06 passa a "leitura proposta", igual ao V-06 |
| C-03 | média | a D-027 registra a configuração que o planejamento da v0.2 usou; nenhuma decisão fixa a de cada frente. O A-12 fica "em aberto" e vai ao K-002, que ganha a configuração do planejamento; o `CLAUDE.md` por frente sai do K-003 |
| C-04 | média | a D-023 fala em "operação da fase 1"; o mapa diz a leitura do brief (sessões de trabalho, com as rotinas na mesma guarda) e a manda ao K-002 |
| C-05 | média | os atritos ganham as linhas do roteiro (l. 101, 120, 176 e 185), da Fundação (l. 199, 243, 246) e do brief (l. 322, 422); o K-003 põe uma nota de ajuste no roteiro |
| C-06 | média | aceito em parte: entram `curador.md`, l. 20 (A-01), `avaliador.md`, l. 32 (A-05) e `extrair-evidencia`, l. 24 (A-06); a l. 19 citada não trata da quarentena (a linha certa é a 23, que não contradiz a D-037) |
| C-07 | média | o A-09 se divide: a menção incidental é leitura dada pela D-037 (4); a CLB nova vinda de Entrada de rotina fica em aberto |
| C-08 | baixa | o A-02 diz que a tela do relatório da rodada B, que Vicente aprova, é portão da ferramenta e fica |
| C-09 | baixa | o K-008 ganha a disponibilidade dos formulários de issue no plano Free (C3.5) |
| C-10 | baixa | os fatos do C3 levam a ressalva do método (extrator do WebFetch) |
| C-11 | baixa | o item 11 da 6C vai ao V-29 e ao V-13 |
| C-12 | baixa | a amostra roda na operação, e o que ela acha vai ao planejamento, nas duas tabelas |

O que cada auditor conferiu e achou certo está em `verificacao.json` (`conferido_sem_achado`: 13, 12 e 21 itens). Nenhuma segunda verificação das correções: o teto da rodada acabou; as correções aplicam achados confirmados e passaram de novo pela checagem mecânica.

## Consumo de agentes (teto da rodada: 300 mil tokens, D-036)

| Lote | Agentes | Estimativa | `orcamento.py` antes | Medido (número da ferramenta) | Chamadas |
|---|---|---|---|---|---|
| Lote C3 | auditor, conferir-fato (Sonnet 5.5 alto) | 60.000 | PODE (0 + 60.000) | 31.342 | 11 |
| Verificação | 3 auditores (Sonnet 5.5 alto) | 180.000 | PODE (31.342 + 180.000) | 267.700 | 41 |
| **Total** | | | | **299.042** | **52** |

- **Dentro do teto, pelo número oficial:** 299.042 de 300.000, com 958 de folga. Nenhum agente pode mais rodar nesta rodada.
- **Desvio do curador na estimativa:** usei a referência genérica do `AGENTS.md` (60 mil por agente Sonnet). O brief (l. 40) manda usar a última medida do mesmo agente com a mesma habilidade: o auditor mediu 76.771, 111.575 e 108.754 nas passadas da v0.2. Com essa estimativa (cerca de 300 mil para três), a conta daria PARAR, e o lote teria de ser menor. O lote veio 49% acima do estimado.
- **As duas contas não batem:** o número do workflow (267.700) soma o contexto de entrada do último turno de cada agente e deixa de fora a saída desse turno. Pelo contexto final de cada auditor no transcript (100.038, 119.616 e 109.794), o lote daria 329.448, e a rodada, cerca de 361 mil, acima do teto. É estimativa pelo transcript, não número oficial, e vai como insumo 15.
- **Sessão principal:** fora da soma, como manda a regra; a medida é o uso da conta que Vicente lê: 4% no início e 12% no fim (leitura de 22/10, ao abrir o K-003). Os 8 pontos de diferença são a medida da conta para a rodada só se não houve outro uso nem renovação da janela entre as duas leituras, o que não está registrado.

## Insumos novos (15 a 19, em `trilhas/insumos-planejamento.md`)

15 · o número do Workflow e o do Agent medem coisas diferentes · 16 · a estimativa do lote tem de vir da medida do mesmo agente e habilidade, também no planejamento · 17 · harness: validação reservada no teto, citação literal de verdade, log de agente de workflow · 18 · o script de checagem do mapa como ferramenta do planejamento · 19 · a configuração e o teto de cada frente, e o sentido de "operação" na D-023.

## Alcance

- **Olhado:** Fundação, l. 1-932 por faixas, e cabeçalhos e contagens dos Anexos C, D e E; brief inteiro; roteiro, l. 1-40 e 124-221; insumos 1 a 14; D-033 a D-037; o estado do planejamento, o quadro e o checklist do piloto; o mapa de decisões de 17/10; a Falta F-0003; `grep` das linhas tocadas pelas D-036 e D-037. Os auditores, cada um a sua fatia (`verificacao.json`, campo `log.alcance`). Web: só o lote C3, 10 páginas de docs.github.com.
- **Fora:** o corpo dos Anexos A, B, C e E; o roteiro, l. 41-123; os outros mapas e a verificação de 17/10; `legado/`. Uma segunda verificação das correções não coube no teto.

## Próximo

O K-003, numa rodada de planejamento: acertar o brief, o roteiro e `.claude/` às D-036 e D-037, com a leitura de Vicente nos quatro pontos em aberto. Depois, o K-103 e o K-101 (bloco 1), quando Vicente autorizar.
