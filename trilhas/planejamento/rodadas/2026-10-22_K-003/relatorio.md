# Relatório da rodada K-003 (22/10/2026)

**Cartão:** K-003, "Acertar o brief de execuções às D-036 e D-037". **Frente:** planejamento de melhorias. **Estado:** em Fazendo, à espera da aprovação de Vicente; com ela, a decisão que registra os padrões (registrar-decisao) e o cartão vai a Concluído.
**Pedido de Vicente (fala original, para a trilha):** "Rodada de planejamento de melhorias: cartão K-003 de trilhas/planejamento/quadro.md. Siga trilhas/planejamento/estado-planejamento.md. Traga para mim os quatro pontos em aberto (A-04, A-05, A-09, A-10), cada um com o padrão proposto e o porquê. Uso atual da conta: 12% (registre também no relatório do K-001, que pediu esse número)."
**Sessão:** `claude-opus-5-5` (conferido), esforço máximo, ultracode (`estado-planejamento.md`, passo 1). **Uso da conta:** 12% no início, informado por Vicente; no fim, a informar. O mesmo número fechou o relatório do K-001, como Vicente pediu.

## Entregas

| Arquivo | O que é |
|---|---|
| `rodadas/2026-10-22_K-003/pontos-em-aberto.md` | os quatro pontos em aberto (A-04, A-05, A-09 b, A-10), cada um com o texto em vigor, o que as decisões dizem, o padrão proposto, o porquê, o que muda e aonde se quer chegar; e as leituras A-03 e A-06, que a aprovação confirma. Corrigido pela verificação |
| `trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md` | o brief com o quadro "Ajustes das D-036 e D-037" no início e os ajustes no lugar: retomada pelo quadro (seção 1); seção 2 até a D-037; segunda leitura e relatório do lote sem aprovação (3a); a camada 2 pelo portão (3b); a ordem com o K-003, o K-103 e o K-102, e a parada (c) do bloco 2 na tabela (seção 4); o que muda em `.claude/` e as regras de harness dos insumos 5, 7 e 17 (bloco 1); fila, amostra, quarentena e eixo 5 no registro (bloco 2); o estado inconsistente e a amostra (bloco 3); os cartões da operação no `fila_curadoria.py` (bloco 5); a amostra e as Faltas a liberar (blocos 7 e 8); a seção nova do script de menções (K-102); o portão por camada e a junção (bloco 10); as horas (bloco 13); a operação e a CLB nova (depois do bloco 14); o "não fazer" (seção 5); a parte D da seção 6 e a trilha |
| `trilhas/2026-10-17_caminhos/caminhos.md` | a nota de ajuste, logo abaixo do cabeçalho |
| `rodadas/2026-10-22_K-003/checar_ajustes.py` | a checagem mecânica, sem IA: passa nos arquivos de agora (código 0) e reprova no commit 71dafff, de antes dos ajustes (código 1, 63 problemas); confere as linhas de `.claude/` que o bloco 1 cita e lista o que o K-101 grava |
| `rodadas/2026-10-22_K-003/verificacao.json` | a verificação dos dois auditores, com a decisão do curador sobre cada achado e o que mudou |
| `trilhas/planejamento/quadro.md` | o K-003 em Fazendo; o texto da operação diz quais cartões chamam Vicente (só os de conflito e de Falta jurídica a liberar), o que antes estava ambíguo |
| `mapa-tres-frentes.md`, `proxima-versao.md` | uma nota sobre o K-003 em cada um; no mapa, os insumos 20 a 23 na seção 6 |
| `trilhas/insumos-planejamento.md` | os insumos 20 a 23 |
| `rodadas/2026-10-21_K-001/relatorio.md` | o uso da conta no fim do K-001: 12% |

## Os quatro padrões, em uma linha cada (o texto inteiro, com o porquê, está em `pontos-em-aberto.md`)

- **A-04, a amostra:** quem a lê é o auditor, depois dos scripts; ela não entra na cota de Vicente e custa tokens do teto da D-023; até 15 itens por amostra (valor provisório novo); o que acha vira correção da ferramenta e insumo, e Vicente vê o resultado na frente de planejamento.
- **A-05, a quarentena:** o item sai pela regra versionada, como proposta que passa pelo portão combinado da fase 1, com Execução; o julgamento de Vicente fica na regra (§8, l. 812); a barreira jurídica sai pela liberação da Falta, no cartão que o chama; a Falta que só vale para publicar espera a decisão de publicar (D-032).
- **A-09 (b), a CLB nova:** nasce candidata, pela regra, com o mesmo cartão de baixa prioridade da menção incidental, que não chama Vicente; os 4 critérios são campos com Evidência ou Falta; a candidata que não passa fica candidata, com a linha "não admitida" na trilha; no piloto, o cartão espera.
- **A-10, a junção:** é portão da ferramenta, por camada; até o K-113, Vicente junta pela página do GitHub, uma vez por semana, o que passou, olhando as checagens e não o conteúdo; é ação fora dos dois cartões da D-037, que ele confirma ou corrige ao aprovar; a rotina nunca junta a própria proposta.

## Como se fez

1. Kit de leitura do `estado-planejamento.md`: `AGENTS.md`, o estado, o quadro, os insumos abertos, as D-031 a D-037, o mapa (seções 2, 5, 6, 7 e 8), a lista da próxima versão, o brief inteiro, o roteiro nas linhas citadas, as linhas da Fundação que os atritos citam (com o Anexo A, P84 a P87) e os arquivos de `.claude/` que o cartão nomeia. K-003 movido para Fazendo.
2. Os quatro padrões, escritos pela sessão principal a partir do plano, cada um com âncora (`pontos-em-aberto.md`).
3. Os ajustes no brief, a nota no roteiro e o texto do quadro.
4. A checagem mecânica (`checar_ajustes.py`): passou nos arquivos de agora e reprovou no commit 71dafff, como devia.
5. A conta do orçamento antes do lote: `orcamento.py --teto 300000 --estimativa 239232` deu PODE. A estimativa é 2 × 119.616, o maior contexto final de um auditor na verificação do K-001, pela conta do transcript (insumo 16: a última medida do mesmo agente com a mesma habilidade; o workflow não dá o consumo por agente, insumo 15).
6. A verificação independente (D-026), num lote de dois auditores (Sonnet 5.5 alto, teto de 20 chamadas cada, sem web) no workflow `wf_a8931ef3-303`: (A) o brief, o roteiro, o quadro e `.claude/` contra as decisões e os atritos; (B) os quatro padrões, para refutar.
7. As correções nos padrões, no brief e na checagem; a checagem de novo (passa; o caso antigo reprova); este relatório; os insumos 20 a 23; o estado do planejamento, o quadro, o mapa e o `AGENTS.md` em dia; o log; a busca de dado pessoal; commit e push.

## Verificação: 27 achados, 25 aceitos, 2 aceitos em parte, nenhum descartado

O auditor B não refutou os padrões A-04, A-05 e A-09 (b), e refutou o A-10 como estava escrito. Os achados, em resumo (o texto inteiro e o que mudou em cada um estão em `verificacao.json`):

| Achados | Gravidade | O que mudou |
|---|---|---|
| F-18 (A-10) | **alta** | o portão passou a ser por camada: na 1, sem IA, o validador e as checagens por script; na 2, também o auditor e a semente, se a rotina de teste mostrar que a rotina chama o auditor, e senão a segunda leitura numa conversa de trabalho |
| F-19 (A-10) | média, aceito em parte | a junção semanal ficou dita como ação de Vicente fora dos dois cartões, lida como auditoria da ferramenta, para ele confirmar; o mesmo rótulo de horas da A-04. Em vez de um terceiro tipo de cartão que chame Vicente, que a D-037 não prevê, o relatório do dia lista as propostas à espera de junção |
| F-20, F-21 (A-10) | média, baixa | a parte reprovada da ramificação permanente é revertida com trilha, com caso de teste na 10a; a regra de a rotina não juntar a própria proposta vale por instrução até a 10b |
| AUD-K003-01, F-11 | média | saiu a exceção inventada ("não conta na fila"); a Falta que só vale para publicar segue a D-032: o cartão espera o K-010 e não chama Vicente antes |
| F-01 a F-07 (A-04) | média e baixa | a amostra não entra na cota (contas separadas); o 15 é valor provisório novo; o gatilho para refazer o item corrigido; o eixo próprio de cada falha; a âncora do lote de correção; a amostra sem achado vira log; o mesmo modelo do auditor e dos produtores, dito e posto no insumo 23 |
| F-08 a F-13 (A-05) | média e baixa | o gatilho da regra com versão nova; a saída como proposta pelo portão; a regra que muda não tira do acervo; a P87 sustenta só o processamento; a calibração chega pela frente de planejamento |
| F-14 a F-17 (A-09 b) | média e baixa | a candidata que não passa; quem muda o eixo 5 (a triagem, pelo portão; "publicada" fica com Vicente; a l. 628 vai à próxima versão); a l. 472 por analogia; a candidata no piloto |
| AUD-K003-02, 03 | baixa | o que Vicente faz no cartão de conflito ficou sem mecanismo inventado; a lista do sorteio virou exemplo (D-017) |
| AUD-K003-04 | baixa | o bloco 1 diz por que nada mais do insumo 5 se grava |
| AUD-K003-05, 06 | baixa, o 06 aceito em parte | a checagem confere as linhas de `.claude/`, os padrões em cada lugar, 19 linhas da Fundação e os termos-chave da seção 2; a paráfrase segue fora do alcance de um script sem IA |

O que cada auditor conferiu e achou certo está em `verificacao.json` (`conferido_sem_achado`: 8 e 10 itens). **Nenhuma segunda verificação das correções:** depois do lote, a folga (85.996) é menor que 2× o lote medido (D-023, regra 2). As correções aplicam achados confirmados e passaram de novo pela checagem sem IA.

## Releitura do brief, a pedido de Vicente ("Ficou algo ambíguo no brief?")

Feita pela sessão principal, sem agente: depois do lote de verificação, a folga da rodada (85.996) é menor que 2× o lote medido (D-023, regra 2). É releitura de quem escreveu, não verificação independente. O brief foi lido inteiro.

**Corrigido no brief, sem mudar o sentido (o plano responde):**
- o quadro de ajustes dizia que tudo vale "depois da aprovação" e, no fim, que só os padrões esperam por ela: agora diz que as leituras dadas valem pelas decisões (D-034) e os padrões e as leituras propostas, com a aprovação, e que até ela nenhum cartão do desenvolvimento começa;
- "frentes" tinha dois sentidos: na retomada, na prioridade da seção 3a e no `relatorio_dia.py`, eram as frentes de trabalho da l. 512 (a CLB do piloto, os vácuos por região e período), e não as três frentes da D-036; agora está dito;
- a regra de valências com versão nova refaz a triagem só do que está em quarentena; o que já entrou só volta à triagem nos gatilhos da l. 592;
- "o que falha no portão é revertido": vale só para a ramificação permanente das rotinas sem IA; na camada 2, a proposta que falha só não entra;
- "teto de 15" ao lado de "15 itens" (blocos 7 e 8) virou "teto de 15 chamadas";
- a fila passa de uma semana quando há mais de 15 cartões à espera (estoque, não ritmo);
- "a saída é proposta": nas conversas, a saída que o curador valida e grava; nas rotinas, a ramificação;
- o script de menções lê o texto que o processamento leu, e não só os Trechos, durante o lote;
- "por acaso", na CLB nova do piloto, confundia-se com a menção incidental;
- "valor provisório novo (D-034)": a D-034 cobre só os [PROPOSTA] da Fundação, e esses valores valem com a aprovação;
- a amostra semanal da operação roda onde roda a segunda leitura das rotinas;
- "15 itens por amostra, ou todos se forem menos", no lugar de "até 15", que deixava o tamanho sem piso (o único ajuste que fecha uma margem; continua padrão a aprovar);
- na seção 3a, "o que precisa de Vicente vira cartão" passou a falar só do conteúdo do lote, e as paradas da seção 0 seguem como estão;
- a precedência (cabeçalho e 6A) ainda falava da v0.2.1 e de registro pendente no bloco 0; a parada do bloco 14 era do K-004; "que junta o que a amostra achou" misturava "juntar" e "junção".

**Pontos de conteúdo que o plano não resolve sozinho** (o texto inteiro, com a leitura proposta, em `pontos-em-aberto.md`, seção da releitura): o que Vicente faz num cartão de conflito; se tudo o que sustenta aviso, saúde ou política passa pelo auditor ou só o que cai na amostra; qual é a cajuína do piloto (a CLB situada); e o kit diante da regra do campo-de-acao sem a v0.2.1 (insumo 25). Mais o cartão do tratamento com IA entre o piloto e o K-113 (insumo 24, para o K-002). O brief marca cada um no lugar.

A checagem sem IA passou a cobrar essas correções e passa no estado atual; no commit 71dafff, reprova.

## Consumo de agentes (teto da rodada: 300 mil tokens, D-036)

| Lote | Agentes | Estimativa | `orcamento.py` antes | Medido (número da ferramenta) | Chamadas |
|---|---|---|---|---|---|
| Verificação | 2 auditores (Sonnet 5.5 alto) | 239.232 | PODE (0 + 239.232) | 214.004 | 30 (17 e 13) |
| **Total** | | | | **214.004** | **30** |

- **Dentro do teto, pelo número oficial:** 214.004 de 300.000, com 85.996 de folga. Nenhum agente pode mais rodar nesta rodada (regra 2).
- **As duas contas, de novo:** o número do workflow bate com a soma dos contextos finais dos auditores no transcript (111.214 + 102.775 = 213.989) e deixa de fora a saída do último turno (16.419 + 21.328); com ela, o lote daria 251.736, também dentro do teto. É estimativa pelo transcript, não número oficial (insumo 15).
- **A estimativa** veio da medida do mesmo agente na mesma habilidade (insumo 16), e o lote ficou 10,5% abaixo dela pelo número oficial.
- **Sessão principal:** fora da soma, como manda a regra; a medida é o uso da conta que Vicente lê (12% no início).
- **Incidente:** um comando da sessão principal, que gravava e apagava um arquivo temporário na raiz do disco, foi barrado pela proteção do harness e não rodou; a checagem foi refeita gravando na pasta temporária da sessão.

## Insumos novos (20 a 25, em `trilhas/insumos-planejamento.md`)

20 · juntar a proposta da rotina sem Vicente, por script sem IA (K-002, K-113) · 21 · o alcance do script de menções é o registro de Termos (K-102, K-117) · 22 · `checar_mapa.py` lê a 6A do brief por linhas fixas e hoje passa sem olhar nada nessa checagem (K-006) · 23 · o auditor da amostra usa o mesmo modelo dos agentes que produzem (K-115; V-24) · 24 · o cartão do tratamento com IA entre o piloto e o K-113 (K-002) · 25 · o kit e a regra do campo-de-acao sobre Falta jurídica aberta, sem a v0.2.1 (K-114).

## Alcance

- **Olhado (sessão principal):** Fundação, l. 74-78, 105-120, 128-134, 196-201, 241-247, 369-377, 393-410, 438-514, 592-612, 618-641, 660-760, 780-831, 832-932 (estas, até 900 caracteres por linha), e 1480-1530 (Anexo A, P84 a P89), com `grep` de quarentena, julgamento e admissão no texto inteiro; o brief inteiro; o roteiro, l. 1-40, 95-125 e 170-190, e as linhas que a nota cita; o mapa, seções 1, 2, 5, 6, 7, 8 e 9; `proxima-versao.md`; os insumos 1 a 19; D-031 a D-037; o checklist do piloto; `curador.md`, `avaliador.md`, `auditor.md`, `extrair-evidencia`, `executar-brief`, `verificar-fundacao` e trechos de `conferir-fato`; `orcamento.py`, `registrar_log.py`, o esquema de log e o de achados; o relatório e a verificação do K-001. Os auditores: cada um a sua fatia (`verificacao.json`, campo `log.alcance` de cada fatia).
- **Fora:** o resto dos Anexos A a E; o roteiro, l. 41-94 e 126-169 (etapas que o brief detalha), salvo as linhas citadas; os mapas de 17/10; `legado/`; a web (nenhum fato novo nesta rodada). Uma segunda verificação das correções não coube no teto.

## Próximo

Vicente lê os quatro pontos (`pontos-em-aberto.md`) e o brief ajustado. Aprovando com os padrões, ou dizendo o que neles não corresponde ao que quis dizer na D-037, a sessão registra a decisão (registrar-decisao), tira as marcas "a aprovar" do brief e do roteiro, fecha o K-003 em Concluído e passa ao K-002, pela ordem do quadro. No desenvolvimento, o K-103 e depois o K-101 (bloco 1), quando Vicente autorizar.
