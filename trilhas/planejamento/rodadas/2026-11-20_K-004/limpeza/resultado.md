# Limpeza dos insumos abertos (K-004, etapa 1, D-058)

Gerado por `limpeza.py resultado` (limpeza-0.1), sem IA, de `proposta.json`, `releitura-R*.json`, `ajustes.json` e `cruzamento-cego.json`. Nenhum insumo foi alterado nem apagado.

- Abertos antes da limpeza: 82 (de 142; os outros 60 já saíram por script na etapa 1).
- **Ficam: 32**. Juntados a outro insumo, a um cartão ou a um V: 29. Saem resolvidos: 6. Saem por não serem problema da promessa: 15.
- Regra: D-058: o insumo repetido se junta ao que já trata do assunto; o que não é problema de fato para a ferramenta cumprir o que promete (coletar, receber pelas formas da fase 1, organizar no wiki, gerar os grafos 4D, criar propostas sob demanda, tudo rastreável até a origem) sai da fila, com o motivo; nada se apaga.

- Refutados na releitura e de volta à fila: 101, 135, 139.

## Leitura do curador: como os problemas se acumularam

- Leitura do curador, sobre o que a releitura e o cruzamento cego mostraram; não é decisão.
- A hipótese de Vicente se confirma: dos 82 abertos, 50 saem da contagem (29 se juntam ao que já trata do assunto, 6 já estavam resolvidos e 15 não são problema da promessa da fase 1) e 32 ficam, em 12 famílias. As famílias, não os insumos, são o tamanho real da fila que a etapa 5 vai montar.
- O mesmo problema foi anotado de novo à medida que a construção avançava, cada vez por um cartão: a medida de tokens (15 no K-001, 43 no K-106, 136 no K-116); as Consultas que não acham outras CLB (21 no K-003, 103 no K-112, 140 no K-116); a regra de conhecimento tradicional (66 no K-109, 87 e 90 no K-110, 124 no K-115a); a proteção do main (insumo 3, item 3, na 6C; 113 no K-112; 126 no K-113); a Falta de busca (45 no K-107, 55 no K-108).
- Fechar o insumo quando o cartão fecha não prova que o problema acabou: o agrupador cego achou 15 abertos que repetem um insumo fechado cujo problema continuou depois do cartão (entre eles 137 e 47, do K-108; 54 e 44, do K-108; 140 e 118, do K-113; 97 e 89, do K-111; 141 e 60, do K-002; 136 e 5, do K-101). O lista_abertos.py fecha pela coluna do quadro, não pelo problema; isso vale ler junto com a etapa 5, que dá o destino de tudo de uma vez.
- Outra parte do acúmulo são regras e números que a construção teve de criar onde o plano não dizia, e que a ferramenta usa sem a aprovação de Vicente nem a calibração pela medida: a cadência das rotinas (101), as listas e perguntas da triagem fixa (53, com o 67 e o 124), a regra das Consultas gerais (103, junto ao 140), os limites da vistoria (135) e o ritmo do Internet Archive (102). Vários moram em scripts, fora do registro de valores.
- Pelas próprias palavras dos insumos, cinco dos 32 tocam a operação com IA em escala que a D-058 libera depois da fila: a principal protegida por regra (126, com o 113), a colisão de IDs entre camadas (129), a amostra que audita cada lote e camada (70), o custo da rodada medido e o lote calibrado (132) e a tabela de nomes ao alcance da rotina (128). É leitura para a etapa 5 e para o [ABERTO] da D-058, não decisão.
- O agrupador cego marcou o 94 (passo de limpeza da ferramenta) e o 135 (vistoria da casa) como fora da promessa; ficam por serem pedido de Vicente (94, de 30/10) e porque a releitura do 135 o deixou na fila. Se arrumar a casa conta como parte do que a ferramenta promete é regra, e a regra é de Vicente.

## O que fica, por família

### A. Medida e custo (4)

- **132** (com 38, 127): O custo da rotina com IA está medido só pelos tokens dos agentes (a sessão da rotina sem medida, a nuvem fora do hook), e o número de lotes por rodada (1) não está calibrado pelo uso medido da conta; a fonte longa não cabe num lote.
- **136** (com 15, 43): O consumo de tokens não tem medida única: a linha do curador soma os subagentes (conta em dobro), o Workflow mede diferente do Agent, o agente retomado conta a releitura, e a tabela da conta mistura medido e estimado.
- **139**: A tabela 'Semana da conta' do checklist é lida por duas cópias da função numero() (orcamento.py e relatorio_piloto.py), com o medido e o estimado na mesma célula; não há leitor único.
- **141** (com 93): O custo por Entrada e por CLB não é medido por parte (leitura da fonte, peso do agente, escrita), e não se testou montar ficha e grafo por script a partir das Proposições; Vicente quer a ferramenta quase independente de IA (essência ainda a confirmar).

### B. Rotinas: segurança, continuidade e auditoria (5)

- **70**: A amostra sorteada tem por universo tudo o que se produziu desde a anterior (amostra-0.2), e não o lote nem a camada: o acúmulo dilui o lote, e a amostra da camada 2 mistura Entradas da camada 1 (parte do 130).
- **101**: A cadência da D-048 roda por uma regra com números que o plano não fixa (o mínimo da linha, a dobra até 28 dias, a volta com novidade), guardados em scripts/agendar.py e ambientes/rotinas.json, fora do registro de valores, sem a calibração pelo rendimento dos primeiros 7 dias.
- **104**: Não se sabe se o agendamento das rotinas no GitHub se desliga depois de 60 dias sem 'atividade' em repositório público, nem se o commit da própria rotina conta.
- **126** (com 113): A rotina com IA consegue gravar direto no main, com a identidade do dono; a barreira é só por instrução, com o vigia avisando depois.
- **129**: As duas camadas das rotinas gravam na mesma faixa de IDs; a colisão se evita pelo horário e se pega no portão.

### D. Achar outras CLB (2)

- **58**: A pré-triagem só lê as formas dos Termos da Consulta; palavras do processo do caju que não são variantes (cajueiro, cajucultura, LCC) ficam fora sem regra que diga o que deve seguir.
- **140** (com 21, 57, 103): As rotinas só acham CLB cujo nome a ferramenta já conhece: a Consulta geral trouxe sobretudo tecnologia de alimentos, nomes de bebidas nativas dão 0, e o alcance de cada Consulta não é medido nem dito.

### E. Ler a fonte (2)

- **68** (com 130): O texto de cada repositório não se lê pela mesma via (DSpace 7 em Angular sem link do PDF, servidor fora do ar, PDF em imagem, agregador que só dá o link de origem), e o que não se lê nem sempre vira Falta com caminho.
- **69**: PDF com fonte mal mapeada dá texto com caracteres trocados ('pedœnculo'); o trecho localiza exato contra o texto errado e entra assim no acervo, sem aviso.

### F. Coleta: Faltas de busca e retirada (2)

- **49**: A Entrada retirada guarda só id, origem e fundido_em, sem o identificador; o deduplicar.py não olha 'retirado', e a coleta seguinte recria o item. A regex de barreira das fichas é mais estreita que o vocabulário delas.
- **55** (com 45): A Falta de busca (interrompida por teto, total desconhecido) entra como 'outro', sem tipo próprio, e não se encerra quando o Recorte se completa.

### G. Registros e relatórios fiéis (4)

- **46**: A Execução descartada não se marca no log, e IDs de registro foram reemitidos por outra Execução (RC-0001 a RC-0007): a trilha diz uma coisa e o acervo outra.
- **63**: O relatório do lote conta as Entradas pela Execução que as criou ou pela data; a triagem muda Entradas antigas, e o relatório diz 0 (o curador completou à mão).
- **111**: No relatório do dia, os commits da ramificação rotinas à frente do main se contam antes do commit da própria rodada (um a menos).
- **137**: Os 69 ambientes seguem 'não iniciado' e 'proposto', embora a rotina consulte quatro todo dia; nada calcula o estado do Ambiente dos seus Recortes (o mesmo do 47, fechado pelo K-108 sem o cálculo).

### H. Acesso às fontes (2)

- **52**: A proibição expressa dos termos de uso barra agora (D-042), mas a ficha de acesso a guarda em texto livre e nenhum script a lê; só o robots.txt se cumpre por máquina.
- **112** (com 109): O [ABERTO] da D-049: se 'intervenção humana' alcança a busca à mão, o pedido de acesso a instituição, a entrada por link, a leitura de termos no navegador e a caixa dos Alertas; e a fonte cujos termos o robô não lê.

### I. Jurídico: conhecimento tradicional e triagem fixa (2)

- **53** (com 67): As listas e perguntas da triagem fixa foram montadas sem medida (substâncias, modo de preparar, palavras de conhecimento tradicional), com normas não conferidas na fonte oficial.
- **87** (com 66, 90, 124): Não há regra geral de conhecimento tradicional para as CLB seguintes: a D-047 vale só para a cajuína e a D-057 só para as três candidatas; a proposta de Vicente é avisar sempre da lei e do caminho em cada uso, sem barrar a descrição do saber público.

### J. Pessoas citadas (2)

- **77**: O avaliador juntou formas do nome de uma pessoa num só código por idade, data e município, sem regra que diga quando a junção vale nem quem confere.
- **128**: A tabela código → nome das pessoas citadas fica na máquina de Vicente; a rotina com IA não a alcança, e a Entrada com fala direta de pessoa fica em bruto, à espera de conversa.

### K. Receber (portas da fase 1) (2)

- **61**: As portas da fase 1 que dependem de Vicente (busca assistida e link ou documento trazido por ele) são comandos de terminal; um link só entra por uma conversa de trabalho.
- **62**: A oralidade gravada em acervo público é porta aberta (§5.4), mas a ferramenta não transcreve: o trecho vira Falta, e a W, que se ancora na fala de quem pratica, fica Falta.

### L. Regras de organização (Termos e CLB) (2)

- **97**: Não há regra para a Proposição cujo trecho não nomeia termo e cujo contexto aponta outra CLB (a PR-0412 ficou na cajuína, em dúvida).
- **123**: Nenhuma regra escrita diz se Evidência de leitura divergente abona o nome do Termo (o registro real a deixa fora; o teste em Haiku a usou).

### M. Casa e harness (3)

- **94**: Cada cartão deixou no código e na trilha passos, comentários e arquivos que serviram ao caminho e não à forma final; Vicente pediu um passo de limpeza ao fim do piloto.
- **105**: Agente ou habilidade cujo cabeçalho YAML não carrega some sem aviso (o rastreador ficou fora de 30/10 a 05/11); a suíte e o portão não percebem.
- **135**: A vistoria da casa (scripts/manutencao.py) rodou uma vez, à mão: falta decidir quando ela roda sozinha; os limites provisórios estão no script e não no registro de valores; a seção de decisões do AGENTS.md pesa em toda conversa e em todo agente (só Vicente pode encurtá-la); o scripts/resumo_coleta.py não é chamado; a ramificação remota claude/rotina-ia-2026-11-13 sobrou.

## O que se juntou

| Insumo | Junta a | Motivo | Releitura |
|---|---|---|---|
| 1 | proxima-versao.md | É a lista do que a v0.2.1 levaria ao texto; o proxima-versao.md nasceu dela no K-001 e a detalha nos V-01 a V-38 (precedência no V-03, rotinas e Actions no V-11, saída de reserva no V-12, IA por rotina no V-16, §8 no V-27, §9 no V-28, §10 no V-29). É a entrada da etapa 6 do K-004 (escrever a Fundação), não conserto da ferramenta. | confirma |
| 2 | V-36 | O pedido ao redator já preparado está no V-36, que o põe como entrada da escrita com o teto, os validadores e a verificação pelo auditor. | confirma |
| 3 | V-12; V-13; V-20; V-23; V-29; V-30; K-005; K-010; K-120 | Os 11 itens da 6C foram distribuídos no K-001 (mapa §6): 1 → K-005; 2 → K-004 com a D-037; 3 → K-113 (concluído) e V-12; 4 → K-010 e V-12; 5 → V-13; 6 → V-23 e K-120; 7 → K-111 (concluído); 8 → K-002 (concluído); 9 → V-20; 10 → V-20 e V-30; 11 → V-29 e V-13. Cada parte está num cartão ou num V. O que o K-113 deixou do item 3 (a principal protegida só por instrução) é o 126, que fica. | confirma |
| 10 | K-006 | É o próprio K-006 (agente de melhorias e contribuições, com consolidar-para-planejamento, preparar-tarefa, medir-custo e triar-contribuicao); a primeira habilidade, registrar-melhoria, foi feita no K-103. O K-006 entra na reunião do K-004 (D-046). Ferramenta do planejamento, não da promessa. | confirma |
| 11 | V-35 | Está no V-35: o checar_fundacao.py volta a cobrar as D-031 em diante quando a próxima versão sair. | confirma |
| 15 | 136 | Mesmo problema: o consumo de tokens não tem uma medida só (o número do Workflow não é o do Agent). O 136 pede 'uma única medida de tokens por agente, sem dupla contagem e sem consumo perdido' e já cita o workflow de 17/10 entre os consumos que só existem na linha do curador. | confirma_em_parte |
| 18 | K-006 | O script do planejamento que confere o mapa e o quadro a cada rodada é do K-006 (o quadro o lista na origem). Ferramenta do planejamento, não da promessa. | confirma |
| 21 | 140 | Mesmo problema: a ferramenta só percebe CLB cujo nome já conhece (o script de menções só vê os Termos do registro). O 140 pede as rotinas achando CLB nativas e de outros termos e diz que complementa os insumos 21, 103 e 118. | confirma_em_parte |
| 22 | K-006 | É o mesmo script do 18 (checar_mapa.py), que o mapa já leva ao K-006 'com o insumo 18'. | confirma |
| 23 | K-115c; V-24 | Resolvido em parte: o avaliador, que produz as Evidências, passou a Haiku 5.5 no K-115a, e o auditor, que relê, segue em Sonnet 5.5 (D-055, D-056: o avaliador propõe, o auditor relê). O que resta (o auditor no mesmo modelo do arquivista e do juridico) é o teste do K-115c, estacionado para a reunião do K-004, e o texto do V-24. | confirma_em_parte |
| 38 | 132 | Resolvido para as conversas: a leitura de uso vem da linha [Uso do plano] do hook (oficial quando há, estimada senão), sem perguntar a Vicente e separada por pasta (AGENTS.md, Orçamento). O que resta é a rodada da rotina na nuvem, que o hook não vê: o mesmo problema do 127, que se junta ao 132. | confirma |
| 43 | 136 | A conta do agente retomado é parte da medida única de tokens por agente (136): o mesmo lote medido igual, aberto ou retomado. | confirma_em_parte |
| 45 | 55 | Mesmo problema: a Falta de busca não existe como tal no contrato da Falta (sem tipo próprio nem estado de encerramento); o conserto é um só, no contrato. O 55 é o mais completo (dita enquanto vale e encerrada quando o Recorte a resolve). | confirma |
| 50 | V-39 | É alinhamento do texto (Fundação, l. 509; brief, bloco 5) à D-043 e à D-048, que tirou a captura nova do plano; o wayback.py já segue as decisões. O proxima-versao.md ainda não tem essa linha: entra como V novo na etapa 6. Não é conserto da ferramenta. | refuta |
| 57 | 140 | O que cada fonte faz com o termo (se a BDTD reduz 'cajuína' a 'caju') é parte do alcance de cada Consulta medido e dito (140, D-030): saber o que a busca alcança antes de ler o rendimento como dado sobre a CLB. | confirma_em_parte |
| 66 | 87 | Mesmo problema: a regra de conhecimento tradicional para as CLB além da cajuína. A D-047 resolveu só a cajuína; a menção histórica a uso indígena em fonte publicada é o caso típico da regra geral que o 87 pede. | confirma |
| 67 | 53 | Mesmo problema: as perguntas e listas da triagem fixa calibradas com o que o piloto mostrou e com a norma conferida; a bebida alcoólica é a pergunta que falta. | confirma_em_parte |
| 75 | K-005 | A fonte longa que não cabe numa chamada é parte do lote calibrado pelo custo medido (132): a regra de lote dizendo como dividir e quanto custa, dentro dos tetos da rotina com IA (D-050). | confirma_em_parte |
| 90 | 87 | Onde fica o detalhe de uma prática com dúvida de conhecimento tradicional é parte da regra geral (87); hoje só a cajuína (D-047) e as três CLB do K-126 (D-057: detalhe de saber indígena na pasta local) têm leitura. | confirma |
| 91 | K-126 | O K-126 (D-057) leva as três CLB por 'tudo o que a ferramenta oferece', com 'Termos pela regra de termos', e cita o insumo 91 na origem: os Termos atestados ganham as variantes das fontes, e a varredura de menções se refaz com eles. | confirma_em_parte |
| 93 | 141 | Mesmo rumo: a IA só onde a regra e o script não alcançam (141); o juridico por regra e script, juntando item, fonte, norma e dúvida para um corpo jurídico, é um dos casos, dito no 141. | confirma_em_parte |
| 102 | K-208 | O ritmo que o Internet Archive aceita só volta a importar se a F-0034 (termos não lidos pelo robô; vale agora) se liberar, e isso depende do [ABERTO] da D-049, que é o 112 (com o 109). | confirma_em_parte |
| 103 | 140 | Mesmo problema, e o 140 o cita: Consultas gerais que achem CLB de outros termos sem escolha manual de palavras. | confirma_em_parte |
| 109 | 112 | A D-049 pôs a fonte cujos termos o robô não lê no mesmo [ABERTO] do alcance de 'intervenção humana' ('a fonte cujos termos o robô não lê (insumo 109)'); a leitura de termos no navegador é um dos casos do 112. | confirma |
| 113 | 126 | Só vale quando houver outra pessoa com escrita no repositório (fase 2); o CLAUDE.md já diz que a proteção volta a exigir pull request então (K-008). | confirma_em_parte |
| 124 | 87 | A releitura da premissa da D-047 diante de atribuição histórica de origem ('foi desenvolvida pelos indígenas') é parte da regra geral de conhecimento tradicional (87). Vão junto, ditas no 87: a lista da triagem fixa sem 'índios' e 'indígenas' (também do 53) e o exemplo da triagem-juridica que cita um guia que não existe (conserto de harness). | confirma_em_parte |
| 127 | 132 | Mesmo problema: medir o custo de cada rodada da rotina com IA em pontos da conta, para calibrar os lotes dentro da D-050 (132). | confirma |
| 130 | 68 | A leitura do agregador (só pelo link de origem, às vezes em host vedado; a página de verificação gravada como texto) é o mesmo problema do 68: ler cada fonte pela via que ela permite e dizer o bloqueio como Falta, nunca gravá-lo como texto. A parte da amostra da camada 2 é a do 70, dita lá. | confirma_em_parte |
| 131 | K-126 | A EN-1066 é uma das 7 Entradas do K-126 (D-057), com o detalhe na pasta local. A primeira junção positiva da rotina com IA é a primeira execução em escala, que a D-058 já põe depois da fila: não há conserto a fazer antes dela. | confirma_em_parte |

## O que saiu

| Insumo | Como | Onde segue | Motivo | Releitura |
|---|---|---|---|---|
| 4 | resolvido | D-040; K-123 | O ritmo em pontos da conta foi aceito por Vicente na 1ª passada do K-005 (D-040), sem a folga de 2× (orcamento.py, K-123); o piloto foi entregue (D-056). O que resta de calibração com medida nova é a 3ª passada do K-005, que já é cartão. | confirma |
| 6 | resolvido | K-123 | As estimativas de lote saem da medida, por agente e habilidade: o orcamento.py toma a última medida do mesmo agente com a mesma habilidade nos logs (K-123). | confirma |
| 9 | fora da promessa | K-008 | Contribuição de outras pessoas com os próprios tokens é da fase 2 (K-008, depois do K-007); a fase 1 é só Vicente e os agentes (D-026). | confirma |
| 14 | fora da promessa | K-008 | O lugar do quadro na fase 1 foi decidido no K-001 (concluído: o quadro mora no arquivo); Issues, Projects, formulários e a LGPD do contribuidor são a porta da fase 2 (K-008). | confirma |
| 16 | resolvido | K-123 | A estimativa sai por script dos logs, por agente e habilidade, antes de cada lote, também no planejamento (orcamento.py com --frente planejamento; K-123). | confirma |
| 34 | resolvido | D-041; K-123 | A regra diz quais Evidências entram: só a de trecho localizado e leitura fiel; a divergente ou não localizada fica visível, fora da conta (D-041). Está no registro (mu-lambda-0.2) e no calcular_mu_lambda.py, que lê a versão do registro (K-123). | confirma |
| 36 | resolvido | D-041; K-123 | Negação e sentido contrário batem exatamente (normalizacao-0.2; localizar_trecho.py, l. 53), e cada linhagem conta uma vez, com a linhagem mista sinalizada como tensão interna, fora de μ e λ (mu-lambda-0.2). | confirma |
| 42 | fora da promessa | K-122 | A exportação do Termo para TBX e SKOS é da fase 2 (K-122: 'exportações SKOS, TBX e PROV'); o Termo da fase 1 funciona sem ela. | confirma |
| 54 | fora da promessa | — | A coleta da BDTD se completa: o recorte.py detecta a página repetida depois do item 1.000 e divide a janela; com o limite_fonte nulo, só faz pedidos a mais antes de perceber. Não impede a promessa. É o mesmo do 44, fechado pelo K-108 sem o limite gravado. | confirma |
| 56 | resolvido | D-048; F-0034 | Superado: a D-048 tirou das rotinas diárias a consulta da cópia da página do registro, e a F-0034 barra agora a consulta automática do Internet Archive (Availability API e leitura da cópia). As rotinas não chamam o wayback.py, e as centenas de Faltas 'sem cópia arquivada' não nascem. | confirma |
| 59 | fora da promessa | D-045 | Não é problema hoje: as pegadas somam 9,4 MB em 50 arquivos e o .git 13 MB, longe do alarme de 200 MB da D-045, que o relatório do dia já vigia. | confirma |
| 64 | fora da promessa | K-010 | A Falta de licença ausente é do ato publicar (as 103 nem foram gravadas); se ela é por obra, por registro ou coberta pela F-0003 se decide com a licença do acervo no K-010. | confirma |
| 65 | fora da promessa | K-010; F-0025; K-204 | A forma da citação com o autor da obra é questão da F-0025 (direito autoral), que espera a decisão de publicar (K-204, K-010); o Git público segue o padrão da F-0003 até o K-010 (D-043; K-201). | confirma |
| 79 | fora da promessa | K-118 | Os plugins do Quartz e os scripts de instalação são decisão do wiki público (Passo 6, K-118); o wiki local, que é a promessa da fase 1, gerou sem eles no K-110. | confirma |
| 85 | fora da promessa | K-010; F-0025; K-204 | Se 448 citações curtas de uma mesma obra, juntas, ficam na medida justificada é questão da F-0025, que espera a decisão de publicar (K-204, K-010). | confirma_em_parte |
| 99 | fora da promessa | — | Não é problema para a promessa: a conferência da camada Educação existe e passa (validar_acervo.py, checar_educacao, educacao-0.1, K-111), sem falha medida; escolher entre item e frase é ajuste de uma regra que funciona. | confirma_em_parte |
| 100 | fora da promessa | — | Não impede a promessa: o texto exato do Trecho fica inteiro e localizado; o corte largo só encurta o contexto em volta, em favor de proteger pessoas (K-111, nomes-0.1). | confirma_em_parte |
| 133 | fora da promessa | K-125 | O Gemini está estacionado pela D-056: a IA da operação é a rotina do Claude; o Gemini volta só com cota paga e decisão nova. | confirma |
| 134 | fora da promessa | K-125 | O Gemini está estacionado pela D-056: a IA da operação é a rotina do Claude; o Gemini volta só com cota paga e decisão nova. | confirma |
| 138 | fora da promessa | K-007 | É a condição 2 do gatilho da fase 2 (horas de Vicente); avaliar o gatilho é o K-007, não conserto da ferramenta. | confirma_em_parte |
| 142 | fora da promessa | — | É do harness do planejamento (habilidade registrar-decisao), não do que a ferramenta promete; o erro concreto já foi corrigido na D-057, e o K-126 cita o insumo 142 na origem. | confirma_em_parte |

## Refutados na releitura (voltam à fila)

| Insumo | Proposto | Motivo da releitura |
|---|---|---|
| 101 | junta | O K-005 não leva a cadência: o escopo escrito dele é 'os números da D-038 e do registro (amostra, fila, lote de máquina, valências)' e a cadência da D-048 não está no registro de valores; os números moram em scripts/agendar.py e em ambientes/rotinas.json, e a rotina diária que o insumo trata é coleta (promessa). |
| 135 | junta | O 94 pede um passo de limpeza único ao fim do piloto (comentários, passos e arquivos temporários sem uso). O 135 junta cinco coisas: quando a vistoria (manutencao.py) roda sozinha, os limites no registro de valores, o peso do AGENTS.md carregado em toda conversa, o script sem uso e a ramificação remota. Só as duas últimas (resumo_coleta.py sem chamada, ramificação sobrada) são resíduo do tipo do 94; o essencial do 135 (vistoria recorrente e peso do AGENTS.md) não cabe no 94. O defeito do peso segue real: o AGENTS.md tem 30.812 bytes e o limite provisório citado é de 24 mil caracteres com o CLAUDE.md. Também o 94 não tem cartão (mapa: 'a definir pelo planejamento'), então juntar não dá destino. |
| 139 | junta | O defeito do 139 (a tabela Semana da conta lida por duas cópias da função numero(), com o estimado na mesma célula) não é o do 136 (tokens dos logs contados em dobro); o conserto de um não resolve o outro. O 'a tabela mistura medido e estimado' só aparece na reescrita da proposta, não no texto original do 136. |

## Confirmados em parte: o que escrever no alvo na etapa 5

A parte que o alvo não cobre não se perde: vai escrita no alvo quando a etapa 5 der o destino de tudo de uma vez (D-046, D-058).

| Insumo | Alvo | Parte não coberta | Onde escrever (sugestão do releitor) |
|---|---|---|---|
| 15 | 136 | A regra de contar o Workflow (entrada do último turno sem a saída, 267.700 contra 329.448) comparável à do Agent: ao juntar, escrever no texto do 136 que a medida única inclui o Workflow. | Juntar ao 136, mas gravar no 136 a cláusula do Workflow; Workflow só roda a pedido (AGENTS.md), então o peso é baixo. |
| 21 | 140 | O script de menções continuar só vendo nomes do registro de Termos (e a restrição 'sem semear Termos fora do plano') não está no texto do 140, que fala das Consultas. | Juntar ao 140, escrevendo nele que o script de menções depende do registro de Termos (K-102 concluído; K-117 é só legado, Passo 3). |
| 23 | K-115c; V-24 | O verificador de modelo diferente do produtor para as saídas do arquivista e do juridico (ambos Sonnet, como o auditor); nem o K-115c nem o V-24 dizem isso no escopo. | Sair da contagem com a nota de que o caso do avaliador está resolvido; levar a sobra (arquivista/juridico contra o auditor) à reunião do K-004 junto ao K-115c, escrita no texto do cartão. |
| 43 | 136 | A regra de escolha entre retomar e abrir agente novo pelo custo medido; escrever no 136 que a medida única vale igual para agente aberto e retomado. | Juntar ao 136 acrescentando a cláusula do agente retomado. |
| 57 | 140 | A verificação concreta do que a busca da BDTD faz com 'cajuína' (radical/AllFields) não está escrita no 140; sem ela o rendimento de CO-0002 segue sem leitura. | Juntar ao 140 acrescentando 'conferir o que cada fonte faz com o termo (BDTD, caju x cajuína)' como parte do alcance. |
| 67 | 53 | A pergunta nova sobre modo de preparar bebida alcoólica e a norma a conferir (precisa do juridico); nenhum Trecho guardado traz modo de preparar, então é dormente. | Juntar ao 53, escrevendo nele 'incluir a pergunta de bebida alcoólica com norma conferida'. |
| 75 | K-005 | A regra de divisão de uma fonte longa em lotes (o limite de 25 turnos do avaliador e o dossiê de 207 páginas): é desenho de regra, não só calibração de número. | O destino melhor é o K-005, 3a passada (lote de máquina, onde o mapa já punha o 75), não o 132; e escrever lá a regra de divisão. A operação com IA em escala só vem depois da fila (D-058), então não trava a promessa antes disso. |
| 85 | K-010; F-0025; K-204 | A pergunta do conjunto de citações de uma mesma obra não está escrita na F-0025 nem no K-204/K-010. | Sair, desde que a pergunta seja escrita no escopo do K-204 (ou K-010) ao fechar a limpeza. |
| 91 | K-126 | Refazer a varredura de menções incidentais (scripts/mencoes_incidentais.py) com os Termos atestados. | Juntar ao K-126 e pôr a nova varredura no pronto-quando do cartão. |
| 93 | 141 | Os casos que a regra fixa não resolve ainda dependem da habilidade triagem-juridica com IA e retêm o item; e o pacote organizado para um corpo jurídico externo é fase de publicação. | Sair da contagem registrando que o juridico por regra e script já existe (triagem_fixa.py) e que o resto é publicação (K-201 a K-204); manter a ligação com o 141 para a IA só onde a regra não alcança. |
| 99 | — | A escolha entre regra por item e por frase, e o que conta como frase sobre a CLB; nenhum cartão ou V a leva (a proposta traz alvo vazio). | O K-126 gera a Educação de três CLB e rodará a regra: levar a pergunta para lá como caso de teste, ou ao V-18; sem isso a decisão fica sem dono. |
| 100 | — | Não conferi se o contexto mais curto mantém a localização única dos 72 Trechos (validar_acervo.py não rodou aqui). | Sair; se o validador acusar Trecho não localizável, reabrir. |
| 102 | K-208 | Conferir o ritmo do Internet Archive e gravá-lo no registro de valores não está no 112. | Juntar ao K-208 (junto da leitura dos termos e da página de bots), com o 112 como contexto. |
| 103 | 140 | Lista de genéricos e classe 'bebida' como regra aprovada por Vicente (D-038) e a regra de que a mista só nasce de Termo atestado de outro termo. | Juntar ao 140 acrescentando essa regra no escopo. |
| 113 | 126 | Nenhum cartão ou V cita o 113 no escrito; o vínculo com o K-008 está só no mapa e numa frase do CLAUDE.md. A decisão sobre como a junção da rotina sobrevive à proteção que exige pull request é a mesma conversa do 126. | Sair do 113 como fora da promessa, mas acrescentar o 113 à origem do K-008 e anotar no 126 que a regra de proteção do main deve já prever a volta do pull request. |
| 124 | 87 | A lista de palavras (indígenas, índios) e o exemplo com guia inexistente: a lista vai ao 53; o exemplo é conserto pequeno de harness, fora da promessa. | Premissa da D-047 ao 87; lista ao 53; exemplo como anotação de harness. |
| 130 | 68 | A amostra da camada 2 (não mede só o que a IA produziu) fica no 70, não no 68; o caso Oasisbr/Sucupira com robots vedado deve constar no 68. | Juntar ao 68 (leitura) e ao 70 (amostra), dizendo as duas partes. |
| 131 | K-126 | A primeira junção positiva da rotina com IA pelo portão (sem Vicente) nunca foi exercitada ponta a ponta; é parte da operação com IA em escala, depois da fila. | Juntar a EN-1066 ao K-126 e levar a junção positiva junto do 132 (rotina com IA), como passo de abertura da operação em escala, para não se perder. |
| 138 | K-007 | A escolha de como medir as horas ou de rever a condição 2: o K-007 não a decide, ela só aparece como 'o que falta dito'. | Sair do 138 como fora da promessa, mas ligá-lo também ao K-005 (3ª passada, horas) e escrever no K-007 que a condição 2 precisa de medida ou de revisão antes de avaliar. |
| 142 | — | O conserto da habilidade registrar-decisao (separar a resposta que confirma a lista da que responde parte; o que a sessão põe ou tira por leitura própria volta a Vicente dito como leitura) não tem cartão. | Sair da fila como fora da promessa, mas juntar o 142 ao K-006 (ciclo execução, insumo, planejamento) ou deixar marcado 'processo do planejamento' na reunião do K-004, para não se perder. |

## Ajustes depois da releitura

| Insumo | Fica como | Proposto por | Aprovado por | Motivo |
|---|---|---|---|---|
| 50 | junta V-39 | releitor R1 (criar um V novo e só então juntar) | curador | A proposta juntava ao proxima-versao.md sem linha que levasse o assunto; o V-39 foi escrito no proxima-versao.md (Fundação l. 509 e brief, bloco 5, diante das D-043 e D-048), e o 50 se junta a ele. |
| 75 | junta K-005 | releitor R2 | curador | O lote de máquina está no escopo escrito da 3ª passada do K-005 ('amostra, fila, lote de máquina, valências'), onde o mapa já punha o 75; o 132 não leva a regra de divisão de fonte longa. A regra de divisão vai escrita no K-005 na etapa 5. |
| 101 | fica | releitor R2 (refutação) | não se aplica (o item volta à fila) | O K-005 não leva a cadência no escopo escrito (os números da D-038 e do registro), e a rotina diária é coleta: fica na fila, com destino na etapa 5. |
| 102 | junta K-208 | releitor R3 | curador | O ritmo do Internet Archive só importa quando a F-0034 se liberar; liberar a F-0034 (ler os termos e a página de bots do Internet Archive) é o K-208. O 112 fica como contexto (o [ABERTO] da D-049). |
| 113 | junta 126 | agrupador cego (mesmo problema que o 126) e releitor R1 (anotar no 126 a volta do pull request) | curador | A proteção do main por regra, com a junção da rotina mantida por um caminho que a proteção aceite, é um conserto só: o 126 o pede agora (a rotina com IA) e o 113 na fase 2 (outra pessoa com escrita). No lugar de sair como fase 2, junta-se ao 126, que deve já prever a volta do pull request. |
| 135 | fica | releitor R1 (refutação) | não se aplica (o item volta à fila) | O 94 limpa uma vez o que sobrou; o 135 mantém a casa limpa. Só o script sem uso e a ramificação são resíduo do tipo do 94; o essencial do 135 não cabe nele. |
| 139 | fica | releitor R2 (refutação) | não se aplica (o item volta à fila) | O defeito não é o do 136 (tokens dos logs contados em dobro): o conserto de um não resolve o outro. Fica na fila, perto do 136. |

## Cruzamento cego (agrupador que não viu a proposta)

Temas: 21. Isolados: 23, 79, 104, 105, 123, 129, 142.

- **Fundação e brief atrás das decisões (próxima versão)** (1, 2, 11, 50): O texto da Fundação e do brief ficou para trás das decisões D-031 em diante e só se alinha na próxima versão, que a D-035 manda não escrever durante a execução; cada insumo anota um pedaço do que essa versão levaria.
- **Contagem e leitura do uso (tokens e pp) sem medida única** (15, 38, 43, 127, 136, 139): Não há uma única medida de consumo: o número do Workflow, o do Agent, o do agente retomado, a linha do curador e a leitura em pp da conta divergem, somam em dobro ou dependem de Vicente informar.
- **Custo do lote e teto: estimativa e calibração** (4, 6, 16, 75, 132, 133, 134, 141): O custo real por lote e por Entrada (avaliador, auditor, fonte longa, escala por bebida) fica acima ou fora da estimativa e do teto, e não há estimativa tirada da medida nem calibração do número de lotes.
- **Descoberta de CLB além da cajuína presa a Termos, listas e Consultas gerais** (21, 57, 58, 91, 103, 140): Tudo o que acha outra CLB (varredura de menções, pré-triagem, Consultas gerais) só enxerga o que já está no registro de Termos ou em listas de palavras; fora a cajuína, nenhuma CLB foi do bruto à ficha e as nativas não aparecem.
- **Evidência e Proposição que caem na CLB errada** (97, 131): A extração e a rotina ainda põem na CLB do lote a Evidência ou a Proposição que trata de outro termo, quando o trecho não nomeia a bebida ou quando o termo é ambíguo.
- **Conhecimento tradicional e o jurídico item a item** (66, 87, 90, 93, 124): Falta uma regra geral de conhecimento tradicional para as CLB além da cajuína (o que se barra, onde fica o detalhe, o que se avisa), e cada dúvida do jurídico retém um item até alguém decidir.
- **Lei 9.610: citação, autor e licença (publicação)** (64, 65, 85): A regra olha cada registro ou cada citação, mas a lei e a publicação pedem o conjunto por obra: autor e origem, medida da citação, licença da obra; as Faltas saem por registro e inflam o acervo.
- **Triagem fixa: listas e regras provisórias** (52, 53, 67): As listas e perguntas da triagem fixa (substâncias, modo de preparar, bebida alcoólica, proibição expressa dos termos) foram montadas sem medida, têm normas não conferidas e deixam casos sem pergunta.
- **Acesso a fontes: Internet Archive, Wayback e termos que o robô não lê** (56, 102, 109, 112): O que pode e como se consulta o Internet Archive e as fontes cujos termos o robô não lê (ritmo, captura, cadastro, intervenção humana) está provisório ou sem regra única.
- **Retirada e descarte rastreáveis** (46, 49): O que é retirado ou descartado (Entrada retirada, Execução descartada) não deixa marca suficiente e pode voltar ou reaproveitar ID.
- **Coleta em escala: Faltas de busca, saturação, pegadas e estado dos ambientes** (45, 54, 55, 59, 137): Os contratos e scripts da coleta não modelam a Falta de busca (tipo, encerramento), percebem a saturação tarde, deixam as pegadas crescerem com as janelas e não atualizam o estado dos ambientes.
- **Contribuição de outras pessoas e fase 2** (9, 10, 14, 61, 62, 138): Portas, agentes e medidas pensados para outras pessoas contribuírem e para o gatilho da fase 2; hoje só há Vicente e os agentes.
- **Guarda-chuva e ferramenta do planejamento (K-006)** (3, 18, 22): Um insumo que reúne 11 itens com cartões próprios e a ferramenta sem IA que confere o mapa e o quadro a cada rodada do planejamento.
- **Arrumação do código e da casa** (94, 135): Sobras, temporários e limites provisórios acumulados durante a construção; o pedido é a pasta simples e verdadeira sobre si mesma.
- **Rotina com IA: junção, protegida do main e amostra** (70, 113, 126, 130): A rotina com IA grava no main só por instrução, e a amostra da segunda leitura mistura no universo o que não é produção da IA.
- **Leitura de fontes que devolve página sem conteúdo ou texto degradado** (68, 69): O ler_fonte e o localizador devolvem casca de página, página de verificação ou texto de PDF com caracteres trocados, e a ferramenta nem sempre trata isso como falha dita.
- **Pessoas citadas e dados pessoais** (77, 100, 128): A regra de junção de pessoas, o corte de nomes e a tabela código-nome têm lacunas: junta por palpite, corta demais ou fica onde a rotina não alcança.
- **Regras escritas provisórias à espera de calibração** (34, 36, 99, 101): Regras de contagem e de conferência ficaram provisórias ou ambíguas (quais Evidências entram em μ e λ, por item ou por frase na Educação, números da cadência).
- **Relatórios por script que contam errado** (63, 111): Relatórios calculados por script (do lote, do dia) contam pelo critério ou pelo momento errado e precisam de acerto à mão.
- **Exportação do Termo para TBX e SKOS** (42): O Termo 0.2.0 não marca a designação preferida nem confere a estrutura de TBX e SKOS; a exportação sem perda fica por provar.
- **Casos sem tema comum** (23, 79, 104, 105, 123, 129, 142): Insumos com defeito ou falta própria, sem outro aberto nem fechado que trate do mesmo ponto.

### Pares que o cego viu como o mesmo problema e o resultado deixou em lugares diferentes

| Insumo | Mãe no cego | No resultado | Mãe no resultado | Por que o cego os junta | Decisão |
|---|---|---|---|---|---|
| 2 | 1 | V-36 | proxima-versao.md | O conserto é um só: escrever a próxima versão da Fundação. Insumo 1: 'a próxima versão da Fundação alinhada às decisões D-031 a D-035'; insumo 50: 'a Fundação e o brief seguem com o texto antigo, pela D-035'; insumo 11: 'volta a cobrá-las quando a próxima versão sair'; insumo 2: 'ponto de partida pronto para escrever a próxima versão'. O 1 é a mãe porque lista o conjunto do que a versão levaria; 2, 11 e 50 são partes dele. | Mesmo destino do 1: a lista do proxima-versao.md (o 2 no V-36), material da etapa 6. |
| 11 | 1 | V-35 | proxima-versao.md | O conserto é um só: escrever a próxima versão da Fundação. Insumo 1: 'a próxima versão da Fundação alinhada às decisões D-031 a D-035'; insumo 50: 'a Fundação e o brief seguem com o texto antigo, pela D-035'; insumo 11: 'volta a cobrá-las quando a próxima versão sair'; insumo 2: 'ponto de partida pronto para escrever a próxima versão'. O 1 é a mãe porque lista o conjunto do que a versão levaria; 2, 11 e 50 são partes dele. | Mesmo destino do 1: a lista do proxima-versao.md (o 11 no V-35), material da etapa 6. |
| 50 | 1 | V-39 | proxima-versao.md | O conserto é um só: escrever a próxima versão da Fundação. Insumo 1: 'a próxima versão da Fundação alinhada às decisões D-031 a D-035'; insumo 50: 'a Fundação e o brief seguem com o texto antigo, pela D-035'; insumo 11: 'volta a cobrá-las quando a próxima versão sair'; insumo 2: 'ponto de partida pronto para escrever a próxima versão'. O 1 é a mãe porque lista o conjunto do que a versão levaria; 2, 11 e 50 são partes dele. | Mesmo destino do 1: a lista do proxima-versao.md (o 50 no V-39, criado na limpeza), material da etapa 6. |
| 21 | 91 | 140 | K-126 | A varredura de menções só vê o que o registro de Termos lista. 21: 'só vê as CLB cujo nome está no registro de Termos'; 91: 'a varredura só vê as formas do registro: ... vinho de caju bateu 43 vezes, mas vinho do caju (9) e vinho-de-caju (2) ficaram fora'. O 91 traz a medida e o conserto (Termos atestados com as variantes das fontes, varredura refeita). | Fica junto ao 140: o 91 se resolve no K-126 atestando os Termos de três CLB, o que não resolve o 21 em geral (CLB cujo nome nenhum Termo registra). Na etapa 5, escrever no 140 que o script de menções só vê o registro de Termos. |
| 130 | 70 | 68 | 70 | Mesmo defeito do universo da amostra. 70: 'uma amostra que audite cada lote do que a ferramenta produziu nele, sem que o acúmulo de uma etapa anterior dilua o lote'; 130 (segunda parte): 'a amostra da camada 2 medindo só o que a IA produziu'. O 130 também trata da leitura do Oasisbr (outro assunto, ver o tema de leitura de fontes). | Fica junto ao 68 (a leitura do agregador e o bloqueio dito como Falta); a parte da amostra da camada 2 vai escrita no 70 na etapa 5, como pede a releitura R3. |

### Abertos que o cego marcou como fora da promessa e o resultado mantém

| Insumo | Por que o cego os marcou |
|---|---|
| 94 | Arrumação do código ao fim do piloto, passo do plano e não defeito para cumprir a promessa. |
| 135 | Manutenção da casa (vistoria, tamanho do AGENTS.md, ramificação sobrando), não a promessa da ferramenta. |

### Abertos que repetem um fechado

| Aberto | Fechado | Cartão do fechado | O problema continuou? | Por quê |
|---|---|---|---|---|
| 136 | 5 | K-003, K-101 (o número oficial é o do Agent; o transcript com cache difere) | sim | O 136 (14/11) diz que a regra do CLAUDE.md ('o número oficial é o do curador') e o esquema de log não dizem se a linha do curador é agregado, e as somas contam em dobro (14,75 milhões contra 6,9). |
| 15 | 5 | K-003, K-101 | nao_sei | Ambos tratam de o número do Workflow e o do transcript diferirem do número do Agent; o 15 é de 22/10 e o texto não mostra se persistiu depois do K-101 (o 136 mostra a forma posterior). |
| 42 | 30 | K-106 | sim | O 30 pedia exportação para TBX e SKOS sem perda; o 42 nasce da conferência do próprio K-106 e diz que o Termo 0.2.0 leva a língua mas não marca a designação preferida e que a estrutura do TBX ficou 'não conferida'. |
| 53 | 32 | K-109 | sim | O 32 pedia as listas da triagem fixa calibradas e as normas conferidas; o 53 repete para a versão 0.3 ('montadas pelo curador ... sem medida'), o 67 (29/10) acha caso sem pergunta e o 124 (13/11) diz que a lista não pega 'índios' nem 'indígenas'. |
| 54 | 44 | K-108 | sim | O 44 pedia a saturação detectada pela regra, com o limite da fonte na ficha; o 54, escrito dentro do K-108, diz que o limite_fonte da BDTD segue nulo e a saturação só se percebe depois de 11 páginas. |
| 57 | 39 | K-107 | sim | O 39 dizia que as formas de hífen levam CO-0002 de 25 a 1441 (cajuí-na 1305, quase o total de caju, 1306); o 57 vê o mesmo total 1.441 trazendo só 14 itens que o caju não tinha e ainda não conferiu o que a busca AllFields faz com o termo. |
| 56 | 96 | K-112 (D-048: a consulta da página do registro sai das rotinas diárias) | nao_sei | O 56 (24/10) trata das 84 rodadas e das centenas de Faltas 'sem cópia arquivada'; o vira do 96 diz que essa consulta sai das rotinas diárias, o que provavelmente esvazia o 56, mas o texto do 56 é anterior e não o confirma. |
| 102 | 78 | K-112 | sim | O 78 era o HTTP 429 do Internet Archive; o 102 (05/11, no K-112) diz que o ritmo de 1 pedido a cada 10 s é 'valor provisório, porque a página do Internet Archive sobre ritmo não foi lida'. Continua só o valor. |
| 97 | 89 | K-111 | sim | O 97 vem do próprio K-111: das quatro Proposições do 89, a PR-0412 'ficou na CL-0001 em dúvida' porque o trecho não nomeia bebida nem termo e o contexto aponta outra CLB. |
| 131 | 89 | K-111 | sim | Em 13/11 as Evidências do mocororó (EN-1066) caíram de novo na CLB da cajuína e só o portão da camada 2 as barrou; o texto diz 'o filtro já separa a Evidência de outra CLB', então o conserto é parcial. |
| 131 | 122 | K-113 | nao_sei | As ressalvas A3 e A4 do auditor são 'de leitura fiel do avaliador em Haiku', tema do 122 (erros de leitura fiel que nenhum validador pega); o 131 é do mesmo cartão K-113 e o texto não diz se algo mudou depois. |
| 99 | 80 | K-111 | sim | O 99 nasce do conserto do 80: a conferência da Educação ficou 'por item de lista ... mais leve que a da ficha' e pede que o planejamento confirme ou ajuste a regra. |
| 90 | 84 | K-111 (mas o vira do 84 diz 'a definir pelo planejamento, com o insumo 93') | sim | O 90 pede a regra de onde fica o detalhe de prática com dúvida de conhecimento tradicional, o mesmo ponto do 84 (o saber atribuído a povo nomeado não chega ao Git antes da triagem). |
| 93 | 84 | K-111 (idem) | sim | O 93 cita o 84 ('ligada aos insumos 84, 87 e 90') e o vira do 84 manda o assunto ao planejamento com o 93: o fechamento por cartão parece só formal. |
| 137 | 47 | K-108 | sim | O 47 pedia o estado do Ambiente calculado dos Recortes; o 137 (14/11) diz que os 69 ambientes seguem 'não iniciado' e 'proposto' embora a rotina consulte quatro todo dia, e 'nada atualiza esses campos'. |
| 140 | 118 | K-113 | sim | O 118 pedia a pré-triagem das Consultas gerais segurando o que não é bebida; o 140 (14/11, depois da entrega) conta 205 'suco', 63 'cerveja' etc. na CO-0008 e diz que 'Complementa os insumos 21, 103 e 118'. |
| 132 | 116 | K-113 | nao_sei | O 116 pedia o K-113 dimensionado pelo volume medido nos 20% da semana; o 132 (13/11, dentro do K-113) mede o lote de 15 e ainda pede o número de lotes calibrado, sem dizer se foi feito depois. |
| 141 | 60 | K-002 | sim | O 60 pedia a triagem de todas as Entradas num ritmo e custo previstos; o 141 (15/11) diz que 'o custo de escala por bebida só apareceu depois do piloto' (5 a 7 milhões de tokens para 199 Entradas). |
| 112 | 108 | D-049 | sim | O 108 foi respondido pela D-049; o 112 diz que a D-049 'ficou com o alcance de intervenção humana em aberto' e lista os casos sem resposta. |
| 100 | 76 | K-111 | nao | O 76 era nome de pessoa chegando ao Git pelo Trecho; o 100 cita o 76 e trata de efeito colateral do conserto (a lista nomes_provaveis é larga e encurta o contexto), não de nome vazando. |
