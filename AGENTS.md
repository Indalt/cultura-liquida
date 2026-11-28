# AGENTS.md — regras do projeto Cultura Líquida

Resumo para qualquer agente que trabalhe nesta pasta. A fonte de verdade é `00_Fundacao_Cultura_Liquida.md` (v0.2, 16–17/10/2026). Na dúvida, vale a Fundação. Exceção até a próxima versão da Fundação (D-034, D-035): nas linhas da seção 6A do brief de execuções (`trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md`), valem o roteiro e o brief.

## O projeto em 5 linhas
- **Cultura Líquida Brasileira (CLB):** uma bebida e tudo o que a faz existir (insumos, modos de fazer, recipientes, tempos, lugares, pessoas, transmissão). Nativos primeiro, aculturados incluídos.
- **Propósito:** encontrar, organizar e devolver o que se pode saber sobre as CLB desde 1900, com cada informação rastreável até a origem.
- **Três movimentos:** rastrear (ambientes e consultas), organizar (wiki, termos, grafo 4D paraconsistente) e devolver e agir (educação, salvaguarda, campo de ação sob demanda).
- **Fase 1:** só Vicente e os agentes, com logs. Responsável: Vicente, pessoa natural (D-026).
- **Casa:** este repositório, `Indalt/cultura-liquida`, **público** (D-021).

## Regra de Ouro e acordos (§0 da Fundação)
- **Regra de Ouro (P38):** nenhum agente inventa solução fora do plano. Diante de dificuldade, recorre à Fundação e ao brief; se não resolverem, **para e pergunta a Vicente**.
- **Acordos:**
  1. Perguntas servem para compreender, nunca para direcionar com escolhas binárias.
  2. Nada de simulação apresentada como execução (P96): o que não foi feito não é relatado como feito.
  3. Não simplificar para conseguir executar (P79): se não couber, dizer e parar.
  4. Tudo deixa trilha: o que se buscou, onde, o que se achou, o que se descartou e por quê.
  5. O plano só muda com entrada no Registro de Decisões e nova versão da Fundação.
  6. Exemplos ilustram e nunca limitam (D-017).
- **[PROPOSTA] não é plano:** nenhum agente executa um item marcado [PROPOSTA] sem decisão registrada. A D-034 é essa decisão só para os valores provisórios no alcance dela (l. 696 da v0.2, os [PROPOSTA] dos §5 e §6 que o brief de execuções usa e as leituras da seção 6B do brief). Os valores provisórios novos dos padrões do K-003, que a Fundação não fixa, valem pela D-038, com os números até o K-005.
- **Comentário novo de Vicente:** captar a essência, conferir palavras ambíguas ("por princípio" pode ser "de início"), devolver o entendido, e só depois registrar como diretriz (nunca como transcrição).

## Princípios (§2, uma linha cada; "Pn" = pedido n de Vicente, Anexo A, buscar `#### Pn`)
1. Transparência e rastreabilidade: cada informação mostra de onde veio, link ou caminho (P90–P93, P97).
2. Ciência terminológica: termos e booleanos de baixo para cima; a variação é dado (P3, P23, P24).
3. Lógica paraconsistente no grafo 4D (X insumo, Y processo, Z tempo, W compreensão local): contradições convivem (P27–P29).
4. Rigor com o poder, hospitalidade com o vestígio: o que sustenta decisão exige fonte forte; fragmentos entram com selo (P22, P13).
5. Cânone rigoroso, aberto ao desconhecido (P5).
6. Nativos primeiro, aculturados incluídos (P6).
7. De baixo para cima: categorias nascem das fontes e das pessoas (P24).
8. Descritores processuais, não genéricos (P3).
9. Fontes reais e verificáveis para tudo, inclusive para o auditor (P90–P92).
10. Quarentena não descarta; valências equilibradas (P85–P87).
11. Persistência e reconstituição: tudo nesta pasta, legível por qualquer IA (P42).
12. Institucionalidade sem invasão: avisar, nunca apagar nem discriminar.
13. Leis brasileiras como moldura.
14. Tiers são grupos de interesse, não monetização.
15. Campo de ação sob demanda, nunca automático.
16. Infraestrutura simples, fidedigna e segura.

## Decisões vigentes (essência confirmada por Vicente)
O texto inteiro: D-030 em diante em `trilhas/decisoes/D-nnn.json`; D-015 a D-029 na Fundação (§9) e no checklist da v0.2. Aqui, só a essência.
- **D-015:** a Fundação passa à v0.2.
- **D-016:** Vicente tem 1 a 3 h por semana de curadoria; os "15" nunca são teto de coleta.
- **D-017:** exemplos ilustram e nunca limitam.
- **D-018:** W é a prática comum da região, episteme própria mas traduzível; tratada como dimensão; o não captado é Falta, dita e nunca completada; o saber comum muda de forma autóctone ou por interação.
- **D-019:** não julgamos: fonte contrária só se documenta, e a correção da própria fonte também; a prática que atende aos critérios pode ignorar revisionismo.
- **D-020:** o juridico é de precaução: cria Faltas, nunca autoriza.
- **D-021:** GitHub na conta Indalt, commits de Vicente, repositório **público**: o que entra no Git é publicação aberta; legado e dado pessoal de terceiros ficam fora.
- **D-022:** os critérios de prática cultural vêm da lei (CF art. 216; Convenção UNESCO 2003, Decreto 5.753/2006; Decreto 3.551/2000).
- **D-023:** medir e parar antes de acabar, com o estado salvo (o teto de 300 mil tokens por semana foi trocado pela D-040).
- **D-024:** do legado, só o verificável e condizente com as regras novas; o resto não se apaga; o site não se aproveita.
- **D-025:** as regras valem "de início" e são proporcionais; revisão de essencialidade depois da fase 1; obrigação legal nunca se despreza; toda barreira jurídica traz porquê e caminho de liberação.
- **D-026:** fase 1 só com Vicente e agentes, com logs; segunda leitura = validador + verificador de harness diferente + amostra sorteada.
- **D-027:** execução em Opus 5.5 médio, subagentes em Sonnet 5.5 alto; depois, o modelo de cada tarefa escolhido por teste.
- **D-028:** a execução não para para aprovar o que já foi decidido.
- **D-029:** agentes, habilidades e harness em `.claude/` antes da v0.2, operados só pelo Claude Code; o caso-piloto continua no Passo 1. *(Alterada pela D-060: Claude Code e Antigravity operam em sequência.)*
- **D-030:** os logs dizem o **alcance**: o que se olhou e o que ficou fora; fala-se só do que se conseguiu olhar, como a ciência preconiza.
- **D-031:** o caso-piloto é a cajuína, começando pelo caju.
- **D-032:** o piloto é teste da ferramenta inteira; as rotinas acham CLB em geral; piloto não é publicação.
- **D-033:** o GitHub é o repositório; se ele impedir a ferramenta, outra nuvem, com o fornecedor nomeado por decisão.
- **D-034:** não se pergunta o que o plano responde; o que restar diz aonde se quer chegar e é insumo para reavaliar o plano; o [PROPOSTA] da Fundação vira valor provisório usado; nas linhas da seção 6A do brief, o roteiro e o brief valem sobre a Fundação até a próxima versão.
- **D-035:** finalizar a v0.2 é construir e testar no piloto a ferramenta que ela descreve; versão nova é da sessão de planejamento; o que surgir vira insumo, sem explorar; uma tarefa por vez.
- **D-036:** três frentes (planejamento, desenvolvimento, operação) e o quadro kanban em `trilhas/planejamento/quadro.md`.
- **D-037:** a base não tem revisão de rotina; Vicente só é chamado por conflito ou por Falta jurídica a liberar; a amostra sorteada audita a ferramenta.
- **D-038:** **a ferramenta decide os itens pela regra; Vicente decide as regras**; quem propõe não aprova; toda decisão automática grava a versão da regra; números provisórios até o K-005.
- **D-039:** a CLB se identifica pelo **termo** enquanto ele não for ambíguo; nenhuma fonte é verdade única, nem a institucional; toda fonte nasce candidata.
- **D-040:** o ritmo em pontos do limite semanal da conta: o projeto até 60 pp, o desenvolvimento até 50, a conta nunca acima de 90%; commit e push a cada lote; acima de 70% da janela de 5 h, um lote e a conversa fecha.
- **D-041:** negação e sentido contrário batem exatamente no trecho; μ e λ só com Evidência localizada e de leitura fiel; cada linhagem conta uma vez.
- **D-042:** o juridico reflete antes de agir; ler, linkar e citar trecho curto de informação pública não gera Falta; barram **agora** proibição expressa, cópia além da citação, dado pessoal e modo de preparar substância controlada; conhecimento tradicional e licença barram **só a publicação**.
- **D-043:** o Wayback só registra a captura que já existe; o Git público segue o padrão da F-0003 (links, citações curtas, fatos, metadados); dado pessoal nunca; conhecimento tradicional em detalhe numa pasta local.
- **D-044:** fonte que barra robô só vai a adaptador se os termos permitem e um host oficial responde sem desafio; nunca se contorna proteção.
- **D-045:** a pegada compacta de todo item visto; Entrada de trabalho só do que passa na pré-triagem por regra; o bruto fora do Git; alarme acima de 20 mil arquivos ou 200 MB.
- **D-046:** os cartões novos nascem numa reunião só (K-004), com tudo reunido; exceções: o que impede o próximo cartão e o que a operação abre pela regra.
- **D-047:** o saber da cajuína é público e não é conhecimento tradicional associado (Lei 13.123); outra CLB só recebe a mesma leitura pelas regras.
- **D-048:** rotinas sem IA **todo dia**, na nuvem, cada fonte no seu ritmo; juntam ao main pelo portão, sem esperar Vicente; abrir todo local de busca pelas vias permitidas; o Internet Archive só para consulta, sem cadastro.
- **D-049:** até haver financiamento, nenhuma conta, chave ou cadastro em fonte; o que fica sem acesso vira insumo. [ABERTO]: o alcance de "intervenção humana" (insumo 112).
- **D-050:** a IA da operação usa no máximo 20% da semana e 50% de cada janela de 5 h; a rotina com IA às quintas (a IA e os tetos mudaram nas D-054 a D-056).
- **D-051:** as regras do K-115 (testes de modelos) ao lado do K-112; a antecipação não foi usada (D-052).
- **D-052:** o K-112 fechou com as fontes automatizadas até 12/11; a que não se automatiza fica com o motivo na ficha.
- **D-053:** o K-115 em três cartões (a, b e c).
- **D-054:** a automatização na API do Gemini; estacionada pela D-056.
- **D-055:** o Claude na segunda leitura da rotina do Gemini; estacionada pela D-056.
- **D-056:** o piloto se entrega com o kit (K-114) e o relatório (K-116); K-125, K-115b e K-115c estacionados; até haver financiamento, a IA da operação é a rotina do Claude (o avaliador propõe, o auditor relê, o portão decide).
- **D-057:** *(substituída pela D-061: o K-126 não roda)* o piloto termina com as três CLB já achadas (vinho de caju, mocororó, e caoi ou caoim, com "caium" de Vicente), no K-126, como proposta, sem verificação nem teste.
- **D-058:** a lista de insumos se limpa antes de virar fila (o repetido se junta; o que não é problema da promessa sai, com o motivo); só depois se libera a operação com IA em escala.
- **D-059:** **limpar e arrumar a ferramenta é o primeiro passo da correção** (K-127): limpar não muda comportamento; lote que quebra volta inteiro; **teste mudado ou tirado só entra com a confirmação de Vicente** (`scripts/trava_testes.py`).
- **D-060:** Claude Code e Antigravity (Gemini) operam juntos de forma sequencial (sem paralelismo), lendo diretamente `AGENTS.md` e `.claude/` (sem `.agents/` nem `GEMINI.md`), com passagem de bastão em `RETOMAR.md`; novas habilidades/agentes entram em `.claude/` sem quebrar testes nem adaptar `orcamento.py` (a descontinuar); `clb coleta` fica para depois.
- **D-061:** decisão consolidada do K-011: piloto encerra na cajuína (substitui D-057; K-126 não roda; demais CLB ficam candidatas, D-039); exemplos e linguagem ilustrativa ficam só no texto explicativo e nunca viram regra, código, lista fixa ou escopo (estende D-017); abre o K-011 (exceção à D-046) e assenta os fundamentos (11 atos no momento, duas vozes, regimes situados sem lógica nova na ferramenta, μ/λ só descrição de linhagens, cultura em mudança, lógica além da ferramenta como viés nos 5 lugares de base.md, vieses como observação nas fichas; [ABERTO] regra vs. declaração, wiki inteiro e campo de ação); mantida a D-060 com diálogo sequencial Claude + Antigravity no K-004.
- **D-062:** não existe fim da linha; nomes novos: **módulo** (o que se acopla ao núcleo: ferramenta própria, serviço próprio, integração, conector de parceria/MCP), **sprint** (unidade de trabalho com objetivos e prazo), **backlog** (os antigos "insumos" e "o que falta"; o arquivo mantém o nome), **versão estável** (tudo com testes passando) e **definição de pronto** (inclusão completa de um módulo); o K-004 torna a ferramenta viável com rigor (coleta verificada, organização, planos de aula) e a escrita da Fundação vira um trabalho entre outros; item do backlog só entra num sprint quando impede um objetivo, salvo obrigação legal ou o que barra agora; fecha os 3 [ABERTO] da D-061 (quadro lógico declarado com a identidade no tempo como primeiro caso; página fixa de vieses + bloco por script; carimbo mínimo no campo de ação, nota de viés só para decisão de poder); 143 junta-se ao 144, dissolvidos nos fund. 6 e 7, código igual; o [ABERTO] da D-058 só depois do sprint e da auditoria.
- **D-063:** as aulas do campo de ação ensinam a CLB e a ciência com que ela se conhece, nunca o sistema (sem códigos nem graus numéricos no texto da aula; fontes citadas como a ciência cita; o rastreio numa nota do educador com espaço para anotar); o programa é da CLB (agora, a cajuína), com qualquer número de aulas, e a apresentação dele abre a aula 1 em até 15 minutos, para encantar; adapta-se a qualquer público e educador (sem descrição, o educador adapta na nota); o kit do professor termina numa aula ao grande público sobre como o programa foi feito com base nas ciências; o campo-de-acao responde por todo o campo de ação, com uma habilidade por ação; **o que um script faz, a IA não faz** (`planejar-aulas` + `scripts/montar_programa.py`, que dá o material fechado e barra a invenção), sem segunda leitura extra; o guia de salvaguarda fica em revisão e não se produz; as instruções de geração levam a regra, nunca as falas de Vicente; "sistema" é a ferramenta, "programa" é o programa de aulas.

## Passo corrente
- **Feito:** a Fundação v0.2; o roteiro e o brief de execuções (aprovados por Vicente em 17/10/2026); no desenvolvimento, os cartões K-100 a K-114, K-115a, K-116, K-123 e K-124; no planejamento, K-001, K-002, K-003 e a 1ª passada do K-005. O que cada cartão entregou está no quadro (`trilhas/planejamento/quadro.md`, coluna Destino) e no checklist do piloto; não se repete aqui (o texto que estava aqui até 14/11 está em `trilhas/2026-11-14_manutencao/passo-corrente-ate-2026-11-14.md`).
- **O piloto já tem:** a cajuína (CL-0001) com a ficha (`acervo/fichas/CL-0001.md`), a camada Educação, o grafo 4D em `grafo/` (μ e λ batendo com o recálculo), os Termos atestados, 520 Evidências e 427 Proposições no acervo, as Faltas jurídicas (só para publicar), o wiki local (fora do Git) e a rotina diária sem IA no GitHub Actions (BDTD, Infoteca-e, Oasisbr e BCR), com o relatório do dia no Issue #1.
- **Em curso:** o cartão **K-004** está em `Fazendo` desde 27/11: a reunião abriu com o K-011 fechado (saída em `trilhas/planejamento/rodadas/2026-11-25_K-011/saida-K-004.md`) e a pauta em 10 blocos em `trilhas/planejamento/rodadas/2026-11-27_K-004/reuniao.md`; o Bloco 1 (os 3 [ABERTO] da D-061 e o gatilho "inconsistente") está com Vicente. O K-127 segue em `A fazer` (lotes 1–4 salvos, D-035). Pela D-060 e fala 14, toda tarefa indica modelo e esforço da LLM.
- **Próximo:** os blocos seguintes da pauta, em diálogo sequencial (D-060, D-061), com o bastão à Antigravity onde a pauta marca ⇄ (D-038): regras de Vicente, a medida (descontinuação formal do `orcamento.py` com os 6 casos da trava), a fila dos 30, os estacionados, a 3ª passada do K-005, o K-006, os cartões novos e a escrita da Fundação. Na operação seguem a rotina diária sem IA, o K-207 e o K-208.
- **Orçamento:** D-040 (o projeto até 60 pp por semana; o desenvolvimento até 50). Em 14/11, Vicente suspendeu os tetos de 50 e 60 pp e manteve a linha de 90% da conta; em 26/11, retirou as limitações por uso estimado (só a leitura oficial limita). A semana da conta vai de 11/11 a 18/11/2026, 23h; a leitura de uso vem da linha [Uso do plano] do hook, sem perguntar a Vicente.
- **Ao abrir:** `scripts/relatorio_dia.py`. Clone novo: `git config core.hooksPath .githooks` para o pre-commit. Insumos para o planejamento: `trilhas/insumos-planejamento.md`. Vistoria da casa, quando pedida: `scripts/manutencao.py` (sem IA; não muda nada).
- **Estado do trabalho:** `trilhas/2026-10-17_execucao-piloto.md` (checklist do piloto). Leia-o antes de qualquer passo. O histórico da v0.2 está em `trilhas/2026-10-16_execucao-v0.2.md`.

## Agentes e habilidades (`.claude/agents/`, `.claude/skills/`)
| Agente | Papel | Habilidades | Modelo inicial |
|---|---|---|---|
| curador | sessão principal: brief, decisões, checklist, orçamento, logs | executar-brief, registrar-decisao, registrar-melhoria | Opus 5.5, médio |
| redator | escreve os textos (v0.2, Educação, boletim) | escrever-secao-fundacao | Opus 5.5, médio |
| auditor | verificação mecânica e independente | verificar-fundacao, conferir-fato | Sonnet 5.5, alto |
| juridico | precaução: cria Faltas, prepara guias de liberação | conferir-fato, triagem-juridica, guia-de-liberacao | Sonnet 5.5, alto |
| rastreador | ambientes, fichas de acesso, consultas, pegadas | ficha-de-acesso, consulta | Sonnet 5.5, alto (testar Haiku) |
| avaliador | valências, quarentena, evidência com trecho literal | extrair-evidencia | Haiku 5.5, alto (K-115a) |
| arquivista | termos, fichas, grafo 4D | registrar-termo, montar-ficha, gerar-grafo | Sonnet 5.5, alto |
| campo-de-acao | ferramentas de ação sob demanda | kit-fonte-primaria | Sonnet 5.5, alto |

Os modelos são provisórios até os testes do bloco 12 do brief de execuções (D-027). Avaliador, arquivista e campo-de-acao recebem o modelo no frontmatter no bloco 1 e só são chamados nos blocos do brief que os usam (4, 7, 8 e 11).

## Orçamento (D-023; D-040)
- Medir e parar antes de acabar, com o estado salvo. O teto é em pontos percentuais (pp) do limite semanal da conta, que Vicente lê: o projeto até 60 pp por semana (três frentes), o desenvolvimento até 50, o planejamento o resto; a conta nunca acima de 90%. No fim do K-113, o teto de manutenção do K-002.
- Ao abrir, Vicente informa o uso semanal e o da janela de 5 h; acima de 70% na janela de 5 h, só um lote e fecha. Commit e push a cada lote.
- Antes de cada agente, a conta da conversa (brief, seção 0) por `scripts/orcamento.py --a0 <uso> --janela <5 h> --agente <a> --habilidade <h> --medidos-conversa <tokens>`: 2 pp da conversa principal + 1,6 pp por 100 mil tokens de agente, até a folga da semana; a conversa não para antes do teto. Uma linha por conversa na tabela "Semana da conta" do checklist do piloto.
- Todo agente tem teto: pesquisa web, 15 a 20 chamadas; leitura só por `grep -n` e faixas de linhas.
- Estimativa do lote: a última medida do mesmo agente com a mesma habilidade; sem medida, 96.520 tokens (medidos: 31 a 160 mil).
- Todo agente grava log (`scripts/registrar_log.py`); o curador soma os tokens no checklist.
- O log registra o **alcance da ferramenta** (campo `alcance`: o que se olhou e o que ficou fora): fala só do que se conseguiu olhar, não de tudo o que se conhece. (D-030)

## Fatos e fontes
- Todo fato novo traz **URL e nível**: "oficial" só se a página oficial abriu; senão "secundária" ou "não conferido". Nada de memória apresentada como conferido.
- Fato que não se consegue conferir não é motivo de parada: marcar "não conferido" e seguir.
- **Proteções anti-robô nunca se contornam** (403, captcha, verificação de navegador).
- Leis no planalto.gov.br: extrair só o artigo (`grep -n` e recorte), nunca a página inteira.

## Onde está cada coisa
- `00_Fundacao_Cultura_Liquida.md`: a Fundação. Anexos A e B são intocáveis (conferir com `scripts/comparar_anexos.py`).
- `trilhas/`: diário, checklist, pesquisa (`2026-10-15_pesquisa/`, com `indice.md`), conferências (`2026-10-16_conferencias/`) e logs (`logs/`).
- `esquemas/`: JSON Schema de log, conferência, Falta, guia de liberação, achado, decisão e insumo.
- `scripts/`: registrar log, registrar insumo, procurar dado pessoal, comparar anexos, checar a Fundação, validar JSON, e a vistoria da casa (`manutencao.py`: sem IA, só avisa, nunca apaga nem corrige).
- `testes/`: relatórios das rodadas de teste dos validadores.
- `.claude/agents/`, `.claude/skills/<nome>/` (SKILL.md, `exemplos/`): agentes e habilidades.
- `legado/`: sistema anterior, **fora do Git e só leitura**.

## O que não fazer
- Não pôr dado pessoal de terceiros no Git (e-mail, telefone, CPF, @perfil, nome de quem não consentiu). O e-mail de Vicente, como responsável, é permitido. Rodar `scripts/procurar_dado_pessoal.py` antes de cada commit.
- Não processar o legado nem abrir os Docs antes do Passo 3.
- Não criar rotinas na nuvem nem GitHub Actions fora do bloco 10 do brief de execuções (10a sem IA; 10b com IA, só depois da aprovação do bloco 9) (D-032).
- Não publicar site.
- Não pedir captura nova ao Wayback nem criar conta no Internet Archive: só consulta, sem cadastro (D-043, D-048); não abrir conta, cadastro ou assinatura em fonte nenhuma até haver financiamento (D-049); não abrir Falta por ler, linkar e citar trecho curto de informação pública e acessível (D-042).
- Não reabrir decisão vigente: registrar o conflito e perguntar a Vicente.
- Não completar Falta por inferência; não julgar a prática; o Jurídico nunca autoriza nem protocola em nome de Vicente.
- Não lançar agentes em paralelo sem teto; não usar Workflow sem pedido explícito de Vicente.
