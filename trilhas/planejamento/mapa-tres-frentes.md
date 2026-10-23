# Mapa das três frentes

**Cartão:** K-001, rodada de planejamento de melhorias de 21 e 22/10/2026 (D-036). **Estado:** verificado por três auditores, cada um numa fatia das fontes, e corrigido pelos 29 achados aceitos (relatório da rodada: `rodadas/2026-10-21_K-001/relatorio.md`).
**Base, no commit 2fe7025:** a Fundação v0.2 (`00_Fundacao_Cultura_Liquida.md`, 1.912 linhas; "l." é a linha dela); o roteiro (`trilhas/2026-10-17_caminhos/caminhos.md`; "rot. l."); o brief de execuções (`trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md`; "brief l."); `trilhas/insumos-planejamento.md` (insumos 1 a 14); as decisões D-001 a D-030 do §9 e as D-030 a D-037 de `trilhas/decisoes/`.
**Entregas do K-001:** este mapa; o quadro completo (`quadro.md`); a lista do que entra na próxima versão da Fundação (`proxima-versao.md`, itens V-01 a V-36).

## Como ler

- **As três frentes (D-036):**
  - **P, planejamento de melhorias:** reavalia o plano. Decisões novas, versões da Fundação, insumos, perguntas, calibrações e o custo e a cadência do próprio planejamento. Sessões curtas, com teto próprio por rodada (D-036), na configuração do `estado-planejamento.md` (Opus 5.5, esforço máximo, ultracode e thinking). Essa é a configuração que o planejamento da v0.2 usou, segundo a D-027; nenhuma decisão a fixa para a frente, e ela vai ao K-002 (A-12).
  - **D, desenvolvimento:** constrói e corrige a ferramenta (harness, esquemas, scripts, adaptadores, agentes e habilidades, wiki local, grafo, rotinas antes de ligar). Sessões na IDE, um cartão por vez, em Opus 5.5 médio, com subagentes Sonnet 5.5 alto, um por vez (D-027, D-035).
  - **O, operação:** a ferramenta trabalhando sem sessão: rotinas, coleta, entrada, processamento por rotina, relatório do dia, grafos, propostas sob demanda e os cartões que os agentes abrem (conflito, Falta a liberar, a lista única das CLB candidatas, pela D-039, e, na fase 2, sugestão). Começa quando a rotina sem IA for ligada (K-112, bloco 10a); até lá, os scripts rodam à mão nas conversas de trabalho (D-033).
  - **PDO:** regra que vale nas três frentes.
- **Estado:** vigente; feito; a fazer; provisório (valor [PROPOSTA] que a execução usa no alcance da D-034); proposta (desenho ainda não decidido); pendente; aberto; adiado; histórico.
- **Vira:** um cartão do quadro (K-nnn); "regra" (vale como está, sem cartão); um item da próxima versão (V-nn, em `proxima-versao.md`); um atrito da seção 2 (A-nn); "histórico" (fica na trilha).
- **Movimentos e frentes:** os três movimentos da Fundação (rastrear, organizar, devolver e agir; l. 78-86) dizem o que a ferramenta faz. As três frentes dizem como o projeto trabalha. Cada movimento nasce no desenvolvimento, roda na operação e melhora pelo planejamento.

## 1. As três frentes hoje

| | Planejamento (P) | Desenvolvimento (D) | Operação (O) |
|---|---|---|---|
| **Memória** | `trilhas/planejamento/` (estado, quadro, este mapa, `proxima-versao.md`); `trilhas/insumos-planejamento.md`; `trilhas/decisoes/`; a Fundação | o brief de execuções e o checklist do piloto (`trilhas/2026-10-17_execucao-piloto.md`); o quadro | os arquivos de estado que as rotinas leem e gravam (Recortes, feed, `ambientes/rotinas.json`, a partir dos blocos 2, 5 e 10a); logs; relatório do dia; o quadro |
| **Começo de cada sessão ou rotina** | `estado-planejamento.md`, quadro, insumos abertos, decisões do cartão e só as seções da Fundação que o cartão pede | retomada do brief (brief l. 67-73) e, pela D-036, o quadro (A-01) | `git pull` e o relatório calculado (l. 512; bloco 10a) |
| **Configuração** | Opus 5.5, esforço máximo, ultracode, thinking (`estado-planejamento.md`, passo 1: a do planejamento da v0.2, D-027; a confirmar no K-002) | Opus 5.5 médio, sem ultracode; subagentes Sonnet 5.5 alto, um por vez (D-027); modelos menores só no bloco 12 | camada 1 sem IA; camada 2 com uma habilidade aprovada por vez, em Sonnet 5.5 alto até o bloco 12 (brief l. 123); a IA da operação é o K-002 |
| **Teto** | o que sobra dos 60 pp por semana do projeto (D-040), com 300 mil tokens de agentes por rodada, provisório até o K-002 (D-036; insumo 13) | até 50 pp por semana do limite da conta, dentro dos 60 do projeto (D-040; brief, seção 0); antes, 300 mil tokens por semana em agentes (D-023) | a mesma guarda (D-023, D-040; l. 511): as rotinas medidas pelo uso da conta, com um teto em execuções por semana a fixar nos blocos 2 e 10b (brief l. 194); o teto das rotinas na nuvem (l. 823), a IA da operação e o teto de manutenção do fim do K-113 (D-040) vão ao K-002 |
| **O que é dela** | as decisões pendentes do §8 e as perguntas do §10 como insumos; as versões da Fundação (D-035); calibrações; IA da operação; gatilho da fase 2; revisão de essencialidade (D-025); o que a amostra acha na ferramenta (D-037) | os blocos 1 a 14 do brief (o 13 é registro, não cartão: D-035), o K-102 e o K-103; depois do piloto, os Passos 3, 6, 7, 8 e 9 e a fase 2 | rotinas das camadas 1 e 2; busca assistida e entrada por link de Vicente; cartões de conflito e de Falta a liberar e o cartão de lista das CLB candidatas (D-039); rodar a amostra que audita a ferramenta (o que ela acha vai ao P); campo de ação sob demanda; medidas (horas, consumo, minutos do Actions) |
| **Cartões** | K-000 a K-010 | K-100 a K-123 | K-201 (Falta F-0003) |

A D-023 fala em "operação da fase 1" antes de a D-036 dar esse nome a uma frente. O brief aplica o teto semanal aos agentes das sessões de trabalho e põe as rotinas na mesma guarda (brief l. 37 e 194). O mapa segue essa leitura, que vai ao K-002 para confirmar (A-13). A D-040 (23/10) mede o teto em pontos percentuais do limite semanal da conta e soma as três frentes, o que supera a leitura A-13: o projeto até 60 pp por semana, o desenvolvimento até 50, o planejamento o resto.

## 2. Atritos das D-036 e D-037 com o texto em vigor

As D-036 e D-037 foram registradas em 21/10, depois do brief (17/10) e sem versão nova da Fundação. A D-035 (diretriz 5) diz que as D-031 a D-035 valem pelos registros até a próxima versão; as D-036 e D-037 estão registradas como vigentes e listadas como tal no `AGENTS.md`. Os pontos abaixo são onde o texto ainda diz outra coisa. Vão ao K-003 (acertar o brief, o roteiro e os arquivos de `.claude/` antes do bloco 1) e à próxima versão. "Leitura dada" é o que o texto da decisão já responde, e a D-034 manda usar sem perguntar; "leitura proposta" é plausível, mas não decorre só do texto, e o K-003 a confirma; "em aberto" é insumo, com o destino e aonde se quer chegar.

**K-003 (22/10/2026):** os atritos A-01 a A-11 estão aplicados no brief (quadro "Ajustes das D-036 e D-037", no início dele), com uma nota no roteiro; o que muda em `.claude/` está no bloco 1 do brief, para o K-101 gravar. Os padrões para A-04, A-05, A-09 (b) e A-10, cada um com o porquê, estão em `rodadas/2026-10-22_K-003/pontos-em-aberto.md`. Vicente os aprovou em 22/10, com as leituras A-03 e A-06, pela D-038, e a D-039 ajustou o A-09 b: os pontos "em aberto" e as "leituras propostas" desta tabela estão decididos, e o que a próxima versão leva está em `proxima-versao.md`. As linhas "brief l." e "rot. l." desta tabela são as do commit 2fe7025, antes desses ajustes.

| A | Onde | O texto diz | A decisão diz | Leitura e destino |
|---|---|---|---|---|
| A-01 | brief l. 67-73 (retomada); `.claude/skills/executar-brief/SKILL.md`; `.claude/agents/curador.md`, l. 20; `AGENTS.md`, "Passo corrente" | a sessão começa pelo `AGENTS.md`, o brief e o checklist | D-036 (2): toda sessão começa pelo quadro e pelo `estado-planejamento.md`, pega um cartão, move-o e termina movendo-o, com log, insumos novos, commit e push | leitura dada: a retomada ganha o quadro e o cartão. Destino: K-003 (brief) e K-101 (executar-brief) |
| A-02 | l. 512; brief l. 110 (§3a, item 6) e l. 173 (bloco 1, "o ritual da l. 512"); rot. l. 17 | cada lote gera uma revisão de uma tela, que Vicente aprova ou devolve | D-037 (1): nada chama Vicente além de conflito e Falta jurídica a liberar | leitura dada: a tela continua como relatório do lote, na trilha, sem pedir aprovação. A outra tela que Vicente aprova, a do relatório da rodada B (brief l. 311-312; l. 701), é portão da ferramenta e fica, porque a D-037 dá à cota a auditoria da ferramenta ("substitui"). Destino: K-003, K-101; V-16 |
| A-03 | l. 199, 243, 246, 472, 498, 813, 886, 902; brief l. 190, 192, 259, 322 e 422; rot. l. 101, 176 e 185 | cota de juízo de até 15 itens por semana, na ordem aviso, saúde ou política → contribuições → amostra; fila = itens à espera de juízo humano; com a fila acima de uma semana, nenhuma porta nova se abre | D-037, "substitui": a cota passa a servir a conflitos, Faltas a liberar e auditoria da ferramenta | leitura dada: a cota serve a esses três. Leitura proposta: a fila passa a ser a dos cartões de conflito e de Falta a liberar à espera de Vicente, e a semana, as horas da D-016; é valor provisório do registro do bloco 2 (D-034), que Vicente pode trocar. Destino: K-003; V-09, V-14, V-30 |
| A-04 | l. 76, 200, 376, 396, 667, 732, 752, 795, 861; brief l. 92, 109, 193, 287, 289 e 299 | a amostra sorteada é parte da segunda leitura; o tamanho dela é "o que sobra da cota"; no Passo 5, vai "para Vicente, dentro da cota" | D-037 (2): a amostra audita a ferramenta (harness, validadores, agentes), na trilha de melhorias, e não revisa a base; o "substitui" dá à cota a auditoria da ferramenta, e a diretriz 1 diz que nada mais chama Vicente | leitura dada: o que a amostra acha vira correção da ferramenta e insumo para o planejamento. **Em aberto:** quem lê a amostra (o auditor, Vicente ou os dois) e se o tamanho dela entra na cota semanal. Aonde se quer chegar: uma auditoria da ferramenta que não vire revisão de rotina da base. Destino: K-003, com a leitura de Vicente; V-24 |
| A-05 | l. 133 (princípio 10), 372, 635 e 750; brief l. 183, 259 e 282; `.claude/agents/avaliador.md`, l. 32 | o item fica em quarentena "até o julgamento de Vicente" (l. 133); o veredito dele tira o item de `PENDENTE_JULGAMENTO` (brief l. 259) | D-037 não cita a quarentena e diz que nada mais chama Vicente | **em aberto:** quem admite no acervo o que está em quarentena. Aonde se quer chegar: uma base que cresce sem revisão de rotina, em que a quarentena não descarta e nada entra sem trilha. Destino: K-003, com a leitura de Vicente; V-07 |
| A-06 | l. 130 (princípio 9) e 598 (§6, Trecho); `.claude/skills/extrair-evidencia/SKILL.md`, l. 24 | o trecho abaixo do limiar vira Falta e "vai para a cota humana" | D-037 não fala dessa Falta; só a Falta jurídica a liberar chama Vicente | leitura proposta: fica Falta "não verificável por máquina", dita e nunca completada (D-018), e a busca assistida pode resolvê-la como fato novo. Destino: K-003, para confirmar; V-06 |
| A-07 | l. 473 e 902 | o que sustenta aviso, saúde ou política exige segunda leitura e é a primeira prioridade da cota | D-037 | leitura que o plano já dá: na fase 1, a segunda leitura é o validador e o verificador de outro harness (l. 396, 473; D-026), sem chamar Vicente; a revisão por profissional antes de circular (l. 575, 787) segue no campo de ação. Destino: K-003 |
| A-08 | brief l. 359 (bloco 13); rot. l. 120 | as horas de Vicente são revisões de uma tela, juízo de até 15 itens e busca assistida | D-037, "substitui" | leitura dada: conflitos, Faltas a liberar, auditoria da ferramenta e busca assistida. Destino: K-003 |
| A-09 | brief l. 377 ("CLB nova a partir de Entrada de rotina") | padrão proposto: o curador abre a CLB situada numa conversa de trabalho, uma por vez, com a fila abaixo de uma semana; se a Fundação não tiver a regra, "é decisão de Vicente" | D-036 e D-037 (4): a menção a uma CLB ainda não registrada, num texto já processado, abre um cartão de baixa prioridade em A fazer, na operação | (a) **menção incidental:** leitura dada pela D-037 (4); o cartão nasce pelo script (K-102). (b) **Entrada de rotina que atende aos 4 critérios da D-022:** a D-037 não cobre; **em aberto**, como o brief já dizia. Aonde se quer chegar: CLB nova entrando sem fila de revisão de rotina e com os 4 critérios. Destino: K-003, com a leitura de Vicente |
| A-10 | l. 473 e 506; brief l. 124, 325 e 328 | quem propõe não aprova; a rotina com IA abre proposta para Vicente revisar; Vicente junta a ramificação das rotinas na revisão semanal | D-037: sem revisão de rotina da base | **em aberto:** se juntar a proposta de uma rotina à versão principal é revisão da base (e sai pela D-037) ou portão da ferramenta (e fica). Aonde se quer chegar: a rotina com IA nunca grava na principal por regra (insumo 3, item 3), e Vicente não revisa a base por rotina. Destino: K-003, com a leitura de Vicente; V-14 |
| A-11 | brief l. 75-100 (§2) e l. 392 | a D-033 como "a registrar" e a D-034 como "proposta"; faltam as D-035 a D-037; a l. 392 ainda proíbe "mudar a Fundação fora dos blocos 0 e 14" | registros em `trilhas/decisoes/`; D-035 (sem versão nova nos blocos 0 e 14; brief l. 10) | leitura dada: a tabela fica em dia, e a l. 392 fica só com "mudar os Anexos A e B". Destino: K-003 |
| A-12 | `CLAUDE.md` ("sessão principal: esforço médio, sem ultracode"; "sem Workflow sem pedido explícito"); brief l. 23, 26 e 387; `estado-planejamento.md`, passo 1 | a configuração da execução, sem distinguir a frente; o estado do planejamento adota esforço máximo, ultracode e thinking "pela D-027" | D-027 registra que o planejamento da v0.2 rodou em esforço máximo, ultracode e thinking; a D-036 cria as frentes sem fixar a configuração de cada uma | **em aberto:** a configuração de cada frente. Destino: K-002; depois, o `CLAUDE.md` por frente (V-34) |
| A-13 | §11, l. 900-929; l. 511 e 858 | só o teto da D-023, "na operação da fase 1" | D-036 (3): teto próprio por rodada de planejamento | destino: K-002 (fixar o teto do planejamento e ler o da D-023 com as frentes) e V-30 |

## 3. Fundação v0.2

### §0 a §2

| Item | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| Cabeçalho: versão e responsável (l. 3), "Quem escreveu esta versão" (l. 7, D-029), "O que mudou" (l. 9-17) e Sumário (l. 19-40) | 1-43 | PDO | vigente | V-01 |
| §0: fonte de verdade e leitura econômica de cada sessão | 46-47 | PDO | vigente | regra; V-02 (leitura por frente) |
| §0: legenda (Pn, D-nnn) e marcadores de status | 48-55 | PDO | vigente | regra |
| §0: "[PROPOSTA] não é plano" | 56 | PDO | vigente, lido com a D-034 | regra; V-04 |
| §0: Regra de Ouro (P38) e acordos 1 a 6 | 57-64 | PDO | vigente | regra |
| §0: comentário novo de Vicente pela essência | 65 | P (habilidade registrar-decisao) | vigente | regra |
| §0: trilhas fora do Registro | 66 | PDO | vigente | regra |
| §1: CLB e propósito | 72-74 | PDO | vigente | regra |
| §1: quem trabalha e segunda leitura | 76 | PDO | vigente, relido pela D-037 | V-05; A-04 |
| §1: rastrear (monitoramento × escavação, Consulta só por descritores, IA em sessão na fase 1) | 80-84 | D constrói (blocos 4, 5, 6, 10a); O roda | desenho em proposta; a l. 84 mudou pela D-032 | K-106, K-107, K-108, K-112; V-05 |
| §1: organizar (wiki, glossário, ilustração, terminologia, grafo 4D) | 85 | D (blocos 2, 3, 7, 8; Passos 6 a 8); O (rotina 10b) | vigente e proposta | K-104, K-105, K-109, K-110, K-118 a K-120 |
| §1: devolver e agir (Educação, pedagogia, salvaguarda, tecnologia comunitária, sob demanda, tiers) | 86 | D (Educação no bloco 8; kit no bloco 11); O (sob demanda); P (tiers) | vigente e proposta | K-110, K-114, K-121, K-010 |
| §1: casa do projeto e legado | 88-90 | PDO; D (Passo 3) | vigente | regra; K-117 |
| Princípio 1, transparência e custódia do texto da fonte | 98-100 | PDO; D (localização do trecho no bloco 3; log no bloco 1) | vigente; "na prática" em proposta | regra; K-101, K-105 |
| Princípio 2, ciência terminológica (Termo candidato → atestado; booleanos por script; laço vivo) | 102-105 | D (blocos 2, 3, 4, 8); O (Consultas novas nas rotinas) | vigente; "na prática" em proposta | K-104, K-105, K-106, K-110, K-112 |
| Princípio 3, paraconsistência: dimensões, W, Falta, admissão, critérios, Proposição, μ e λ | 107-117 | D (contratos e scripts nos blocos 2, 3 e 8); O (cálculo por script); P (perguntas 17 a 19 do §10) | W, Falta, admissão e critérios vigentes; registros e μ e λ em proposta | K-104, K-105, K-110; V-20 |
| Princípio 4, rigor com o poder | 119 | PDO | vigente | regra; A-07 |
| Princípios 5 a 8 (cânone aberto, nativos primeiro, de baixo para cima, descritores processuais) | 121-127 | PDO; D (status botânico-cultural no contrato do Insumo, bloco 2; Consultas nos blocos 4 e 10a) | vigente | regra |
| Princípio 9, fontes reais; anti-robô; trecho conferido por script; abaixo do limiar, cota humana | 129-131 | PDO; D (bloco 3) | vigente; partes em proposta | regra; K-105; V-06; A-06 |
| Princípio 10, quarentena não descarta | 133 | D (bloco 7); O | vigente, relido pela D-037 | V-07; A-05 |
| Princípio 11, persistência e reconstituição | 135-136 | PDO; D (teste de reconstituição, bloco 9) | vigente | K-111; seção 9 deste mapa |
| Princípio 12, institucionalidade sem invasão; papel da cartilha [PENDENTE] | 138-139 | O (aviso sob demanda); P (pergunta 13 do §10) | vigente; cartilha pendente | K-121; K-004 |
| Princípio 13, leis como moldura | 141 | PDO; D (juridico) | vigente | regra |
| Princípio 14, tiers | 143 | P (Passo 6) | vigente | K-010 |
| Princípio 15, campo de ação sob demanda | 145 | O | vigente | regra; K-114, K-121 |
| Princípio 16, infraestrutura simples | 147 | PDO | vigente | regra; seção 9 deste mapa |

### §3 e §4

| Item | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| §3: regra do legado (D-024); legado como ambiente | 153 | D (Passo 3, depois do piloto) | regra vigente; ambiente em proposta | K-117 |
| §3.1: onde está; possível acervo de pesquisa [ABERTO] | 155-164 | D (Passo 3); P (pergunta 11 do §10) | aberto | K-117 |
| §3.2: inventário de 12/10 | 166-178 | — | histórico | histórico |
| §3.3: o que vale aproveitar (conceitos, conteúdo com links, termos candidatos, régua da P14, formulário de 8 perguntas, papéis, varreduras) | 180-188 | D (Passo 3; o formulário é da fase 2) | proposta | K-117; K-008 |
| §3.4: o que melhorar (13 lições) | 190-206 | as lições viraram regras de PDO; o item 6 (lote de máquina e cota humana, l. 199) e o item 7 (amostra sorteada, l. 200) se releem pela D-037; o item 10 (compartilhamento do Drive) segue não conferido | histórico | V-09, V-24 |
| §3.5: acesso ao legado | 208-212 | PDO (nada se lê antes do Passo 3) | resolvido em 16/10 | regra |
| §4.1: origem e modo de trabalhar (P1, P2, P25, P35-P37, P38, P42, P79, P96) | 220-231 | PDO; P36 (consolidação ao fim de cada etapa) é a semente do K-103 e do K-006 | vigente e reformulado; o [ABERTO] da l. 227 está defasado | V-08, V-10 |
| §4.2: busca, ambientes e mineração (P3-P5, P73-P75, P84, P88, P89, P94-P95) | 233-246 | D (blocos 2 a 6 e 10a); O; P84 e P94 relidos pela D-037 | vigente e proposta | V-09 |
| §4.3: insumos, cultura e crítica (P6, P18-P20, 13/10) | 248-256 | PDO (lentes de leitura); P (cartilha) | vigente | regra |
| §4.4: tempo (P9, P31) | 258-263 | D (eixo Z nos contratos) | vigente | regra |
| §4.5: grafo e visualização (P7-P11, P27-P29; P43, P60 e P83, problema do Passo 7; P61 e P66) | 265-277 | D (blocos 3 e 8; Passo 7) | vigente | K-110, K-119 |
| §4.6: terminologia (P23, P24) | 279-285 | PDO | vigente | regra |
| §4.7: entrada, lacunas e contribuição (P12-P14, P22, P26, P47, P48, P53, P57) | 287-300 | D (entrada, bloco 5); P (fase 2: régua da P14, e-mail para pessoas, P48, formulário da P53) | vigente e adiado | K-107; K-008 |
| §4.8: rotinas e governança do fluxo (P15, P79, P85-P87, P90-P93, P97) | 302-312 | D (bloco 10: o "Relógio" da P15 precisa de agendamento real); O | vigente | K-112, K-113 |
| §4.9: agentes (P16, P36, P62) | 314-320 | D (harness); P (P36) | vigente | V-10 |
| §4.10: acesso e públicos (P44-P48) | 322-328 | P (pergunta 5 do §10; Passo 6) | aberto | K-010 |
| §4.11: plataforma (P49-P59, P64-P72) | 330-335 | PDO (requisitos: manutenção simples e online; complexidade conceitual com infraestrutura simples) | histórico; requisitos vigentes | regra |
| §4.12: campo de ação (P17, P30, P56, 13/10) | 337-344 | O (sob demanda); D (Passos 6 e 9) | vigente | K-114, K-121 |
| §4.13 e §4.14: viabilidade e execução | 346-357 | — | histórico; o [ABERTO] da l. 351 está defasado | V-08 |

### §5 Arquitetura

| Item | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| Introdução: nenhum servidor; "nada desta seção é criado agora"; nem Actions antes do Passo 4 | 363 | D, O | proposta; mudou pela D-032 (rotinas e Actions no piloto) | V-11 |
| Fluxo e laço vivo (termo novo → booleano → Consulta) | 365-389 | D constrói cada caixa (blocos 2 a 10); O roda o fluxo; a amostra no portão (l. 376) se relê pela D-037 | proposta | K-104 a K-113; A-04; V-24 |
| §5.1: repositório, público, dados pessoais fora do Git, proteção do `main`, ritual de sincronização | 393-397 | PDO; a amostra no portão da fase 1 (l. 396) se relê pela D-037 | vigente | regra; A-04; V-12, V-24 |
| §5.1: mapa de custódia; tabela código → nome "no Passo 4"; chaves "onde, a decidir" | 399-409 | D (layout no bloco 2); Vicente decide nas paradas (c) dos blocos 2 e 5, com padrão | proposta | K-104, K-107; V-12 |
| §5.2: ambiente ([ABERTO] o sentido); mapeamento persistente; dois eixos; Matriz de Pegadas e Vácuos | 413-416 | D (blocos 3, 4 e 5); O (pegadas a cada execução); P (pergunta 3 do §10) | vigente, proposta e aberto | K-105, K-106, K-107; V-13 |
| §5.2: legado como ambiente | 417 | D (Passo 3) | proposta | K-117 |
| §5.2: ficha de acesso testada em cada lugar de execução; anti-robô | 418-419 | D (blocos 1, 4 e 10a); O (ficha refeita quando o ambiente muda) | proposta, já seguida | K-101, K-106, K-112 |
| §5.2: catálogo dos ambientes (Anexo E) | 420 | D (semeado em `ambientes/` no bloco 3); O | — | K-105 |
| §5.3: Consulta e Recorte | 426-427 | D (blocos 2, 4 e 5); O | proposta, usada pela D-034 | K-104, K-106, K-107 |
| §5.3: monitoramento; novidade é ID não visto | 428 | D (feed no bloco 10a); O | proposta | K-112 |
| §5.3: escavação; modo assistido | 429 | D (bloco 5); O (busca assistida de Vicente) | proposta | K-107, K-108 |
| §5.3: adaptadores por protocolo, só os do piloto | 430 | D (blocos 5 e 10a) | proposta; mudou pela D-032 | K-107, K-112; V-13 |
| §5.3: regras de busca (saturação, variantes por família, país e idioma anotam, uma Entrada por item, funil "inspirado em" PRISMA) | 431-436 | D (bloco 5); O | proposta | K-107 |
| §5.3: fontes com regra própria | 437 | PDO (brief l. 382) | conferido em 15/10 | regra |
| §5.3: fase 2 (bola de neve, Wikidata, demais fichas) | 438 | P (gatilho) → D | fase 2 | K-007, K-122; V-13 |
| §5.4: a fase 1 não recebe contribuições externas | 442 | PDO | vigente | regra |
| §5.4: canais (monitoramento e escavação; link ou documento de Vicente; e-mail dos Alertas na fase 1; formulário, e-mail para pessoas e envio de documentos na fase 2; WhatsApp adiado) | 444-453 | D (entrada por link no bloco 5; e-mail quando a conta existir); O (canais da fase 1); P (fase 2) | vigente, proposta e adiado | K-107, K-108; K-008 |
| §5.4: registro da Entrada, devolutiva e régua da P14 | 455 | D (contrato da Entrada, bloco 2); P (devolutiva e régua, fase 2) | proposta | K-104; K-117; K-008 |
| §5.4: portas por tipo de evidência | 457-468 | D (blocos 2 e 7) | proposta | K-104, K-109 |
| §5.4: voz no trecho; papéis de pessoa | 470-471 | D (Pessoa e papéis, bloco 2) | proposta | K-104 |
| §5.4: cuidados; a fila que fecha portas | 472 | D; O | proposta; a fila se relê pela D-037 | A-03; V-14 |
| §5.4: portão único | 473 | D (validador, bloco 3); O (rotinas propõem) | proposta; relido pela D-037 | A-07, A-10; V-14 |
| §5.4: degraus jurídicos | 475-481 | P (decisões do degrau 2 = condição 3 do gatilho; degrau 3 antes do Passo 6) | proposta | K-007, K-010 |
| §5.4: repositório público e degraus (Falta F-0003) | 483 | O (cartão de Falta a liberar, D-037); D (guia da Lei 9.610, bloco 7); P (lugar e visibilidade, de Vicente) | Falta aberta | K-201, K-109, K-010 |
| §5.4: Lei 13.123 | 484 | P (antes do Passo 6); D (guia do SisGen, bloco 7) | só para publicar (D-032) | K-109, K-010; V-15 |
| §5.4: simplificação pela ANPD; conteúdo de terceiros (Marco Civil) | 485-486 | P (fase 2) | conferido em parte | K-008 |
| §5.4: triagem jurídica leve | 487 | D (regras fixas no bloco 3; juridico no bloco 7); O | proposta | K-105, K-109 |
| §5.4: enquadramento (Res. CNS 510); licenças; quem responde; consulta pontual | 488-491 | P (Vicente; antes do Passo 6 ou na fase 2) | aberto, proposta e vigente | K-010, K-008 |
| §5.4: segurança (conteúdo de entrada é dado) | 493 | PDO; D (harness da extração) | proposta seguida | regra |
| §5.5: cadência D-012 ("cumprida em parte") | 497 | O | vigente; "em parte" mudou pela D-032 | K-112, K-113; V-16 |
| §5.5: lote de máquina e cota de juízo | 498 | D (valores do bloco 2); O; a cota se relê pela D-037 | proposta | A-03; V-09, V-16 |
| §5.5: quem executa (IA em sessão na fase 1) | 499 | D; O | proposta; mudou pela D-032 | V-16 |
| §5.5: camada 1, GitHub Actions | 505 | D (bloco 10a) → O | proposta; fatos de 17/10 | K-112; V-17 |
| §5.5: camada 2, rotina do Claude | 506 | D (bloco 10b) → O; P (IA da operação) | proposta; na fase 1 pela D-032 | K-113, K-002 |
| §5.5: termos do Actions e leitura do Flat Data | 508 | P (Vicente, na parada (a) do bloco 10) | pendente; o "rodar em sessão" virou a saída da D-033 | K-112; V-16 |
| §5.5: cópia no Wayback | 509 | D (bloco 5); O | proposta | K-107 |
| §5.5: Apps Script fora | 510 | — | descartado | histórico |
| §5.5: guarda de orçamento e a sua mecânica | 511 | PDO; P (K-002, K-005) | vigente; mecânica em proposta | regra; K-002, K-005 |
| §5.5: ritual e prioridade de cada sessão ou rotina | 512 | D (sessões); O (rotinas) | proposta; a revisão de uma tela se relê pela D-037 | A-02; K-003, K-101 |
| §5.6: acervo; unidade da ficha [ABERTO] | 514-516 | D (valor provisório no bloco 2) → P | aberto | K-104; V-20 |
| §5.7: wiki (Quartz [PENDENTE]; hospedagem no Passo 6; Educação [ABERTO]) | 520-534 | D (só na máquina no bloco 8; Passo 6); O (republica sozinho); P (gerador; pergunta 14) | pendente e aberto | K-110, K-118; V-18 |
| §5.7: Lugar | 536-543 | D (contrato no bloco 2; tabela do IBGE no bloco 4; páginas no Passo 6) | proposta | K-104, K-106, K-118 |
| §5.7: grafo 4D, primeira vista, outras vistas, componente próprio | 545-551 | D (blocos 3 e 8; Passo 7); P (pergunta 19) | proposta | K-105, K-110, K-119 |
| §5.8: ilustração técnica | 553-557 | D (Passo 8; o dono está por definir, insumo 3, item 6) | proposta | K-120 |
| §5.9: tiers; site público; restrito fora do Git | 561-563 | P (Passo 6); D | vigente, proposta e aberto | K-010, K-118 |
| §5.9: grupos candidatos e ferramentas | 564-570 | P (pergunta 5); O (sob demanda); D | proposta | K-010, K-121 |
| §5.9: três jeitos de construir; regras das ferramentas | 571-575 | D (gerador no navegador); O (sob demanda); P (IA por fila, adiada até haver demanda) | proposta | K-121 |
| §5.9: começar com um grupo e uma ferramenta, o kit | 576 | D (bloco 11) → O | proposta; mudou pela D-032 (teste no fim do piloto, sem publicar) | K-114; V-19 |

### §6 Modelo de dados

| Item | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| Regras de todo registro (IDs imutáveis, campos de proteção, data e origem) | 584-587 | D (bloco 2; validador no bloco 3) | proposta | K-104, K-105 |
| Busca: Ambiente, Consulta, Recorte, Execução | 589-593 | D (log no bloco 1; contratos no bloco 2) → O | proposta | K-101, K-104 |
| Entrada, Fonte, Trecho | 595-598 | D (bloco 2); o Trecho se relê pela D-037 | proposta | K-104; V-06 |
| Evidência, Proposição | 600-602 | D (bloco 2; blocos 7 e 8) | proposta | K-104, K-109 |
| CLB situada, Elemento, Insumo, Processo, Compreensão local, Transformação, Aresta | 604-610 | D (bloco 2; bloco 8) | proposta | K-104, K-110 |
| Termo, Lugar, Pessoa e papéis | 612-615 | D (bloco 2) | proposta | K-104 |
| Falta | 617-618 | D (esquema já existe; regras fixas no bloco 3); O (a Falta jurídica a liberar abre cartão, D-037) | dita e nunca completada (vigente); campos em proposta | K-105; K-201 |
| Eixos de status e selos | 620-641 | D (bloco 2; eixo 5 provisório); `PENDENTE_JULGAMENTO` se relê pela D-037 | proposta | K-104; V-07, V-20 |

### §7 Passos e ordem

| Item | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| Ordem dos passos; "só começa quando o anterior está pronto" | 647-660 | D (cartões do quadro) | mudou pela D-032 no piloto | V-21 |
| Passo corrente e "único bloqueio" | 662 | — | defasado (D-031) | V-21 |
| Fase 1 | 666-672 | PDO; D; a amostra da segunda leitura (l. 667) se relê pela D-037 | pessoas vigente; resto em proposta, mudado em parte pela D-032 | V-22, V-24 |
| Fase 2 | 674 | P (gatilho) → D, O | proposta | K-007, K-122 |
| Gatilho da fase 2 | 676-679 | P | proposta | K-007 |
| Revisão de essencialidade (D-025) | 681 | P | vigente | K-009 |
| Passo 0 | 683-687 | — | feito, segundo Vicente; a revisão do compartilhamento do Drive não foi conferida | histórico |
| Passo 1 | 689-702 | D (blocos 1 a 12 do brief) | em curso; bloco 0 feito | K-101 a K-115 |
| Passo 2 | 704-726 | D (validador no bloco 3; README e reconstituição no bloco 9; validador a cada envio no bloco 10a) | feito em parte; o validador e a localização do trecho nascem no Passo 1 (6A) | K-105, K-111, K-112; V-21 |
| Passo 3 | 728-737 | D (depois do piloto); a amostra da etapa B se relê pela D-037 | a fazer | K-117; V-24 |
| Passo 4 | 739-745 | D (blocos 4, 5 e 10a) → O; P (canais da fase 2) | em parte no piloto; a camada 2 na fase 1 (l. 742) e as rotinas além do piloto (l. 741) mudaram pela D-032 | K-106, K-107, K-112; K-008; V-12, V-16, V-22, V-25 |
| Passo 5 | 747-757 | D (blocos 7 e 9) → O; a amostra se relê pela D-037 | no piloto | K-109, K-111, K-113; V-24 |
| Passo 6 | 759-763 | P (precondições: Lei 13.123 e licença) → D; Educação e wiki local antecipados no bloco 8 | depois do piloto | K-010, K-118 |
| Passo 7 | 765-773 | D (dados e cálculo nos blocos 3 e 8; vista navegável depois); P (pergunta 19) | em parte no piloto | K-105, K-110, K-119 |
| Passo 8 | 775-776 | D | a fazer | K-120 |
| Passo 9 | 778-789 | O (sob demanda); D (ferramentas) | o kit no piloto | K-114, K-121 |
| Passo 10, governança contínua | 791-797 | P (Registro, revisão de essencialidade, tiers, o checklist mensal de 5 itens, que a v0.2 não lista); O (auditoria pela amostra, novos ambientes, devolutiva na fase 2) | contínuo | K-009; V-26 |

### §8 Decisões pendentes (l. 801-828)

| Linha do §8 | Frente | Estado | Vira |
|---|---|---|---|
| 807 caso-piloto | — | resolvido (D-031; fontes aprovadas com o brief em 17/10) | V-27 |
| 808 caminho na Lei 13.123 | P | só para publicar | K-010; guia no K-109 |
| 809 repositório público e degraus (F-0003) | O; P (lugar e visibilidade, de Vicente) | Falta aberta | K-201, K-010 |
| 810 modo de expor a ferramenta | P | aberto, depois do piloto | K-010 |
| 811 unidade da ficha | D | provisório (bloco 2) | K-104; V-20 |
| 812 escala de valências e `PENDENTE_JULGAMENTO` | D | provisório (bloco 2); calibra no Passo 5 | K-104; V-20 |
| 813 tamanho do lote e da cota | D; P | provisório; a cota se relê pela D-037 | A-03; V-09 |
| 814 camadas e termos do Actions | P (Vicente) | pendente, na parada (a) do bloco 10 | K-112 |
| 815 dados pessoais dos canais de pessoas | P | fase 2 | K-008 |
| 816 P48 para entrevistas | P | fase 2 | K-008 |
| 817 licença do acervo | P | antes do Passo 6 | K-010 |
| 818 gerador do wiki e componente da vista 4D | D (Quartz só na máquina no bloco 8); P (Passos 6 e 7) | pendente | K-110, K-118, K-119 |
| 819 grupos (tiers) | P | Passo 6 | K-010 |
| 820 régua de 4 filtros | D | Passo 3 | K-117 |
| 821 modo de produzir a ilustração | D | modo já escrito | K-120 |
| 822 papel da cartilha | P | aberto (pergunta 13) | K-121 |
| 823 teto das rotinas na nuvem | P; D (medida das rotinas no bloco 2; teste no bloco 10b) | passa ao piloto (6A) | K-002 |
| 824 forma jurídica | P | só se o projeto ganhar uma organização | sem cartão |
| 826 decisões que nascem do §10 | P | — | K-004 |
| 828 resolvidas desde a v0.1 | — | histórico | histórico |

### §9, §10 e §11

- **§9, Registro de Decisões (l. 832-867):** cada decisão está na seção 7 deste mapa. A próxima versão traz as D-031 a D-037 (V-28).
- **§10, perguntas (l. 871-896):** todas são da frente de planejamento e viram insumos que dizem aonde querem chegar (V-29). Destino de cada uma:

| Pergunta | Frente | Destino |
|---|---|---|
| 1, a pessoa que abre o wiki; 22, como quem lê percorre o conteúdo | P | K-010 (modo de expor), depois do piloto |
| 2, o item que é "exatamente isso" | P | K-004, com as valências calibradas pelo piloto |
| 3, o que conta como ambiente | P | K-004 (V-13) |
| 4, "fidedigno e seguro" para quem envia | P | K-008 (fase 2) |
| 5, grupos de cada tier | P | K-010 |
| 6, unidade da ficha | D (provisório no bloco 2) → P | K-004 |
| 7, links do legado; 11, documentos da raiz do Drive | D (Passo 3) e P | K-117 |
| 8, relação com as comunidades | P | K-004 |
| 9 e 15, respondidas (D-016 e D-029) | — | histórico |
| 10, ferramentas sem IA | P | K-002 |
| 12, lote e ritmo de revisão | P | K-004 (relida pela D-037) e K-005 |
| 13, cartilha de biossegurança | P | K-121 e K-004 |
| 14, Educação e campo de ação | P | K-004 (insumo 3, item 6) |
| 16, consumo com rotinas na nuvem | P | K-002 |
| 17, revisionismo; 20, fonte forte | P | K-004 |
| 18, W e etnografia | D (provisório: W só da fala de quem pratica) → P | K-004 |
| 19, pergunta de pesquisa do grafo | P | K-004; decide se a vista navegável vem antes do K-119 |
| 21, entrevista própria | P | K-008 (fase 2) |

- **§11, orçamento e ritmo (l. 900-929):**

| Item | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| cota de juízo | 902 | P; O | vigente (D-016) e proposta; relida pela D-037 | A-03; V-09, V-30 |
| guarda de orçamento | 904 | PDO | vigente | regra; V-30 |
| "nesta execução", 600 mil por janela | 906 | — | histórico (só valeu para a escrita da v0.2) | V-30 |
| medidas reais | 908-921 | P (estimativas por agente e habilidade) | medido | K-005; V-30 |
| ainda não medido | 923 | D (bloco 13); P | a medir | K-005; V-30 |
| regras de prudência | 925-930 | PDO | vigente | regra |

### Anexos

| Anexo | Linhas | Frente | Vira |
|---|---|---|---|
| A e B, verbatim | 933-1625 | PDO: intocáveis (`scripts/comparar_anexos.py`); consulta por busca | regra |
| C, referências e nível (o C.3 tem 37 linhas "não conferido", cada uma com o passo em que se confere) | 1627-1811 | PDO (fato com nível); D (cada bloco confere o que usa) | V-31 |
| D, trilha da análise | 1812-1836 | — | V-32 |
| E, 69 ambientes candidatos | 1838-1912 | D (semeados em `ambientes/` no bloco 3; os com via por programa ligados no bloco 10a); O; P (demais fichas na fase 2) | K-105, K-112; V-33 |

## 4. Roteiro (aprovado em 17/10)

O roteiro serviu à aprovação de 17/10; para a execução, vale o brief onde os números divergirem (rot. l. 36).

| Parte | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| Cabeçalho e marcas das etapas | 1-9 | — | aprovado | histórico |
| §1, onde se quer chegar (uma semana da ferramenta em uso na fase 1) | 11-20 | O (o retrato da operação); P (gatilho, l. 20) | aprovado; a l. 17 se relê pela D-037 | A-02; K-007 |
| §2, onde estamos | 22-32 | — | estado de 17/10, defasado em parte | histórico |
| §3, etapas 0 a 14 | 34-128 | D (viraram os blocos do brief) | a etapa 14 (v0.3) mudou pela D-035 | K-100 a K-116; K-004 |
| §4, onde a ferramenta mora (padrão, fatos conferidos, quando muda de lugar, candidatas) | 130-156 | O (lugar da execução); P (fornecedor por decisão, D-033); PDO (custódia) | aprovado; fatos de 17/10 | K-002; V-17 |
| §5, o que não é mais pergunta; valores provisórios | 158-179 | D (a execução usa) | aprovado (D-034) | K-104 |
| §6, insumos para reavaliar | 181-191 | P | = brief, 6C | insumo 3 |
| §7, decisões que só Vicente toma | 193-208 | P (Vicente) | 1, 2 e 4 feitas em 17/10; 3 na parada (a) do bloco 10; 5 na parada (c) do bloco 5; 6 podem esperar | K-112; K-107; K-010 e K-008 |
| §8, próximo passo concreto | 210-216 | — | feito no bloco 0; o item 4 (v0.2.1) saiu pela D-035 | histórico; insumo 2 |
| Trilha e desvios declarados | 218-221 | — | — | histórico; insumo 7 |

## 5. Brief de execuções (aprovado em 17/10, com os ajustes da D-035)

### Partes gerais

| Parte | Linhas | Frente | Estado | Vira |
|---|---|---|---|---|
| Para quem, versão, base, precedência | 1-6 | D; PDO (precedência) | vigente pela D-034 e pela D-035 | V-03 |
| Ajustes da D-035 | 8-12 | D | vigente | regra; o K-003 acrescenta os das D-036 e D-037 |
| §0, autorização (D-028) | 18-20 | D | vigente | regra |
| §0, modelos (D-027) | 22-26 | D; P (os testes do bloco 12 voltam ao plano) | vigente | regra; A-12 |
| §0, paradas (a) a (d) | 28-34 | D; as decisões das paradas são de Vicente (P) | vigente | regra |
| §0, orçamento da execução | 36-44 | D; P (calibrar) | vigente; a semana e a estimativa são leituras da 6B | K-005 |
| §0, fatos; dados, Git e commits; Windows | 46-53 | PDO | vigente | regra |
| §1, estado de partida | 57-65 | — | estado de 17/10 | histórico |
| §1, retomada | 67-73 | D | vigente; sem o quadro | A-01; K-003 |
| §2, decisões vigentes | 75-100 | PDO | desatualizada | A-11; K-003 |
| §3a, em cada conversa (9 passos) | 104-113 | D | vigente; os passos 5 e 6 se releem pela D-037 | A-02, A-04; K-003 |
| §3b, em cada rotina (camadas 1 e 2) | 115-128 | O (desenho da operação); D (construída no bloco 10) | vigente e proposta | K-112, K-113 |
| §4, sequência e ordem | 130-150 | D | vigente | o quadro |
| Depois do bloco 14: operação (cadência, orçamento, CLB nova) | 374-377 | O | proposta; a l. 377 se relê pelas D-036 e D-037 | A-09; coluna Operação do quadro |
| §5, não fazer | 379-392 | D; PDO; a l. 387 é da execução; a cláusula "fora dos blocos 0 e 14" da l. 392 está superada pela D-035 (brief l. 10) | vigente, menos essa cláusula | regra; A-11, A-12 |
| §6A, o que a próxima versão leva ao texto (17 linhas, l. 400-416) | 396-416 | P | vale até a próxima versão (D-034, D-035) | V-03, V-05, V-08, V-11 a V-13, V-15 a V-19, V-21, V-22, V-27 a V-29, V-34 |
| §6B, leituras que a Fundação não fixa | 418 | D (usa como valor provisório); P (confirma ou corrige) | provisório | V-16, V-20, V-25, V-30 |
| §6C, insumos 1 a 11 | 420-431 | P | — | insumo 3 |
| Trilha | 433-435 | — | — | histórico |

### Blocos

| Bloco | Linhas | O quê | Agentes | Parada | Cartão | Depois, em outra frente |
|---|---|---|---|---|---|---|
| 0 | 152-165 | plano em dia | redator e auditor previstos (l. 162; a tabela do §4, l. 134, diz "—"); nenhum rodou | (a) feita em 17/10 | K-100, concluído em 18/10 | — |
| 1 | 167-178 | harness e operação | auditor | — | K-101 | — |
| 2 | 180-216 | contratos do §6 e valores provisórios | auditor | (c) lugar da tabela código → nome, antes do bloco 7 (l. 212; a tabela do §4, l. 136, e a l. 216 dizem "nenhuma") | K-104 | os valores voltam ao P para calibrar (V-20); a fila e a amostra se releem pela D-037 (A-03, A-04) |
| 3 | 218-230 | scripts do núcleo | auditor, juridico | — | K-105 | os scripts rodam na O |
| 4 | 232-249 | fichas de acesso, Termos e Consultas do caju | rastreador, arquivista, auditor | (a) feita (fontes aprovadas em 17/10) | K-106 | fichas e Consultas servem às rotinas |
| 5 | 251-267 | adaptadores, Recorte, deduplicação, modo assistido, entrada por link, Wayback, fila, pegadas, relatório do dia | auditor, juridico | (c) chave do Internet Archive | K-107 | a fila do `fila_curadoria.py` se relê pela D-037 (A-03, A-05) |
| 6 | 269-278 | primeira coleta real | rastreador | — | K-108 | a busca assistida de Vicente vira canal da O; a medição do bloco 13 começa |
| 7 | 280-290 | do bruto à Evidência, com triagem jurídica e guias | avaliador, juridico, auditor | — | K-109 | as Faltas jurídicas a liberar abrem cartões na O (D-037) |
| 8 | 292-302 | Termos, ficha, grafo, Educação e wiki local | arquivista, juridico, redator, auditor | — | K-110 | — |
| 9 | 304-312 | pares reais, rodada B, README e reconstituição | auditor | (a) Vicente aprova o harness, só para o 10b e o 12 | K-111 | — |
| 10a | 314-328 e 332-335 | rotinas sem IA (Actions) | rastreador, auditor, redator | (a) termos do Actions; (a) fornecedor, se valer a D-033 | K-112 | ligada, rodar sozinha é O (D-035) |
| 10b | 329-331, 332-333 e 336-337 | rotina com IA | auditor (reconfere os fatos das rotinas do Claude Code e faz a segunda leitura em cada execução, l. 332-333); a habilidade aprovada roda na rotina | (c) conta e rotina | K-113 | O; depende do K-002 (D-036, diretriz 4) |
| 11 | 339-345 | kit de fonte primária | campo-de-acao | (a) feita (pedido aprovado com o brief) | K-114 | o campo de ação sob demanda é O |
| 12 | 347-355 | testes de modelos | agentes do piloto, auditor | — | K-115 | o resultado volta ao P (modelos por tarefa, D-027) |
| 13 | 357-364 | horas e consumo | — | — | sem cartão: registro desde o K-108 (D-035) | medida da O e do P; as horas se releem pela D-037 (A-08; K-003) |
| 14 | 366-372 | relatório do piloto para o planejamento | redator, auditor | a aprovação da v0.3 passa ao K-004 (D-035) | K-116 | P: K-004 e K-007 |

## 6. Insumos 1 a 38 (os 15 a 19 nasceram no K-001; os 20 a 26, no K-003)

| Insumo | Frente | Vira |
|---|---|---|
| 1, o que a v0.2.1 levaria ao texto (6A) | P | `proxima-versao.md`; K-004 |
| 2, o pedido ao redator já preparado | P | K-004 (V-36) |
| 3, os insumos 1 a 11 da 6C | P; o item 3 também D (teste no bloco 10b); o item 9 também D (Fonte sem nome no bloco 2) | item 1 → K-005; 2 → K-004 (com a D-037); 3 → K-113 e V-12; 4 → K-010 (Vicente) e V-12; 5 → V-13; 6 → V-23 e K-120; 7 → K-111 (só com pares reais); 8 → K-002; 9 → V-20; 10 → V-20 e V-30; 11 → V-29 (perguntas do §10) e V-13 (sentido de "ambiente") |
| 4, ritmo do piloto (1 a 2 agentes por semana) | P | K-005 |
| 5, achados de harness | D (bloco 1: lista exata de campos do log, teto de chamadas contado como o harness conta); PDO (o número oficial é o do Agent; agente novo só em sessão nova); P (termos-chave das decisões no `checar_fundacao.py`) | K-003 (o que cabe no bloco 1), K-101; V-23, V-35 |
| 6, custos medidos | P; D (a estimativa no registro de valores, bloco 2) | K-005; V-30 |
| 7, mapa de hospedagem em Haiku | D (reconferência em Sonnet no bloco 10); P (tipo de agente preso ao harness) | K-112; K-003 (regra no bloco 1); V-23 |
| 8, o planejamento gastou 57% da semana | P | K-002 |
| 9, contribuição com tokens próprios (fase 2) | P | K-008 |
| 10, agente de melhorias e contribuições | P (desenho); D (habilidades) | K-103 (primeira habilidade); K-006 |
| 11, `checar_fundacao.py` volta a cobrar as D-031 em diante | P; D | K-004 (V-35) |
| 12, a IA da operação | P | K-002 |
| 13, cadência e teto do planejamento | P | K-002 |
| 14, o quadro como porta de contribuição | P | K-001 (seção 9 deste mapa); K-008 |
| 15, o número do Workflow e o do Agent não batem (desta rodada) | P | K-002 |
| 16, estimativa do lote pela medida do mesmo agente e habilidade (desta rodada) | P | K-002, K-005 |
| 17, harness: validação reservada no teto, citação literal de verdade, log de agente de workflow (desta rodada) | D | K-003 (o que cabe no bloco 1), K-101 |
| 18, script de checagem do mapa (desta rodada) | P (ferramenta do planejamento); D (construir) | K-006 |
| 19, configuração e teto de cada frente; "operação" na D-023 (desta rodada) | P | K-002 |
| 20, juntar a proposta da rotina sem Vicente, por script sem IA (K-003) | P; D (teste na 10b) | K-002, K-113 |
| 21, o alcance do script de menções é o registro de Termos (K-003) | D; P | K-102, K-117 |
| 22, `checar_mapa.py` lê a 6A do brief por linhas fixas (K-003) | P (ferramenta do planejamento); D (construir) | K-006 |
| 23, o auditor da amostra usa o mesmo modelo dos agentes que produzem (K-003) | P; D (bloco 12) | K-115; V-24 |
| 24, o cartão do tratamento com IA entre o piloto e o K-113 (K-003) | P; O | K-002 |
| 25, o kit e a regra do campo-de-acao sobre Falta jurídica aberta, sem a v0.2.1 (K-003) | P; D (bloco 11) | K-114 |
| 26, o termo ambíguo e o desdobramento da CLB na registrar-termo e na montar-ficha (K-003, D-039) | D (blocos 8 e 9); P | K-110, K-111 |
| 27, o curador.md e o executar-brief ainda sem a registrar-melhoria (K-103) | D | K-101 |
| 28, prefixo do id da Execução | D | K-104 |
| 29, agente sem Write não valida JSON por heredoc | D | K-111 |
| 30, Termo sem a língua das designações (TBX langSec) | D | K-106 |
| 31, User-Agent do projeto não definido | D | K-107 |
| 32, triagem fixa: listas e normas a calibrar | D; P | K-109 |
| 33, validar_acervo: papéis da W e frase da ficha | D | K-110 |
| 34, μ e λ: quais Evidências contam | P; D | K-005 (regra pela D-041); K-123 (no script) |
| 35, pre-commit em cada cópia | D; O | K-111 |
| 36, limiar do trecho e linhagem nos dois lados | P; D | K-005 (regra pela D-041); K-123 (no script) |
| 37, o planejamento medido em pp da conta (K-005) | P | K-002 |
| 38, a leitura da conta depende de Vicente (K-005) | P; O | K-002 |

## 7. Decisões D-001 a D-041

| D | Essência curta | Frente | Estado e leitura de hoje | Vira |
|---|---|---|---|---|
| D-001 | sistema novo em paralelo; o Drive é fonte a verificar | — | resolvida pela D-024 (l. 867) | histórico |
| D-002 | primeiro trabalho nos agentes | — | feito antes da v0.2 (D-029) | histórico |
| D-003 | princípios: terminologia, paraconsistência, transparência | PDO | vigente | regra |
| D-004 | tiers são grupos de interesse | PDO; P (Passo 6) | vigente | K-010 |
| D-005 | campo de ação sob demanda, dentro da lei | PDO; O | vigente | regra |
| D-006 | Educação no wiki; pedagogia como ferramenta de aulas | D (bloco 8; Passo 9); P (pergunta 14) | vigente | K-110, K-121 |
| D-007 | tecnologia comunitária avisa; cartilha [PENDENTE] | PDO; P (pergunta 13) | vigente | K-121 |
| D-008 | infraestrutura simples | PDO | vigente | regra |
| D-009 | WhatsApp e áudios adiados | P (fase 2 ou depois) | adiado | K-008 |
| D-010 | wiki alimentado por RSS nossos | PDO | lida pelo modelo monitoramento × escavação (l. 867) | regra |
| D-011 | abertura a documentação de outras pessoas | P (fase 2); D | vigente, para a fase 2 | K-008 |
| D-012 | rotinas diárias; cada ambiente toda semana até exaurir | O; D (bloco 10) | cumprida em parte; cumpre-se com a rotina do piloto (6A) | K-112, K-113; V-16 |
| D-013 | caixa de entrada multicanal | D (bloco 5); O; P (canais da fase 2) | vigente | K-107; K-008 |
| D-014 | glossário clicável com ilustração | D (Passos 6 e 8) | vigente | K-118, K-120 |
| D-015 | Fundação v0.2 | — | feita | histórico |
| D-016 | 1 a 3 h por semana; os "15" nunca são teto de coleta | PDO | vigente; o uso das horas se relê pela D-037 | V-09, V-28 |
| D-017 | exemplos ilustram e nunca limitam | PDO | vigente | regra |
| D-018 | W como prática comum; o não captado é Falta | PDO; D (contratos) | vigente | regra; K-104 |
| D-019 | não julgamos | PDO | vigente | regra |
| D-020 | Jurídico de precaução | PDO; D (juridico); O (Faltas viram cartões) | vigente | regra; K-201 |
| D-021 | GitHub público na conta Indalt; Google só se necessário; fechar no futuro | PDO; P (lugar e visibilidade, insumo 3, item 4) | vigente | regra; K-010 |
| D-022 | critérios de prática cultural vêm da lei | PDO; D (CLB situada) | vigente | regra; K-104 |
| D-023 | medir e parar; 300 mil por semana em agentes "na operação da fase 1" | PDO; o brief aplica o teto aos agentes das sessões de trabalho e põe as rotinas na mesma guarda (brief l. 37 e 194); P (calibrar) | vigente na guarda; o número foi substituído pela D-040, em pontos da conta, e a leitura A-13 também | regra; K-002, K-005; V-30 |
| D-024 | legado: só o verificável; nada se apaga | PDO; D (Passo 3) | vigente | regra; K-117 |
| D-025 | regras "de início" e proporcionais; revisão de essencialidade | PDO; P | vigente | K-009 |
| D-026 | fase 1 só Vicente e agentes; segunda leitura | PDO | vigente; a amostra se relê pela D-037 | A-04; V-28 |
| D-027 | o planejamento da v0.2 rodou em esforço máximo, ultracode e thinking; a execução roda em esforço médio, sem ultracode; subagentes Sonnet alto; modelos por teste | D e O (configuração da execução e, pelo bloco 12, das rotinas); P (a configuração das rodadas não está fixada: A-12, K-002) | vigente | A-12; K-002, K-115; V-34 |
| D-028 | a execução não para para aprovar o decidido | PDO | vigente | regra |
| D-029 | agentes em `.claude/`; só o Claude Code os opera | PDO; D | vigente | regra |
| D-030 | o log diz o alcance | PDO; D (log no bloco 1); O | vigente | regra; K-101 |
| D-031 | piloto: cajuína, a partir do caju | D | vigente | K-106 a K-110; V-21 |
| D-032 | o piloto usa tudo; rotinas procuram CLB em geral; piloto não é publicação | D; O | vigente | K-101 a K-116; V-11, V-15, V-22 |
| D-033 | GitHub como repositório; outra nuvem se ele impedir | O; P (fornecedor por decisão) | vigente | K-002, K-112; V-12, V-16 |
| D-034 | modo de trabalhar; valores provisórios; precedência da 6A | PDO | vigente (prazo pela D-035) | V-03, V-04 |
| D-035 | finalizar a v0.2 é construir e testar; sem versão nova na execução; insumos; uma tarefa por vez | PDO | vigente | o quadro; K-004 |
| D-036 | três frentes, quadro kanban, rodadas com teto próprio | PDO | vigente | o quadro; K-001, K-002; A-01, A-12, A-13; V-02 |
| D-037 | base sem revisão de rotina; Vicente só por conflito ou Falta a liberar; amostra audita a ferramenta; sugestões na fase 2; script de menções | O (cartões de conflito e de Falta; rodar a amostra); D (K-102); P (o que a amostra acha; sugestões, K-008) | vigente; o "substitui" (a cota serve a conflitos, Faltas e auditoria da ferramenta) convive com a diretriz 1 (nada mais chama Vicente): A-04 | K-102, K-201, K-003; A-02 a A-10; V-06, V-07, V-09, V-14, V-24 |
| D-038 | regra-mãe: a ferramenta decide os itens pela regra, e Vicente decide as regras; os padrões e as leituras do K-003 aprovados; estrutura fixada (estados do modelo, versão da regra em toda decisão automática, quem propõe não aprova com o papel trocável); números provisórios até o K-005; kit e F-0003 no K-114 | PDO; D (blocos 1, 2, 5, 7, 8 e 10); O (cartões, junção); P (calibração, K-005) | vigente, registrada em 22/10 no fechamento do K-003 | K-003, K-005, K-101, K-104, K-114; A-03 a A-06, A-09, A-10; V-37 |
| D-039 | a CLB pelo termo enquanto ele não for ambíguo, com lugares, grupos e períodos como dados; nenhuma fonte como verdade única, nem a institucional; a valência mede lastro, trecho localizado e voz; no piloto, toda a cajuína que as fontes mostrarem; só CLB de outro termo vira candidata, num único cartão de lista | PDO; D (bloco 2, unidade da ficha e valências; blocos 7, 8 e K-102); O (cartão de lista) | vigente, registrada em 22/10; ajusta o A-09 b e a forma do cartão da D-037 (4) | K-104, K-109, K-110, K-102; A-09; V-20, V-38 |
| D-040 | o ritmo em pontos percentuais da conta: projeto até 60 pp por semana (três frentes), desenvolvimento até 50, planejamento o resto, conta nunca acima de 90%; a conversa não para antes do teto; a guarda é não perder trabalho (commit e push a cada lote; janela de 5 h informada ao abrir; acima de 70%, só um lote); teto de manutenção do fim do K-113 no K-002; muda só o que está em vigor | PDO; D (seção 0 do brief; K-123); P (K-002, K-005) | vigente, registrada em 23/10 no fechamento do K-005 | regra; K-005, K-123, K-002 |
| D-041 | no `localizar_trecho.py`, negação e sentido contrário batem exatamente, e a semelhança tolera só OCR e grafia; em μ e λ só conta Evidência com trecho localizado e leitura fiel, cada linhagem uma vez, e a linhagem com Evidência a favor e divergente vira tensão interna sinalizada; regras com versão e recálculo por script | D (K-123; blocos 7 e 8); P (K-005) | vigente, registrada em 23/10 no fechamento do K-005; no registro e nos scripts pelo K-123 | K-123, K-109, K-110; insumos 34 e 36 |

## 8. Ordem dos cartões e por quê

- **Planejamento:** K-001 (esta rodada) → **K-003** → **K-005** (1ª passada, 23/10, por escolha de Vicente) → **K-002** → K-006 → K-005 (3ª passada) → K-004 → K-007 → K-010 → K-008 → K-009.
  - O K-003 vem antes do bloco 1 porque o bloco 1 muda o `executar-brief` "com o ritual da l. 512" (brief l. 173), que a D-037 relê (A-02), e porque a retomada tem de começar pelo quadro (A-01). Ele acerta o brief, põe no roteiro uma nota de ajuste (rot. l. 17, 101, 120, 176 e 185) e diz o que muda em `.claude/` (curador, avaliador, extrair-evidencia, executar-brief), que o K-101 grava. Leva a Vicente os quatro pontos em aberto: A-04, A-05, A-09 (b) e A-10.
  - O K-002 vem antes do K-113: a operação com IA depende da escolha da IA da operação (D-036, diretriz 4). A configuração, a cadência e o teto do planejamento (A-12, A-13) também valem já para a rodada seguinte.
  - O K-005 espera medidas: o insumo 4 pede o teto e a regra de folga "calibrados pela medida". Entra depois dos blocos 1 a 3 medidos, ou na primeira Parada (b). A 1ª passada (23/10) deu as D-040 e D-041; a 2ª, que traria as regras dos insumos 34 e 36 antes do K-109, ficou dispensada pela D-041; a 3ª vem depois do K-110, quando os blocos 7 e 8 e as horas do bloco 13 trazem medida para os números da D-038 e do registro.
  - O K-004 vem depois do relatório do piloto (K-116): é a D-035 e o destino do insumo 1.
- **Desenvolvimento:** **K-103** → K-101 → K-104 → K-105 → **K-123** → K-106 → K-107 → K-108 → K-109 → K-110 → **K-102** → K-111 → K-112 → K-113 → K-114 → K-115 → K-116; depois do piloto, K-117 a K-122, a detalhar pelo K-004.
  - O K-123 vem antes do K-106: o bloco 4 é o primeiro com agentes depois da D-040, e a conta de cada conversa passa a ser feita por script; e o K-109 (bloco 7) e o K-110 (bloco 8) usam o `localizar_trecho.py` e o `calcular_mu_lambda.py`, que têm de rodar com as regras da D-041.
  - O K-103 vem antes do K-101: a D-036 pede que toda sessão termine com insumos novos, num formato fixo, e habilidade nova só carrega em sessão nova (insumo 5). Pronta antes, o bloco 1 a liga no `executar-brief`.
  - O K-102 vem depois do K-110 e antes do K-111: o script compara o texto processado (bloco 7) com o registro de Termos (bloco 4, atestados no bloco 8) e liga a menção no grafo (bloco 8). Entra no harness com um caso que passa e um que reprova em `rodar_testes.py`, como os scripts do bloco 3 (brief l. 228-229); o brief só pede par real para habilidades (l. 311). A posição vem da D-037 ("durante o processamento normal de cada CLB"), que o brief não conhece, e de o harness estar completo quando Vicente aprovar o K-111.
  - Os blocos seguem a ordem do brief (D-035): a 10a depois do bloco 9; a 10b e o bloco 12 depois da aprovação do bloco 9; o bloco 13 é registro desde o K-108.
- **Operação:** o K-201 espera o guia da Lei 9.610 (K-109) e a decisão de lugar e visibilidade de Vicente (K-010).

## 9. Onde o quadro mora (conclusão do K-001)

A D-036 (diretriz 1) deixou ao K-001 dizer se o quadro migra para as Issues e o Projects do GitHub; o insumo 14 traz a questão da porta de contribuição na fase 2.

- **Na fase 1, o quadro fica no arquivo `trilhas/planejamento/quadro.md`.** O plano responde (D-034):
  - princípio 11 (l. 135-136): tudo fica na pasta e no repositório, em arquivos legíveis por qualquer IA, e o projeto se reconstitui só por eles. O quadro em arquivo volta num `git clone`; se o clone traz as Issues e o Projects, o lote C3 não conseguiu conferir (C3.4, "não conferido");
  - princípio 16 e §5.1 (l. 409, chaves fora da pasta): para uma rotina do Actions mover cartões no Projects, o `GITHUB_TOKEN` não serve; a documentação recomenda um token pessoal para projeto de usuário (C3.2, oficial). Seria uma chave da conta de Vicente a mais, guardada e renovada. No arquivo, o agente move o cartão por commit, com a trilha do Git (acordo 4);
  - D-026 e §5.4 (l. 442): a fase 1 não recebe contribuições externas; a porta que o Projects abriria não tem uso agora.
- **Na fase 2, a porta de contribuição pelo quadro é o K-008.** Lá entram os fatos que ficaram "não conferido" no lote C3: gratuidade do Projects no plano Free (C3.1), disponibilidade dos formulários de issue no plano Free e conta exigida para abrir issue (C3.5), autenticação da GraphQL (C3.3) e o clone (C3.4). Entram também a triagem jurídica (LGPD e nome de usuário público, consentimento no formulário) e o caminho de quem não usa GitHub (o formulário público do §5.4). Fica como ideia, sem decisão, um espelho do arquivo em Issues por script, com o arquivo como fonte.
- **Fatos do lote C3 que valem já** (`rodadas/2026-10-21_K-001/lote-C3.json`, oficial): o `GITHUB_TOKEN` não acessa Projects; um projeto tem até 50.000 itens e 50 campos; a API REST lê dados públicos sem autenticação, até 60 pedidos por hora; os formulários de issue são arquivos YAML em `.github/ISSUE_TEMPLATE`, rotulados "public preview" na página. Ressalva do lote: as citações vieram pelo extrator da ferramenta WebFetch (um modelo pequeno devolve o trecho), não da página crua.

## Trilha

- **Lido nesta rodada (sessão principal):**
  - Fundação: l. 1-93, 94-215, 216-360, 361-644, 645-800, 801-932; cabeçalhos do Anexo C, início do C.3, Anexo D, início do Anexo E e contagens por `grep`;
  - brief inteiro; roteiro, l. 1-40 e 124-221;
  - `trilhas/insumos-planejamento.md`; D-033 a D-037 (essência e diretriz); `estado-planejamento.md` e `quadro.md`; checklist do piloto; fim do log do curador de 17/10 e o de 18/10;
  - itens e mudanças de plano do `mapa-decisoes-e-perguntas.json`; `falta-F-0003.json`; o agente auditor e as habilidades conferir-fato e verificar-fundacao (tamanho e cabeçalho); `orcamento.py`, `registrar_log.py` e os esquemas de log e de conferência;
  - `grep` das linhas que as D-036 e D-037 tocam no brief, na Fundação e em `.claude/`.
- **Fora:** o corpo do Anexo C (só o cabeçalho, o início do C.3 e a contagem de "não conferido") e do Anexo E (só o início e a contagem de linhas); os Anexos A e B; o roteiro, l. 41-123 (etapas, que o brief detalha); os demais mapas de 17/10 e a verificação daquela rodada; `legado/`; a web, salvo o lote C3.
- **Checagem por script, sem IA** (`rodadas/2026-10-21_K-001/checar_mapa.py`): cada decisão, insumo, bloco, subseção da Fundação, linha do §8, pergunta do §10 e linha da 6A tem destino; os cartões, os V e os A citados existem.
- **Agentes:** auditor no lote C3 (conferir-fato): 31.342 tokens, 11 chamadas. Verificação deste mapa por três auditores (Sonnet 5.5 alto), um por fatia (brief e quadro; Fundação e próxima versão; decisões, insumos e atritos), no workflow `wf_beec673c-cdd`: 267.700 tokens, 41 chamadas. Dos 30 achados, 29 foram aceitos (um deles em parte) e 1 descartado. O detalhe está no relatório da rodada (`rodadas/2026-10-21_K-001/relatorio.md`).
