# Relatório do piloto (K-116)

**Para:** a reunião do K-004, que abre a sessão de planejamento de melhorias (D-046).
**Cartão:** K-116, bloco 14 do brief de execuções (`trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md`, l. 408-414), na parte "Antes da v0.3" (l. 412). Pela D-035, este texto **não é** a v0.3 nem seção da Fundação: durante a execução não se escreve versão nova, que é da sessão de planejamento, e se faz uma tarefa por vez. Pela D-056, fecha a entrega do piloto, depois do kit (K-114).
**Escrito por:** redator, em 14/11/2026. **Conferido** pelo auditor, com os 8 achados aplicados (seção "Conferência").

**De onde vêm os números.** Quase todos vêm de `trilhas/2026-11-14_relatorio-piloto/dados.json`, gerado por `scripts/relatorio_piloto.py` (versão relatorio-piloto-0.2, sem IA), no instantâneo de 14/11/2026, 10h53 (`logs.gerado_em`). Neste texto, "dados.json, `chave`" aponta o lugar do número no arquivo. Os outros números vêm de um arquivo citado com caminho e linha. Onde o dado não existe, o texto diz **não medido** e trata a lacuna como **Falta**: uma lacuna dita, que não se completa por inferência.

**Regras da conta do script** (docstring de `scripts/relatorio_piloto.py`):
- as linhas do agente "curador" (executar-brief, registrar-decisao, planejamento) agregam os agentes da conversa, que já têm linha própria: desde a 0.2, ficam fora da soma (seção 5.1);
- tokens e chamadas de agente só das linhas de log que não vêm do hook `SubagentStop` (o hook grava só uma linha mínima de segurança);
- os registros de teste de modelo (com "[teste de modelo]" na `entrada_ref`, D-051) ficam à parte, fora da produção;
- os pp por frente são a soma da coluna pp da tabela "Semana da conta" do checklist; "não lido" e "—" não somam.

---

## 1. O que o piloto foi e o que se olhou

**O piloto.** O caso-piloto é a cajuína (D-031), registrada como CL-0001. "CL" é o código de uma Cultura Líquida Brasileira (CLB): uma bebida e tudo o que a faz existir. O trabalho começou pelo caju, o insumo. Pela D-032, o piloto é teste da ferramenta inteira, usada por completo em cada conversa e nas rotinas, e não é publicação.

**Período dos registros.** Os logs vão de 16/10/2026 a 14/11/2026 (dados.json, `logs.primeira_data` e `logs.ultima_data`). Os dias 16 e 17/10 são os da escrita da v0.2 da Fundação; o script não separa esses registros do piloto.

**Alcance** (D-030: cada parte fala só do que conseguiu olhar, nunca de tudo o que se conhece, como a ciência preconiza). Pelo próprio script (dados.json, `alcance`):
- **Olhado:** `acervo/` inteiro (contagem de arquivos; Proposições, Evidências, Trechos, CLB, Termos e Fontes lidos por inteiro); `entrada/EN-*.json` e `ambientes/pegadas/*.jsonl` (contagem); todas as linhas de `trilhas/logs/*.jsonl`; as tabelas "Semana da conta" e "Horas de Vicente" do checklist do piloto (`trilhas/2026-10-17_execucao-piloto.md`).
- **Fora:** o bruto, que fica fora do Git (D-045), e o wiki local; os tokens da conversa principal (não há registro por linha, só os pp da tabela); o consumo do Gemini, que tem contador próprio (K-125).

Este relatório olhou também: `scripts/relatorio_dia.py` (rodado em 14/11), `ambientes/rotinas.json`, `testes/relatorio-modelos.md`, `trilhas/planejamento/quadro.md`, `trilhas/insumos-planejamento.md`, as D-052, D-054, D-055 e D-056 em `trilhas/decisoes/`, e faixas da Fundação (l. 440-483, 670-680, 871-930) e do brief (l. 399-477).

---

## 2. Itens

### 2.1 Entradas e pegadas
Uma **Entrada** é um item coletado que segue na pré-triagem por regra, sem IA (D-045). Uma **pegada** é o registro compacto de todo item visto, siga ele ou não; fica um arquivo por Recorte em `ambientes/pegadas/`.

| Medida | Número | Fonte |
|---|---|---|
| Entradas, total | 2.578 | dados.json, `entradas.total` |
| por estado: bruto / extraído / quarentena | 2.544 / 28 / 6 | `entradas.por_estado` |
| por pré-triagem: segue / sem o campo | 2.574 / 4 | `entradas.por_pretriagem` |
| por mês de entrada: out. / nov. 2026 | 1.006 / 1.572 | `entradas.por_mes_de_entrada` |
| por ambiente: AM-0022 / AM-0021 / AM-0029 / AM-0061 | 1.531 / 803 / 220 / 24 | `entradas.por_ambiente` |
| Entradas sem cópia no Wayback | 2.566 | `relatorio_dia.py`, 14/11 |
| Pegadas: arquivos / itens vistos | 50 / 22.872 | `pegadas` |
| Pegadas por pré-triagem: segue / fora do escopo pela regra | 16.717 / 6.155 | `relatorio_dia.py`, 14/11 |
| Tamanho da guarda (alarme acima de 20 mil arquivos ou 200 MB) | 5.860 arquivos, 20,9 MB | `relatorio_dia.py`, 14/11 |

Os quatro ambientes das Entradas são a Oasisbr (AM-0022), a BDTD (AM-0021), a Infoteca-e da Embrapa (AM-0029) e o BCR do IPHAN (AM-0061) (nomes em `ambientes/AM-*.json`).

### 2.2 Evidências e Trechos
Uma **Evidência** é o que uma fonte diz, com o trecho literal. O **Trecho localizado** é o trecho achado de novo na fonte por script (D-041).

| Medida | Número | Fonte |
|---|---|---|
| Evidências | 520 | `evidencias.total` |
| por voz: autor / instituição / pessoa citada em fala direta | 272 / 160 / 88 | `evidencias.por_tipo_de_voz` |
| Trechos, todos localizados | 520 | `trechos.por_estado` |

### 2.3 Proposições
Uma **Proposição** é uma afirmação sobre a prática, sustentada por Evidências. O estado vem de dois graus da lógica paraconsistente do grafo: **μ**, o grau de evidência a favor, e **λ**, o grau de evidência contrária. Pela regra, contradições convivem e não se apagam (princípio 3). "Paracompleto" é o estado em que falta evidência dos dois lados.

| Medida | Número | Fonte |
|---|---|---|
| Proposições | 427 | `proposicoes.total` |
| por estado: intermediário / verdadeiro / paracompleto | 371 / 52 / 4 | `proposicoes.por_estado` |
| que sustentam aviso, saúde ou política | 69 | `proposicoes.sustentam_aviso_saude_politica` |
| com Evidência fora da conta (divergente ou não localizada, D-041) | 3 | `proposicoes.com_evidencia_fora_da_conta` |
| com tensão interna sinalizada (D-041) | 2 | `proposicoes.com_tensao_interna` |
| versão da regra de μ e λ | mu-lambda-0.2, em todas as 427 | `proposicoes.versao_regra` |

**Por atributo** (`proposicoes.por_atributo`): processo e modo de fazer 66; transmissão 49; uso e consumo 48; significados 38; utensílio 26; quem pratica 25; insumo 24; recipiente 23; época 23; reconhecimento 22; lugar 22; mudança 20; risco 18; nomes e variantes 11; salvaguarda 9; composição 3.

### 2.4 CLB, Termos e Fontes
| Medida | Número | Fonte |
|---|---|---|
| CLB: total / ficha montada / candidata | 4 / 1 / 3 | `clb` |
| Termos: total / atestado / candidato | 5 / 2 / 3 | `termos` |
| Fontes: total, todas do tipo "escrito publicado, de arquivo ou oficial" | 34 | `fontes` |

A CLB com ficha é a CL-0001. As três candidatas são CLB de outro termo (D-039), na lista de baixa prioridade do K-207.

A pasta `acervo/termos` tem 6 arquivos (`acervo_arquivos.termos`): os 5 Termos e o `glossario.md`, gerado por `scripts/gerar_termo.py` (conferência do auditor).

### 2.5 Faltas
| Medida | Número | Fonte |
|---|---|---|
| Faltas | 44 | `faltas.total` |
| por tipo: outro / impedimento jurídico / compreensão local não captada / fonte inacessível | 32 / 6 / 5 / 1 | `faltas.por_tipo` |
| jurídicas por subtipo: direito autoral / conhecimento tradicional / LGPD / outro | 2 / 2 / 1 / 1 | `faltas.por_subtipo_juridico` |
| por `vale_para`: publicar / agora / sem o campo | 4 / 2 / 38 | `faltas.por_vale_para` |
| caminho de liberação: não iniciado / em andamento / sem o campo | 5 / 1 / 38 | `faltas.caminho_de_liberacao_estado` |

O campo `vale_para` diz se a Falta barra o trabalho agora ou só a publicação (D-042). Só 6 Faltas o têm, e são exatamente as 6 jurídicas (conferência do auditor): F-0004 e F-0034 valem agora; F-0024, F-0025, F-0032 e F-0033, só para publicar.

---

## 3. Ambientes, Recortes e rotinas

**Ambiente** é um lugar de busca (um repositório, uma hemeroteca, uma API). **Recorte** é um corte de busca num ambiente, com uma Consulta e um período, que guarda o total que a fonte informa e o total que se viu.

### 3.1 Ambientes
| Medida | Número | Fonte |
|---|---|---|
| Ambientes | 69 | `ambientes.total` |
| estado de monitoramento: "não iniciado" | 69 | `ambientes.por_estado_monitoramento` |
| estado de escavação: "proposto" | 69 | `ambientes.por_estado_escavacao` |
| por tipo: outro / documento oficial / hemeroteca / repositório de teses / periódico científico / rede social / blog | 52 / 7 / 3 / 2 / 2 / 2 / 1 | `ambientes.por_tipo` |

**Dado desatualizado (a apontar como insumo, sem corrigir aqui).** Os 69 ambientes aparecem como "não iniciado" e "proposto", mas as rotinas rodam: `ambientes/rotinas.json` tem 4 ambientes ligados (AM-0021, AM-0022, AM-0029 e AM-0061), as Entradas vêm desses 4 (seção 2.1) e há Recortes em 5 ambientes (seção 3.2). O estado nas fichas dos ambientes não acompanhou o trabalho.

### 3.2 Recortes
| Medida | Número | Fonte |
|---|---|---|
| Recortes | 52 | `recortes.total` |
| por estado: percorrido pela busca / aberto / interrompido por teto | 34 / 12 / 6 | `recortes.por_estado` |
| por ambiente: AM-0022 / AM-0021 / AM-0029 / AM-0061 / AM-0026 | 24 / 19 / 6 / 2 / 1 | `recortes.por_ambiente` |
| soma do total informado pelas fontes | 418.775 | `recortes.soma_total_informado` |
| soma do total visto | 383.457 | `recortes.soma_total_visto` |
| Recortes sem total informado | 1 | `recortes.sem_total_informado` |
| Consultas | 8 | `consultas` |
| Vácuos de busca (ambiente × Consulta não percorrido ou interrompido) | 35 | `relatorio_dia.py`, 14/11 |

### 3.3 A rotina diária sem IA
A configuração (`ambientes/rotinas.json`, versão rotinas-0.1) tem 6 ambientes:
- **ligados:** BDTD (AM-0021), Oasisbr (AM-0022), Infoteca-e (AM-0029) e BCR (AM-0061);
- **desligados, com o motivo na configuração:** Hemeroteca Digital Brasileira (AM-0001), "via humana: 403 com desafio do Cloudflare" (D-044; o teste de 24/10 não passou); OpenAlex (AM-0026), busca anônima com respostas 429 e 503, sem chave pela D-049.

No relatório do dia de 14/11 (`relatorio_dia.py`): 0 ambiente rodado no dia; 0 Entrada nova; 22 links quebrados no total; 1 proposta das rotinas à espera de junção (a ramificação `claude/rotina-ia-2026-11-13`, "portão não rodado").

**O que não se automatizou (D-052).** Os 63 ambientes fora de `rotinas.json` não são consultados pela rotina. A D-052 manda que cada um fique com o motivo na ficha e entre num insumo (passo para melhoria, D-049). A lista por ambiente e por motivo não foi medida neste relatório: o script não a calcula. A coluna `ambientes.por_via` de dados.json mostra a variedade das vias (APIs abertas, cadastro, assinatura, 403, robots.txt), mas não é a lista dos motivos.

---

## 4. Fichas, Educação e grafo

| Medida | Número | Fonte |
|---|---|---|
| arquivos em `acervo/fichas` | 2 | `acervo_arquivos.fichas` |
| ficha da CL-0001 | `acervo/fichas/CL-0001.md` | `gatilho_fase2_dados.1_caso_piloto_do_bruto_a_ficha` |
| camada Educação | `acervo/fichas/educacao/CL-0001.md` | `fichas` |
| Compreensões locais (W) em `acervo/` | 10 arquivos | `acervo_arquivos.compreensoes-locais` |
| Grafo: nós / arestas | 72 / 24 | `grafo` |
| Arestas por estado: intermediário / verdadeiro / paracompleto | 17 / 6 / 1 | `grafo.arestas_por_estado` |
| versão da regra do grafo | mu-lambda-0.2 | `grafo.versao_regra` |

O grafo é o grafo 4D: X é o insumo, Y o processo, Z o tempo e W a compreensão local (D-018): a prática comum da região, episteme própria mas traduzível, tratada como dimensão; o não captado é Falta; o saber comum muda de forma autóctone ou por interação. O script não achou campo de tipo nos 72 nós (`grafo.nos_por_tipo`: "(sem campo)" 72): a divisão dos nós por eixo **não foi medida**.

O kit de fonte primária (K-114) é um rascunho em `campo_de_acao/`, sem publicar (seção 8).

---

## 5. Custos

### 5.1 Tokens e chamadas de agentes, produção
Fonte: dados.json, `logs.producao_por_agente_habilidade`. Total de produção: **6.912.130 tokens** e **1.130 chamadas** (`logs.producao_total_tokens`, `logs.producao_total_chamadas`). Linhas de log lidas: 327 (curador 135, hook 119, script 68, pessoa 5; `logs.por_fonte_do_registro`).

**A regra do script mudou na 0.2.** A primeira versão deste relatório dava 14.753.953 tokens e 2.306 chamadas: **somava em dobro**. As linhas do agente "curador" nos logs medem o consumo dos agentes lançados na conversa, o mesmo da coluna "Tokens de agentes" do checklist; não medem a conversa principal. Esses agentes já têm linha própria. Provas do auditor: o K-109 em 29/10 (1.064.272 tokens e 166 chamadas, a soma exata de 10 linhas de agentes do dia) e o registrar-decisao de 05/11 (401.790 tokens e 65 chamadas, a soma de 5 linhas do auditor). Na 0.2, as linhas do curador saem da soma e ficam em `logs.agregados_do_curador_nao_somados` (8.058.244 tokens, `logs.agregados_do_curador_total_tokens`).

**A produção é um piso, não o total exato.** Há consumos registrados na linha do curador que podem não ter linha própria de agente: o workflow de 17/10 (1.920.145 tokens), o K-113 (561.185, a rotina na nuvem) e parte do K-112 (55.558) (ressalva do auditor). O que não tiver linha própria ficou fora dos 6.912.130.

| Agente / habilidade | Execuções | Tokens | Chamadas | Modelo |
|---|---|---|---|---|
| auditor / conferir-fato | 20 | 1.432.808 | 242 | Sonnet 5.5 |
| avaliador / extrair-evidencia | 7 | 1.212.590 | 155 | Sonnet 5.5 |
| auditor / verificar-fundacao | 10 | 1.080.247 | 158 | Sonnet 5.5 |
| redator / escrever-secao-fundacao | 11 | 895.134 | 182 | Opus 5.5 |
| juridico / triagem-juridica | 5 | 361.104 | 67 | Sonnet 5.5 |
| juridico / guia-de-liberacao | 3 | 278.283 | 47 | Sonnet 5.5 |
| rastreador / ficha-de-acesso | 3 | 273.890 | 36 | Sonnet 5.5 |
| arquivista / registrar-termo | 3 | 149.782 | 32 | Sonnet 5.5 |
| juridico / conferir-fato | 2 | 147.848 | 40 | Sonnet 5.5 |
| juridico / conferir-fato + triagem-juridica | 1 | 145.933 | 15 | Sonnet 5.5 |
| juridico / triagem-juridica e guia-de-liberacao | 1 | 132.441 | 21 | Sonnet 5.5 |
| juridico / conferir-fato e triagem-juridica | 1 | 130.428 | 20 | Sonnet 5.5 |
| auditor / verificar-fundacao + conferir-fato | 1 | 112.866 | 18 | Sonnet 5.5 |
| arquivista / montar-ficha | 1 | 111.618 | 18 | Sonnet 5.5 |
| arquivista / gerar-grafo | 1 | 104.796 | 15 | Sonnet 5.5 |
| campo-de-acao / kit-fonte-primaria | 1 | 103.960 | 14 | Sonnet 5.5 |
| redator / escrever-relatorio-piloto (a primeira versão deste relatório) | 1 | 103.555 | 18 | Opus 5.5 |
| juridico / n/a | 1 | 82.949 | 24 | Sonnet 5.5 |
| rastreador / consulta | 1 | 51.898 | 8 | Sonnet 5.5 |

**Agregados do curador, fora da soma** (`logs.agregados_do_curador_nao_somados`):

| Linha do curador | Execuções | Tokens | Chamadas |
|---|---|---|---|
| executar-brief | 14 | 6.859.879 | 1.011 |
| registrar-decisao | 4 | 716.661 | 130 |
| planejamento de melhorias | 2 | 481.704 | 71 |

O juridico aparece com cinco nomes de habilidade para combinações parecidas: é como os logs gravaram.

### 5.2 Teste de modelo, à parte
Fonte: dados.json, `logs.teste_de_modelo_por_agente_habilidade`. Total: **2.256.949 tokens** (`logs.teste_total_tokens`). Por família (`logs.teste_tokens_por_familia`): **Claude 1.413.955; Gemini 842.994**. No log, o token do Gemini é a soma de entrada e saída que a API informa; o do Claude é o que o Agent informa. As linhas de 0 token (as provas do Gemini que não rodaram, como a do argon) não contam como execução.

| Agente / habilidade | Execuções | Tokens | Chamadas | Modelos |
|---|---|---|---|---|
| avaliador / extrair-evidencia | 6 | 962.624 | 133 | Haiku 5.5, gemini-4-hydrogen |
| arquivista / gerar-grafo | 4 | 525.224 | 76 | Haiku 5.5, Sonnet 5.5, gemini-3.8-flash |
| juridico / triagem-juridica | 3 | 300.713 | 37 | Haiku 5.5, Sonnet 5.5 |
| arquivista / registrar-termo | 2 | 203.507 | 35 | Haiku 5.5, gemini-4-hydrogen |
| arquivista / montar-ficha | 1 | 139.247 | 18 | Haiku 5.5 |
| auditor / conferir-fato | 1 | 125.634 | 22 | Sonnet 5.5 |

O consumo semanal do Gemini tem registro próprio em `trilhas/rotina-ia/consumo-gemini.jsonl`. Em `testes/relatorio-modelos.md`, l. 74, a semana do Gemini estava em 764.943 tokens de entrada (76% do teto da D-054).

### 5.3 Pontos da conta (pp)
**pp** são pontos percentuais do limite semanal da conta da assinatura (D-040). A fonte é dados.json, `semana_da_conta`, que soma a tabela do checklist (`trilhas/2026-10-17_execucao-piloto.md`, l. 459-496).

| Semana da conta | Desenvolvimento | Planejamento | Não atribuído |
|---|---|---|---|
| 21/10–28/10/2026 | 54 | 33 | 4 |
| 28/10–04/11/2026 | 61 | 6 | — |
| 04/11–11/11/2026 | não medido | não medido | — |
| 11/11–18/11/2026 (em curso) | 59 medidos (63 com 4 estimados) | — | — |
| **Soma por frente** | **174 medidos (178 com a estimativa)** | **39** | **4** |

- Linhas da tabela: 32; sem pp medido: 7 (`semana_da_conta.linhas`, `linhas_sem_pp_medido`).
- **04/11–11/11:** nenhuma linha tem pp somável. O K-112 abriu em 5% e o fechamento não foi lido ("a semana renovou"; checklist, linha do K-112).
- **11/11–18/11:** os 4 pp do K-114 são estimados ("4 (estimado: 2 da conversa + 1,66 do lote)") e ficam fora da soma (`semana_da_conta.pp_estimados_nao_somados`). O `relatorio_dia.py` de 14/11 dá os mesmos 59. Os 9 pp da l. 488 do checklist incluem a conversa de planejamento de 12/11 (D-053), lançada no desenvolvimento.
- Nos tetos (D-040: desenvolvimento até 50, projeto até 60), o desenvolvimento passou de 50 nas três semanas medidas. A tabela registra suspensões dos tetos por Vicente (checklist, l. 476, 478-479, 485 e 496; a última é a do K-114). Em 14/11, Vicente suspendeu os tetos de 50 e 60 pp e manteve a linha de 90% (AGENTS.md, Passo corrente).
- Antes da tabela em pp, a semana de 12–18/10 tem 3.352.741 tokens de agentes (checklist, l. 435).

### 5.4 O que não está medido
- **Tokens da conversa principal:** não registrados por linha (dados.json, `alcance.fora`). A única medida dela são os pp lidos por Vicente.
- **Gemini:** só os testes de modelo estão no script (seção 5.2); o consumo semanal fica no contador próprio.
- **Minutos do GitHub Actions:** a coluna existe na tabela de horas, com "—" nas duas linhas (checklist, l. 456-457). Não medido.
- **Peso de cada modelo no limite da assinatura:** não conferido (`testes/relatorio-modelos.md`, l. 9 e 58).

---

## 6. Horas de Vicente

Fonte: dados.json, `horas_de_vicente`; checklist, l. 452-457.

| Semana | Revisões (h) | Juízo de itens (h) | Busca assistida (h) | Uso da conta | Minutos do Actions |
|---|---|---|---|---|---|
| 12–18/10 | não informado | — | — | não informado | — |
| 19–25/10 | não registrado (Vicente, 29/10: "não precisa") | — | 0 | ver "Semana da conta" | — |

**Falta:** as horas de Vicente não estão medidas. A tabela tem 2 semanas com linha, nenhuma com horas de revisão ou de juízo, e nenhuma linha depois de 25/10. As colunas pedidas pelo bloco 13 (cartões de conflito e de Falta jurídica, leitura da amostra, junção das ramificações, busca assistida; brief, l. 400-403) não foram criadas na tabela. O bloco 13 fica pronto com 4 semanas seguidas medidas (brief, l. 405).

Fila de curadoria em 14/11: 1 cartão à espera de Vicente (K-208) e 7 itens no acervo que pedem cartão (`relatorio_dia.py`).

---

## 7. Modelos por habilidade (K-115a)

Fonte: `testes/relatorio-modelos.md`, l. 37-59. Regra: fica o modelo mais barato que passa nos validadores; antes de subir de modelo, reforça-se o harness (Fundação, l. 698; D-027: execução em Opus 5.5 médio, subagentes em Sonnet 5.5 alto, e depois modelos escolhidos por teste).

| Habilidade | Agente | Modelo que fica |
|---|---|---|
| extrair-evidencia | avaliador | Haiku 5.5 (passou na 3ª rodada, depois do reforço 0.2.1) |
| registrar-termo | arquivista | Haiku 5.5 |
| montar-ficha | arquivista | Haiku 5.5 |
| gerar-grafo | arquivista | Sonnet 5.5 (o Haiku reprovou 2 vezes) |
| triagem-juridica | juridico | Sonnet 5.5 (o Haiku reprovou 2 vezes) |

- **Tokens nas provas em que os dois rodaram:** o Haiku gastou mais que o Sonnet (gerar-grafo: 158.529 contra 81.323; triagem-juridica: 127.077 contra 65.298; l. 58).
- **Segunda leitura do auditor:** achou erros de leitura fiel que nenhum validador pega, nos dois modelos; vão ao insumo 122 (l. 57).
- **Gemini (K-125):** nenhuma prova passou. As do hydrogen reprovaram ou pararam pela cota diária. A do argon não rodou: no nível gratuito, ele não tem cota (l. 64-80).

**Por testar** (fora do K-115a):
- K-115b: guia-de-liberacao e conferir-fato (juridico), ficha-de-acesso e consulta (rastreador);
- K-115c: conferir-fato e verificar-fundacao (auditor), escrever-secao-fundacao (redator) e o fecho do bloco 12 (quadro, l. 40-41);
- o kit (kit-fonte-primaria), que a D-056 tirou do K-114;
- as rodadas que faltam no Gemini (l. 80).

O que não foi feito no K-115a (l. 59): uma rodada por modelo, sem repetição para medir variação; só Haiku e Sonnet; o esforço sempre alto.

---

## 8. Estacionado e pendente

- **K-125** (rotina com IA na API do Gemini), **K-115b** e **K-115c**: estacionados pela D-056, com o estado salvo, e vão à reunião do K-004 (quadro, l. 39-41). O estado do K-125 está em `trilhas/2026-11-14_manutencao/retomar-K-125.md`.
- **IA da operação:** pela D-056, até haver financiamento, é a rotina do Claude do K-113, nos tetos da D-050. A reconfiguração dela (o avaliador propõe, o auditor relê, o portão decide) é o próximo passo da operação (AGENTS.md, Passo corrente). Há 1 proposta da rotina de 13/11 à espera de junção, com o portão não rodado (seção 3.3).
- **Operação:** K-207 (lista das CLB candidatas, baixa prioridade, não chama Vicente) e K-208 (Falta F-0034 a liberar, chama Vicente) (quadro, l. 73-74).
- **Faltas jurídicas à espera da decisão de publicar (K-010):** K-201 (F-0003), K-203 (F-0024, a parte de outras bebidas de caju), K-204 (F-0025), K-205 (F-0032) e K-206 (F-0033) (quadro, l. 67-72).
- **Kit (K-114):** rascunho em `campo_de_acao/`, sem publicar; fechado em 14/11 com a revisão de Vicente "para o piloto" (commit 6d5e12f).
- **Rotina diária:** 6 Recortes interrompidos por teto e 35 vácuos de busca (seção 3.2); 2 ambientes desligados (seção 3.3).
- **Primeira execução em escala:** é da operação, depois da entrega (D-056). Das 2.578 Entradas, 2.544 seguem em estado bruto (seção 2.1).

---

## 9. Gatilho da fase 2

A Fundação (l. 676-679, [PROPOSTA]) pede **as três condições juntas**. A avaliação formal é do K-007 (quadro, l. 19), "depois do K-116 e de 4 semanas medidas". Aqui vão só os números.

| Condição | Situação | Por quê |
|---|---|---|
| 1. o caso-piloto foi do bruto à ficha com a trilha completa | **atende na ficha; trilha completa não medida** | A CL-0001 está em "ficha montada", com a ficha em `acervo/fichas/CL-0001.md` (dados.json, `gatilho_fase2_dados.1_...`). Há 520 Evidências com Trecho localizado e todas as Proposições com a versão da regra (seção 2). O script não mede se a trilha está completa, item a item. |
| 2. as horas reais de 4 semanas couberam em 1 a 3 h | **não medido** | Só 2 semanas têm linha, sem horas de revisão ou de juízo ("não informado"; "não registrado") (`gatilho_fase2_dados.2_...`; seção 6). |
| 3. as decisões do degrau 2 do §5.4 estão tomadas (licença, aviso de privacidade, canal com o titular) | **não decidida** | A busca por "aviso de privacidade" ou "canal com o titular" em `trilhas/decisoes/` (grep -rli) acha 0 arquivos (conferência do auditor). Nenhuma das decisões vigentes listadas no AGENTS.md (da D-015, que levou a Fundação à v0.2, à D-056) trata desses pontos. A licença do acervo está no K-010, "A fazer" (quadro, l. 20). O degrau 2 é [PROPOSTA] na Fundação (l. 475-481). Pelo brief (l. 406), essa condição é de Vicente e não trava o piloto. |

---

## 10. As perguntas do §10 com números do piloto

O §10 da Fundação (l. 871-899) tem 22 perguntas para compreender. A seção 6C do brief (l. 474) pede números reais para as perguntas 1 a 3, 6 a 8, 10 a 14, 16 a 20 e 22. Os números abaixo **informam** a pergunta e não a respondem: a resposta é de Vicente.

| Pergunta | Números do piloto |
|---|---|
| 1. a pessoa que abre o wiki | sem número no piloto (o wiki é local, fora do script) |
| 2. o item que faria pensar "é exatamente isso" | 2.578 Entradas: 28 extraídas, 6 em quarentena (seção 2.1); 22.872 itens vistos nas pegadas |
| 3. o que conta como ambiente | 69 ambientes; 6 na configuração da rotina, 4 ligados; Recortes em 5; Entradas de 4 (seções 3.1-3.3) |
| 6. o nome e as práticas que ele nomeia | 5 Termos (2 atestados, 3 candidatos); 4 CLB (1 com ficha, 3 candidatas de outro termo); 11 Proposições de "nomes e variantes" (seção 2) |
| 7. os links do legado | sem número no piloto (o legado é do Passo 3, K-117) |
| 8. a relação com as comunidades | sem número no piloto |
| 10. ferramentas sem a IA | sem número no piloto (a rotina diária roda sem IA nos 4 ambientes ligados, seção 3.3) |
| 11. os documentos da raiz do Drive | sem número no piloto (o legado ficou fora) |
| 12. tamanho de lote e ritmo de revisão | Entradas por mês: 1.006 em outubro e 1.572 em novembro; fila de curadoria em 14/11: 1 cartão e 7 itens que pedem cartão; horas de Vicente não medidas (seções 2.1 e 6) |
| 13. o risco como Falta | 18 Proposições do atributo "risco"; 69 que sustentam aviso, saúde ou política; 44 Faltas (seção 2) |
| 14. a Educação e o campo de ação | 1 camada Educação (CL-0001); 1 kit em rascunho, sem publicar (seções 4 e 8) |
| 16. o consumo com rotinas na nuvem | produção: pelo menos 6.912.130 tokens de agentes (um piso, seção 5.1); pp por frente: desenvolvimento 174 medidos (178 com 4 estimados), planejamento 39; a conversa principal e o Gemini não medidos em tokens (seção 5) |
| 17. quem reconhece o revisionismo | sem número no piloto |
| 18. o que ancora W | 10 arquivos de compreensão local; 5 Faltas de "compreensão local não captada"; 88 Evidências na voz de pessoa citada em fala direta (seções 2 e 4) |
| 19. a pergunta de pesquisa no grafo 4D | o grafo tem 72 nós e 24 arestas (17 intermediárias, 6 verdadeiras, 1 paracompleta); a divisão por eixo não foi medida (seção 4) |
| 20. o que faz uma fonte ser forte | 34 Fontes, todas "escrito publicado, de arquivo ou oficial"; Evidências por voz: 272 do autor, 160 de instituição, 88 de pessoa citada; 69 Proposições que sustentam aviso, saúde ou política (seção 2) |
| 22. o que quem lê precisa ver da ferramenta | Recortes: 418.775 informados e 383.457 vistos; 35 vácuos de busca; 2.566 Entradas sem cópia no Wayback (seções 2.1 e 3.2) |

---

## 11. O que vai à reunião do K-004

A reunião reúne os insumos abertos, este relatório e `trilhas/planejamento/proxima-versao.md` (quadro, l. 18; D-046). Com ela entram a 3ª passada do K-005, o K-006 e os cartões estacionados (D-056). Este relatório só aponta; não propõe decisão.

**Insumos.** `trilhas/insumos-planejamento.md` tem 135 insumos numerados (o último é o 135, de 14/11). O arquivo não tem coluna de estado: quantos estão abertos e quantos o planejamento já tratou **não foi medido**. Só 2 linhas citam o K-004; uma delas é o insumo 95, sobre a preparação da reunião (l. 101).

**Pontos que este relatório levanta** (a registrar como insumo pelo curador, se couber):
1. O estado dos 69 ambientes está desatualizado ("não iniciado" e "proposto") diante das rotinas que rodam (seção 3.1).
2. A lista dos ambientes não automatizados, com o motivo de cada um (D-052), não sai do script (seção 3.3).
3. As horas de Vicente não estão medidas, e a tabela não tem as colunas do bloco 13; a condição 2 do gatilho depende delas (seções 6 e 9).
4. A semana 04/11–11/11 não tem pp somável (seção 5.3).
5. As linhas do curador nos logs agregam os agentes da conversa, que têm linha própria: a soma antiga contava em dobro, e a regra do script mudou na 0.2. A produção de agentes é um piso (seção 5.1). Os tokens da conversa principal ficam fora; o Gemini só entra pelos testes (seção 5.2).
6. Os nós do grafo não têm campo de tipo que o script leia (seção 4).
7. Os cartões estacionados (K-125, K-115b, K-115c), a reconfiguração da rotina do K-113 e o gatilho da fase 2 (K-007) (seções 7 a 9).

---

## Conferência

- **Auditor:** 8 achados, todos aplicados nesta versão (registro em `trilhas/logs/2026-11-14_auditor.jsonl`), com os números do dados.json regerado pela relatorio-piloto-0.2.
- **BNCC:** as 7 habilidades citadas na camada Educação da CL-0001 conferem em código, texto e página no PDF oficial do MEC (https://www.gov.br/mec/pt-br/cne/arquivos/bncc_ensino_medio.pdf; p. 82, 115, 119, 134 e 137). Nível: oficial.
- **Fora da conferência:** a coluna "Por que serve" da camada Educação (é interpretação) e o consumo semanal do Gemini.

---

## Faltas deste relatório (não medido)
- o total exato de tokens de agentes (a produção é um piso, seção 5.1);
- horas de Vicente em qualquer semana;
- tokens da conversa principal;
- consumo semanal do Gemini dentro do script;
- minutos do GitHub Actions;
- pp da semana 04/11–11/11;
- a lista dos ambientes não automatizados, com o motivo;
- a completude da trilha da CL-0001, item a item;
- a divisão dos nós do grafo por eixo;
- quantos insumos estão abertos;
- o peso de cada modelo no limite da assinatura.
