# Os quatro pontos em aberto do K-003 (A-04, A-05, A-09 b, A-10)

**Cartão:** K-003, rodada de planejamento de melhorias de 22/10/2026 (D-036). **Estado:** padrões propostos e corrigidos pela verificação (dois auditores; `verificacao.json`), a aprovar por Vicente junto com o brief ajustado.
**O que é um ponto em aberto:** um lugar onde o texto em vigor (Fundação v0.2, brief de execuções, roteiro) diz uma coisa e a D-037 não responde sozinha (mapa das três frentes, seção 2). O K-001 os deixou para a leitura de Vicente; a D-034 manda dizer aonde se quer chegar, não perguntar o que o plano responde.
**Como ler:** "l." é a linha da Fundação v0.2 (`00_Fundacao_Cultura_Liquida.md`); "brief l." e "rot. l." são linhas do brief de execuções e do roteiro no commit 71dafff, antes dos ajustes desta rodada. "Padrão" é o que vale se Vicente aprovar o brief com os padrões, como nas paradas do brief (brief l. 34); aprovados, os quatro entram no Registro de Decisões (habilidade registrar-decisao), como entraram as partes 2 e 3 da D-034 em 17/10. "Valor provisório novo" é valor que a Fundação não fixa e que a execução usa pela D-034 até a calibração. O texto da Fundação muda só na próxima versão (D-035; K-004).

## A-04 — Quem lê a amostra sorteada, e se ela entra na cota

**O texto em vigor.** A amostra é parte da segunda leitura (l. 76, 200, 376, 396, 667, 795, 861; D-026). No Passo 5, vai "para Vicente, dentro da cota" (l. 752). O brief fixa o tamanho como "o que sobra da cota semanal" e põe o auditor relendo o mesmo número (brief l. 193); nos blocos 7 e 8, o auditor relê a amostra (brief l. 287, 289, 299).
**O que as decisões dizem.** D-037 (2): a amostra audita a ferramenta (harness, validadores, agentes), na trilha de melhorias, e não revisa a base. D-037 (1): nada além de conflito e de Falta jurídica a liberar chama Vicente. D-037, "substitui": a cota passa a servir a conflitos, Faltas a liberar e auditoria da ferramenta.

**Padrão proposto.**
1. **Quem lê:** o auditor, o verificador de outro harness (D-026). Os scripts reconferem primeiro o que tem resposta exata: o trecho relocalizado e o hash comparado (`localizar_trecho.py`) e as ligações (`validar_acervo.py`). O auditor lê só o que script não decide: se a nossa leitura do trecho é fiel (eixo 3), a voz, a regra de valências aplicada, a Falta não completada, as perguntas da triagem jurídica. O harness dele difere do dos agentes que produzem (outro agente, outras habilidades, sem Write); o modelo e o esforço são os mesmos (Sonnet 5.5 alto), limite que o bloco 12 testa (D-027) e que vai como insumo (23).
2. **O que a amostra acha:** cada falha é achado sobre a ferramenta (qual agente, habilidade, validador ou script deixou passar), com o item como exemplo. Vai à trilha de melhorias: `trilhas/insumos-planejamento.md`, pela registrar-melhoria quando ela existir (K-103). Numa conversa de trabalho, vira lote de correção no mesmo bloco, o mecanismo que a brief l. 110 dava à devolução de Vicente, agora com origem no achado da amostra; na operação, cartão no desenvolvimento.
3. **O item afetado** volta ao estado do eixo próprio (eixo 3 em "leitura divergente" se a falha foi de leitura do trecho; eixo 1 se foi de triagem) e é refeito pela ferramenta corrigida; ninguém o corrige à mão. Esquema ou validador novo já reabre o Recorte (l. 592); refazer o item quando o que se corrigiu foi agente, habilidade ou harness é valor provisório novo (D-034), que a próxima versão confirma (V-24).
4. **A amostra sem achado** também vira linha de log: tamanho, semente, itens lidos e zero achados. O K-005 usa essas linhas para calibrar.
5. **Vicente:** não lê os itens da amostra. A parte dele na auditoria da ferramenta, que o "substitui" põe na cota, é ler o que a amostra achou quando a trilha de melhorias chega à frente de planejamento. Isso não é chamado da operação e conta nas horas do bloco 13 como "auditoria da ferramenta".
6. **Tamanho e cota:** a amostra não entra na cota de Vicente; o custo é do auditor, em tokens, dentro do teto da D-023, e é medido. O tamanho é valor provisório novo do registro do bloco 2 (D-034), porque a Fundação não o fixa: até 15 itens por amostra, número emprestado da cota (l. 902) e do lote de máquina (l. 498), sorteados com semente registrada entre o que a ferramenta produziu desde a amostra anterior. Uma amostra por lote nos blocos que produzem itens (7 e 8, como o brief já prevê) e uma por semana na operação. Os 15 da amostra e os 15 cartões da semana de curadoria (A-03) são contas separadas. O K-005 calibra o tamanho com o custo medido e com o que as amostras acharem.

**Por quê.**
- Vicente lendo itens da amostra toda semana seria revisão de rotina da base com outro nome, e um chamado fora dos dois casos da D-037 (1).
- A D-037 (2) põe a auditoria "na trilha de melhorias", e quem lê essa trilha é a frente de planejamento (D-036). É ali que o "substitui" se cumpre sem contrariar a diretriz 1.
- A D-026 já tem o verificador de outro harness na segunda leitura, e o brief já põe o auditor na amostra (blocos 7, 8 e 10b). Para o "auditor igual ao produtor" do legado (l. 200), o remédio que o plano dá é esse: checagem por script, harness diferente e amostra.
- Princípio 9 e P62 (pedido 62 de Vicente, Anexo A: no legado, uma IA conferindo outra repetiu o erro): o que tem resposta exata fica com o script, e o auditor só lê o resto.

**O que muda.** Brief: seção 3a, item 5; bloco 2 (tamanho); bloco 3 (`sortear_amostra.py`); blocos 7 e 8 (o que o auditor confere e o "pronto quando"); bloco 13 (horas). Próxima versão: V-24 e V-09. A amostra do legado (l. 732, Passo 3, "dentro da cota de juízo") fica para o K-117, que a lê com esta mesma regra.
**Aonde se quer chegar.** Uma auditoria da ferramenta que não vire revisão de rotina da base.

## A-05 — Quem tira um item da quarentena

**O texto em vigor.** O item "permanece em quarentena até o julgamento de Vicente, que é sobre a admissão no acervo, não sobre a prática" (l. 133, princípio 10). No eixo 1, quem define é "agentes e Vicente" (l. 624). No brief, o veredito de Vicente tira o item de `PENDENTE_JULGAMENTO` (brief l. 259). Os agentes já processam a quarentena sem autorização quando o item preenche os critérios (P87; l. 133, 635).
**O que as decisões dizem.** D-037: a base não tem revisão de rotina, e nada além de conflito e de Falta jurídica a liberar chama Vicente. A D-037 não fala da quarentena. D-032: o que só vale para publicar fica para quando a publicação for decidida.

**Padrão proposto.**
1. **Quarentena por valências** (o item que "fica no topo do funil e não passa", P85): sai pela regra, não por veredito. A triagem refeita aplica a regra versionada do registro do bloco 2 (a escala de valências e o critério de `PENDENTE_JULGAMENTO`) quando algo muda: nos gatilhos que a l. 592 dá para reabrir um Recorte (variante nova, título novo, OCR refeito, novidade no canal da fonte, esquema ou validador novo, Falta resolvida) e num gatilho próprio, a regra de valências com versão nova, como a da calibração do Passo 5 (l. 812). O gatilho próprio é valor provisório novo (D-034).
2. **A saída passa pelo portão:** é uma proposta como as outras. Quando a regra é aritmética, o script a calcula; o validador e o portão combinado da fase 1 (l. 396: validador, log e segunda leitura) a conferem antes de o item entrar em `acervo/`; a amostra audita a aplicação da regra (A-04). A Execução diz quem aplicou a regra (agente ou script), a versão dela e o motivo.
3. **Quando a regra muda:** o que já entrou não sai do acervo só porque a regra mudou. Se a ferramenta refizer a triagem de um item e ele não passar, ele volta à quarentena com o selo e uma Execução; nunca é descartado (princípio 10).
4. **Quarentena por barreira jurídica** (brief l. 290; D-025): sai quando a Falta é liberada pelo caminho do guia, no cartão de Falta jurídica a liberar, que chama Vicente (D-037, 1). Quem decide, assina e protocola é ele; o juridico nunca autoriza (D-020). A Falta jurídica que só vale para publicar (a Lei 13.123 no que se publica, a F-0003, a licença) fica registrada, e o cartão dela espera a decisão de publicar (K-010) sem chamar Vicente antes disso (D-032), como o K-201 espera para a F-0003.
5. **Enquanto não sai:** o item segue processável com o selo (P87), à vista no Git com o selo (l. 394) e nunca descartado (princípio 10). Se fizer parte de uma proposição em tensão, chega a Vicente pelo cartão de conflito, que é o único caminho item a item.
6. **O julgamento de Vicente muda de lugar:** do item para a regra. A escala de valências e o critério de `PENDENTE_JULGAMENTO` já são decisão dele (§8, l. 812): provisórios no bloco 2, e a calibração chega a ele pela frente de planejamento (K-005), não por chamado da operação.
7. **Fase 2:** as contribuições de pessoas, que passam pela quarentena e pela régua da P14 (l. 455), ficam com o K-008.

**Por quê.**
- A D-037 tira a revisão de rotina da base, e um veredito item a item sobre a quarentena seria essa revisão.
- A P85 ("permanece em quarentena até que eu analise") fica no nível da regra, que o §8 (l. 812) já deixa nas mãos de Vicente, e não no de cada item. A saída pela regra é extensão, apoiada na D-037 e nessa leitura da P85; a P87 sustenta só o processamento da quarentena, não a saída.
- O julgamento era "sobre a admissão no acervo, não sobre a prática" (l. 133; D-019). Admitir pela regra, pelo portão e com trilha mantém isso.
- Nada entra sem trilha (acordo 4) nem sem portão (l. 396, 473): a saída é proposta, Execução e segunda leitura.
- O que só vale para publicar não se problematiza agora (D-032).

**O que muda.** Brief: bloco 2 (a regra de saída e o gatilho da regra nova), bloco 5 (`fila_curadoria.py` sem veredito sobre a quarentena), bloco 7 (triagem refeita; a Falta que só vale para publicar). Em `.claude/`, gravado no K-101: `avaliador.md`, l. 32; `extrair-evidencia/SKILL.md`, l. 19 e 23. Próxima versão: V-07 (l. 133, 372, 624, 635, 750).
**Aonde se quer chegar.** Uma base que cresce sem revisão de rotina, em que a quarentena não descarta e nada entra sem trilha.

## A-09 (b) — A CLB nova que chega por Entrada de rotina

**O texto em vigor.** O brief não achou na Fundação quem abre a CLB situada nova que chega por Entrada de rotina e propôs: o curador a abre numa conversa de trabalho quando uma Entrada triada atende aos 4 critérios, na prioridade da l. 512, uma CLB nova por vez e só com a fila abaixo de uma semana (l. 472). E disse: "se a Fundação não a tiver, muda o plano e é decisão de Vicente" (brief l. 377).
**O que as decisões dizem.** D-031 (diretriz): as outras CLB entram pelo fluxo normal das rotinas, e não pelo piloto. D-032: as rotinas procuram CLB em geral. D-036: a operação trabalha sem sessão, e os agentes movem os cartões. D-037 (4): a menção, num texto já processado, a uma CLB ainda não registrada abre um cartão de baixa prioridade em A fazer. A D-037 não cobre a Entrada que trata de uma CLB nova (a leitura (a), da menção incidental, já é dada; esta é a (b)).

**Padrão proposto.**
1. **Nasce candidata, pela regra.** Quem processa a Entrada registra a CLB situada (a bebida num lugar, num grupo e num período) como candidata quando a Entrada, já triada e fora da quarentena, traz Evidência localizada de uma prática que o registro ainda não tem. Na operação, quem processa é a rotina com a habilidade aprovada (depois do K-113). Nas conversas do piloto, a candidata só nasce, como registro e cartão, quando uma Entrada do piloto a traz por acaso: o piloto não abre CLB nova (D-031). É o caminho do Termo, que nasce candidato e vira atestado com a primeira abonação (l. 733; habilidade registrar-termo). "Candidata" é um valor do eixo 5, o estado editorial da ficha, que o bloco 2 fixa (l. 628).
2. **Quem muda o eixo 5:** a triagem, pela regra, com o portão combinado da fase 1 (l. 396) e a amostra (A-04). Fica com Vicente o valor "publicada", que só vem com a decisão de publicar (D-032; K-010). A l. 628 diz "Vicente, pelo portão"; a mudança vai à próxima versão (V-14, V-20).
3. **O mesmo cartão da menção incidental:** ligação no grafo e cartão de CLB candidata, de baixa prioridade, em A fazer, na operação (D-037, 4). O cartão não chama Vicente.
4. **Os 4 critérios da D-022 são campos, não portão.** Cada um traz a Evidência que o atesta ou uma Falta, nunca recusa (l. 114, 605). A ficha da candidata sai quando valem as diretrizes de admissão: contra o revisionismo, contra a história de uma pessoa só, contra CLB sem lastro histórico, cultural ou antropológico (D-037; D-019; l. 112-114). Quem as aplica é a triagem, e a amostra audita.
5. **A candidata que não passa** fica candidata, com a Evidência à vista e a linha de trilha "não admitida: <diretriz>" (l. 112; acordo 4); nada se descarta. Enquanto o §10 não disser o que conta como revisionismo (pergunta 17), o caso duvidoso fica como Falta, sem decisão da triagem.
6. **Quando.** Na prioridade da l. 512: risco, CLB do piloto, vácuos por região e período, escolha de Vicente. No piloto, o cartão espera, porque o piloto leva só a cajuína de ponta a ponta (D-031, D-032), salvo escolha de Vicente. A ficha de uma CLB nova só começa com a fila abaixo de uma semana: é o freio que a l. 472 dá à porta nova, aplicado por analogia à ficha nova, valor provisório (D-034) que depende da leitura A-03.
7. **Vicente** só entra por conflito ou por Falta jurídica a liberar que a CLB nova trouxer (D-037, 1).

**Por quê.**
- A D-031 já diz o caminho das outras CLB: o fluxo normal das rotinas, e não o piloto nem uma conversa aberta para isso. Pela D-036, a operação não depende de sessão, e abrir a CLB só "numa conversa de trabalho" prenderia a operação à sessão.
- Um caminho só para a menção incidental e para a Entrada mantém a ferramenta simples (princípio 16) e usa o que a D-037 (4) já criou.
- A l. 114 diz que o critério não atestado vira Falta, nunca recusa. "Atende aos 4 critérios" não é um juízo que alguém precise fazer: são campos que a evidência preenche, e a D-019 admite a prática que atende aos critérios, sem julgar.
- A candidata que não passa segue a l. 112 ("não admitida", com linha na trilha) e o princípio 10.

**O que muda.** Brief: "Depois do bloco 14" (brief l. 377); bloco 2 (o valor "candidata" e quem muda o eixo 5); a seção nova do script de menções (K-102), entre os blocos 8 e 9; bloco 10b. O texto da operação no quadro. Próxima versão: V-14, V-20 (l. 628) e V-21.
**Aonde se quer chegar.** CLB nova entrando sem fila de revisão de rotina e com os 4 critérios da D-022.

## A-10 — A junção da ramificação das rotinas à versão principal

**O texto em vigor.** Quem propõe não aprova (l. 473). A rotina com IA abre proposta numa ramificação `claude/` "para Vicente revisar" e nunca grava na versão principal (l. 506; brief l. 124, 331). A ramificação das rotinas sem IA, se a proteção do `main` barrar o commit do workflow, "Vicente a junta na revisão semanal" ou "na revisão de uma tela" (brief l. 325, 328; leitura da 6B). Na fase 1, o portão é combinado: o validador roda em toda proposta, os agentes gravam logs e a segunda leitura vem do validador, do verificador de outro harness e da amostra (l. 396; D-026).
**O que as decisões dizem.** D-037: a base não tem revisão de rotina, e nada além de conflito e de Falta jurídica a liberar chama Vicente. D-036: a operação trabalha sem sessão, e Vicente acompanha sem precisar da IDE.

**Padrão proposto.**
1. **Juntar é portão da ferramenta, não revisão da base.** A proposta de uma rotina só entra na versão principal se passou, inteira, no portão da sua camada (l. 396):
   - camada 1 (sem IA, 10a): o validador e as checagens por script, com o log. Ela grava Entradas brutas e o estado da coleta, que a triagem e a amostra tratam depois;
   - camada 2 (com IA, 10b): o validador, o auditor da segunda leitura com o log dele e a semente da amostra, se a rotina de teste da 10b mostrar que a rotina chama o auditor (hoje, não conferido: brief l. 333). Se não mostrar, a segunda leitura da proposta se faz numa conversa de trabalho, antes da junção.
2. **Quem junta, até o K-113:** Vicente, dono do repositório (D-021) e única pessoa da fase 1 (D-026), pela página do GitHub, sem IDE e sem sessão, uma vez por semana, olhando o resultado do portão (as checagens da proposta e o relatório do dia, que lista as propostas à espera de junção), e não o conteúdo. **É uma ação dele fora dos dois cartões da D-037 (1).** O padrão a lê como parte da "auditoria da ferramenta" que o "substitui" da D-037 põe na cota, e é essa leitura que Vicente confirma ou corrige ao aprovar. Nas horas do bloco 13, conta com o mesmo rótulo da A-04, "auditoria da ferramenta".
3. **O que falha no portão** não entra e vira correção da ferramenta (cartão no desenvolvimento, insumo), nunca correção de conteúdo por Vicente. Na ramificação única e permanente das rotinas sem IA (brief l. 325), que a execução seguinte lê, a parte reprovada é revertida por commit, com a trilha, e a execução seguinte retoma do último estado que passou; o caso de teste entra na 10a.
4. **A rotina nunca junta a própria proposta.** É a regra que o insumo 3 (item 3) pede. Até a rotina de teste da 10b mostrar o que a conta conectada barra, ela vale por instrução.
5. **Juntar sem Vicente**, por um script sem IA que não gera a proposta e só junta quando o portão passou, é o caminho para a operação deixar de chamá-lo (insumo 20; K-002, K-113). Depende de fatos não conferidos: as permissões de gravação do token do workflow (brief l. 325) e o modo como os commits da rotina passam pela proteção do `main` (insumo 3, item 3; l. 396).

**Por quê.**
- "Quem propõe não aprova" (l. 473): a rotina propõe, e outro junta. Na fase 1, sem o script, esse outro só pode ser Vicente (D-026).
- A l. 396 já diz o que é o portão da fase 1: validador, logs e segunda leitura. Vicente lendo o conteúdo não faz parte dele, e a D-037 tira a revisão de rotina da base. A camada 1 não tem IA, e o portão dela é o validador; o auditor só entra onde a rotina pode chamá-lo.
- O K-001 leu a aprovação do relatório da rodada B como portão da ferramenta que fica (A-02). Aquela aprovação é pontual, e esta é semanal: por isso o padrão diz que é ação fora dos dois cartões e pede a confirmação de Vicente, em vez de tratá-la como leitura dada.
- Pela D-036, Vicente acompanha sem a IDE: juntar uma proposta pela página do GitHub não pede sessão.

**O que muda.** Brief: seção 3b (o que a camada 2 grava); bloco 10 (brief l. 325, 328, 330-331, 333, e o caso de teste da reversão na 10a); bloco 13; "não fazer". Próxima versão: V-14 (l. 473), V-16 (l. 506) e V-12 (l. 396).
**Aonde se quer chegar.** A rotina com IA nunca grava na principal por regra (insumo 3, item 3), e Vicente não revisa a base por rotina.

## Junto com os quatro, a aprovação do brief confirma

- **A-03, leitura proposta (valor provisório, D-034):** a fila da l. 472 passa a ser a dos cartões de conflito e de Falta jurídica a liberar que esperam uma ação de Vicente, e a semana de curadoria, até 15 desses cartões (o número da l. 902), até que as horas medidas no bloco 13 deem outro valor (K-005). O cartão que espera outra coisa antes (como o K-201, que espera o K-109 e o K-010) não espera ainda a ação de Vicente.
- **A-06, leitura proposta:** o trecho abaixo do limiar fica Falta "não verificável por máquina", dita e nunca completada (D-018), sem ir a ninguém; a busca assistida pode resolvê-la como fato novo.
- **Ficam para o K-002:** a configuração de cada frente (A-12) e a leitura do teto da D-023 com as frentes (A-13). Até lá, o brief lê o teto semanal como o das sessões de desenvolvimento, e as rodadas de planejamento com o teto próprio delas (D-036, 3), como o mapa já lê (seção 1).
