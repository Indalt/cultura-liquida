# Checklist do caso-piloto (cajuína, teste da ferramenta inteira)

**Brief:** `trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md` (aprovado), com o roteiro `trilhas/2026-10-17_caminhos/caminhos.md`. Vale a Fundação, menos nas linhas da seção 6A do brief até a v0.2.1 (D-034).
**Histórico anterior:** `trilhas/2026-10-16_execucao-v0.2.md` (Fundação v0.2 e rodada de planejamento de 17/10).
**Orçamento (D-023; brief, seção 0):** 300 mil tokens por semana em agentes; semana de segunda a domingo, pela data do log. Conta antes de cada agente com `scripts/orcamento.py --teto 300000`.

## Conversa 1 — bloco 0, aberta em 17/10/2026 (sábado)
- **Autorização (D-028), fala original de Vicente:** "aprovo o roteiro e o brief de execuções; executar o bloco 0".
- **Leitura:** aprovação com os padrões das paradas (brief, bloco 0, parada (a)): confirma a D-033, registra a D-034, fixa as fontes do piloto do bloco 4 (BCR/IPHAN, Infoteca-e, BDTD e a Hemeroteca pela via humana) e faz o pedido do kit do bloco 11 com os critérios do brief.
- **Sessão principal:** `claude-opus-5-5`, esforço médio, sem ultracode (conferido).
- **Uso inicial em claude.ai/settings/usage:** não informado.
- **Retomada:** `git pull` sem novidade; árvore limpa em `368a295`; `Indalt/cultura-liquida` público, remote `origin`; `rodar_testes.py`: OK 27 · FALHA 0 · PENDENTE 9.

### Bloco 0 — Plano em dia

| Item | Estado | Consumo (tokens) | Modelo / esforço | Observação |
|---|---|---|---|---|
| 1 Log da rodada de planejamento | já feito | — | sessão principal | A linha completa já estava em `trilhas/logs/2026-10-17_curador.jsonl` (22:53, 1.920.145 tokens, 231 chamadas, com alcance), e os três `.jsonl` de 17/10 já estavam no Git desde `368a295`. Não se gravou de novo. |
| 2 D-033 e D-034 | feito | — | sessão principal | `trilhas/decisoes/D-033.json` e `D-034.json`, validados (`validar.py decisao`: PASSA). A D-034 traz as três partes: modo de trabalhar (essência de 17/10), valor provisório no alcance do brief e precedência do roteiro e do brief só na seção 6A até a v0.2.1; as partes 2 e 3 vieram da proposta dos agentes e entraram pela aprovação. |
| 3 Este checklist | feito | — | sessão principal | estado por bloco, tabela semanal de consumo e de horas |
| 4 Fundação v0.2.1 (redator) e verificação (auditor) | retirado (D-035) | — | — | Parou por orçamento em 17/10 (abaixo) e saiu do bloco em 18/10: durante a execução não se escreve versão nova. A seção 6A e o pedido ao redator foram para `trilhas/insumos-planejamento.md`. |
| 5 `AGENTS.md` e `CLAUDE.md` | feito | — | sessão principal | precedência até a v0.2.1 (l. 3); "[PROPOSTA] não é plano" lido com a D-034; D-033 e D-034; passo corrente e checklist novo; modelos da rodada B (Sonnet 5.5 alto, frontmatter no bloco 1); rotinas e Actions só no bloco 10 (D-032). |
| 6 `checar_fundacao.py` com D-031 a D-034 | feito | — | sessão principal | `DECISOES` até a D-034; `essencias.json` com os termos-chave das D-031 a D-034; caso da v0.1 passa a 42 ausências. Em 18/10, pela D-035, o script voltou a cobrar só até a D-030 no texto (o caso da v0.1 voltou a 38) e passa na v0.2 com 0 achados; `essencias.json` guarda os termos das D-031 a D-035 para a próxima versão (insumo 11). |
| 7 Roteiro e brief no Git, aprovados | feito | — | sessão principal | Já estavam no Git desde `368a295`; o cabeçalho dos dois passou de [PROPOSTA] a "aprovado por Vicente em 17/10/2026". |

### Parada por orçamento (caso b), antes do item 4
- Agentes com log nesta semana (segunda 12/10 a domingo 18/10): janela 1 (81.852 + 77.351), janela 2 (46.051), janela 3 (481.781), janela 4 (445.715), janela 5 (299.846) e rodada de planejamento (1.920.145) = **3.352.741 tokens**.
- `scripts/orcamento.py --teto 300000 --medidos <os 17 lotes> --estimativa 115000` → código 1, **PARAR**. Estimativa: redator na v0.2.1 ≈ 115 mil (maior medida do redator num grupo de seções; nenhuma medida da habilidade em correção de várias seções esparsas).
- A semana pela data do log é o valor provisório da seção 0 do brief, agora coberto pela D-034. Os lotes anteriores rodaram sob o brief da v0.2 (600 mil por janela), mas a regra do brief novo soma "cada agente já rodado na semana", sem exceção: pela leitura literal, a semana está fechada para agentes.
- **Retomada:** segunda-feira, 19/10/2026, semana nova (consumido 0). Conta prevista: redator ≈ 115 mil; auditor ≈ 110 mil (passada 2 da v0.2) → 225 mil, dentro de 300 mil; a folga depois do redator (185 mil) fica abaixo de 2 × 115 mil = 230 mil, então o auditor pode precisar esperar outra semana, ou o redator vem mais barato que a estimativa. A conta se refaz com a medida.
- **Insumo para reavaliar o plano (D-034), aonde se quer chegar:** com 300 mil por semana e a folga de 2× o maior lote, cabem 1 a 2 agentes por semana nos lotes de 100 mil ou mais. O brief prevê 40 a 60 chamadas (seção 6C, insumo 1). Vai à v0.3 com as medidas do piloto.

### Pedido ao redator para a v0.2.1 (guardado como insumo 2; não se executa pela D-035)
- Habilidade escrever-secao-fundacao; teto de 15 chamadas; entrada: brief, seção 6A (as linhas da tabela), D-031 a D-034 em `trilhas/decisoes/`, o mapa `mapa-decisoes-e-perguntas.json` (`mudancas_de_plano`, menos a do lugar do material, que fica na seção 6C) e os fatos de 17/10 do roteiro, seção 4, com o nível que lá têm.
- Validador: `checar_fundacao.py` com `--essencias` (os 4 achados atuais devem sumir) e `comparar_anexos.py`.
- Depois: auditor com verificar-fundacao, olhares das decisões e das contradições (teto de 15).

### Comentário de Vicente em 18/10 (D-035)
- **Fala original** de 18/10: no checklist da v0.2, seção "18/10/2026: o fio condutor" (commit b8394ea). **Essência como Vicente a formulou nesta conversa:** "Finalizar a v0.2 é construir e testar no piloto a ferramenta que ela descreve: coletar dados; recebê-los de diferentes formas; organizá-los no wiki conforme as diretrizes; criar os grafos 4D; criar propostas. Durante a execução não se escreve versão nova da Fundação: versões novas são da sessão de planejamento de melhorias. O que surgir das análises no meio da execução não se explora; anota-se para essa sessão. Uma tarefa por vez, terminada antes da próxima."
- **Essência devolvida e palavras conferidas;** resposta de Vicente, fala original, em resumo fiel por ponto: "uma tarefa" é um bloco do brief, e a pausa por orçamento retoma o mesmo bloco; medir horas e consumo é registro, desde o bloco 6; a 10a é tarefa, depois do bloco 9, e rodar sozinha depois de ligada é operação; "receber de diferentes formas" são as formas da fase 1 do §5.4 (coleta por programa, inclusive as rotinas; busca assistida; link ou documento que ele traz, que precisa funcionar no piloto; e-mail dos Alertas quando ele criar a conta), nenhum canal de outras pessoas; "criar propostas" é o campo de ação sob demanda (Passo 9); o arquivo `trilhas/insumos-planejamento.md` serve, com data, origem e aonde se quer chegar, por apontamento, e recebe a seção 6A, o pedido ao redator, o ritmo, os aprendizados do checklist da v0.2, a contribuição com tokens próprios (fase 2), a ideia do agente de melhorias e contribuições e a volta da cobrança no `checar_fundacao.py`; o resto do entendido está certo.
- **Registrado:** `trilhas/decisoes/D-035.json` (valida). Ajustes: quadro "Ajustes da D-035" no início do brief; tabela da seção 4 (blocos 0 e 14); ordem; bloco 0, item 4 retirado; bloco 5 com a entrada por link ou documento trazido por Vicente (§5.4, l. 449); bloco 6 com uma Entrada real por esse canal; 10a depois do bloco 9; bloco 14 sem v0.3; `AGENTS.md` (precedência até a próxima versão, D-035, passo corrente); `checar_fundacao.py` de volta à D-030; `trilhas/insumos-planejamento.md` com 11 entradas.

### Fechamento do bloco 0 (18/10/2026)
- **Pronto quando** (ajustado pela D-035): as decisões D-033 a D-035 validam; `checar_fundacao.py` passa na v0.2 (0 achados); Anexos A e B intactos; commit e push feitos. Sem agente neste bloco: consumo 0.
- **Próximo:** bloco 1 (harness e operação), quando Vicente autorizar. A semana de 12 a 18/10 está fechada para agentes; o bloco 1 usa o auditor, então começa na semana de 19/10.

## Conversa do cartão K-103 — 22/10/2026 (quinta)

- **Autorização de Vicente:** cartão K-103 (habilidade registrar-melhoria), pela retomada do brief; Opus 5.5, esforço médio; uso da conta informado: 29% no início.
- **Retomada:** modelo `claude-opus-5-5` conferido; `git pull` em dia (51ceee8), árvore limpa; quadro e estado do planejamento lidos; cartão movido para Fazendo e, no fim, para Concluído.
- **Feito:** `.claude/skills/registrar-melhoria/` 0.1.0 (SKILL.md e 5 casos em `exemplos/`); `esquemas/insumo.schema.json` (formato fixo: data, origem, insumo, aonde, rótulo, frente, cartão proposto, `sem_explorar: true`, nenhum campo a mais); `scripts/registrar_melhoria.py` (sem IA: valida, recusa dado pessoal, texto repetido, `|` ou quebra de linha e a lista fora de sincronia com o mapa; dá o número e grava a linha em `trilhas/insumos-planejamento.md` e na seção 6 do mapa); o fixture com e-mail fictício na lista de `procurar_dado_pessoal.py`.
- **Testes:** `rodar_testes.py` dá OK 32 · FALHA 0 · PENDENTE 9 (eram 27 OK; os 5 novos são da registrar-melhoria). A gravação real foi testada antes em cópias no scratchpad (uma linha a mais em cada arquivo, fim de linha preservado).
- **Primeiro uso real:** insumo 27 (o `curador.md` e o `executar-brief` ainda sem a registrar-melhoria; vai ao K-101, que versiona os dois).
- **Não feito:** verificação independente pelo auditor (nenhum agente nesta conversa); a ligação no `executar-brief` e no `curador.md`, que é do K-101.
- **Consumo:** 0 tokens de agentes.

## Conversa do cartão K-101 (bloco 1) — 22/10/2026 (quinta)

- **Autorização de Vicente:** cartão K-101 (bloco 1 do brief: harness e operação), retomando pelo quadro e parando nas paradas do brief; Opus 5.5, esforço médio; uso da conta: não informado (veio em branco, "__%").
- **Retomada:** modelo `claude-opus-5-5` conferido; `git pull` em dia (cd5e26e), árvore limpa; `Indalt/cultura-liquida` público; `rodar_testes.py`: OK 32 · FALHA 0 · PENDENTE 9; cartão movido para Fazendo e, no fim, para Concluído.

### Bloco 1 — Harness e operação

| Item | Estado | Consumo (tokens) | Modelo / esforço | Observação |
|---|---|---|---|---|
| `curador.md` 0.1.1 | feito | — | sessão principal | Agent com avaliador, arquivista e campo-de-acao; retomada pelo quadro e pelo estado do planejamento; relatório sem aprovação de rotina; Vicente só por cartão de conflito ou de Falta jurídica a liberar; Agent só com os tipos de `.claude/agents/` (insumo 7); `registrar-melhoria` (insumo 27); regras até a D-039, com a regra-mãe da D-038 |
| avaliador, arquivista, campo-de-acao 0.1.1 | feito | — | sessão principal | `claude-sonnet-5-5`, esforço alto, deixa de ser marcador; avaliador com a saída da quarentena pela regra versionada (A-05) |
| `extrair-evidencia` 0.1.1 | feito | — | sessão principal | Falta abaixo do limiar sem cota humana (A-06); quarentena pela regra (A-05); valências sem peso institucional (D-039); marca de aviso, saúde ou política ao auditor (D-038) |
| `consulta` e `ficha-de-acesso` 0.1.1 | feito | — | sessão principal | bola de neve só na fase 2; novidade por ID; entrada pelo Anexo E e por `ambientes/`; `robots` e `cobertura` nos três exemplos, com "não conferido" onde faltava dado |
| `conferir-fato` 0.1.1 | feito | — | sessão principal | chamada reservada para validar, com `resposta`; citação por `curl` e `grep -n`; WebFetch só para localizar (insumo 17) |
| `executar-brief` 0.1.1 | feito | — | sessão principal | retomada pelo quadro; `--teto 300000` por semana; teto contado como o harness conta; log por arquivo; tokens do retorno do Agent (insumo 5); relatório sem aprovação (A-02); `registrar-melhoria` |
| `esquemas/log.schema.json` 0.1.1 e `registrar_log.py` | feito | — | sessão principal | alcance obrigatório em toda linha com id e em script, rotina e pessoa; id EX-nnnn (prefixo provisório; insumo 28); Ambientes, Consultas, Recortes e saídas; `automatica` e `versao_regra` (D-038); tokens null com motivo para script, rotina, pessoa e workflow. Logs antigos válidos nos dois validadores. Primeiro id emitido: EX-0001 (log do auditor) |
| Validador | feito | — | sessão principal | 8 casos novos no `executar-brief`, entre eles log sem alcance e log de workflow sem motivo, que reprovam; `rodar_testes.py`: OK 40 · FALHA 0 · PENDENTE 9 |
| `testes/relatorio-rodada-A.md` | feito | — | sessão principal | regenerado com `--rodada A` (OK 40; o caso da v0.1 diz 38 ausências) |
| Auditor, olhar mecânico (§5.3, §6) | feito | 73.464 (18 chamadas) | Sonnet 5.5 alto | Todos os itens gravados, sem divergência do pedido. Achados em `trilhas/2026-10-22_K-101/achados-auditor.json`: A-001 (citação l. 584 → 585) e A-003 (campo `saidas` da l. 593) corrigidos; A-002 (l. 130 × A-06) já está em `proxima-versao.md`, V-06; A-004 (prefixo EX) virou o insumo 28, para o K-104. O agente passou do teto de 15 chamadas (18 pelo retorno), por uma validação refeita. Conta antes: `orcamento.py --teto 300000 --estimativa 110000` → pode |

- **Pronto quando:** `rodar_testes.py` sem FALHA (OK 40 · FALHA 0 · PENDENTE 9); os casos novos reprovam como esperado; as versões 0.1.1 têm Histórico; o curador e o `executar-brief` começam pelo quadro. **Fica para a abertura da próxima conversa (K-104):** conferir que a ferramenta Agent do curador lista avaliador, arquivista e campo-de-acao, porque agente editado só carrega em conversa nova.
- **Insumos:** 28 novo (prefixo do id da Execução, para o K-104); 27 atendido pelo `curador.md` e pelo `executar-brief` 0.1.1 (fica aberto até o planejamento fechá-lo).
- **Não feito:** nenhuma parada; nada "não conferido" novo além dos dois `robots` e da `cobertura` da Hemeroteca nos exemplos.
- **Consumo:** 73.464 tokens de agentes (auditor).

## Conversa do cartão K-104 (bloco 2) — 22/10/2026 (quinta)

- **Autorização de Vicente, fala original:** "Autorizo o cartão K-104 (Bloco 2 do brief de execuções: contratos do §6 e valores provisórios). Retome pelo quadro, mova o cartão e pare nas paradas do brief; na parada (c), vale o padrão: a tabela código → nome numa pasta da minha máquina, fora da pasta versionada. Opus 5.5, esforço médio. Uso atual: 34%."
- **Uso da conta no início:** 34%.
- **Retomada:** modelo `claude-opus-5-5` conferido; `git pull` em dia (fc0c5c3), árvore limpa; `Indalt/cultura-liquida` público; `rodar_testes.py`: OK 40 · FALHA 0 · PENDENTE 9; cartão movido para Fazendo. A ferramenta Agent desta conversa lista avaliador, arquivista e campo-de-acao (pendência do K-101 conferida).
- **Parada (c) do bloco 2:** não acontece; vale o padrão dado por Vicente na autorização.

### Bloco 2 — Contratos do §6 e valores provisórios

| Item | Estado | Consumo (tokens) | Modelo / esforço | Observação |
|---|---|---|---|---|
| Registro de valores provisórios | feito | — | sessão principal | `esquemas/valores-provisorios.json` (19 valores) com `valores-provisorios.schema.json`. A estrutura fixada pela D-038 (eixos 1 a 4, selo, versão da regra, quem propõe não aprova) fica separada dos valores; cada valor diz a linha da Fundação, a base, quem usa e quando se calibra. Esquemas leem por `$ref` (resolvido em `_comum.carregar_esquema`), scripts por `carregar_valores()` (`registrar_log.py`, `orcamento.py`) |
| Contratos do §6 | feito | — | sessão principal | 18 contratos (Termo, Proposição, Evidência, Fonte, Ambiente, Consulta, Recorte, Entrada, Trecho, CLB situada, Elemento, Insumo como `insumo-x`, Processo, Compreensão local, Transformação, Aresta, Lugar, Pessoa), mais `comum`, `ficha-acesso` e `estado-consulta`; proteção, origem, eixos, retirada (l. 585) e a marca de aviso, saúde ou política |
| Exemplos | feito | — | sessão principal | `esquemas/exemplos/`: um que passa e um que reprova por contrato, mais a retirada e o registro (40 casos). Com dado real (mapa de 17/10): Termo, Proposição, Fonte, Ambiente, Recorte, Trecho, Lugar; os demais levam "exemplo de esquema". IDs dos exemplos na faixa 900000-999999 |
| Casos do rastreador | feito | — | sessão principal | ficha-de-acesso e consulta 0.1.2: os 4 casos reais passam; reprovam a ficha com 403 e "aceito" e o total visto acima do informado sem explicação (regra entre campos de `validar.py`) |
| Parada (c) | padrão | — | — | tabela código → nome numa pasta da máquina de Vicente, fora da pasta versionada: caminho padrão `C:/Antigravity/Cultura Liquida - privado/pessoas/` ou a variável `CL_PRIVADO` (registro: `tabela_codigo_nome`) |
| Auditor, olhar mecânico e lote C4 | feito | 143.833 (20 chamadas) | Sonnet 5.5 alto | Conta antes: `orcamento.py --medidos 73464 --estimativa 73464` → pode. 5 achados (`trilhas/2026-10-22_K-104/achados-auditor.json`), os 5 corrigidos: retirada sem o conteúdo; proteção obrigatória na Pessoa e permitida em todos; "não calculado" fora do eixo 4 (estado ausente até o cálculo); `estado_detalhe` na Aresta; estados da busca no registro. C4 (`conferencia-C4.json`): SKOS oficial (w3.org); TBX oficial pelo tbxinfo; ISO 30042 não conferida (403). O agente conta 24 chamadas pelos pedidos HTTP; o retorno diz 20. Ele não validou os JSON (heredoc); o curador gravou e validou: PASSA |

- **Pronto quando:** cada esquema com um exemplo que passa e um que reprova; os 4 casos do rastreador fora de PENDENTE; um caso que reprova por habilidade; `rodar_testes.py`: OK 86 · FALHA 0 · PENDENTE 5 (os 5 pendentes são das habilidades dos blocos 7 e 8, sem exemplo do piloto ainda).
- **Insumos novos:** 29 (agente sem Write não valida JSON por heredoc; K-111), 30 (Termo sem a língua das designações, TBX langSec; K-106), 31 (User-Agent do projeto; K-107).
- **Não conferido:** a ISO 30042 na página da ISO (403); a equivalência campo a campo do Termo com TBX e SKOS; as correções A-001 a A-005 não passaram por segunda leitura independente.
- **Consumo:** 143.833 tokens de agentes (auditor).

## Conversa do cartão K-105 (bloco 3) — 22/10/2026 (quinta)

- **Autorização de Vicente, fala original:** "Autorizo o cartão K-105 (Bloco 3 do brief de execuções: scripts do núcleo). Retome pelo quadro e mova o cartão. Orçamento desta semana (autorização minha; o K-005 calibra depois): o limite é o uso da conta — pare com o estado salvo antes de 50%; o teto provisório de 300 mil tokens de agentes por semana não se aplica nesta semana; o teto de chamadas por agente continua. Na passada do auditor, inclua uma conferência rápida das correções A-001 a A-005 do K-104; o auditor devolve o JSON e o curador valida (insumo 29). Opus 5.5, esforço médio. Uso atual: 37%."
- **Uso da conta no início:** 37%. Parada (b) desta semana: antes de 50% do uso da conta, com o estado salvo; o `orcamento.py --teto 300000` não se aplica nesta semana (autorização de Vicente).
- **Retomada:** modelo `claude-opus-5-5` conferido; `git pull` em dia (dcff3b0), árvore limpa; `Indalt/cultura-liquida` público; `rodar_testes.py`: OK 86 · FALHA 0 · PENDENTE 5; cartão movido para Fazendo.

### Bloco 3 — Scripts do núcleo

| Item | Estado | Consumo (tokens) | Modelo / esforço | Observação |
|---|---|---|---|---|
| Juridico, normas da triagem fixa (lote C5) | feito | 67.580 (12 chamadas) | Sonnet 5.5 alto | Sem conta do `orcamento.py` nesta semana (autorização de Vicente). 18 itens, 17 oficiais (planalto.gov.br) e a Portaria SVS/MS 344/1998 não conferida (503 e 404). Pistas corrigidas: o art. 66 da Lei 11.343 nomeia a Portaria; o art. 2º, IX, da Lei 13.123 inclui fontes secundárias. O agente não validou (heredoc); o curador gravou com Write e validou: PASSA (`trilhas/2026-10-22_K-105/conferencia-C5.json`) |
| `localizar_trecho.py` | feito | — | sessão principal | normalizacao-0.1 do registro, SHA-256 do texto lido, seletor W3C (exato, antes, depois), localizador com página do PDF (pypdf), Falta abaixo do limiar e no PDF sem texto, transcrição por IA marcada, Wayback (`id_`), pasta temporária recusada dentro do repositório; `conferir` relê e compara hash e grau |
| `validar_acervo.py` e pre-commit | feito | — | sessão principal | acervo-0.2: esquema por prefixo, colisão e faixa de ID, referências, Evidência → Trecho → Fonte, Proposição com Evidência, Termo atestado com abonação localizada, OCR fora das variantes, W pela voz de quem pratica, dado pessoal, frase da ficha com [PR-nnnn] ao fim, deriva_de sem ciclo. Gancho em `.githooks/pre-commit` (`git config core.hooksPath .githooks`), testado reprovando e passando |
| `triagem_fixa.py` | feito | — | sessão principal | triagem-fixa-0.2 em `esquemas/triagem-fixa.json`: seis casos com a norma do C5 e o guia; norma incompleta ou "não conferido" não gera Falta |
| `calcular_mu_lambda.py` | feito | — | sessão principal | mu-lambda-0.1: linhagens por união de deriva_de, μ, λ, Dc, Dct, estado e quadrante intermediário; `--conferir`, `--gravar`; gera `grafo/` (nós, arestas, X×Y com "não observada", Z); W não captada = paracompleto |
| `gerar_termo.py` | feito | — | sessão principal | termo-0.1: booleanos, glossário do acervo inteiro e a Consulta nova proposta (válida no contrato) |
| `sortear_amostra.py` | feito | — | sessão principal | amostra-0.2: semente registrada, 15 itens do registro, universo sem o que já esteve em amostra, marcados lidos todos fora da amostra; `--conferir` |
| `semear_ambientes.py` | feito | — | sessão principal | 69 ambientes em `ambientes/` (AM-0001 a AM-0069), "proposto", Execução EX-0006; a contagem bate com o Anexo E (69) |
| Auditor, verificador de outro harness e K-104 | feito | 159.897 (19 chamadas) | Sonnet 5.5 alto | 18 achados (`trilhas/2026-10-22_K-105/achados-auditor.json`): 13 corrigidos no cartão com 6 casos novos; A-008, A-009, A-010 e A-015 são regra a decidir (insumos 34 e 36); A-018 explicado (o `registrar_melhoria.py` do curador). K-104: A-002, A-003 e A-005 corrigidos; A-001 persistia na Pessoa e foi corrigido agora; A-004 conferido pelo curador (só na descrição). O curador validou o JSON: PASSA |

- **Pronto quando:** cada script com caso que passa e que reprova (`testes/nucleo/casos.json`, 32 casos); `procurar_dado_pessoal.py` sem achado; os 69 ambientes validam e batem com o Anexo E; o pre-commit roda (bloqueou um registro inválido de teste e passou o acervo real). `rodar_testes.py`: OK 120 · FALHA 0 · PENDENTE 5.
- **Insumos novos:** 32 (listas e normas da triagem fixa; K-109), 33 (papéis da W e frase da ficha; K-110), 34 (quais Evidências contam em μ e λ; K-005), 35 (pre-commit em cada cópia; K-111), 36 (limiar do trecho e linhagem nos dois lados; K-005).
- **Não conferido:** a Portaria SVS/MS 344/1998; imagem e voz de adulto (CF art. 5º, X; Código Civil art. 20) e o ECA art. 2º; os scripts que leem rede (Wayback e URL) não rodaram contra fonte real, só contra arquivo local; as correções dos achados do K-105 não passaram por nova leitura independente.
- **Consumo:** 227.477 tokens de agentes (juridico e auditor).

## Consumo semanal de agentes (D-023)

| Semana | Agente / lote | Tokens | Chamadas | Acumulado da semana |
|---|---|---|---|---|
| 12–18/10 | lotes da v0.2 e da rodada de planejamento (ver acima) | 3.352.741 | — | 3.352.741 |
| 12–18/10 | bloco 0, conversa 1 | 0 (nenhum agente) | — | 3.352.741 |
| 19–25/10 | K-103, desenvolvimento (os agentes do K-001 e do K-003 estão no estado do planejamento) | 0 (nenhum agente) | — | 0 |
| 19–25/10 | K-101, auditor (olhar mecânico do harness) | 73.464 | 18 | 73.464 |
| 19–25/10 | K-104, auditor (contratos do §6 e lote C4) | 143.833 | 20 | 217.297 |
| 19–25/10 | K-105, juridico (lote C5) | 67.580 | 12 | 284.877 |
| 19–25/10 | K-105, auditor (scripts do núcleo e K-104) | 159.897 | 19 | 444.774 (teto de 300 mil suspenso nesta semana por Vicente) |

## Horas de Vicente e uso da conta (bloco 13; medição desde o bloco 6)

| Semana | Revisões (h) | Juízo de itens (h) | Busca assistida (h) | Uso da conta antes / depois | Minutos do Actions |
|---|---|---|---|---|---|
| 12–18/10 | não informado | — | — | não informado | — |
