# Brief de execuções: o caso-piloto cajuína com a ferramenta inteira

**Para quem:** a sessão do Claude Code que executa, em conversas novas abertas em `C:\Antigravity\Cultura Líquida`, sem memória da rodada de planejamento de 17/10/2026. E Vicente, que acompanha.
**Versão:** v0.1, rascunho de 17/10/2026, escrito na rodada de planejamento (workflow `wf_b6288315-eba`). É [PROPOSTA] até Vicente aprová-lo junto com o roteiro `trilhas/2026-10-17_caminhos/caminhos.md`.
**Base:** a Fundação v0.2 (`00_Fundacao_Cultura_Liquida.md`, 1.912 linhas, commit 118f65c; "l." é a linha dela); o roteiro, cujas etapas 0 a 14 viram aqui os blocos 0 a 14; os seis mapas em `trilhas/2026-10-17_caminhos/mapas/`; o checklist `trilhas/2026-10-16_execucao-v0.2.md`. Não há fato novo: os fatos externos vêm dos mapas e do roteiro, com o nível que lá têm.
**Precedência:** vale a Fundação (`AGENTS.md`: "Na dúvida, vale a Fundação"; acordo 5). As linhas da seção 6A sustentadas só pela D-031 e pela D-032, já registradas, valem como este brief diz até a v0.2.1 (bloco 0) acertar o texto; as que dependem da D-033 ou da D-034 ficam pendentes até o registro no bloco 0. Pôr o roteiro e este brief à frente do texto da Fundação, nessas linhas e só até a v0.2.1, muda o plano: o bloco 0 registra essa precedência (na D-034 ou em decisão própria, com a aprovação de Vicente) e ajusta a l. 3 da `AGENTS.md`. As leituras da seção 6B ficam como [PROPOSTA] sob a Fundação.

---

## 0. Autorização, modelos e regras

**Autorização (D-028).** A primeira mensagem de Vicente em cada conversa autoriza os blocos que ela indicar, e a autorização vale para todos os passos desses blocos.
- As memórias "plano não é execução" e "registrar a essência" não pedem nova autorização para o que este brief cobre. As essências da seção 2 estão confirmadas, menos a D-033 e a D-034: estas só valem depois do registro no bloco 0, com a aprovação deste brief, e o que nelas se apoia (a regra das perguntas, logo abaixo, e a seção 5) espera esse registro. Pedir confirmação vale só para comentário novo: captar a essência, conferir as palavras ambíguas, devolver o entendido e registrar com a habilidade registrar-decisao.
- Aprovar este brief também fixa as fontes do piloto (bloco 4) e faz o pedido do kit (bloco 11), salvo se Vicente disser outra coisa.

**Modelos (D-027; l. 697-698).**
- **Conversa principal (o curador):** Opus 5.5, esforço médio, sem ultracode. A sessão confere o ID do modelo; se não for `claude-opus-5-5`, avisa e para. Esforço máximo e ultracode foram só do planejamento.
- **Subagentes:** os agentes de `.claude/agents/`, pela ferramenta Agent, um por vez. Sonnet 5.5 alto para auditor, juridico, rastreador, avaliador, arquivista e campo-de-acao; o redator segue em Opus 5.5 médio (AGENTS.md). Antes de executar, o agente diz qual é o modelo indicado; se a sessão estiver em outro, avisa e para (l. 698).
- **Modelos menores** (Haiku 5.5 ou outros) só no bloco 12, depois que o harness de cada habilidade passa nos validadores com pares reais e o bloco 9 está aprovado (Vicente, 17/10). Harness é o conjunto de instruções, exemplos, validadores (scripts que aprovam ou reprovam uma saída) e scripts que prende cada agente ao plano. Pares reais são exemplos reais de entrada e saída, conferidos, que viram teste.
- **Sem Workflow** (rodada orquestrada de vários agentes) sem pedido explícito de Vicente.

**Paradas.** A execução não para para aprovar o que já está decidido (D-028). Para só em quatro casos:
- (a) uma decisão nova, que este brief e a Fundação não cobrem;
- (b) a regra de orçamento;
- (c) um bloqueio que só Vicente resolve (login, conta, chave, permissão);
- (d) um conflito que mude o sentido de uma decisão vigente: registra-se o conflito, sem reabrir a decisão.

Cada parada prevista na seção 4 diz o que Vicente decide e qual é o padrão; se ele aprovar o brief com os padrões, ela não acontece. Fato que não se consegue conferir não para nada: marca-se "não conferido" e segue-se. O que ficar sem resposta não vira pergunta: vai à seção 6 como insumo, dizendo aonde se quer chegar (D-034).

**Orçamento (D-023; l. 511).**
- **Teto:** 300 mil tokens por semana em agentes, somando o consumo que o retorno de cada Agent informa. A semana vai de segunda a domingo, pela data do log [PROPOSTA].
- **Lote:** uma chamada de agente, ou um conjunto de scripts, com saída verificável, fechado por commit e push.
- **Conta antes de cada agente:** `scripts/orcamento.py --teto 300000 --medidos <consumo de cada agente já rodado na semana> --estimativa <N>`. Código 1 é a Parada (b): o estado vai ao checklist do piloto, com commit e push, e o trabalho retoma na semana seguinte.
- **Estimativa N**, que é também o teto de tokens do lote: a última medida do mesmo agente com a mesma habilidade; sem medida, 60 mil (AGENTS.md) [PROPOSTA]. Medidas da v0.2: de 46 a 146 mil por chamada (§11, l. 908-921).
- **Teto de chamadas** em cada pedido, contado como o harness conta (cada ferramenta e cada pedido HTTP, mesmo agrupados num só comando), com margem; o número oficial é o do retorno do Agent. Pesquisa web: 15 a 20 chamadas; ficha de acesso: até 6 por ambiente. Leitura só por `grep -n` e faixas de linhas.
- **Conversa principal:** fica fora da soma, mas é medida. Vicente anota o uso da conta em claude.ai/settings/usage antes e depois de cada conversa e de cada rodada de rotina (l. 511, 923). O código que o curador escreve pesa nela.
- **Custos são medidos** (l. 700). Estimativa nunca é relatada como medida (P96, o pedido 96 de Vicente: nada de simulação apresentada como execução).
- **Compactação:** se o contexto for compactado, reler este brief e o checklist do piloto antes de seguir.

**Fatos.** Todo fato novo traz URL e nível: "oficial" só se a página oficial abriu; senão, "secundária" ou "não conferido". Nada de memória apresentada como conferido. Leis no planalto.gov.br: só o artigo, por `grep -n` e recorte. Proteção anti-robô (403, captcha, verificação de navegador) nunca se contorna: vira modo assistido, pedido de acesso ou a Falta "fonte inacessível" (l. 419).

**Dados, Git e commits.**
- Dado pessoal de terceiros (e-mail, telefone, CPF, @perfil, nome de quem não consentiu) nunca entra no Git, nem em registros, logs, exemplos ou respostas gravadas. O e-mail de Vicente, como responsável, é permitido.
- Texto integral de fonte, chaves e a saída do wiki local também ficam fora do Git (l. 100, 409). `legado/` não se lê: é do Passo 3 (D-024).
- Antes de cada commit, `scripts/procurar_dado_pessoal.py --git`. Autor `Vicente <vicente@dacaatinga.com.br>`, configurado só neste repositório. Mensagem em português, com a linha de atribuição que o sistema indicar. Push depois de cada commit. O aviso "Bypassed rule violations" é esperado.

**Ambiente Windows.** Python real `C:/Users/alqui/AppData/Local/Programs/Python/Python312/python.exe`, ou `.venv/Scripts/python.exe`, que tem `jsonschema`; sempre com `PYTHONUTF8=1`. Acrescentar `|| true` em buscas que podem não achar nada. No Git Bash, `gh api` sem a barra inicial. Nada de `sleep` em primeiro plano. Nada de heredoc longo nem de aspas aninhadas no Bash: arquivos se gravam com a ferramenta Write, e o log entra por `scripts/registrar_log.py <arquivo>`.

## 1. Estado de partida e retomada

**Estado em 17/10/2026:**
- **Fundação v0.2** completa, escrita pelos agentes e verificada em três passadas e pelo juridico, com 35 achados corrigidos; Anexos A e B intactos. Últimos commits: 118f65c (D-031 e D-032) e c5afef4 (os seis mapas).
- **Decisões** em `trilhas/decisoes/`: D-030, D-031 e D-032; as anteriores estão no §9. A D-033 e a D-034 se registram no bloco 0.
- **Harness:** 8 agentes e 14 habilidades em `.claude/`; 6 esquemas em `esquemas/` (log, conferência, Falta, guia de liberação, achado, decisão); 10 arquivos `.py` em `scripts/`; o hook SubagentStop, o gatilho que grava uma linha mínima de log quando um subagente termina.
- **Testes:** `scripts/rodar_testes.py` dá OK 27 · FALHA 0 · PENDENTE 9. Os 9 são da rodada B, as habilidades que esperavam o caso-piloto: 4 casos do rastreador, 4 do avaliador e do arquivista, 1 do kit.
- **Não existem:** `.github/`, `ambientes/`, `entrada/`, `acervo/`, `grafo/`, esquema do §6 além da Falta, adaptador.
- **Fora do Git (não rastreados):** o roteiro, este brief e três logs de 17/10 em `trilhas/logs/` (`2026-10-17_claude-code-guide.jsonl`, `2026-10-17_rastreador.jsonl`, `2026-10-17_workflow-subagent.jsonl`).
- **Consumo:** escrita e verificação da v0.2, 1.227.342 tokens de subagentes (checklist, l. 189); rodada de planejamento de 17/10, 580.337 tokens e 106 chamadas na primeira execução (checklist, l. 212), mais a retomada.
- **Abertos:** a Falta F-0003 (até onde o Git público já é publicação; `trilhas/2026-10-17_verificacao/falta-F-0003.json`) e os fatos "não conferido" do Anexo C.3 (checklist, l. 195).

**Retomada: sempre, ao abrir uma conversa, com a habilidade executar-brief.**
1. Conferir o modelo: `claude-opus-5-5`, esforço médio.
2. Rodar `git pull`, `git log --oneline -10` e `git status --short`.
3. Ler `AGENTS.md`, este brief (seções 0 e 4 e o bloco em curso) e o checklist do piloto, `trilhas/AAAA-MM-DD_execucao-piloto.md`, criado no bloco 0. Antes dele, ler `trilhas/2026-10-16_execucao-v0.2.md` a partir da l. 200.
4. Rodar o relatório calculado das frentes (l. 512): `scripts/relatorio_dia.py` a partir do bloco 5; antes, `scripts/rodar_testes.py` e a contagem dos registros por pasta.
5. Fazer a conta da semana (seção 0) com as medidas do checklist.
6. Pular o que está pronto. Cada bloco tem um "pronto quando" conferível; um bloco pela metade retoma do último lote com commit. Nunca refazer o pronto nem criar um segundo repositório do projeto.

## 2. Decisões vigentes (essência confirmada)

D-nnn é a entrada no Registro de Decisões (§9 e `trilhas/decisoes/`).

| D | Essência |
|---|---|
| D-015 | A Fundação passa à v0.2, com as melhorias da análise de 15 e 16/10 (feita em 17/10). |
| D-016 | Vicente tem de 1 a 3 h por semana de curadoria; os "15" nunca são teto de coleta. |
| D-017 | Exemplos ilustram e nunca limitam o trabalho. |
| D-018 | W, a compreensão local, é a prática comum da região: episteme própria, mas traduzível, tratada como dimensão. O não captado é Falta, dita e nunca completada. O saber comum muda de forma autóctone ou por interação. |
| D-019 | Não julgamos: fonte contrária só se documenta; se a fonte se corrige, documenta-se a correção; não é preciso documentar tudo; prática que atende aos critérios é admitida e pode ignorar revisionismo. |
| D-020 | O Jurídico é de precaução: cria Faltas e nunca autoriza. |
| D-021 | GitHub na conta Indalt, sincronizado, com commits de Vicente. O repositório é público, e o que entra no Git é publicação aberta; legado e dados pessoais de terceiros ficam fora. Google só se necessário; nuvem a considerar. |
| D-022 | Os critérios de prática cultural vêm da lei: CF, art. 216; Convenção da UNESCO de 2003 (Decreto 5.753/2006, art. 2); Decreto 3.551/2000. |
| D-023 | Medir e parar antes de acabar, com o estado salvo. Teto provisório de 300 mil tokens por semana em agentes na operação da fase 1. |
| D-024 | Do legado só entra o verificável e condizente com as regras novas; o resto não se apaga (Drive e `legado/`, só leitura); o site não é aproveitado. |
| D-025 | As regras valem "de início" e são proporcionais, com revisão de essencialidade depois da fase 1. Nenhuma obrigação legal é desprezada, e toda barreira jurídica traz o porquê e um caminho de liberação assistido. O grafo 4D fica fora da revisão. |
| D-026 | Fase 1 só com Vicente e os agentes, com logs. Segunda leitura = validador + verificador de harness diferente + amostra sorteada. |
| D-027 | Execução em Opus 5.5 médio, com harness; subagentes em Sonnet 5.5 alto; depois, modelos por tarefa escolhidos por teste. |
| D-028 | A execução não para para aprovar o que já foi decidido. |
| D-029 | Agentes, habilidades e harness ficam em `.claude/`, e só o Claude Code os opera. O caso-piloto é do Passo 1. |
| D-030 | Todo log traz o alcance: o que se olhou e o que ficou de fora. O que se publica diz o seu alcance. |
| D-031 | O caso-piloto é a cajuína, e o trabalho começa pelo caju, o insumo. As outras CLB entram pelas rotinas. |
| D-032 | O piloto é realista, mas é teste. Tudo o que foi desenvolvido (agentes, habilidades, harness, esquemas, scripts, logs) é usado por completo, em cada conversa e em cada rotina. As rotinas procuram todas as CLB; o piloto leva uma de ponta a ponta. Piloto não é publicação: o que só vale para publicar não se problematiza agora. |
| D-033 | O GitHub fica como repositório. Se ele impedir abrigar a ferramenta com o potencial pretendido (rotinas, buscas, tratamento com IA), usa-se outra solução em nuvem para isso. **Essência a registrar** com a aprovação deste brief; o arquivo nasce no bloco 0 e, até lá, a D-033 não vale como decisão. |
| D-034 | **Proposta, não registrada** (número e texto dos agentes). Modo de trabalhar. Fala de Vicente (17/10; checklist, l. 207; essência anotada na l. 210): depois do plano executado, não se pergunta o que o plano responde; o que restar diz aonde se quer chegar e é insumo para reavaliar o plano. Cláusula proposta, que a essência da l. 210 não traz e o pedido da rodada de 17/10 formula mais estreita: onde a Fundação permite valor provisório ([PROPOSTA]), a execução usa o valor e segue. Alcance proposto: os valores da l. 696, os [PROPOSTA] dos §5 e §6 que este brief usa e as leituras da seção 6B. O bloco 0 guarda na trilha a fala que origina a cláusula e registra tudo só com a aprovação de Vicente (roteiro, seção 7, item 1); até lá, a D-034 não vale. |

## 3. O uso completo da ferramenta (D-032)

### 3a. Em cada conversa de trabalho
1. **Abertura:** a retomada da seção 1.
2. **Um agente por vez, com teto.** O pedido traz a entrada (arquivos e faixas de linhas), a habilidade, o teto de chamadas, o critério de parada e o esquema da saída. O agente devolve JSON e o bloco LOG com o alcance (D-030).
3. **Gravação e validação.** Rastreador, avaliador, arquivista, juridico e auditor não têm Write. O curador grava a saída com Write no lugar indicado pelo bloco e a valida (`scripts/validar.py <esquema> <arquivo>`; a partir do bloco 3, também `scripts/validar_acervo.py`). O que não valida não entra, e o erro vai ao log.
4. **Log.** `scripts/registrar_log.py <arquivo>`, com modelo, habilidade, versão do harness, entrada, Ambientes, Consultas e Recortes usados, o que foi aceito, descartado ou posto em quarentena e por quê, tokens e chamadas do retorno do Agent, tempo, erros e alcance (l. 593, 699). A soma vai à tabela da semana.
5. **Segunda leitura (D-026):** o validador; o auditor, como verificador de outro harness; e a amostra sorteada com semente registrada (`scripts/sortear_amostra.py`, bloco 3). Quem produz não confere.
6. **Revisão de uma tela por lote** (o que entrou, o que ficou em quarentena, as Faltas novas), que Vicente aprova ou devolve (l. 512). A devolução vira um lote de correção, sem parar os outros blocos.
7. **Fechamento do lote:** checklist do piloto em dia, `procurar_dado_pessoal.py --git`, commit e push. É o ponto de retomada.
8. **Prioridade entre frentes** (l. 512): risco (princípio 4) → CLB do piloto → vácuos por região e período → escolha de Vicente.
9. **Paradas:** só as da seção 0.

### 3b. Em cada rotina automática

As rotinas procuram CLB em geral, nunca só a cajuína (D-031, D-032). Usam Consultas de termo, mistas e só por descritores; esta última é a busca que acha o que ainda não tem nome (l. 84). Cadência (D-012, l. 497): processar todo dia e alimentar cada ambiente toda semana, até exauri-lo.

| | Camada 1, sem IA (l. 505) | Camada 2, com IA (l. 506) |
|---|---|---|
| **O que roda** | scripts Python: adaptadores nos ambientes com ficha testada; deduplicação; feed de novidades por ID não visto; captura no Wayback; checagem de links; reconferência dos trechos; validador; relatório calculado do dia | rotina do Claude Code: uma habilidade aprovada no bloco 9 por vez, sobre um lote de `entrada/`, com o harness do repositório |
| **Onde** | GitHub Actions, por cron (a regra de horários de uma tarefa que se repete, em UTC) e a cada envio. Se o GitHub impedir, outra nuvem, nomeada por decisão (D-033) | infraestrutura da Anthropic, na conta de Vicente, gastando a cota da assinatura |
| **Limites** | robots.txt, robô identificado, 1 pedido por segundo; teto de chamadas e de divisões por Recorte, com Falta ao estourar (l. 427); tarefa de até 6 h; agendamento a cada 5 min no mínimo, que pode atrasar e é desativado após 60 dias sem atividade em repositório público; nenhuma porta nova com a fila acima de uma semana de curadoria (l. 472) | prévia de pesquisa; intervalo mínimo de 1 h e os tetos por hora da l. 506; rede só com domínios permitidos (fora deles, 403), por isso a lista leva os domínios das fontes; lote de máquina de 15 itens [PROPOSTA] (l. 498); Sonnet 5.5 alto até o bloco 12; cadência diária só dentro do teto da D-023 |
| **O que grava** | `entrada/`, o estado dos Recortes, o feed, o relatório do dia e a Execução em `trilhas/logs/`, com origem "rotina" | proposta numa ramificação `claude/` (cópia paralela, revisada antes de entrar na versão principal), com a saída validada e o log; nunca na principal |
| **Como avisa** | o relatório do dia; uma falha avisa por e-mail nativo do Actions (l. 505) | a proposta; o relatório do dia lista as execuções da rotina e as que faltaram |
| **Como se mede** | minutos do Actions; Entradas por ambiente e por Consulta (o rendimento, l. 435); a Matriz de Pegadas e Vácuos, que mostra onde já se olhou e onde voltar (l. 416) | uso da assinatura antes e depois de cada rodada (l. 511); tokens e chamadas no log |

Fatos da tabela (nível oficial, páginas abertas em 17/10; roteiro, seção 4): https://docs.github.com/en/actions/reference/limits, https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows e https://code.claude.com/docs/en/routines. Não conferidos: se os commits do próprio workflow contam como atividade; se a rotina carrega o `CLAUDE.md`; a lista exata dos domínios padrão. Em nenhuma rotina entram senha institucional (l. 418), servidor de RSS de terceiros (l. 428) ou leitura por robô do que tem regra própria (l. 437). A busca por pessoa fica com Vicente.

## 4. A sequência do caso-piloto

| Bloco | O quê | Passo da Fundação | Agentes | Parada prevista |
|---|---|---|---|---|
| 0 | plano em dia: log da rodada, D-033, D-034, v0.2.1 | — | redator, auditor | (a) aprovar o brief |
| 1 | harness e operação | 1 | auditor | — |
| 2 | contratos do §6 e valores provisórios | 1 | auditor | — |
| 3 | scripts do núcleo | 1 (antecipa partes do 2 e do 7) | auditor, juridico | — |
| 4 | fichas de acesso, Termos e Consultas do caju | 1 e 4 | rastreador, arquivista, auditor | (a) fontes do piloto |
| 5 | adaptadores, Recorte, deduplicação, modo assistido, Wayback | 1 e 4 | auditor, juridico | (c) chave do Internet Archive |
| 6 | primeira coleta real | 1 e 5 | rastreador | — |
| 7 | do bruto à Evidência, com triagem jurídica | 1 e 5 | avaliador, juridico, auditor | — |
| 8 | Termos, ficha, grafo, Educação e wiki local | 1, 6 e 7 | arquivista, juridico, redator, auditor | — |
| 9 | pares reais, rodada B, README e reconstituição | 1 e 2 | auditor | (a) harness pronto, só para 10b e 12 |
| 10 | rotinas de verdade: 10a sem IA, 10b com IA | 4 e fase 2 | rastreador, auditor, redator | (a) termos do Actions e nuvem; (c) conta e rotina |
| 11 | kit de fonte primária | fase 1 (l. 670) e 9 | campo-de-acao | (a) pedido do kit |
| 12 | testes de modelos | 1 | agentes do piloto, auditor | — |
| 13 | horas e consumo, desde o bloco 6 | gatilho da fase 2 | — | — |
| 14 | Fundação v0.3 | — | redator, auditor | (a) aprovar a v0.3 |

**Ordem.** Um bloco por vez, de 0 a 14. A 10a, sem IA, pode correr junto com os blocos 7 a 9, e a medição do bloco 13 corre desde o 6. **Conversa 1:** itens 1 a 3 e 7 do bloco 0, depois o bloco 1 e, se a conta da semana deixar, os itens 4 a 6 do bloco 0 (a v0.2.1). **Conversa 2, nova**, porque agente editado só carrega em sessão nova (checklist, l. 75): abre o bloco 2. Daí em diante, quantas conversas a conta pedir. As chamadas previstas em cada bloco são estimativas; o que vale é a medida.

### Bloco 0 — Plano em dia · *muda o plano: é o bloco que registra a D-033 e a D-034* · roteiro, etapa 0
- **Entrada:** a aprovação deste brief e do roteiro na primeira mensagem de Vicente; o checklist, l. 200-212; o mapa `mapa-decisoes-e-perguntas.json` (`mudancas_de_plano`).
- **Faz e grava:**
  1. o log completo da rodada de planejamento de 17/10, com `registrar_log.py`, a partir dos três `.jsonl` não rastreados e dos números do checklist (l. 212). O que não estiver registrado entra como "não informado";
  2. `trilhas/decisoes/D-033.json` e `D-034.json`, com registrar-decisao;
  3. o checklist do piloto, `trilhas/AAAA-MM-DD_execucao-piloto.md`: estado por bloco e lote, tabela semanal de consumo e horas;
  4. a Fundação v0.2.1, só com as consequências das D-031 a D-034 (seção 6, parte A);
  5. `AGENTS.md` e `CLAUDE.md` em dia: passo corrente, checklist novo, decisões até a D-034, modelos da rodada B, rotinas no piloto, e "[PROPOSTA] não é plano" lido com a D-034;
  6. `scripts/checar_fundacao.py` reconhecendo as D-031 a D-034;
  7. commit do roteiro e deste brief, aprovados.
- **Agentes:** redator com escrever-secao-fundacao (Opus 5.5 médio; teto de 15 chamadas); auditor com verificar-fundacao, nos olhares das decisões e das contradições (Sonnet 5.5 alto; teto de 15). Previstas: 2 chamadas.
- **Validador:** `scripts/validar.py decisao`; `checar_fundacao.py`; `scripts/comparar_anexos.py`.
- **Pronto quando:** as decisões validam; `checar_fundacao.py` passa com as D-031 a D-034; os Anexos A e B estão intactos; o auditor não acha contradição entre o texto e as decisões; commit e push feitos.
- **Parada (a):** Vicente aprova este brief e o roteiro. Padrão: aprovar com os padrões das paradas abaixo; a aprovação confirma a D-033 e registra a D-034. Sem aprovação, só se faz o item 1.

### Bloco 1 — Harness e operação · *dentro do plano* · etapa 1
- **Faz e grava:**
  - `.claude/agents/curador.md` com avaliador, arquivista e campo-de-acao na lista Agent; os três com `claude-sonnet-5-5` e esforço alto no frontmatter, no lugar do marcador;
  - `consulta` 0.1.1: bola de neve só na fase 2 (l. 438; §6, Recorte, l. 592); novidade por ID não visto, nunca por data (l. 428); entrada pelo Anexo E e por `ambientes/`;
  - `ficha-de-acesso` 0.1.1: a mesma entrada; os campos `robots` e `cobertura` nos três exemplos, com "não conferido" onde faltar dado;
  - `esquemas/log.schema.json`: `alcance` obrigatório fora da linha do hook (D-030); Ambientes, Consultas e Recortes usados (l. 593); `fonte_do_registro` também para script, rotina e pessoa; um `id` da Execução, com prefixo próprio no registro de valores, que os registros do bloco 2 guardam na origem e o `validar_acervo.py` confere (l. 587, 593); para script e rotina, os campos de agente (modelo, esforço) dispensados e tokens e chamadas null com o motivo, porque a rotina não recebe esses números de um Agent, e um caso que reprova log de script sem alcance. Os logs antigos continuam válidos;
  - `executar-brief`: teto de chamadas contado como o harness conta, com margem; log por arquivo (Write + `registrar_log.py`), sem heredoc; o ritual da l. 512;
  - `testes/relatorio-rodada-A.md` regenerado com `rodar_testes.py --relatorio` (hoje diz 37 ausências; o script dá 38).
- **Agentes:** auditor, olhar mecânico contra o §5.3 e o §6 (Sonnet 5.5 alto; teto de 15). Prevista: 1 chamada.
- **Validador:** `rodar_testes.py`, com um caso novo: log sem alcance reprova.
- **Pronto quando:** `rodar_testes.py` sem FALHA; o caso novo reprova como esperado; as versões 0.1.1 têm Histórico; numa conversa nova, a ferramenta Agent lista os três agentes.
- **Parada:** nenhuma prevista.

### Bloco 2 — Contratos do §6 e valores provisórios · *dentro do plano nos contratos (l. 693) e nos valores provisórios (l. 696); o registro único em arquivo e o layout são leituras da seção 6B, que mudam o plano e esperam o registro no bloco 0* · etapa 2
- **Entrada:** o §6, l. 584-641; os exemplos reais de 15/10 (`ficha-de-acesso/exemplos/`, `consulta/exemplos/cauim-totais.json`); os dados reais dos mapas de 17/10.
- **Faz e grava o registro de valores provisórios.** `esquemas/valores-provisorios.json`, com esquema próprio, é o registro único dos [PROPOSTA] que a execução usa. Cada valor traz a linha da Fundação que o permite, quem o usa e quando se calibra; esquemas e scripts leem dele, sem cópia. Os valores:
  - a escala de valências e o critério de `PENDENTE_JULGAMENTO`, o selo da quarentena (l. 696, 812);
  - a unidade da ficha: a CLB situada, com o Termo como entrada própria e ligação muitos para muitos (l. 811);
  - os valores do eixo 5, o estado editorial da ficha, em que "publicada" existe mas não se usa no piloto (l. 628);
  - o limiar de semelhança e a regra de normalização do texto antes do hash, com versão (l. 130, 598);
  - a regra que leva das contagens de linhagens a μ e λ e os limites entre os estados (l. 116-117; Anexo C, item F-12, secundária);
  - um prefixo de ID por tipo: F- fica com a Falta e P- com a pessoa (l. 585);
  - o formato da marcação frase → Proposição (l. 605);
  - o lote de máquina de 15 itens e o juízo de até 15 itens por semana (l. 498, 902);
  - o número dos IDs: nunca se repete nem se reaproveita (l. 585), mesmo com três gravadores ao mesmo tempo (workflow, conversa e rotina). Padrão: derivado do identificador da fonte ou numa faixa por gravador; o `validar_acervo.py` reprova colisão;
  - a fila e a semana da l. 472: fila = itens à espera de juízo humano; uma semana de curadoria = a cota de até 15 itens (l. 902), salvo outro valor que Vicente indicar ao aprovar. O `relatorio_dia.py` a calcula, e o script das rotinas não abre ambiente novo acima dela;
  - o tamanho da amostra sorteada (D-026), que a Fundação não fixa. Padrão: o que sobra da cota semanal depois das duas primeiras prioridades da l. 902, e o mesmo número na releitura do auditor; calibra-se no Passo 5;
  - a medida das rotinas na conta da D-023 (l. 511): a leitura semanal do uso da conta atribuída às rotinas, marcada como medida da conta e não de agente, e um teto em número de execuções por semana, fixado com o consumo medido na rotina de teste (bloco 10b);
  - a parada da conversa principal (D-023: medir e parar antes de acabar): Vicente lê o uso ao abrir e ao fim de cada bloco; a sessão para no limite que ele indicar, com o estado salvo antes. Somar o consumo dela pelo registro da sessão, se houver, é não conferido;
  - a semana e a estimativa do orçamento (seção 0) e o layout abaixo.
- **Faz e grava os contratos em `esquemas/`,** na ordem do Passo 1 (l. 693):
  - primeiro Termo (l. 613; campos compatíveis com TBX e SKOS, padrões de troca de terminologia e de vocabulários, a conferir: l. 103; Anexo C, item F-13), Proposição (l. 602), Evidência (l. 601) e Fonte (l. 597, com `deriva_de`, perspectiva e Correção);
  - depois Ambiente com a ficha de acesso (l. 590, 418), Consulta (l. 591), Recorte (l. 592), Entrada (l. 596) e Trecho (l. 598);
  - depois CLB situada com os 4 critérios (l. 605; D-022), Elemento de prática (l. 606), Insumo e Processo (l. 607), Compreensão local (l. 608), Transformação (l. 609), Aresta (l. 610) e Lugar (l. 614);
  - todos com os campos de proteção e de origem (l. 586-587) e os eixos de status (l. 620-641). A Falta já existe (l. 618).
- **Fonte no Git público [PROPOSTA]:** a "referência completa" (l. 597) vai sem nome de pessoa: título, instituição, ano, tipo e link permanente (DOI, handle ou URL). A autoria entra por código opaco só quando a linhagem ou a perspectiva pedirem, com a tabela código → nome fora do Git (l. 615; §5.1).
- **Layout fixado [PROPOSTA]** (as pastas nascem no passo em que entram, l. 723):
  - `ambientes/<id>.json`: o Ambiente, a ficha e os dois eixos de estado (l. 415);
  - `ambientes/consultas/` e `ambientes/recortes/`, este com o estado de cada Recorte;
  - `ambientes/traducao-consultas.json`: o arquivo de tradução da l. 426, com Consulta × Ambiente → sintaxe, a data e o teste que a conferiu. O campo de tradução da Consulta (l. 591) aponta para ele;
  - `entrada/`; `acervo/<tipo>/` para Fonte, Trecho, Evidência, Proposição, Termo, CLB situada, Elemento, Insumo, Processo, Compreensão local, Transformação, Aresta, Lugar, Falta e Pessoa (só código opaco e papéis; l. 405, 615);
  - `acervo/fichas/<id>.md`; `grafo/`, só com o que o script gera;
  - `ambientes/rotinas.json`: a configuração das rotinas, ambiente × Consulta × cadência × reserva (l. 430, 497; bloco 10a);
  - fora da pasta versionada, uma pasta temporária para o texto das fontes (l. 100, 407): o `localizar_trecho.py` (bloco 3) baixa ali a fonte ou a captura do Wayback e extrai o texto do PDF; o caminho vai ao avaliador, que lê por `grep -n` e faixas; a pasta se apaga ao fim do lote e, na busca assistida, recebe o que Vicente salvar.
- **Pessoa e papéis** (dentro do plano, l. 405, 615): contrato no bloco 2, com código opaco e papéis (por exemplo, detentor ou mestre, ou quem fala), sem nome. Autoria da Fonte, voz da Evidência e executor "pessoa" usam esse código; o `validar_acervo.py` confere a W pela voz de quem pratica, pelo papel, e reprova registro com nome.
- **Parada (c), antes do bloco 7: lugar da tabela código → nome.** A Fundação deixa o lugar a Vicente no Passo 4 (l. 406), mas o piloto cria códigos desde o bloco 7: muda a ordem do plano (D-032; seção 6A). Padrão: uma pasta na máquina de Vicente, fora da pasta versionada, com a cópia que ele definir. Rotinas não criam código de pessoa; a reconstituição (bloco 9) não espera a tabela no repositório e registra a ausência dela.
- **Agentes:** auditor confere campo a campo contra o §6 e, com conferir-fato, TBX e SKOS, com URL e nível (Sonnet 5.5 alto; teto de 20, até 10 na web). Previstas: 1 a 2 chamadas.
- **Validador:** `.venv/Scripts/python.exe scripts/validar.py <esquema> <arquivo>`. O validador mínimo de `scripts/_comum.py` cobre só parte do padrão JSON Schema.
- **Pronto quando:** cada esquema tem um exemplo que passa e um que reprova, montados com dados reais já levantados (sem dado real, o exemplo leva a marca "exemplo de esquema" e não conta como par real). Os 4 casos do rastreador saem de PENDENTE, e cada habilidade ganha um caso que reprova: `total_visto` maior que `total_informado` sem explicação; ficha com 403 e decisão "aceito".
- **Parada:** nenhuma. Onde o §6 não fixa valor, vale o registro de valores provisórios (l. 696).

### Bloco 3 — Scripts do núcleo · *muda a sequência: localização do trecho e validador são do Passo 2 (l. 130-131, 707), e μ e λ do Passo 7 (l. 602); sustenta-se na D-032, com texto na v0.2.1* · etapa 3
- **Faz e grava** em `scripts/` (nomes provisórios; dependência nova entra no `requirements.txt`, de onde o `.venv` e o Actions instalam):
  - `localizar_trecho.py`. Lê a fonte, ou a captura datada do Wayback (o arquivo de páginas do Internet Archive), em memória ou em pasta temporária fora do repositório. Normaliza pela regra versionada e calcula o hash SHA-256 (a impressão digital do texto). Acha o trecho exato ou mede a semelhança, e devolve o trecho, um pedaço antes e outro depois (o seletor de citação da W3C), o localizador e o grau. Abaixo do limiar, emite a Falta "trecho não verificável por máquina". PDF sem texto legível vira essa Falta ou transcrição por IA marcada, com o link da imagem (l. 598). Reconfere relendo a mesma captura e comparando o hash. Nunca grava texto integral no repositório (l. 100);
  - `validar_acervo.py`. Confere os esquemas e as ligações: Evidência → Trecho → Fonte; Proposição com Evidências; Falta sem valor; Termo atestado só com abonação localizada; W só com a voz de quem pratica; frase factual da ficha com marcação de Proposição. Fica instalado como gancho de pre-commit, que roda antes de cada commit (l. 707);
  - `triagem_fixa.py`: as regras fixas do Jurídico para os casos óbvios (l. 695). São eles: licença ausente; pessoa identificável e dado pessoal, reaproveitando `procurar_dado_pessoal.py`; possível conhecimento tradicional; substância controlada; criança ou adolescente. A saída são Faltas válidas no `falta.schema.json`;
  - `calcular_mu_lambda.py`. Fecha as linhagens pelos componentes de `deriva_de` e conta as linhagens a favor e as divergentes. Aplica a regra provisória e calcula μ e λ (graus de evidência a favor e contra), Dc = μ − λ e Dct = μ + λ − 1 (graus de certeza e de contradição) e o estado. Põe a W não captada como paracompleta. Gera `grafo/` (nós e arestas) e as tabelas X×Y, com "não observada", e Z (l. 116-117, 547-549);
  - `gerar_termo.py`: do Termo, os booleanos (variantes, formas de busca e descritores), o glossário e os links. Fecha o laço termo → booleano → Consulta nova (princípio 2, l. 103-105);
  - `sortear_amostra.py`: a amostra da segunda leitura, com semente registrada (D-026);
  - `semear_ambientes.py`: `ambientes/` com um arquivo por linha do Anexo E (69), em estado "proposto", a partir dos mesmos dados do `gerar_anexo_e.py` (l. 415).
- **Agentes:** auditor testa como verificador de outro harness (Sonnet 5.5 alto; teto de 20); juridico dá as normas da triagem fixa, com nível, por conferir-fato (teto de 15; lei só pelo artigo). Previstas: 2 a 3 chamadas.
- **Validador:** `rodar_testes.py` com casos "comando" (código 0 = passa) que passam e que reprovam: trecho alterado marcado como localizado; duas fontes da mesma linhagem contadas como duas; forma de OCR registrada como variante; Falta jurídica sem norma ou sem caminho.
- **Pronto quando:** cada script tem um caso que passa e um que reprova; `procurar_dado_pessoal.py` não acha nada nas saídas; os 69 ambientes validam e a contagem bate com a do Anexo E; o pre-commit roda.
- **Parada:** nenhuma.

### Bloco 4 — Fichas de acesso, Termos e Consultas do caju · *dentro do plano (l. 415-419, 426, 691)* · etapa 4
- **Entrada:** as fontes do piloto (ver a parada); `ambientes/` semeado; os esquemas do bloco 2.
- **Faz e grava:**
  - fichas testadas e datadas em `ambientes/` (data, pedido e resposta literal) das quatro fontes. A da Hemeroteca registra a via humana a partir do teste de 15/10 (403), com no máximo um pedido novo, sem insistir;
  - a tabela de municípios do IBGE (geocódigo e bioma) em `acervo/lugares/ibge/`, com fonte, edição e data, e o nível reconferido; hoje o nível está dividido (Anexo C, item F-23; l. 538, 543);
  - os Termos candidatos de caju e de cajuína em `acervo/termos/`;
  - as Consultas de termo, mistas e só por descritores, com variantes por família de grafia e de OCR (leitura automática de texto em imagem; l. 433), em `ambientes/consultas/`, traduzidas em `ambientes/traducao-consultas.json`. "Caju" é termo agrícola amplo: Consultas mistas e Recortes por período e lugar evitam a saturação. Os descritores processuais (P3) saem das fontes e dos Termos (princípio 7), nunca de lista prévia.
- **Agentes:** rastreador com ficha-de-acesso (até 6 chamadas por ambiente, 1 pedido por segundo) e com consulta (teste da sintaxe, 1 pedido por fonte e Consulta); arquivista com registrar-termo (teto de 15); auditor com conferir-fato no nível da tabela do IBGE (teto de 10). Todos em Sonnet 5.5 alto; o curador grava, porque os três não têm Write. Previstas: 3 a 4 chamadas.
- **Validador:** `validar.py` com os esquemas de ambiente, consulta e termo.
- **Pronto quando:** fichas, Termos e Consultas validam; cada Consulta cita os seus Termos; a tradução de cada Consulta para cada fonte está testada e datada.
- **Parada (a): Vicente fixa as fontes do piloto** (l. 691, 807). Padrão, tirado dos testes de 17/10 (`mapas/web-cajuina-fontes.json`): três fontes de protocolos diferentes e a via humana. A aprovação deste brief com a lista vale como a escolha.

| Ambiente | Via (teste de 17/10) | O que traz | Nível e URL |
|---|---|---|---|
| BCR, o Banco de Bens Culturais Registrados do IPHAN | páginas abertas; API não conferida | o registro da cajuína no Livro dos Saberes (15/05/2014; revalidado em 17/06/2025), o dossiê (2009) e o parecer técnico (07/04/2014) | oficial, https://bcr.iphan.gov.br/bens-culturais/producao-tradicional-e-praticas-socioculturais-associadas-a-cajuina-no-piaui/ |
| Infoteca-e, da Embrapa | página do item aberta; OAI-PMH pelo Anexo E, não retestado | Documentos 123, "Processamento do pedúnculo do caju: cajuína" (2009; CC BY-NC-ND 4.0): do caju ao processo | oficial, https://www.infoteca.cnptia.embrapa.br/handle/doc/748513?locale=en |
| BDTD, do IBICT | API VuFind sem chave, HTTP 200 | "cajuína": 25 resultados, com ruído; entre eles, a tese da USCS (2017) sobre os significados culturais da bebida, pista de W | oficial, https://bdtd.ibict.br/vufind/api/v1/search?lookfor=caju%C3%ADna&type=AllFields&limit=25 |
| Hemeroteca Digital Brasileira | só pessoa: recusou o robô (403) em 15/10, segundo o Anexo E; nunca se contorna | imprensa histórica, pela busca assistida de Vicente | existência oficial; o 403 não foi retestado; https://hemerotecadigital.bn.gov.br/ |

### Bloco 5 — Adaptadores, Recorte, deduplicação, modo assistido e Wayback · *dentro do plano (l. 416, 427-435, 509, 740)* · etapa 5
- **Faz e grava** em `scripts/` (nomes provisórios):
  - os adaptadores, só os que o piloto pede. Adaptador é o código que conversa com um tipo de fonte, um por protocolo (l. 430). VuFind, o sistema de catálogo da BDTD. OAI-PMH, o protocolo em que um programa pede ao acervo o que mudou, para a Infoteca-e, se a ficha o confirmar. Para o BCR, a via que a ficha mostrar ou o modo assistido. Todos respeitam o robots.txt, identificam o robô e fazem 1 pedido por segundo;
  - `recorte.py`: grava o estado de cada Recorte a cada página (cursor, o marcador de onde a coleta parou; total informado e visto; saturação; erros; próxima ação; reserva). Divide a janela saturada e registra a Falta "busca interrompida por teto" (l. 427, 432);
  - `deduplicar.py`: uma Entrada por item em `entrada/`, por DOI, handle ou ID da fonte, com os Recortes de origem e o rendimento de cada Consulta (l. 435). A Entrada não guarda autoria (l. 596);
  - o registro do modo assistido: o modelo de Recorte para a busca manual de Vicente, com link permanente por página e "pessoa" como executor (l. 429);
  - `wayback.py`: captura pelo Save Page Now 2, em ritmo baixo (l. 509; os limites vêm de documentação de comunidade, nível secundária). Não captura página de ambiente cuja ficha registra 403, captcha ou verificação de navegador: a Entrada fica com o link permanente da página e, se preciso, a Falta "fonte inacessível" (l. 419), e o juridico registra a dúvida;
  - `fila_curadoria.py` (nome provisório; l. 512, 902): monta a tela de cada lote (o que entrou, o que ficou em quarentena, as Faltas novas) e a fila semanal de até 15 itens na ordem da l. 902. O veredito de Vicente vira Execução com executor "pessoa" e muda o eixo de status do item (por exemplo, a saída de `PENDENTE_JULGAMENTO`); caso que passa e caso que reprova em `rodar_testes.py`; o tempo gasto entra no bloco 13;
  - em todos os scripts deste bloco e do bloco 10, o alcance calculado vai ao log (D-030): Recortes previstos e rodados, páginas vistas e total informado, ambientes com erro;
  - `pegadas.py`: a Matriz de Pegadas e Vácuos, gerada das Execuções (l. 416);
  - `relatorio_dia.py`: o relatório calculado das frentes e do dia (entradas novas, Recortes, Faltas, consumo). Abre cada conversa e, a partir do bloco 10, cada rotina (l. 505, 512).
- **Antes da primeira captura,** o juridico faz a triagem da política de cópias arquivadas (Lei 9.610; l. 740). A dúvida vira Falta e não trava o piloto (D-032). Barreira que valha para a captura em si deixa aquele item sem cópia, com a Falta, o porquê e o caminho (D-025).
- **Agentes:** auditor na segunda leitura do código (teto de 15); juridico com triagem-juridica (teto de 10); ambos em Sonnet 5.5 alto. Previstas: 2 chamadas.
- **Validador:** cada adaptador testado com uma resposta gravada (fixture), sem nome de pessoa. Dois casos de deduplicação: um que passa (um item achado por duas Consultas vira uma Entrada, com as duas na origem) e um que reprova (uma duplicata forçada).
- **Pronto quando:** cada adaptador passa no teste e numa rodada real curta, com Recorte válido; os casos de deduplicação dão o esperado; `relatorio_dia.py` roda.
- **Parada (c): a chave da conta do Internet Archive** (l. 409, 509) é de Vicente. Padrão: sem chave, no ritmo anônimo. Com chave, ela fica na máquina, fora da pasta versionada, e, numa rotina, no cofre de segredos do serviço que a roda (recursos não conferidos). Nenhuma fonte do piloto pede chave.

### Bloco 6 — Primeira coleta real · *dentro do plano (l. 691, 753)* · etapa 6
- **Faz e grava:**
  - os Recortes nas fontes do piloto, primeiro o insumo e depois a bebida (D-031);
  - as Entradas em `entrada/`, com captura no Wayback;
  - as Execuções nos logs, com Recortes e Consultas (l. 593), e a primeira Matriz de Pegadas;
  - um Recorte assistido real, feito por Vicente na Hemeroteca.
- **Agentes:** os scripts do bloco 5 coletam, rodados pelo curador na conversa. O rastreador, com consulta, confere os totais e a saturação de cada Recorte e propõe a divisão da janela (Sonnet 5.5 alto; teto de 15 por lote). O curador grava. Previstas: 1 a 2 chamadas.
- **Pronto quando:** todo Recorte tem estado válido; o que não se exauriu é Falta com o motivo ("total desconhecido", "busca interrompida por teto"); uma segunda rodada no mesmo Recorte só traz o não visto.
- **Sem parada.** A busca assistida cabe nas horas de Vicente (D-016). Se não couber na semana, o Recorte fica com "próxima ação: busca assistida", e os blocos 7 e 8 seguem com as outras fontes. A medição do bloco 13 começa aqui.

### Bloco 7 — Do bruto à Evidência, com triagem jurídica · *dentro do plano (l. 484, 487, 691-701)* · etapa 7
- **Faz e grava:**
  - a triagem por valências e a quarentena que não descarta (selo `PENDENTE_JULGAMENTO`, princípio 10), em lotes de 15 Entradas (o lote de máquina [PROPOSTA], l. 498);
  - as Evidências com trecho localizado por `localizar_trecho.py`, voz (quem fala, por código opaco) e hash, em `acervo/`; a Fonte com `deriva_de` e perspectiva. Uma Fonte achada por um agregador (por exemplo, a tese da USCS, pela BDTD) se lê no repositório de origem, que ganha ficha de acesso; o texto fica em memória e só o trecho entra (l. 100);
  - antes da triagem jurídica, a conferência do que ela usa e hoje está "não conferido": se o caju é planta nativa e se há fermentação no modo de fazer (l. 484; conferir-fato, com URL e nível);
  - a triagem de cada fonte e de cada Evidência, por `triagem_fixa.py` e pelo juridico, com Faltas válidas em `acervo/faltas/`;
  - os guias de liberação como rascunhos, um por chamada. Primeiro o da Lei 9.610, que é o caminho da F-0003 e hoje está "a preparar". Depois completar o do SisGen e do consentimento prévio informado (Lei 13.123), que já existe como exemplo. Depois os da LGPD e do IPHAN (ordem da l. 695). Nenhum guia circula antes de os formulários e prazos serem conferidos no portal oficial (l. 695).
- **Agentes:** avaliador com extrair-evidencia (teto de 15 por lote; 2 a 3 lotes); juridico com conferir-fato, triagem-juridica e guia-de-liberacao (até 10 chamadas na web por guia); auditor relê a amostra sorteada (teto de 15). Todos em Sonnet 5.5 alto; o curador grava. Previstas: 8 a 10 chamadas.
- **Validador:** `validar_acervo.py`; `validar.py` com os esquemas de Falta e de guia de liberação.
- **Pronto quando:** `validar_acervo.py` passa; cada dúvida jurídica é uma Falta com norma e caminho; nenhuma Falta foi completada por inferência; o auditor confirma a amostra.
- **Sem parada.** O que só vale para publicar (Lei 13.123 no que se publica, F-0003, licença) vira Falta e não trava (D-032). Barreira que valha para o item em si o deixa em quarentena, com a Falta (D-025).

### Bloco 8 — Termos, ficha, grafo, Educação e wiki local · *Termos, ficha e grafo dentro do plano (l. 522, 547, 672); Educação e wiki local antecipam o Passo 6 sem publicar: muda a sequência, D-032, texto na v0.2.1* · etapa 8
- **Faz e grava:**
  - os Termos de caju e de cajuína, atestados por abonação localizada, e os booleanos novos de `gerar_termo.py`. Cada Consulta nova entra no próximo Recorte: é o laço vivo;
  - a ficha da CLB situada (a bebida num lugar, num grupo e num período; l. 605) em `acervo/fichas/`. Traz os 4 critérios de prática cultural (D-022), cada um com Evidência ou Falta; a W antes da tradução; toda frase factual marcada; as tensões lado a lado; as Faltas à vista;
  - `grafo/` e as tabelas X×Y e Z, por `calcular_mu_lambda.py`, sem a vista navegável, que é do Passo 7;
  - a camada Educação da ficha (l. 529, 761): fontes, "como citar" e as habilidades da BNCC (Base Nacional Comum Curricular) sugeridas pela tabela do PDF do MEC, com a página; e a Falta sobre a escuta da comunidade, se o material visar escolas indígenas ou quilombolas;
  - o wiki gerado só na máquina com o Quartz, um gerador de site a partir dos `.md` (recomendação [PENDENTE], l. 818; rodar só local: não conferido), com a saída numa pasta do `.gitignore`. Se o Quartz não rodar só na máquina, a ficha em `.md` é a primeira versão do wiki (l. 522), e o fato vai à seção 6.
- **Agentes:** arquivista com registrar-termo, montar-ficha e gerar-grafo (uma chamada por habilidade, teto de 15 cada); juridico com triagem-juridica sobre a ficha (teto de 10); auditor na amostra (teto de 15). Todos em Sonnet 5.5 alto. O redator escreve a Educação com o papel que já tem (Opus 5.5 médio; teto de 15), e o curador cuida do Quartz. Previstas: 5 a 6 chamadas.
- **Validador:** `validar_acervo.py`; o recálculo de `calcular_mu_lambda.py`.
- **Pronto quando:** `validar_acervo.py` aceita a ficha e reprova uma frase de teste sem Proposição; μ, λ, Dc e Dct batem com o recálculo; o wiki abre na máquina e nada dele entra no Git.
- **Sem parada.** Se as fontes não trouxerem divergência nem fala de quem pratica, λ fica 0 e a W fica Falta. É o comportamento correto, e não se inventa par.

### Bloco 9 — Pares reais, rodada B e o que falta do Passo 2 · *dentro do plano (l. 694, 701, 707-709, 726)* · etapa 9
- **Faz e grava:**
  - para cada habilidade usada, o caso real que passa e o que reprova. O que reprova é uma cópia do real com o erro injetado (padrão da rodada A), mais os casos ditos em cada `exemplos/LEIA-ME.md`. Os erros: ficha-de-acesso (403 com decisão "aceito"); consulta (total visto acima do informado, sem explicação); extrair-evidencia (trecho não localizado marcado como localizado); registrar-termo (forma de OCR como variante); montar-ficha (frase factual sem Proposição); gerar-grafo (duas fontes da mesma linhagem contadas como duas); triagem-juridica e guia-de-liberacao (os casos do bloco 3 e o guia da Lei 9.610);
  - `testes/relatorio-rodada-B.md` e o harness 0.2.0, com Histórico em cada habilidade;
  - o README para humanos e o teste de reconstituição: uma conversa nova, só com o repositório, retoma do ponto salvo (princípio 11).
- **Agentes:** auditor confere pares e casos (Sonnet 5.5 alto; teto de 15). Contratos, pares e casos nascem no mesmo piloto; sem segunda leitura, os validadores passariam por construção. Previstas: 1 a 2 chamadas.
- **Validador:** `rodar_testes.py --rodada B --relatorio testes/relatorio-rodada-B.md`.
- **Pronto quando** (harness pronto, l. 701): FALHA 0 e PENDENTE 0 nas habilidades dos blocos 4 a 8 (a do kit sai no bloco 11); cada uma com par real que passa e caso real que reprova; as regras fixas do Jurídico reprovam os casos de teste; o custo de cada habilidade está nos logs; a reconstituição passa (l. 726); Vicente aprova.
- **Parada (a), só para os blocos 10b e 12:** Vicente aprova o harness pronto pela revisão de uma tela do relatório da rodada B (l. 701). Padrão: aprovar se os números baterem com o critério. Enquanto isso, 10a, 11 e 13 seguem.

### Bloco 10 — Rotinas de verdade · *muda o plano: rotinas antes do Passo 4 e para CLB em geral (l. 363, 438, 669, 674, 741) sustentam-se na D-032, e a saída de reserva na D-033; texto na v0.2.1* · etapa 10
- **10a, camada 1, sem IA** (pode correr junto com os blocos 7 a 9):
  - `.github/workflows/` com o validador a cada envio e, por cron, as buscas, a deduplicação, a captura no Wayback, a checagem de links (`scripts/verificar_links.py`) e o feed de novidades por ID não visto (`scripts/feed.py`, gravado em `entrada/`, l. 428);
  - o relatório do dia, gravado em `trilhas/relatorios/` [PROPOSTA]; uma falha avisa por e-mail nativo (l. 505);
  - a ordem: primeiro as fontes do piloto. Depois, ambiente por ambiente, Consultas só por descritores e mistas de CLB em geral, começando pelos que responderam por API em 17/10: Oasisbr (https://oasisbr.ibict.br/, VuFind; oficial; a página inicial pediu verificação de navegador em 15/10, e a via é a API) e OpenAlex (https://openalex.org/; oficial; sem chave, com cota diária compartilhada). Depois, os 29 ambientes do Anexo E com via por programa e sem 403 nem captcha (contagem por texto, a confirmar em ficha). Cada ambiente novo entra com ficha testada e uma linha de configuração (l. 430); com a fila acima de uma semana de curadoria, nenhuma porta nova se abre (l. 472; fila e semana no registro de valores);
  - **Consultas gerais** (dentro do plano: princípios 2 e 7; D-032): antes de ligar os ambientes novos, `gerar_termo.py` tira descritores processuais dos Insumos (X), dos Processos (Y) e dos Termos atestados do piloto e propõe as Consultas só por descritores e mistas de CLB em geral; o curador as grava, validadas no esquema de Consulta, e o rastreador as testa em cada ambiente, nos lotes de ficha. Semear com o Wikidata ou com o legado antes da fase 2 muda o plano (l. 438; Passo 3) e pede decisão;
  - **adaptadores novos** (*muda o plano*: pela l. 430 só nascem os que o piloto pede; D-032; seção 6A): um lote por protocolo que as rotinas pedirem, a começar pela API com cursor (OpenAlex), e depois o leitor de feed (l. 428), SRU e CKAN; cada um com resposta gravada sem nome de pessoa, caso que reprova e rodada real curta antes de ligar o ambiente;
  - **teste em cada lugar de execução** (l. 418): cada ficha ganha um teste datado no próprio runner do Actions (a máquina do GitHub que roda a tarefa, com outro endereço de rede) antes de ligar o ambiente e, na 10b, na rotina de teste. Resultado diferente entra na ficha e, se barrar, vira modo assistido ou a Falta "fonte inacessível" (l. 419);
  - **configuração e agenda** (l. 430, 497; princípio 11): `ambientes/rotinas.json` (layout, bloco 2) e um script (nome provisório `agendar.py`) que decide o que roda em cada dia (qual Recorte, de onde retoma, com que reserva), dentro da D-012 (cada ambiente toda semana, l. 497) e da fila (l. 472), com caso de teste. Na 10b, um arquivo versionado por rotina (texto, cadência, domínios, modelo), copiado para a conta;
  - **dado pessoal** (D-021; §5.1): o workflow roda `procurar_dado_pessoal.py` antes de cada commit e falha se achar algo; o adaptador descarta nome de pessoa dos metadados (caso de teste com resposta gravada que traz nome);
  - **entrega do relatório** (l. 505, 744): além de gravado, o relatório do dia chega a Vicente por um canal de notificação que o próprio GitHub ofereça [PROPOSTA] (recurso não conferido; seção 6B);
  - **estado contínuo** (D-033; §5.1): se a proteção do `main` barrar o commit do workflow (abaixo), ele grava sempre na mesma ramificação de trabalho das rotinas, única e permanente [PROPOSTA] (seção 6B), que toda execução lê e grava com o estado da coleta (IDs vistos, cursores e reserva dos Recortes, feed); Vicente a junta na revisão semanal. Caso de teste: duas execuções seguidas, e a segunda só traz o não visto. Permissões de gravação do token do workflow: não conferido;
  - o hook SubagentStop deixa de depender do caminho do Python do Windows;
  - ao fim dos 7 dias, o redator escreve uma vez o boletim semanal do que entrou (l. 743), a partir dos relatórios, para testar o papel; a cadência fica para a v0.3, com o custo medido;
  - ao ligar, conferir como o commit do workflow passa pela proteção do `main` (l. 396) e se ele conta como atividade contra a desativação de 60 dias (ambos não conferidos). Se a proteção barrar, o workflow grava numa ramificação e Vicente a junta na revisão de uma tela, como na camada 2.
- **10b, camada 2, com IA** (só depois da aprovação do bloco 9):
  - primeiro, uma rotina pequena num repositório de teste, anotando a rede permitida, o consumo, a ramificação e a conta que assina (l. 506). A rotina de teste mostra se carrega o `CLAUDE.md` e as habilidades (não conferido), se alcança os domínios das fontes e se não grava na principal;
  - depois, uma habilidade aprovada por vez sobre lotes de `entrada/`, em Sonnet 5.5 alto até o bloco 12, abrindo proposta em `claude/`.
- **Agentes:** rastreador com ficha-de-acesso nos ambientes novos (até 6 chamadas por ambiente; lotes de até 4 ambientes); auditor com conferir-fato no texto inteiro dos termos do Actions, porque a citação de 17/10 veio por uma ferramenta que resume a página (teto de 10); redator no boletim (teto de 10); curador nos workflows e scripts e nas Consultas gerais. O mesmo auditor reconfere os fatos das rotinas do Claude Code que vieram do mapa de hospedagem, escrito em Haiku 5.5 (conflito com a D-027; roteiro, trilha). Previstas: 4 a 6 chamadas.
- **Pronto quando:** 7 dias seguidos de relatório do dia que chegou a Vicente, e uma falha provocada que gera aviso (l. 744); Entradas vindas de Consultas que não citam Termos de caju nem de cajuína, cada uma com a Consulta de origem; o boletim passou por `procurar_dado_pessoal.py` e pela amostra do auditor; na 10b, a rotina de teste mostrou os pontos acima, e cada execução da rotina roda a segunda leitura da D-026: o validador, o auditor chamado pela ferramenta Agent e a semente da amostra gravada (se a rotina carrega `.claude/agents/`: não conferido; as sessões na nuvem carregam, oficial, roteiro, seção 4).
- **Parada (a): termos do Actions** (l. 508, 814). Vicente decide se aceita a leitura proposta. Padrão: aceitar a leitura do Flat Data (a coleta produz o conteúdo que o próprio repositório publica) para os scripts sem IA, relendo o texto inteiro ao ligar.
- **Quando vale a D-033:** Vicente não aceita a leitura; o GitHub diz que a coleta está fora dos termos; a desativação de 60 dias não se evita; ou o volume passa dos limites (tarefa acima de 6 h, repositório acima de 1 GB). Então o GitHub fica como repositório, e outra nuvem abriga rotinas, buscas e IA. **Parada (a)** para nomear o fornecedor. Padrão: nenhum antes da decisão (candidatas na seção 6, parte C, insumo 8); enquanto isso, os scripts rodam à mão nas conversas de trabalho.
- **Parada (c): conta e rotina** (l. 506). São de Vicente o plano da conta com rotinas, o GitHub conectado, a rotina de teste e os créditos de uso. Padrão: repositório de teste na conta Indalt, só com o harness e um lote pequeno sem dado pessoal; créditos de uso desligados, para que o teto pare a rotina (l. 511); chave de fonte no cofre de segredos do serviço.
- **Sem parada:** os Alertas do Google por e-mail (l. 437, 451) esperam a caixa que Vicente abrir; só esse canal fica fechado.

### Bloco 11 — Kit de fonte primária, sob pedido · *muda o plano: o kit como teste no fim do piloto, sem publicar (l. 670), e a leitura da regra do campo-de-acao sobre Falta jurídica aberta sustentam-se na D-032 e na D-020, com texto na v0.2.1 (seção 6A); o pedido segue a l. 576 e 784-788* · etapa 11
- **Pedido** (princípio 15; a aprovação deste brief é a demanda): o kit de fonte primária para educadores, com a cajuína. É o material que ensina a registrar e enviar uma fonte primária (documento, depoimento já gravado, objeto) com trilha, consentimento e sem dado pessoal exposto.
- **Critérios de aceitação [PROPOSTA]**, que Vicente pode trocar ao aprovar: toda afirmação sobre a cajuína aponta para uma Proposição da ficha; só fontes do acervo do piloto, com link e nível; nenhum dado pessoal de terceiros; o alcance dito (D-030); as Faltas à vista; rascunho, sem publicar (D-032).
- **Faz e grava:** o rascunho em `campo_de_acao/` (l. 723); a saída vira o par real da kit-fonte-primaria. A regra do campo-de-acao "não usa conteúdo com Falta jurídica aberta" (`.claude/agents/campo-de-acao.md`, l. 30) não tem exceção na Fundação nem nas decisões: lê-la como regra do que se publica, sem alcançar a F-0003 no piloto, muda o plano (D-032, D-020) e só vale se a v0.2.1 a trouxer. Sem isso, a regra vale como está, e o kit usa só conteúdo sem Falta jurídica aberta.
- **Agentes:** campo-de-acao com kit-fonte-primaria (Sonnet 5.5 alto; teto de 15); o curador grava; Vicente revisa (l. 788). Previstas: 1 a 2 chamadas.
- **Pronto quando:** o rascunho, com fontes, foi revisado por Vicente; os casos do kit estão sem PENDENTE (par real e caso que reprova).
- **Parada (a):** o pedido e os critérios são de Vicente. Padrão: os de cima.

### Bloco 12 — Testes de modelos · *dentro do plano (l. 698)* · etapa 12
- **Entrada:** o bloco 9 aprovado; para o kit, o bloco 11.
- **Faz e grava:**
  - o banco de provas: os mesmos pares reais em cada modelo candidato, com validação e custo no log. Hipóteses de partida (l. 698): Sonnet 5.5 alto para ajustes e Haiku 5.5 para rotinas;
  - `testes/relatorio-modelos.md`, com a tabela habilidade × modelo × aprovação × tokens, calculada dos logs;
  - antes de começar, a conferência na documentação, com conferir-fato, de como escolher o modelo em cada chamada de agente (não conferido).
- **Agentes:** cada agente nas habilidades que usa, uma rodada por habilidade e modelo; o auditor valida (Sonnet 5.5 alto). Previstas: 10 a 15 chamadas.
- **Pronto quando:** cada habilidade fica com o modelo mais barato que passa. Se falha, reforça-se o harness antes de subir de modelo. Frontmatters e rotinas atualizados, com Histórico.
- **Sem parada:** a troca de modelo é o resultado do teste previsto (D-027), não uma decisão nova.

### Bloco 13 — Horas e consumo, desde o bloco 6 · *dentro do plano (l. 511, 678, 902, 923)* · etapa 13
- **Faz e grava,** na tabela semanal do checklist do piloto:
  - as horas de Vicente: revisões de uma tela, juízo de até 15 itens na ordem do §11 e busca assistida;
  - os tokens por agente, com `orcamento.py`;
  - o uso da conta antes e depois de cada conversa e rotina, lido em claude.ai/settings/usage (só Vicente lê; é a única medida da conversa principal, l. 923);
  - os minutos do Actions.
- **Pronto quando:** 4 semanas seguidas medidas, a condição 2 do gatilho da fase 2 (l. 678).
- **Sem parada.** A sessão registra os números que Vicente der; sem eles, "não informado", nunca estimado (P96). A condição 3 do gatilho (as decisões do degrau 2 do §5.4) é de Vicente e não trava o piloto.

### Bloco 14 — Fundação v0.3 · *dentro do plano (acordo 5)* · etapa 14
- **Faz e grava:** a v0.3, com o que o piloto mostrou. Entram os custos e os modelos por habilidade; as horas reais; os valores provisórios calibrados (valências no Passo 5, limiar, μ e λ, lote de máquina); as respostas aos insumos da seção 6; o lugar das rotinas (D-033); as decisões novas no §9.
- **Agentes:** redator com escrever-secao-fundacao (Opus 5.5 médio); auditor com verificar-fundacao (Sonnet 5.5 alto); curador com registrar-decisao. Previstas: 2 a 4 chamadas.
- **Antes da v0.3** (até 2 chamadas a mais): o relatório do piloto, calculado dos logs (itens, ambientes, fichas, grafo, custos e horas), escrito pelo redator e conferido pelo auditor, que também confere com conferir-fato cada habilidade da BNCC citada na Educação do bloco 8, com página e URL do PDF do MEC. É ele que dá às perguntas do §10 os números reais (seção 6C, insumo 11).
- **Pronto quando:** o relatório do piloto foi conferido; o auditor não acha contradição; `checar_fundacao.py` e `comparar_anexos.py` passam; o gatilho da fase 2 (l. 676-679) é avaliado com os números medidos.
- **Parada (a):** Vicente aprova a v0.3 (acordo 5). Sem a aprovação, valem a v0.2.1 e este brief.

### Depois do bloco 14 — Operação
- **Cadência** (ritual e prioridade da l. 512; seção 3a): toda semana, as conversas de trabalho que a conta da D-023 permitir, cada uma aberta pela retomada da seção 1; as rotinas seguem a configuração do bloco 10a.
- **Orçamento:** o da D-023 (300 mil tokens por semana em agentes), com a medida das rotinas e a parada da conversa principal do registro de valores (bloco 2).
- **CLB nova a partir de Entrada de rotina:** a regra de quem abre a CLB situada nova, com os 4 critérios da D-022, não foi achada no §5.4 por `grep -n` (l. 440-494 trazem as portas por tipo de evidência). Se a Fundação não a tiver, muda o plano e é decisão de Vicente (sustentaria: D-031, D-032). Padrão proposto: o curador a abre numa conversa de trabalho quando uma Entrada triada atende aos 4 critérios, na prioridade da l. 512, uma CLB nova por vez e só com a fila abaixo de uma semana (l. 472).

## 5. Não fazer

- Publicar qualquer coisa fora do repositório: site, wiki hospedado, kit, guia ou boletim (D-032; l. 520, 695).
- Contornar proteção anti-robô; usar senha institucional (l. 418); usar servidor de RSS de terceiros (l. 428); ler por robô o Google Notícias e os Alertas, a Meta ou o TikTok; o YouTube só entra pela API, e o Google Acadêmico só à mão (l. 437).
- Pôr no Git dado pessoal de terceiros (inclusive em fixtures, Entradas, logs e exemplos), texto integral de fonte, chaves ou a saída do wiki local.
- Ler `legado/` ou abrir os Docs antes do Passo 3.
- Completar Falta por inferência; julgar a prática (D-019); deixar o juridico autorizar ou protocolar em nome de Vicente (D-020).
- Usar data como critério de novidade (l. 428); fazer bola de neve, que é da fase 2 (l. 438); dar por exaurida uma fonte que não informa o total (l. 592).
- Usar modelo menor antes do bloco 12; lançar agentes em paralelo; usar Workflow sem pedido explícito de Vicente.
- Ligar a camada 2 com habilidade não aprovada no bloco 9; deixar uma rotina gravar na versão principal.
- Escolher fornecedor de nuvem sem decisão (D-033); usar `claude -p`, Managed Agents, Agent SDK ou o lote da API sem decisão, porque mudam o plano.
- Relatar estimativa como medida ou o que não foi feito como feito (P96).
- Executar item [PROPOSTA] fora do que este brief e a D-034 cobrem; reabrir decisão vigente (registra-se o conflito: Parada (d)).
- Mudar os Anexos A e B; mudar a Fundação fora dos blocos 0 e 14.

## 6. Divergências com a Fundação e o que vai para a v0.3

**A. O que a v0.2.1 (bloco 0) leva ao texto.** As linhas sustentadas só pela D-031 e pela D-032, já registradas, valem como este brief diz até a v0.2.1; as que dependem da D-033 ou da D-034 ficam pendentes até o registro no bloco 0. No resto, vale a Fundação.

| O que muda | Linhas | Decisão |
|---|---|---|
| Precedência do roteiro e deste brief sobre o texto da Fundação, só nas linhas desta tabela e só até a v0.2.1; `AGENTS.md`, l. 3 | — | D-034 ou decisão própria (pendente) |
| Regra do campo-de-acao "não usa conteúdo com Falta jurídica aberta" lida como regra do que se publica, para o kit do piloto | `.claude/agents/campo-de-acao.md`, l. 30 | D-032, D-020 |
| Adaptadores além dos que o piloto pede, para as rotinas de CLB em geral | 430 | D-032 |
| Lugar da tabela código → nome fixado antes do Passo 4, porque o piloto cria códigos desde o bloco 7 | 406, 742 | D-032 |
| Ordem dos passos: um ciclo do piloto atravessa os Passos 1, 2 (o que falta), 4 (camada 1), 5 e a parte de fichas do 6, sem publicar; cada passo mantém o seu "pronto quando"; localização do trecho, validador e μ e λ nascem no Passo 1 | 130-131, 602, 660, 707 | D-032 |
| Rotinas e Actions já no piloto, procurando CLB em geral; as fichas das demais fontes saem da fase 2 | 363, 438, 505, 669, 674, 741; `AGENTS.md` | D-031, D-032 |
| Tratamento com IA também por rotina na fase 1, depois do teste e da aprovação da habilidade | 84, 363, 499, 506, 674 | D-032, D-027 |
| Saída de reserva: outra nuvem, com o GitHub como repositório, em vez de "rodar em sessão" | 393, 508, 814 | D-033 |
| Fim do "único bloqueio": a CLB está decidida, e as fontes são aprovadas com este brief | 662, 691, 807 | D-031 |
| O teto das rotinas passa ao piloto, dentro da D-023 | 511, 823 | D-032, D-023 |
| A D-012 se cumpre quando a rotina do piloto rodar o tratamento agendado | 497 | D-032 |
| O §8 fica só com o que trava, cada item com padrão, e ganha um bloco "só para publicar" (Lei 13.123, F-0003, licença). O §10 vira "insumos para reavaliar o plano", e cada pergunta diz aonde quer chegar | 801-831, 871-899 | D-034, D-032 |
| Kit usado como teste no fim do piloto, sem publicar (e a descrição da kit-fonte-primaria) | 670 | D-032 |
| Educação e wiki local antes do Passo 6, sem publicar | 520-531, 759-763 | D-032 |
| Fatos de 17/10 no §5.5 e no Anexo C: Actions gratuito em repositório público; agendamento de 5 min, em UTC, com desativação após 60 dias (fecha duas das quatro linhas do item F-08, as do agendamento e dos minutos em repositório público; o Flat Data, do GitHub Next, base do padrão da parada dos termos no bloco 10, segue não conferido); tarefa de até 6 h; os termos (reler o texto inteiro); rotinas com excedente medido, que corrige o "sem excedente" | 505-506; Anexo C | fatos do roteiro, seção 4 |
| Os [ABERTO] do orçamento, já defasados | 227, 351 | D-023 |
| O §9 com as D-031 a D-034; `AGENTS.md` ("[PROPOSTA] não é plano" lido com a D-034; rotinas no piloto) e `CLAUDE.md` (modelos da rodada B) | 832-870 | D-031 a D-034 |

**B. Leituras deste brief que a Fundação não fixa.** Cada uma *muda o plano* num ponto de execução: vale como [PROPOSTA] sob a Fundação, com a decisão que a sustentaria entre parênteses, só depois do registro no bloco 0, com a aprovação de Vicente; a v0.3 confirma ou corrige. O registro único em `esquemas/valores-provisorios.json` (D-034; l. 696); o layout das pastas, a pasta temporária do texto e o arquivo de tradução em `ambientes/traducao-consultas.json` (D-032; l. 100, 407, 426, 591, 723); a configuração das rotinas em `ambientes/rotinas.json` (D-032; l. 430, 497); a Fonte sem nome de pessoa no Git público (D-021; l. 597 e 615; `AGENTS.md`); a semana e a estimativa do orçamento, a medida das rotinas e a parada da conversa principal (D-023; l. 511); o relatório do dia em `trilhas/relatorios/` e o canal que o leva a Vicente (D-032; l. 505, 744); a ramificação única e permanente das rotinas (D-033; l. 396); os créditos de uso desligados nas rotinas (D-023; l. 511); o boletim escrito uma vez (D-032; l. 743).

**C. Insumos para reavaliar o planejamento (vão para a v0.3).** Nenhum trava a execução; cada um diz aonde se quer chegar e o que o piloto traz.
1. **Ritmo.** Aonde: o ciclo inteiro num prazo que Vicente aceite. Os blocos preveem de 40 a 60 chamadas de agente. Com a folga de 2× o maior lote (D-023) e os custos medidos na v0.2 (46 a 146 mil), cabem 2 a 3 agentes por semana: 8 a 12 semanas ou mais. É estimativa, e o piloto mede. O código escrito na conversa principal fica fora dessa conta.
2. **Rotinas para todas as CLB e 1 a 3 h de curadoria.** Aonde: abrir as rotinas a todas as CLB sem que a fila passe de uma semana de curadoria (l. 472). O piloto traz as Entradas por semana e por ambiente e as horas reais.
3. **Rotina com o harness inteiro e a principal protegida.** Aonde: uma rotina que carrega o `CLAUDE.md`, alcança os domínios das fontes e nunca grava na principal por regra, e não só por instrução. Hoje os commits da rotina saem com o usuário do GitHub conectado, que é o dono, e uma regra que essa conta contorna não barra o envio (oficial, https://code.claude.com/docs/en/routines; l. 396). A rotina de teste (10b) traz a resposta.
4. **Material do piloto fora do Git público.** Aonde: que o piloto não seja lido como publicação. Caminho levantado: `entrada/` e `acervo/` num repositório privado da conta Indalt, com dois custos já registrados. No plano gratuito, a revisão obrigatória só existe em repositório público (l. 396); o Actions privado tem 2.000 min/mês (oficial, https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-actions). Ajustar a D-021 é de Vicente; até lá vale a custódia (l. 483).
5. **Bola de neve.** Aonde: usar todo o desenvolvido (D-032) sem contrariar a fase 2 (l. 438, 674).
6. **Educação e ilustração sem habilidade própria.** Aonde: a Educação com harness próprio, o que muda o inventário de 14 habilidades (l. 690; §10, pergunta 14), e um dono para a ilustração (§5.8, l. 553; Passo 8), que fica fora deste ciclo.
7. **Divergência e fala de quem pratica.** Aonde: pares reais para o estado "inconsistente" (l. 772) e para a W ancorada. Não se inventa par.
8. **Lugar das rotinas (D-033).** Aonde: o GitHub como repositório e a execução onde couber o potencial. As candidatas estão no roteiro, seção 4, cada uma com nível e URL: Oracle Always Free, Cloudflare (R2 e Workers), Render Cron Jobs e AWS; para a IA fora da rotina, `claude -p` sem `--bare`, Managed Agents e o lote da API.
9. **Autoria nas fontes.** Aonde: a referência completa (l. 597) sem expor pessoa que não consentiu.
10. **Calibrações.** A escala de valências (Passo 5), o limiar e a normalização, a regra de μ e λ, o lote de máquina, os modelos e custos por habilidade, as horas reais e a cadência do boletim.
11. **Perguntas do §10** (1 a 3, 6 a 8, 10 a 14, 16 a 20 e 22) e o sentido de "ambiente" (l. 413). Na v0.2.1, cada uma passa a dizer aonde quer chegar (o texto está no mapa de decisões); o relatório do piloto lhes dá itens, ambientes, fichas e grafo reais.

## Trilha deste brief
- **Lido:** o roteiro inteiro; os seis mapas e o de hospedagem, como vieram no pedido; o brief da v0.2 (sumário e l. 1-102); na Fundação, as l. 411-439, 495-513, 584-598, 613-618, 664-682 e 689-746, mais `grep -n` de frases-chave (l. 84, 363, 396, 409, 426-428, 438, 472, 483, 497-512, 662, 691, 696, 807, 814, 823, 902, 906, 923); o checklist, l. 186-212; `trilhas/decisoes/D-030.json` a `D-032.json`; as listas de `scripts/`, `esquemas/`, `.claude/`, `testes/` e dos mapas; os argumentos dos scripts e `scripts/orcamento.py`, l. 1-38.
- **Fora:** a web (nenhum fato novo; os níveis são os dos mapas e do roteiro); `legado/`; os Anexos A e B; o corpo dos scripts e dos esquemas; as linhas da Fundação citadas só pelos mapas e pelo roteiro (por exemplo, l. 100, 116-117, 130-131, 522, 529, 547, 553, 576, 753, 761, 772, 784-788 e 818), que não foram relidas nesta rodada.
