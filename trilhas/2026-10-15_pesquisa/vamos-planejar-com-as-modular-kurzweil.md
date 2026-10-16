# Cultura Líquida — análise de melhorias da Fundação v0.1 e plano da v0.2

## Contexto

Na pasta há um único arquivo, `00_Fundacao_Cultura_Liquida.md` (v0.1). Vicente pediu para planejar a partir das ideias expostas e analisar o que realmente pode melhorar. Foco, nas palavras dele: "uma modelagem profissional do que vamos construir planejando". A análise foi feita em duas leituras independentes (a minha e a de um subagente revisor) e corrigida em três rodadas com Vicente em 15/10.

### O que Vicente decidiu em 15/10 e 16/10 (entra como [VIGENTE]; na v0.2, vai a essência confirmada, e a fala original fica só na trilha)

- **Curadoria:** de 1 a 3 h por semana.
- **Passo 0:** feito e testado.
- **Exemplos:** "nunca usar exemplos para limitar o nosso trabalho".
- **Dimensão W:**
  - "a matriz identificada como 'prática comum' e não como prática de um indivíduo (conhecimento compartilhado) da região";
  - "uma episteme própria, mas não como algo impossível de tradução";
  - "deve ser considerada como tal" (uma dimensão de verdade);
  - "é o modo como se entende do que se pode coletar";
  - "quando não é possível captar a compreensão local, se diz isso como falta e não se tenta completar";
  - "o saber comum muda com o tempo de forma autóctone ou em razão de interações de conhecimentos com outras comunidades".
- **Fontes contrárias:**
  - "uma fonte contrária não corrige evidência por nós, apenas documenta. Se a fonte corrige, documenta a correção. Não julgamos";
  - "não é necessário documentar tudo";
  - "uma prática lida como atendendo aos critérios de prática cultural será admitida como evidência e pode ignorar as tentativas de revisionismo".
- **Jurídico:**
  - "podemos ter um agente especialista";
  - "se o agente jurídico percebe que não se pode falar por questões de direito autoral ou de problemas com a legislação brasileira como a necessidade de cadastrar no SisGen, isso é compreendido como uma falta e documentado como tal".
- **Nuvem:**
  - "não é necessário Google se não é necessário";
  - "se for possível alimentar a nuvem com as buscas e os tratamentos por IA vamos considerar";
  - cópia "idêntica, sincronizada. Pode ser um GitHub";
  - "aprovo publicação externa mesmo que privado".
- **Bancada:** entendida; daqui em diante, "caso-piloto (bancada)".
- **GitHub:** "Sim, Indalt e Vicente". O repositório é privado, na conta Indalt, com commits assinados por Vicente <vicente@dacaatinga.com.br>.
- **Legado:** "vamos apenas aproveitar o que já foi coletado se for verificável e condizente com as novas regras/diretrizes. Não vamos aproveitar o site."
- **Proporcionalidade das regras (16/10; essência confirmada por Vicente):**
  - **"De início"** (e não "por princípio"): as regras valem **neste momento** e podem mudar se ficarem restritivas demais;
  - o projeto é uma **biblioteca informativa consequente, com proposições**, e não uma réplica da legislação;
  - **diretriz:** depois das coletas e verificações da fase 1, revisar as regras e manter **só o essencial para o projeto existir**: o jurídico, a colaboração e a capacidade de organização;
  - a nota pode caducar e ficar desnecessária;
  - **o grafo 4D não faz parte dessa revisão** (ver item 21);
  - **toda barreira jurídica vem com porquê e com caminho:** nenhuma obrigação legal é desprezada, e a Falta jurídica sempre oferece o motivo e um passo a passo assistido de liberação, com os documentos e o modo de preencher (itens 1 e 7);
  - **de início, só Vicente e os agentes trabalham.** Não há segunda pessoa, e os agentes geram logs (item 22);
  - **responsável:** a conta Indalt é pessoal de Vicente e ainda não há empresa. O responsável é Vicente, pessoa natural;
  - **modelos e harness:** ver item 22.
- **Critérios:** "Práticas culturais têm critérios objetivos na legislação brasileira". Perguntas de Vicente: "práticas culturais que são amplamente conhecidas também precisam de autorização? E quando não tem quem autorizar?" Todos os textos legais citados abaixo foram conferidos na fonte oficial em 15/10 por um agente de pesquisa, salvo indicação em contrário.

---

## Análise: o que realmente melhora

### 1. A Falta como registro de primeira classe (conceito novo que unifica três pedidos)

Três falas de Vicente apontam para o mesmo mecanismo: a compreensão local que não foi captada, o impedimento jurídico e o estado paracompleto (lacuna, P13, P22). **[PROPOSTA]** Um registro **Falta**:
- **tipo:** compreensão local não captada / impedimento jurídico (direito autoral, SisGen, LGPD, substância controlada) / fonte inacessível / trecho não verificável por máquina / outro;
- **o que falta** e **por quê**;
- **onde aparece:** ficha, célula, aresta;
- **caminho de liberação (para a Falta jurídica):** o motivo (a norma, citada) e o passo a passo para destravar (item 7).

**Regra única:** uma falta **é dita, nunca completada**. Nenhum agente preenche uma falta por inferência. No wiki, a falta aparece como tal: é o estado paracompleto à vista.

### 2. W como dimensão de verdade (§2 princ. 3, §6)

Hoje o §2 fala em "5 matrizes epistêmicas temporais", uma lista vinda de cima (resposta do Gemini à P27). **[VIGENTE pela fala de Vicente; o desenho dos campos é PROPOSTA]:**
- **Coordenadas:** cada ponto do grafo (elemento de prática: técnica, uso de insumo, recipiente…) tem **quatro**:
  - X (insumo) e Y (processo) vêm da **tradução** curta;
  - Z é o período;
  - **W é o modo como aquilo é entendido no lugar**, como prática comum.
- **Registro próprio:** W tem um registro **Compreensão local**, como X tem Insumo e Y tem Processo. Ele traz a designação local, o lugar, a comunidade, o período e as fontes. Os valores nascem dos dados (princ. 7). Se a compreensão não foi captada, a coordenada W é uma **Falta** (item 1).
- **W no tempo:** uma relação **Transformação** liga compreensões de períodos diferentes, com o tipo: *autóctone* ou *por interação* (com qual comunidade ou conhecimento).
- **Prática de um indivíduo:** entra no acervo, porque nada é descartado (princ. 10). Ela passa a ancorar W quando é atestada como prática comum.
- **No wiki:** a ficha mostra primeiro a compreensão local e depois a tradução. Os filtros por W (§5.7) passam a navegar uma dimensão real.

### 3. Admissão, documentação e "não julgamos" (§2 princ. 3, §6)

O que muda no modelo **[VIGENTE pela fala de Vicente; o desenho dos campos é PROPOSTA]:**
- **Admissão:** a prática que atende aos **critérios de prática cultural** é admitida como evidência.
  - **Os critérios vêm da legislação [VIGENTE].** Não existe uma definição única: os critérios estão combinados em três normas (conferidas na fonte oficial).
    - **CF, art. 216:** bens "portadores de referência à identidade, à ação, à memória dos diferentes grupos formadores da sociedade brasileira", incluindo "II - os modos de criar, fazer e viver".
    - **Convenção da UNESCO de 2003 (Decreto 5.753/2006), art. 2:** "práticas, representações, expressões, conhecimentos e técnicas" que
      - os grupos "reconhecem como parte integrante de seu patrimônio cultural";
      - se transmitem "de geração em geração";
      - são "constantemente recriado[s] [...] em função de seu ambiente, de sua interação com a natureza e de sua história";
      - geram "um sentimento de identidade e continuidade".

      Os campos que interessam ao projeto incluem "d) conhecimentos e práticas relacionados à natureza" e "e) técnicas artesanais tradicionais".
    - **Decreto 3.551/2000:** o Livro dos Saberes trata de "conhecimentos e modos de fazer enraizados no cotidiano das comunidades". A "continuidade histórica" e a "relevância nacional" valem só para o registro no IPHAN, não para admitir uma prática no acervo.
  - **[PROPOSTA]** Cada critério vira um campo da CLB situada, preenchido com a evidência que o atesta:
    - referência à identidade ou à memória de um grupo;
    - reconhecimento pelo grupo;
    - transmissão entre gerações;
    - recriação (é a Transformação de W, item 2).

    O critério que ainda não foi atestado vira **Falta**, nunca recusa (princ. 10).
  - A Convenção admite "em alguns casos, os indivíduos" como portadores (um mestre, por exemplo). Uma prática assim pode ser cultural sem ser, ainda, a prática comum que ancora W.
  - A régua de 4 filtros (P14) continua para triar as contribuições de pessoas; não define o que é prática cultural.
- **Fonte contrária:** é documentação, nunca correção feita por nós. Fica anexada, e a prática admitida continua de pé. Uma tentativa de revisionismo pode ficar fora; na trilha resta uma linha só: "não admitida: revisionismo" (acordo 4).
- **Fonte que corrige** (a si mesma ou a outra): registra-se uma relação **Correção** entre as fontes. Nós não aplicamos a correção.
- **Proposição e Evidência:** a Proposição (CLB situada × atributo × valor × período) junta as suas Evidências, cada uma um trecho de fonte.
  - μ e λ descrevem quanta documentação há a favor e quanta documentação divergente foi registrada, contadas por **linhagens independentes** (`deriva_de`): dez textos que copiam o mesmo autor contam como um.
  - Não são um veredito. O estado "inconsistente" significa "há documentação divergente", e as duas convivem (P29). O estado paracompleto é a Falta.
- **Peso por tipo de fonte (l.74):** **[PROPOSTA]** não usar. Ele faria da epistemologia contemporânea o juiz das outras, o que a P27 rejeita (Anexo A, l.890).

### 4. Status em eixos separados (§6)

Hoje "verificado" mistura coisas diferentes. **[PROPOSTA]** Um eixo para cada coisa:
1. **Fluxo da Entrada.**
2. **Localização do trecho** (script): localizado / não localizado / não verificável por máquina, que vira Falta.
3. **Fidelidade da leitura:** o trecho diz o que afirmamos que ele diz? Isso confere a **nossa** leitura, não a verdade da prática; não é julgar.
4. **Estado da proposição:** calculado, descritivo.
5. **Estado editorial da ficha.**

Uma tabela liga os eixos aos selos atuais.

### 5. Trecho literal conferido por script (§6, Passo 2)

- **Script, não IA.** A pergunta "o trecho X está no texto Y?" tem resposta exata. Uma IA conferindo outra IA repete a falha nº 7 do legado.
- **Python:** já previsto no Passo 2; tem as bibliotecas certas (normalização, comparação aproximada para OCR, extração de HTML e PDF) e roda igual na máquina e na nuvem. Roda **a cada envio ao GitHub**. No plano gratuito privado, ele **avisa, mas não bloqueia**: o bloqueio depende da decisão sobre o portão (item 16, lote B).
- **Custódia do texto da fonte [PROPOSTA]:** a v0.1 (§5.1) não deixa cópias de terceiros no Git. Por isso o trecho é conferido **no momento da extração**, lendo o texto da fonte (ou a cópia do Wayback, o arquivo público de páginas da web) na hora. No Git ficam só o trecho, o localizador, o hash (impressão digital) do texto lido e a data.
- **O difícil é ter o texto da fonte.** Uma transcrição feita por IA fica marcada como tal, com o link da imagem da página. Abaixo do limiar de semelhança, o trecho vira Falta ("não verificável por máquina") e vai para a cota humana.
- **Formato:** como no seletor de citação da W3C Web Annotation: o texto exato, um pedaço antes, um depois e o localizador.

### 6. Termo como entrada terminológica (princ. 2, §5.7, §6)

**[PROPOSTA]** Conceito → designações → variantes, cada uma com seu uso no lugar e no tempo → abonações com fonte (estrutura do TBX, ISO 30042; exportável para SKOS).
- **Variante linguística** (vai ao glossário) ≠ **forma de busca** (OCR, grafia truncada; só vai ao booleano).
- O termo nasce **candidato** e vira **atestado** com a primeira abonação de trecho localizado. Os termos do legado entram como candidatos.
- Um único registro gera, por script, os booleanos, os links do wiki e o glossário. O link leva à página do termo, que separa os sentidos regionais (P23).
- O contrato do Termo entra já na 1ª rodada do Passo 1 (l.508).

### 7. Agente Jurídico de precaução (§7 Passo 1, §5.4, §8)

**[PROPOSTA]** Um papel novo no mapa de agentes: **Jurídico**. Ele examina cada item antes da publicação.
- **Ele só pode criar Faltas, nunca autorizar.** Na dúvida, falta.
- **Regras fixas por script** cobrem os casos óbvios, para não depender só da percepção do agente.
- A consulta jurídica externa sai do caminho crítico. A revisão por profissional habilitado dos artefatos jurídicos e sanitários que circulam (Passo 9) fica como está na v0.1.
- **Barrar não basta: toda Falta jurídica traz o porquê e um caminho de liberação assistido [VIGENTE pela fala de Vicente de 16/10; o formato é PROPOSTA]:**
  - **por que está barrado:** a norma, citada, em português simples;
  - **o que destravaria,** por exemplo cadastro no SisGen, consentimento da comunidade, licença do autor, parecer ou consulta ao CGen;
  - **passo a passo:** onde fazer, em que ordem, que documentos reunir e como preencher cada campo, com modelos prontos que o agente deixa quase completos para Vicente conferir e assinar;
  - **estado do caminho:** não iniciado / em andamento / liberado, com data e comprovante.
- **Limites honestos:** o agente orienta e prepara, e **nunca autoriza nem protocola em nome de Vicente**. Cada guia só é publicado depois de os formulários e os prazos serem conferidos no portal oficial (nível "oficial"). Onde a lei exige profissional habilitado, o guia diz isso, e o passo vira "contratar ou consultar".
- **Guias a preparar, em ordem de provável uso:** cadastro no SisGen e consentimento prévio informado (Lei 13.123); licença de uso de texto, imagem e áudio de terceiros (Lei 9.610); termo de consentimento e atendimento ao titular (LGPD); pedido de registro de bem imaterial no IPHAN (Decreto 3.551 e Res. 1/2006, a conferir).
- **Voltou o "modelo de pedido de registro":** o revisor o tinha descartado, e agora ele volta como guia assistido, com revisão profissional. É uma revisão de decisão por pedido novo de Vicente.

**A sequência de perguntas que o agente faz** (textos conferidos na fonte oficial):

1. **Direito autoral (Lei 9.610):**
   - **O modo de fazer em si é livre.** "Não são objeto de proteção [...] as idéias, procedimentos normativos, sistemas, métodos [...] como tais" (art. 8º, I). O que tem dono é o texto, a foto ou o vídeo de quem descreveu.
   - **Citação literal é permitida** "na medida justificada para o fim a atingir, indicando-se o nome do autor e a origem da obra" (art. 46, III). Isso casa com o trecho literal e com a trilha.
   - **Fontes antigas:** os direitos patrimoniais duram 70 anos a partir de 1º de janeiro do ano seguinte à morte do autor (art. 41). Muitas fontes do início do século XX estão em domínio público.
   - **Atenção:** a obra de "autor desconhecido" é de domínio público, "ressalvada a proteção legal aos conhecimentos étnicos e tradicionais" (art. 45, II).
   - **Imagem ou vídeo de terceiros:** só por link. Republicar sem licença vira Falta.
2. **Conhecimento tradicional (Lei 13.123/2015, Decreto 8.772/2016):**
   - **É conhecimento de "população indígena, comunidade tradicional ou agricultor tradicional sobre as propriedades ou usos [...] associada ao patrimônio genético"** (art. 2º, II), por exemplo o uso de uma planta nativa? Se não for, esta lei não se aplica.
   - **Se for, a origem é identificável?** "Qualquer [...] comunidade tradicional [...] que cria, desenvolve, detém ou conserva" o conhecimento é origem identificável (Decreto 8.772, art. 12, §3º).
     - **Identificável:** o acesso depende de consentimento prévio informado (art. 9º), e a comunidade pode negá-lo (Decreto, art. 13). **Sem consentimento: Falta.**
     - **Não identificável:** o acesso "independe de consentimento prévio informado" (art. 9º, §2º).
   - **Cadastro no SisGen:** se a atividade for "acesso", o cadastro vem antes da "divulgação dos resultados" (art. 12, §2º). O cadastro é declaratório; não é um pedido de licença (a confirmar no SisGen).
   - **Sempre:** indicar a origem do conhecimento em toda publicação (art. 10, II). É o princípio da rastreabilidade, agora também como dever legal.
3. **Restrição por costume:** a Convenção pede respeito aos "costumes que regem o acesso a determinados aspectos" do patrimônio (art. 13, d, ii). Isso vai para o campo "restrição".
4. **LGPD:** pessoas citadas e quem contribui.
5. **Substâncias controladas:** Portaria SVS/MS 344/1998.

**Respostas às perguntas de Vicente:**
- **Prática amplamente conhecida precisa de autorização?**
  - Para documentar e publicar práticas culturais **em geral, nenhuma norma lida exige autorização**.
  - A única exceção possível é a Lei 13.123, e "ser conhecida" não basta para escapar dela. A lei alcança o conhecimento "ainda que obtido de fontes secundárias tais como feiras, publicações, inventários, filmes, artigos científicos" (art. 2º, IX). Uma prática conhecida que alguma comunidade ainda detém ou conserva tem origem identificável.
- **E quando não há quem autorizar?**
  - Se nenhuma comunidade pode ser ligada à origem, o conhecimento é "de origem não identificável" e **não precisa de consentimento** (art. 9º, §2º). Se houver "acesso", o cadastro continua.
  - Desde 2025, qualquer cidadão pode pedir ao CGen que declare isso (Resolução CGen 47/2025, arts. 4º e 7º, que criam a "Lista de CTA - ONI").
  - Se a origem é identificável mas não se alcança ninguém para consentir, a lei aceita, entre outras formas, o "parecer do órgão oficial competente" (art. 9º, §1º, III). Até lá, **Falta**.

**A incerteza que nenhuma norma resolve (conferido):** não existe orientação do CGen dizendo se um acervo histórico-cultural como este é "acesso". "Pesquisa" inclui atividade "teórica" (art. 2º, X). A exclusão não foi encontrada em nenhuma das listas oficiais do CGen.
- **Pela regra de Vicente,** o agente trata esse caso como Falta sempre que o conhecimento for de origem identificável e associado ao patrimônio genético. Também trata como Falta quando a origem não é identificável, mas a atividade pode ser "acesso" e não há cadastro no SisGen.
  - **Efeito a ver:** quase toda CLB com planta nativa teria o modo de fazer retido como Falta até haver cadastro, consentimento ou resposta do CGen. Isso pode travar o Passo 6. Por isso o caminho a seguir é uma das decisões que bloqueiam, no topo da lista. Esse patrimônio inclui as plantas e talvez os microrganismos da fermentação; a definição do art. 2º, I, ainda não foi conferida, e a v0.2 a confere.
- **Formas formais de desfazer a Falta** (a escolha é de Vicente): cadastro no SisGen, consentimento conforme o art. 9º, consulta ao CGen.

**Campos de proteção no modelo:**
- origem do conhecimento: identificável / não identificável;
- comunidade detentora;
- restrição;
- consentimento granular;
- **pessoas citadas:** "quem ensinou" expõe quem não consentiu.

### 8. Governança e legibilidade do plano (§0, §9, §11.4)

**[PROPOSTA, vira VIGENTE se aprovada aqui]:**
- Nenhum agente executa um item [PROPOSTA]. Um item vira plano um a um, com uma entrada D que traz a **essência confirmada por Vicente** e a diretriz resultante. A fala original fica guardada só na trilha, e o texto de trabalho registra o sentido, não a transcrição.
- **Como registro um comentário de Vicente:** (1) capto a essência, (2) interpreto "princípio" como "de início" quando o contexto indicar, (3) devolvo o que entendi e peço confirmação, (4) só então escrevo a diretriz.
- O diário de sessão vai para `trilhas/`, não para o Registro de Decisões (l.692).
- O Passo 1 deixa de pedir custos estimados antes de executar (P96); eles são medidos no caso-piloto.
- **Legenda das referências no §0:** "Pn = pedido n de Vicente na conversa original, transcrito no Anexo A (buscar `#### Pn`)". Cada Pn citado nos princípios ganha um resumo curto ao lado.
- **Acordo de trabalho 6:** exemplos ilustram, nunca limitam.

### 9. Operação dimensionada por 1 a 3 h de curadoria (§5.5, §8, §11)

**[PROPOSTA]:**
- **Dois parâmetros** no lugar dos "15" que divergiam:
  - lote de máquina: 15 itens por rodada (P94);
  - cota de juízo humano: até 15 por semana (P84), que cabe em 1,25 a 2,5 h.
- **Ordem da cota humana:**
  1. o que sustenta aviso, saúde ou política (princ. 4);
  2. as contribuições de pessoas;
  3. uma amostra **sorteada, com semente registrada**.
- Declarar que a D-012 está cumprida em parte enquanto o tratamento com IA não estiver agendado (item 10).

### 10. A nuvem faz as buscas e os tratamentos; Google só se necessário (§5.1, §5.5)

**Repositório privado no GitHub** = a cópia idêntica e sincronizada.
- **Ritual de sincronização:** cada sessão começa com `git pull` e termina com commit e `git push`. Mapa de custódia (o que vive onde) e **teste de reconstituição** no Passo 2.

**Duas camadas, sem Google e sem depender do computador ligado [PROPOSTA]:**

| Camada | Faz | Custo |
|---|---|---|
| **GitHub Actions** (cron + a cada envio), scripts Python, sem IA | buscas em feeds e APIs, deduplicação, cópia no Wayback, checagem de links, validação de trechos, relatório do dia; falhas avisam por e-mail nativo | grátis até 2.000 min/mês em repositório privado (Anexo C) |
| **Rotina agendada do Claude na nuvem** (fase 2, depois de um teste) | tratamento com IA em lotes de 15 (P94) e buscas por API já aprovadas, abrindo proposta para revisão (lote B); buscas assistidas ficam com pessoas | gasta a cota da assinatura; teto definido por Vicente (pergunta 16) |

- **Fase 1:** só o GitHub Actions, para o validador e as buscas das 2 ou 3 fontes do caso-piloto.
- **Se Vicente não aceitar a leitura dos termos do Actions** (item 13), as buscas do piloto rodam em sessão, na máquina de Vicente.
- **Tipos de trabalho e quem os executa:**
  - **monitoramento** (o que é novo): script ou API;
  - **escavação** (o que é retrospectivo): por API quando a fonte permite e por pessoa quando ela barra robôs;
  - **tratamento com IA:** em sessão na fase 1 e por rotina na fase 2.

- **A verificar na implementação, para o Anexo C.3:** como funcionam as rotinas do Claude (limites, acesso ao repositório, custo) e se feeds bloqueiam os servidores do GitHub.
- **Canais de pessoas** (formulário, e-mail, envio de documentos) precisam de um lugar para dados pessoais fora do Git, com acesso controlado. O Google só fica se continuar sendo necessário para isso. Decisão no Passo 4, comparando opções.

### 11. Busca e ambientes (§5.2, §5.3, §6)

**[PROPOSTA]:**
- **Consulta** registrada, com tipo: termo / mista / **só descritores**. Só a busca sem o nome da bebida acha o que ainda não tem nome (P3, P5).
- A Matriz de Pegadas e Vácuos (P89) é **gerada** do registro de execuções.
- "Exaurido" vale por ambiente × consulta × período; uma variante nova reabre o ambiente.
- **Monitoramento** (automático, barato) é distinto de **escavação** (a partir de 1900, assistida, cara).
- O legado vira **um ambiente** do Registro; o Passo 3 deixa de bloquear o Passo 4.

### 12. Critérios de pronto realistas e padrões de campo

**Critérios:**
- **Passo 6:** reprovar só a frase **factual** sem marcação.
- **Passo 7:** a célula X×Y vazia é "não observada"; vira **Falta** ou vácuo só com indício.

**Padrões, como convenção de campos:**
- EDTF (ISO 8601-2) para datas incertas;
- CSL-JSON para Fonte e "como citar";
- JSON Schema para os contratos;
- PROV para a trilha;
- Flora e Funga do Brasil para a origem botânica, separada do status cultural (P6).

**Risco de privacidade, que vai para o Passo 0 (não é padrão de campo):** a implantação "App da Web" do Apps Script (P70–P71) pode ler as planilhas restritas. É uma checagem de 5 minutos em Implantar > Gerenciar implantações. Como o site não será aproveitado (D-024), o caminho mais seguro é Vicente **arquivar essa implantação e despublicar o Google Site**.

---

## Parte 2 — Perguntas de 15/10 à tarde: fontes, admissão, trabalho coletivo, região, continuidade e ferramentas de ação

**Como esta parte foi feita e quanto custou (medido).**
- **Estrutura:** dez frentes de pesquisa em paralelo, cada uma com um verificador independente.
- **Custo:** quatro frentes chegaram a rodar e cada uma consumiu de 200 a 450 mil tokens, em cerca de 25 minutos. Com 1,4 milhão de tokens consumidos, o limite de uso da sessão foi atingido.
- **Resultado:**
  - três frentes terminaram: fontes históricas, fontes acadêmicas, mídia atual e oralidade gravada;
  - duas morreram no meio, sem deixar resultado, e cerca de 544 mil tokens se perderam;
  - cinco nem começaram;
  - os verificadores não rodaram. Os fatos das três frentes foram conferidos na web pelos próprios pesquisadores, com nível declarado, mas sem uma segunda leitura independente.
- **O que eu desenhei:** as frentes interrompidas (fontes oficiais e de patrimônio, métodos de busca, admissão de pessoas, coletivo, região, continuidade e ferramentas). Usei o documento e o que as três frentes acharam, sem novas buscas, para não esgotar o limite de novo. Tudo o que depende de norma ou de serviço externo está marcado "a conferir".
- **Rastreabilidade:** os códigos FH-n, PA-n e MO-n remetem às propostas completas das três frentes, guardadas no registro do workflow (`wf_89a76895-c9b`); elas vão para o Anexo D.
- **Retomada com guarda de orçamento (15/10):**
  - **Lote A** (`wf_5e7f9960-6a1`): 5 agentes Sonnet, com teto de 15 a 18 consultas à web, gastaram **212 mil tokens** no total (de 34 a 47 mil cada, cerca de 20 minutos). Cobriu fontes oficiais, admissão de pessoas, ferramentas por tier, região e a reconferência de 10 fatos.
  - **Lote B** (`wf_c21065e2-8ff`): 3 agentes Sonnet gastaram **137 mil tokens** (de 38 a 54 mil cada), cobrindo o jurídico do coletivo (16-J), o coletivo operacional (16) e a continuidade com os métodos (14, 18, 19).
  - **Total da janela até aqui:** 349 mil tokens de subagentes, abaixo do teto de 600 mil.
  - Por último, um crítico sem web.

### Respostas às perguntas de 15/10, em uma linha cada

| Pergunta de Vicente | Resposta curta | Onde |
|---|---|---|
| (a) Revisão das fontes e de como buscar | Cerca de 60 fontes conferidas. Fontes que barram robôs viram trabalho de pessoa, pedido à instituição ou Falta. O RSS do Google está vedado e os Alertas chegam por e-mail. Redes sociais entram só por link. As fontes acadêmicas têm API. **Resposta parcial:** das fontes oficiais, o Querido Diário é instável, o LexML está barrado, e RTID, RCID e INCRA ainda não foram testados | 13, 14 |
| (b) Admissão de dados, pessoas e oralidades | Tipos de evidência e porta de cada um. Abrem já: escrito, oralidade publicada, depoimento em acervo, relato, imagem e objeto. Entrevista própria e observação de campo ficam fechadas. Na fase 1 não entra oralidade não escrita, e W fica como Falta onde não houver etnografia ou gravação | 15 |
| (c) A ingestão e o coletivo podem melhorar? | Sim. Um fluxo só: a máquina grava em `entrada/`; pessoas e IA propõem para `acervo/`; o validador confere; outra pessoa aprova | 16 |
| (d) O coletivo tem o mesmo tratamento do individual (jurídico, sem reduzir a isso)? | Não. São três degraus: só Vicente pesquisa / outras pessoas contribuem / o projeto publica. Cada degrau traz deveres próprios | 16-J e 16 |
| (e) O wiki está organizado por região? | Não na v0.1. Proposta: Lugar com UF, município, localidade e bioma derivado; território e região cultural nascem de baixo para cima | 17 |
| (f) 15 CLB não esgotam uma fonte? | Correto. 15 é lote e cota. Sem total conhecido, nada se esgota; o limite real é o teto por recorte | 18 |
| (g) Como organizar as continuidades? | Arquivos de estado por recorte e por consulta, ritual com ponto de retomada a cada lote e guarda de orçamento | 19 |
| (h) Os tiers têm ferramentas de ação, como planos de aula? | Sim, sob demanda. A fase 1 é um kit de fonte primária para educadores; o planejador de aulas (D-006) vem depois | 20 |
| (i) Critérios legais; autorização; quando não há quem autorize | Os critérios vêm da CF 216, da Convenção de 2003 e do Decreto 3.551. Documentar não pede autorização em geral, salvo pela Lei 13.123. A origem não identificável dispensa consentimento, mas pode exigir cadastro | 3, 7 |

### Fase 1 e fase 2 (o conceito fica inteiro; muda só a ordem) [PROPOSTA]

- **Fase 1, para caber em 1 a 3 h por semana:**
  - **pessoas:** só Vicente e os agentes, com logs. A segunda leitura vem do validador, de agentes verificadores com harness diferente e da amostra sorteada de Vicente;
  - **fontes:** caso-piloto com 2 ou 3;
  - **máquina:** validador; GitHub Actions só para o validador e as buscas do piloto;
  - **contribuições externas:** nenhuma ainda. O formulário só abre quando os deveres do degrau 2 do 16-J existirem: licença, aviso de privacidade e canal com o titular;
  - **ferramenta:** o kit de fonte primária (20);
  - **lugar:** UF, município, localidade e bioma derivado (17);
  - **admissão:** as portas da admissão escritas (15). O relato de contribuinte espera a fase 2;
  - **Jurídico:** com regras fixas (7);
  - **legado (D-024):** chegou em 15/10 à pasta `legado/`: 45 verbetes, o Feed de 69 e o grafo v7, sem as planilhas pessoais. Um script faz o inventário, separa os termos e testa os links. Uma amostra sorteada é conferida dentro da cota, e os termos entram como candidatos.
- **Fase 2, depois de medir as horas reais:**
  - **contribuições e publicação:** contribuições externas e os degraus 2 e 3 (15, 16, 16-J);
  - **coleta:** rotina do Claude na nuvem, depois de um teste (19); mutirão (16); bola de neve, relatório do funil e Wikidata (14); fichas de acesso das outras fontes (13);
  - **wiki e ferramentas:** mapa, território e região cultural (17); outros grupos e ferramentas (20);
  - **padrões:** exportações para SKOS, TBX e PROV (6, 12). Os campos já nascem compatíveis na fase 1.
- **Gatilho para passar à fase 2 [PROPOSTA]:** as três condições juntas:
  1. o caso-piloto foi do bruto à ficha com a trilha completa;
  2. as horas reais de 4 semanas couberam em 1 a 3 h;
  3. as decisões do degrau 2 do 16-J estão tomadas.
- **Revisão de essencialidade (D-025), depois das coletas e verificações da fase 1:**
  - reavaliar as regras jurídicas, de colaboração e de organização e manter só o essencial para a biblioteca existir;
  - o Jurídico é moldura, não conteúdo: o projeto não replica a legislação, mas **nenhuma obrigação legal é desprezada** e cada barreira traz porquê e caminho assistido;
  - o grafo 4D fica fora desta revisão (item 21);
  - a nota pode caducar.

### 13. Revisão das fontes de busca: o que a conferência de 15/10 mudou

Foram conferidas cerca de 60 fontes. **Regras novas [PROPOSTA]:**
- **Proteção contra robôs nunca é contornada.**
  - **Em 15/10:** 8 de 20 sites históricos recusaram o leitor automático (erro HTTP 403, "acesso negado"): Hemeroteca Digital, BNDigital, o site da BHL, HathiTrust, a API do Gallica, o catálogo do IBGE, o CRL e o Tesauro do CNFCP. O SIAN pediu captcha, o teste de "não sou robô".
  - **pyHDB:** a ferramenta acadêmica pyHDB contorna a proteção da Hemeroteca; esse recurso não se usa.
  - **O que é barrado** vira escavação por pessoa, pedido de acesso à instituição ou Falta "fonte inacessível" (FH-1).
- **Cada Ambiente ganha uma ficha de acesso testada e datada**, conferida em cada lugar de execução (navegador, script local, GitHub, rotina do Claude):
  - via permitida;
  - sintaxe de busca;
  - texto disponível (OCR, PDF ou nenhum);
  - padrão de link permanente;
  - termos de uso;
  - o robots.txt, que é o arquivo em que cada site diz o que robôs podem ler;
  - limites de uso (FH-1, MO-1).
- **Google [oficial; corrige o Anexo C.2]:**
  - O RSS de busca do Google Notícias e os feeds do Google Alertas ficam fora do que o robots.txt do Google libera. Os termos do Google proíbem o acesso automático que contrarie esse arquivo.
  - Os Alertas passam a chegar **por e-mail** à caixa do projeto (MO-1).
- **Redes sociais [oficial]:** Meta e TikTok proíbem a coleta automática. O YouTube só permite a coleta pela API oficial (100 buscas por dia, dados guardados por no máximo 30 dias, legendas de vídeos de terceiros inacessíveis). Postagens e vídeos entram **quando uma pessoa manda o link** (MO-7).
- **Fontes acadêmicas [oficial]:** quase todas têm uma porta para programas:
  - API (porta de consulta para programas): VuFind na BDTD, no Oasisbr e na LA Referencia; e a Crossref, aberta;
  - OAI-PMH (o protocolo em que um programa pede ao acervo "o que mudou desde a data X"): SciELO, Embrapa, eduCAPES e revistas em OJS;
  - dados abertos: CAPES.
- **Exceções e custos acadêmicos [oficial]:**
  - **OpenAlex agora cobra:** com chave grátis, o orçamento é de US$ 1 por dia; a paginação completa exige chave; os filtros por data de entrada são pagos.
  - **Google Acadêmico:** só manual, porque o robots.txt proíbe robôs (PA-1).
- **Licença e acesso na Fonte** (PA-5):
  - a Fonte registra o acesso (aberto, assinado, físico) e a licença;
  - trecho longo, figura ou PDF só entram no wiki se a licença permitir;
  - nenhuma rotina usa senha institucional de ninguém.
- **Dados abertos com lista positiva de campos:** o arquivo da CAPES traz identificadores de pessoas, que são descartados antes de gravar (PA-6).
- **Termos do GitHub Actions [oficial; ajusta o item 10]:**
  - O que dizem: as máquinas do Actions "não devem ser usadas em atividades alheias à produção, ao teste, à implantação ou à publicação" do projeto do repositório. Usá-las para coletar tem risco.
  - Leitura proposta: a coleta produz o conteúdo que o próprio repositório publica. O Flat Data, do GitHub Next, faz exatamente isso.
  - Vicente decide se aceita essa leitura ou se a coleta roda na rotina do Claude (MO-6).
- **Sem servidores de RSS de terceiros** (RSS-Bridge, RSSHub, changedetection.io, instâncias públicas). Usamos geradores próprios em Python, que respeitam o robots.txt e espaçam os pedidos (MO-6).
- **Tesauro de Folclore e Cultura Popular Brasileira (CNFCP):** existe (Portaria CNFCP/IPHAN nº 82/2026, oficial), mas o acesso online não foi confirmado. Serve como correspondência para os termos, nunca como hierarquia imposta (FH-4).
- **Fontes oficiais e de patrimônio** (IPHAN, Querido Diário, LexML, DOU, FUNAI, INCRA, Palmares, ISA, Museu do Índio, MAPA): a frente foi interrompida, então ficam **a conferir no Passo 4**. A Biblioteca Digital do Iphan abriu e tem busca.
- **O catálogo inteiro vira o novo Anexo E — Ambientes candidatos**, semente do Registro de Ambientes do Passo 4. Ele traz, para cada fonte, a via de acesso, a sintaxe, os termos, o uso (monitoramento ou escavação) e o nível de verificação.

**Lote A (15/10): fontes oficiais e reconferência**
- **Querido Diário** (diários oficiais municipais):
  - a API é aberta, mas instável: 2 de 5 chamadas falharam, e o leitor da web falhou no certificado, embora o curl funcione;
  - a busca traz muito ruído, e o total aparece travado em 10.000;
  - convém restringir a busca por município e por data.
- **LexML:** está atrás de uma verificação anti-robô do Senado, que não foi contornada. A busca oficial alternativa (SRU) ainda não foi testada.
- **IPHAN:** o Banco de Bens Registrados (bcr.iphan.gov.br) libera robôs no robots.txt e tem mapa do site; também existe o inrc.iphan.gov.br. Falta testar a busca.
- **DOU:** pelo INLABS, com cadastro, em XML diário, que não é a versão certificada.
- **Câmara:** tem dados abertos com API.
- **FUNAI:**
  - geodados de terras indígenas por WFS (um serviço padrão de mapas para baixar camadas);
  - o rodapé declara **CC BY-ND 3.0, que proíbe obra derivada**;
  - por isso guardamos só a referência, o trecho e o link.
- **Palmares:** comunidades certificadas numa planilha mensal.
- **Teste real de busca:**
  - nenhuma lei municipal achada;
  - achou-se o **autógrafo do PL 169/2023 de SC**, que declara a "Cachaça com Butiá" Patrimônio Cultural Imaterial do estado (oficial; sanção não confirmada);
  - há projetos semelhantes no CE, TO e PB (secundária).
  - Regra nova [PROPOSTA]: **projeto de lei e autógrafo entram como vestígio com estado**, e só viram "lei" quando a publicação no diário oficial for achada.
- **Reconferência independente dos fatos que sustentam decisões:**
  - **Confirmados:** o RSS do Google Notícias está vedado no robots.txt; os termos do GitHub Actions; o orçamento do OpenAlex com chave; a Meta proíbe coleta automatizada; a Research API do TikTok no Brasil é só para segurança de jovens; o YouTube tem 100 buscas por dia.
  - **Corrigidos:**
    - os Alertas do Google estão bloqueados, com exceções em /alerts/manage, /alerts/remove e /alerts/$;
    - no YouTube, os dados da API devem ser **apagados ou atualizados** depois de 30 dias;
    - a proibição de scripts do TikTok foi lida nos termos dos EUA; os termos brasileiros não foram lidos.
  - **Não reconferidos** (ficam com uma só conferência): os termos gerais do Google, a sintaxe da Hemeroteca, o Wikisource, a tabela de biomas do IBGE e a BHL.

### 14. Como as buscas são feitas (§5.3, item 11)

**[PROPOSTA]**
- **Cinco adaptadores por protocolo** substituem um script por fonte: API do VuFind; OAI-PMH; APIs com cursor (o marcador de onde a coleta parou); dados abertos (CKAN); modo assistido (registra a busca manual).
  - O "RSS criado por nós" vira uma consulta repetida que anota só o que ainda não foi visto e publica um feed com as novidades.
  - Um ambiente novo com protocolo conhecido entra com uma linha de configuração (PA-1).
- **Sintaxe e limites por ambiente:**
  - um arquivo traduz cada Consulta para a linguagem de busca daquele ambiente;
  - **resposta saturada:** a que bate no limite da fonte (ex.: GDELT, 250 resultados e 3 meses). Ela divide a janela e repete; só a passada completa e não saturada conta como pegada (MO-2, FH-4).
- **Formas de busca medidas.** As grafias antigas e os erros de OCR são gerados por regra e só ficam se renderem ocorrências; o rendimento de cada forma é registrado (FH-4). As reformas ortográficas desde 1900, que servem de base às regras, ficam a conferir.
- **Bola de neve:** a partir de cada fonte admitida, buscar o que ela cita, quem a cita e os assuntos que os catalogadores lhe deram. Isso gera candidatos, com o caminho registrado (P97) (PA-3).
  - Exemplo conferido: "Cauim: entre comida e ebriedade" (Boletim Goeldi, 2018) tem 22 referências e 8 citações, e a consulta custou US$ 0,0001.
- **País e idioma anotam, nunca recortam.** "Do cauim à garapa" (2026) está sem país e sem idioma no OpenAlex e sumiria com um filtro (PA-4).
- **Novidade é um ID ainda não visto, nunca uma data.** O RSS da BDTD só traz o ano, e a Embrapa reescreveu datas antigas em 10/10/2026 (PA-2).
- **Canal de novidades por fonte:** OAI com data, RSS do Internet Archive, comparação de página por script ou verificação manual mensal (FH-7).
- **Uma Entrada por item**, mesmo quando várias consultas acham o mesmo item; as descobertas registradas medem o rendimento de cada consulta (MO).
- **Wikidata** (dados em CC0) semeia termos candidatos, nunca abonações (MO-8).
- **Relatório do funil** com números calculados, no formato do fluxograma PRISMA (padrão de revisões sistemáticas e de escopo; a conferir).

**Lote B (15/10): métodos de busca conferidos e ajustes do revisor**
- **Grafias:**
  - a Lei 5.765/1971 aboliu acentos diferenciais e o trema em certos casos (oficial, Senado);
  - o Formulário Ortográfico de 1943 eliminou th, ph, rh, y e as consoantes dobradas, salvo rr e ss (secundária);
  - a reforma portuguesa de 1911 não foi adotada pelo Brasil, e os acordos de 1931 e 1945 não vingaram aqui (secundária);
  - o Acordo de 1990 foi promulgado pelo Decreto 6.583/2008 (oficial), com transição prorrogada pelo Decreto 7.875/2012 até 31/12/2015 (a data é secundária).
  - **Consequência:** entre 1911 e 1943, duas grafias convivem. As regras geram **variantes por família** (ph/f, th/t, y/i, consoantes dobradas, acentos, trema, hífen), sem data de corte, e **nunca corrigem o texto da fonte**. Cada forma gerada guarda a regra, a fonte da norma e a data.
- **PRISMA 2020** (Page et al., BMJ 2021;372:n71) e **PRISMA-ScR** (Tricco et al., Ann Intern Med 2018;169(7):467–473) são guias de relato de revisões (secundária). A CLB não é uma revisão e não julga qualidade, então o relatório do funil é **"inspirado em"**, sem alegar conformidade.
- **Adaptadores:** começar com os que as fontes do caso-piloto exigem e acrescentar outros só quando uma fonte real pedir, em vez de cinco de saída.
- **Teto por recorte:** cada recorte tem um teto de chamadas e de divisões da janela. Ao estourar, salva o estado e registra a Falta "busca interrompida por teto".

### 15. Admissão de novos dados, pessoas e oralidades (§5.4, §6)

**Resposta: pode melhorar.** Hoje o plano admite bem o documento e o formulário, mas faltam tipos de dado e papéis de pessoas.

**Tipos de evidência e a porta de cada um [PROPOSTA]:**

| Tipo | Como entra | Localizador | Cuidado |
|---|---|---|---|
| Escrito publicado, de arquivo ou oficial | coleta ou pessoa | página, URL | trecho conferido pela escada máquina → pessoa (FH-3) |
| Oralidade registrada por pesquisa (fala publicada em tese ou etnografia) | coleta | página | a fala de quem pratica fica separada da análise do pesquisador, que fica visível como mediação (PA-7) |
| Depoimento gravado em acervo (Museu da Pessoa, CPDOC, YouTube…) | pessoa | `t=início,fim` em segundos (W3C Media Fragments) + transcrição | termos do acervo; o áudio nunca é republicado, entra o link com marca de tempo (MO-4) |
| Entrevista feita pelo projeto | — | — | é "áudio": **reabre a P48**, decisão de Vicente; protocolo abaixo |
| Relato de contribuinte (as 8 perguntas) | formulário ou e-mail | ID da Entrada | quarentena + régua de 4 filtros (P14, P47) |
| Imagem ou foto | pessoa | URL | sem licença, só link (item 7) |
| Objeto ou recipiente | pessoa ou museu | catálogo do acervo | descrição; foto só com licença |
| Observação de campo | colaborador de confiança | nota datada | consentimento de quem aparece |

- **Voz no trecho** (FH-5):
  - cada evidência registra quem fala: o autor, uma pessoa citada em fala direta, uma instituição ou um anúncio;
  - W só se ancora na **fala de quem pratica**;
  - a leitura do repórter, do médico ou do folclorista é a perspectiva da fonte;
  - sem a fala de quem pratica, W fica como Falta.
- **Papéis das pessoas:**
  - contribuinte;
  - detentor ou mestre;
  - quem ensinou (a cadeia de transmissão, P53);
  - quem fala no trecho;
  - mediador (pesquisador ou entrevistador);
  - comunidade (coletivo e sujeito de direitos);
  - colaborador do projeto.

  Cada papel define o que se registra, o consentimento e a forma de atribuição (nome, anônimo ou coletivo). No Git fica só um ID opaco e o papel.
- **Admissão de pessoas como colaboradoras**, em níveis:
  - anônima, pelo formulário;
  - identificada;
  - colaboradora de confiança, que assina um termo e aprende o protocolo;
  - guardiã indicada pela comunidade.

  A declaração de interesse (ex.: quem vende a bebida) vira um campo registrado, sem julgar nem excluir (P18; "não julgamos").
- **Entrevista feita pelo projeto** (só se Vicente reabrir a P48 para isso):
  - roteiro a partir das 8 perguntas e dos eixos X, Y, Z e W;
  - consentimento registrado, por escrito ou gravado, e carta de cessão de direitos;
  - transcrição literal com marca de tempo (a feita por IA fica marcada);
  - revisão pela pessoa entrevistada e devolutiva;
  - áudio fora do Git.

  **Normas a conferir antes:** Res. CNS 510/2016 (ética em pesquisa em ciências humanas e sociais), Res. CNS 304/2000 (povos indígenas), a regra da FUNAI para pesquisa em terra indígena, Código Civil art. 20 (imagem e voz), Lei 9.610 art. 7º (obras orais), LGPD art. 11 (dado sensível). Enquanto não forem conferidas, o Jurídico registra Falta.
- **Guarda de dado pessoal antes de cada gravação no Git** (MO-3): e-mail, telefone, CPF e URL com @perfil vão para fora do Git. Do YouTube, guarda-se o ID público do vídeo, nunca o canal nem o @. O hash foi retirado no lote A.

**Lote A (15/10): normas conferidas e ajustes do revisor**
- **Res. CNS 510/2016 (oficial):**
  - vale para pesquisa em ciências humanas e sociais com dados obtidos diretamente dos participantes ou com informação que identifica pessoas (art. 1º);
  - ficam fora do sistema de comitês de ética, entre outras, a pesquisa com informação de acesso público e a com informação de domínio público (parágrafo único do art. 1º);
  - a definição de pesquisa é ampla e inclui "saberes das pessoas e dos grupos" (art. 2º, XVI);
  - em comunidades tradicionais, a autorização do líder ou do coletivo vem somada ao consentimento individual (art. 13).
  - **Consequência:** o enquadramento do projeto (pesquisa ou documentação cultural independente) é uma **Falta aberta, a decidir por Vicente**.
- **Res. CNS 304/2000 (oficial):** exige a concordância da comunidade, por suas organizações ou conselhos, além do consentimento individual (item III.2.4).
- **FUNAI:** a IN nº 01, de 29/11/1995, sobre ingresso em terra indígena para pesquisa científica, está listada como vigente (oficial). A Portaria 1.401/2026 ainda não foi lida.
- **Ainda não conferidos, porque o Planalto caiu:** Código Civil art. 20, Lei 9.610 art. 7º (as obras orais podem estar no inciso II ou no III, e não no I) e LGPD. Vão no lote B.
- **Ajustes [PROPOSTA]:**
  - **Portas que abrem já:** escrito publicado, oralidade registrada por pesquisa, depoimento em acervo, relato de contribuinte, imagem e objeto.
  - **Portas fechadas:** entrevista própria e observação de campo, até Vicente decidir a P48 e o enquadramento. Em terra indígena, só com a FUNAI e a comunidade, e o projeto não faz esse trâmite sozinho.
  - **Colaboradores:** começar com **dois níveis**, anônimo e identificado. "De confiança" e "guardião" só existem quando houver uma pessoa ou comunidade concreta.
  - **Papéis viram etiquetas simples.** O código opaco (ex.: P-0042) liga a pessoa ao registro, e a tabela código → nome fica fora do Git, em lugar que Vicente define.
  - **YouTube:** guardar o ID público do vídeo quando uma pessoa registra a Fonte pela página. O que vem pela API segue a regra de apagar ou atualizar em 30 dias. O hash foi retirado, porque o hash de um ID público não protege nada.
  - **Novos:**
    - **pedido de retirada:** o registro passa a dizer "havia uma fala retirada", sem o conteúdo;
    - **crianças e adolescentes:** nunca registrar imagem, voz nem nome;
    - **medir a carga semanal da curadoria:** se a fila passar de uma semana de trabalho, nenhuma porta nova se abre.

### 16. Uma ferramenta coletiva tem o mesmo tratamento de um trabalho individual?

**Resposta: não. O registro é o mesmo; o tratamento muda.** [PROPOSTA]
- **Portão único:** nada entra no acervo direto, nem pessoa, nem IA, nem script que produz conteúdo.
  - **Onde vale:** a máquina grava as entradas brutas em `entrada/`. O portão vale para o que entra em `acervo/`.
  - **No GitHub gratuito privado,** o portão é **combinado, não imposto** (lote B; decisão no topo da lista).
  - Quem produz propõe, o validador confere e outra pessoa aprova, na medida do risco.
  - No GitHub, a proposta é um *pull request* (pedido de inclusão revisável) e o validador roda sozinho.
  - Quem não usa GitHub manda pelo formulário, e um curador transforma o envio em proposta.
- **Quem propõe não aprova.** No Wikisource, uma página "validada" exige dois contribuidores diferentes (oficial). O que sustenta aviso, saúde ou política exige duas pessoas (princ. 4).
- **Reserva de trabalho com prazo** (recortes, fatias de escuta), para não duplicar nem abandonar trabalho sem rastro.
- **Mutirão de escavação:** pessoas fazem o que os robôs não podem fazer nas fontes que os barram (FH-6, MO-5).
- **Curadoria distribuída:** revisores de confiança fazem as segundas leituras. A cota de Vicente vai para o risco alto e para as decisões. A capacidade passa a ser a soma de horas, medida.
- **Divergência de leitura** (o que o trecho diz): as duas leituras ficam lado a lado ou vão a uma terceira pessoa. Nunca vira julgamento da prática.
- **Crédito:** quem transcreveu, conferiu ou curou aparece na ficha e no "como citar", do jeito que escolheu (nome, anônimo ou coletivo).
- **Licença das contribuições e do acervo:** decisão de Vicente (ex.: CC BY 4.0 ou CC BY-NC-SA 4.0, a conferir), sempre abaixo das restrições comunitárias.
- **Governança comunitária:**
  - protocolo para pedir restrição, correção ou retirada, com prazo de resposta;
  - registro público das decisões editoriais, sem dado pessoal;
  - direitos do titular na LGPD (art. 18, a conferir).
- **Segurança:** contribuição é dado, nunca instrução (§5.4); quarentena; limite de envios no formulário.
- **Segunda pessoa de referência** com acesso ao repositório, para não depender de uma pessoa só.
- **Fila:** os arquivos de estado no repositório são a verdade. Um quadro de tarefas (GitHub Projects) é só uma vista, opcional.

**Lote B (15/10): coletivo operacional conferido e ajustes do revisor**
- **Achado central (oficial, documentação do GitHub):**
  - no plano **gratuito**, exigir revisão antes de juntar uma proposta (regras de ramo protegido) só existe em repositório **público**;
  - em repositório **privado**, isso pede plano pago (Pro ou Team);
  - **o "portão único" não pode ser imposto pela plataforma num repositório privado gratuito.**
- **Três saídas** (decisão de Vicente):
  1. **portão combinado:** o validador automático roda em toda proposta, e as pessoas combinam não gravar direto na versão principal. É grátis, mas depende de disciplina;
  2. **pagar o plano Pro ou Team**, com o preço a conferir;
  3. **tornar público só o acervo já liberado.** Exige cuidado, porque a quarentena continua privada.
- **Licenças (oficial):**
  - **CC BY 4.0:** permite copiar, adaptar e usar comercialmente, com crédito.
  - **CC BY-NC-SA 4.0:** só uso não comercial, e as obras derivadas usam a mesma licença.
  - **Atenção:** "não comercial" é vago e pode atrapalhar escolas, museus e editoras.
  - **Camadas de licença [PROPOSTA]:** textos e fichas escritos pelo projeto / dados estruturados / trechos de terceiros, que mantêm a regra da própria fonte / restrição comunitária, que vale acima de todas.
- **TK Labels (oficial):** etiquetas da Local Contexts com que comunidades anexam condições de acesso e uso, em três grupos (Proveniência, Protocolo, Permissão). Como convivem com as licenças abertas não foi conferido.
- **CRediT (oficial):** 14 papéis de contribuição. Começar com **3 ou 4 papéis simples** inspirados nele, com o crédito escolhido pela pessoa (nome, pseudônimo, anônimo ou coletivo) e o consentimento guardado fora do Git.
- **CARE (secundária):** Benefício coletivo, Autoridade para controlar, Responsabilidade e Ética, publicados pela Global Indigenous Data Alliance em 2019.
- **Editores para quem não é técnico:**
  - **Pages CMS e Decap CMS** são de código aberto, mas exigem conta e acesso de escrita no GitHub. O Decap precisa ainda de um servidor de login.
  - **Decisão:** não adotar agora. Quem não usa GitHub manda pelo formulário, e o contato fica fora do Git.
- **Mutirão:** quem participa respeita os termos de cada fonte e registra só o permitido (referência e trecho curto). O mutirão não é um jeito de contornar as regras da fonte.
- **Começar pequeno e medir:**
  - **fase 1:** Vicente, uma segunda pessoa, o formulário e o validador;
  - **depois:** mutirão e revisores distribuídos;
  - **horas reais:** medidas toda semana.

### 16-J. Como as questões jurídicas mudam do uso individual para o coletivo

Vicente esclareceu: a pergunta sobre trabalho coletivo era sobre **como o jurídico se aplica**. Este rascunho é meu, e todas as normas aqui estão **a conferir no lote B**. [PROPOSTA]

**Ideia central:** quem pesquisa para si tem a proteção de várias exceções da lei. Numa ferramenta coletiva e pública, essas exceções deixam de valer, e surgem papéis com responsabilidade: quem publica, quem trata os dados, quem responde pelo conteúdo de terceiros.

1. **Direito autoral (Lei 9.610):**
   - **No uso individual:** a cópia de pequenos trechos para uso privado de quem copia é permitida (art. 46, II).
   - **No coletivo:** pôr à disposição do público pede autorização (art. 29). Ficam as exceções, como a citação "na medida justificada", com autor e origem (art. 46, III, já conferido).
   - **Cópias arquivadas:** guardar uma cópia para conferir ≠ republicá-la.
   - **Quem contribui** com texto, foto ou áudio é o autor. O projeto precisa de uma licença dada por essa pessoa no momento do envio (arts. 49 e 50).
2. **Dados pessoais (LGPD):**
   - **No uso individual:** o tratamento feito por pessoa natural "para fins exclusivamente particulares e não econômicos" fica fora da LGPD (art. 4º, I).
   - **No coletivo:** a ferramenta trata dados de quem contribui e de pessoas citadas, e o projeto vira **controlador**, isto é, quem decide sobre os dados (art. 5º, VI). Daí vêm as obrigações:
     - base legal (art. 7º; para dado sensível, art. 11);
     - aviso de privacidade;
     - atendimento aos direitos do titular (art. 18);
     - segurança (art. 46);
     - registro das operações (art. 37).
   - **Possível simplificação:** para agente de pequeno porte (Resolução CD/ANPD nº 2/2022).
   - **Exceção acadêmica:** existe, mas é parcial e só vale para fim exclusivamente acadêmico (art. 4º, II, b).
3. **Conteúdo de terceiros (Marco Civil da Internet, Lei 12.965/2014, art. 19, e a decisão do STF de 2025 sobre a responsabilidade dos provedores):**
   - **Papel do projeto:** uma ferramenta que publica contribuições é provedora de aplicação. Precisa de canal de notificação e retirada, com prazo de resposta.
   - **O portão único** (nada é publicado sem revisão) reduz o risco. A hipótese de que ele faria do projeto um "editor" saiu no lote B, porque não tinha base.
4. **Conhecimento tradicional (Lei 13.123):**
   - **Quem responde:** o "acesso" é de quem realiza a pesquisa, seja pessoa natural ou jurídica (art. 12, I, já conferido).
   - **Proposta:** no coletivo, quem cadastra no SisGen e responde pelo consentimento é o projeto, não cada contribuinte.
   - **Limite:** quem contribui nunca consente em nome de uma comunidade. O consentimento é só da comunidade (art. 9º, §1º).
5. **Imagem e voz (Código Civil, art. 20):** o indivíduo guarda para si; o coletivo publica. Por isso precisa da autorização de quem aparece, ou fica só o link.
6. **Ética em pesquisa (Res. CNS 510/2016):** se quem colabora é pesquisador de uma instituição, valem as regras dessa instituição. O projeto não pode virar caminho para coleta feita sem ética.
7. **Quem responde, juridicamente, pelo projeto:**
   - **Hoje:** é uma pessoa natural, Vicente, que responde pessoalmente.
   - **Formas a estudar** (decisão de Vicente):
     - seguir como pessoa natural;
     - associação sem fins lucrativos (Código Civil, arts. 53 e seguintes);
     - coletivo reconhecido como Ponto de Cultura mesmo sem CNPJ (Lei Cultura Viva, 13.018/2014);
     - parceria com uma universidade.
   - **O que muda:** a forma escolhida altera responsabilidades e abre portas (Meta Content Library, comitê de ética, editais).
8. **Termos das plataformas:**
   - conta pessoal ou de organização no GitHub;
   - quem é o dono do repositório num coletivo.
9. **O Jurídico no coletivo:**
   - cada contribuição passa por ele antes de entrar na quarentena;
   - a licença dada por quem contribuiu fica registrada;
   - as Faltas são registradas por contribuição.

**Lote B (15/10): conferência e resposta à pergunta de Vicente.** O planalto.gov.br caiu em todas as tentativas, e o espelho da Câmara trouxe só os metadados. Por isso a Lei 9.610 (arts. 7º, 29, 46, II, 49 e 50), a LGPD e o Código Civil seguem **a conferir**.

**Resposta: não, o uso coletivo não tem o mesmo tratamento jurídico do individual.** As exceções pensadas para o uso privado deixam de cobrir o caso, e surgem responsáveis. A mudança vem **em degraus [PROPOSTA]:**

| Momento | O que ainda vale | O que começa |
|---|---|---|
| 1. Só Vicente pesquisa para si | cópia de pequenos trechos para uso próprio (art. 46, II, a conferir); a LGPD não vale para fins exclusivamente particulares e não econômicos (art. 4º, I, a conferir) | trilha e Faltas, como sempre |
| 2. Outras pessoas enviam contribuições | — | **licença de quem contribui** (texto curto em linguagem simples, de entrada e de saída); o projeto vira **controlador** dos dados de quem envia: base legal, aviso de privacidade e canal com o titular; **triagem jurídica leve** antes da quarentena; **dado sensível** (saúde, religião, origem étnica, comunidade tradicional) vira Falta até haver base legal (art. 11, a conferir) |
| 3. O projeto publica para o público | citação curta com autor e origem (art. 46, III, conferido) | **autorização para o resto** (art. 29, a conferir); **canal de notificação e retirada**; imagem e voz só com autorização de quem aparece e de quem gravou; Lei 13.123 se houver "acesso" |

- **Resolução CD/ANPD 2/2022 (oficial):**
  - **quem pode usar:** uma **pessoa natural** pode ser "agente de tratamento de pequeno porte". Quem faz tratamento de **alto risco** fica de fora (art. 3º; o que é "alto risco" está no art. 4º, a conferir), e dado sensível em larga escala pode tirar o projeto da simplificação;
  - **o que simplifica:** registro das operações (art. 9º), **dispensa do encarregado**, desde que haja canal de contato (art. 11), prazo em dobro para atender o titular (art. 14) e declaração simplificada (art. 15).
- **Marco Civil, art. 19 + STF, 26/06/2025** (Temas 987 e 533; secundária, a tese literal está por ler):
  - o artigo foi declarado parcialmente inconstitucional;
  - para ilícitos em geral, o provedor pode responder se, **avisado por notificação extrajudicial**, não agir;
  - em crimes contra a honra, segue valendo a ordem judicial;
  - os embargos ainda estão pendentes.
  - **Consequência:** o projeto que publica contribuições é, **provavelmente**, provedor de aplicação. A ideia de que vira "editor" não tem base conferida e saiu do texto.
- **GitHub (oficial):**
  - a organização é um espaço compartilhado, e o dono administrativo responde pelas ações nela, sempre por meio de uma conta pessoal;
  - num coletivo, o repositório fica melhor numa organização do que na conta pessoal de um membro.
  - **Pergunta:** a **Indalt** é uma empresa ou uma conta pessoal de Vicente?
- **Lei Cultura Viva (13.018/2014; secundária):**
  - coletivos sem CNPJ podem ser reconhecidos como Ponto de Cultura, por seleção pública;
  - **recursos só vão para entidades constituídas**;
  - **reconhecimento não é personalidade jurídica**;
  - alterações de 2022 e 2023 ficam a conferir.
- **Quem responde, com o ônus de cada forma** (decisão de Vicente):
  - **(a) Vicente, pessoa natural:** responde pessoalmente. **É a situação de início (16/10):** a Indalt é conta pessoal, e não há empresa;
  - **(b) associação sem fins lucrativos:** pessoa jurídica própria, com estatuto, CNPJ e contabilidade;
  - **(c) Ponto de Cultura:** reconhecimento cultural, sem criar pessoa jurídica;
  - **(d) parceria com universidade:** traz as regras dela.
- **Ajustes [PROPOSTA]:**
  - "guardar cópia não é republicar" vira "**guardar cópia para conferir fica em limites estreitos, caso a caso**";
  - **imagem e voz:** o link só serve quando a fonte original é legitimamente pública;
  - **Lei 13.123:** a responsabilidade do projeto vale "**se o trabalho configurar acesso**". Na dúvida, Falta;
  - **o Jurídico faz uma triagem leve**, com perguntas fixas: há licença registrada? aparece pessoa identificável? há dado pessoal? há possível conhecimento tradicional? Cada dúvida vira Falta.
- **Recomendação do revisor** (decisão de Vicente, que preferiu um agente especialista): **uma consulta pontual de 1 a 2 h** com um advogado de propriedade intelectual ou de proteção de dados, **antes do primeiro contribuinte externo**. Ela valida o texto de licença, o aviso de privacidade e a forma de quem responde, e o roteiro é o quadro de degraus.

### 17. Lugar e organização do wiki por região (§5.7, §6)

**Resposta: ainda não está organizado.** [PROPOSTA]
- **Entidade Lugar**, com níveis:
  - bioma;
  - grande região;
  - UF;
  - região imediata e intermediária do IBGE;
  - município (geocódigo do IBGE);
  - distrito;
  - localidade, com o nome literal da fonte;
  - território tradicional, com o nome que a comunidade usa;
  - **região cultural**, com o nome dado pelas fontes ou pelas pessoas (de baixo para cima, princ. 7).
- **Três lugares por evidência:** o da prática (vem do trecho), o da publicação e o de quem pesquisa. Só o da prática organiza o wiki; sem ele, Falta (FH-5, PA-4).
- **Topônimo histórico:** guardado como está na fonte e ligado ao município atual só quando não há ambiguidade, com período de validade. Se for ambíguo, Falta.
- **Bioma:** vem da tabela do IBGE de 2024 com o bioma predominante de cada município, marcado como "derivado". 963 municípios estão em mais de um bioma, e o IBGE declara fim só estatístico. É oficial, mas teve uma só conferência: a reconferência falhou, e há revisão de limites de 2025.
- **O lugar não é uma 5ª dimensão.** Ele é a situação da CLB (bebida × lugar × grupo × período) e a âncora de W (o saber comum "da região"). A Transformação de W por interação liga lugares, como na migração.
- **Precisão publicada por registro** (exata, localidade, município, UF, bioma), escolhida pela restrição. O padrão é generalizado para territórios tradicionais, lugares sagrados e onde houver planta.
- **No wiki:**
  - páginas geradas só para UF, município, território e região cultural que tenham pelo menos um registro, cada uma com as CLB, os termos, o "não observado" e as Faltas. O bioma é filtro, não página (lote A);
  - mapa estático no navegador, com o componente a conferir no Passo 6.

**Lote A (15/10): conferências e ajustes do revisor**
- **Confirmado:** o Quartz **não tem mapa nativo** (oficial). Tem grafo de notas, tabelas (Bases), Canvas e Mermaid.
- **Secundários**, porque o IBGE recusou o leitor automático:
  - biomas 2019 em escala 1:250.000, com seis biomas continentais e o Sistema Costeiro-Marinho;
  - revisão de limites nas Notas metodológicas 01/2025;
  - regiões imediatas e intermediárias de 2017;
  - "Evolução da Divisão Territorial do Brasil 1872–2010", com os nomes da época e os limites tirados da malha de 1991;
  - Linked Places, o formato de lugares históricos do World Historical Gazetteer.
- **Ajustes [PROPOSTA]:**
  - **No começo:** UF, município (geocódigo), localidade literal e bioma derivado.
  - **Território tradicional e região cultural** só nascem quando uma fonte ou uma comunidade os nomeia.
  - **Bioma** é filtro e contagem, não página. Página gerada, só para lugar com pelo menos um registro.
  - **Passo 6:** começa com tabelas por UF e município. O mapa vem depois (Leaflet, uma biblioteca de mapas gratuita, ou SVG estático), no nível de município.
  - **Linked Places** é só inspiração para os campos, e a exportação seria em planilha (LP-TSV).
  - **Todo atributo derivado** guarda a fonte, a edição e a data. Cada vínculo de lugar guarda **o ano da divisão territorial usada**, porque a divisão de 2017 não vale para 1930.
  - **Códigos do IBGE:** uma cópia local, baixada uma vez.
  - **Malhas da FUNAI e do INCRA** só entram depois de a licença ser confirmada por escrito.

### 18. Exaustão: "15 CLB" nunca esgota uma fonte

**Resposta: correto.** O 15 é lote e cota, nunca teto de coleta.

**Proposta [PROPOSTA]:**
- **Unidade:** o **Recorte** = ambiente × consulta × período × lugar de publicação × modo (termo, descritores ou **folheio**, isto é, leitura página a página) (FH-2).
- **Dois estados diferentes:**
  - **"Percorrido pela busca":** todas as ocorrências que a fonte informa foram abertas e triadas, em todas as formas de busca, sem resposta saturada, e a bola de neve está fechada;
  - **"Lido por inteiro":** só com folheio.
- **Total desconhecido:** a fonte que não informa o total nunca é dada como exaurida e fica com a Falta "total desconhecido" (PA-2).
- **A cobertura mede o que a busca vê, não o que existe.** A busca da Hemeroteca não acha todas as ocorrências, por causa do OCR (Brasil e Nascimento, 2020; secundária).
- **Reabrem um recorte:** variante nova, título novo, OCR refeito, novidade no canal da fonte, esquema ou validador novo, Falta resolvida.
- **Monitoramento nunca se exaure.** O Ambiente tem dois eixos de estado: escavação e monitoramento (MO-5).
- **Estimativas de quanto falta** (saturação; captura-recaptura entre ambientes independentes) servem só como informação, nunca como critério de parada. Referências a conferir.

### 19. Continuidade do trabalho e guarda de orçamento

**Continuidade [PROPOSTA]:**
- **Arquivo de estado por consulta e por recorte:** cursor, total informado, total visto, saturação, erros, próxima ação e reserva (ID opaco e prazo) (PA-2, MO-5, FH-2). Fontes longas são divididas em fatias de escuta.
- **Ritual:**
  - começar com `git pull` e o relatório calculado das frentes;
  - trabalhar em lotes de 15, gravando um ponto de retomada (commit) depois de cada lote;
  - terminar atualizando o estado e com `git push`.
- **Prioridade:** risco (princ. 4) → CLB do caso-piloto → vácuos por região e período → escolha de Vicente.

**Guarda de orçamento [VIGENTE pela fala de Vicente; a mecânica é PROPOSTA].** "Se deve medir para parar antes de acabarem." Toda sessão ou rotina com IA:
1. mede o custo de cada lote no caso-piloto;
2. antes de cada lote, compara o custo esperado com o que resta e para, com o estado salvo, antes de chegar ao limite;
3. nunca lança agentes em paralelo sem teto de chamadas e de tokens, e usa o modelo mais barato que faça bem a tarefa;
4. registra na trilha o consumo medido.

Foi a falta disso que fez se perderem 544 mil tokens em 15/10.

**Lote B (15/10): exaustão, continuidade e rotinas na nuvem**
- **Rotinas do Claude Code na nuvem** (oficial, documentação da Anthropic):
  - são uma configuração salva (instruções, repositórios GitHub, conectores) que roda na nuvem da Anthropic por agenda (no mínimo de hora em hora), por chamada de API ou por evento do GitHub;
  - **gastam a mesma cota da assinatura**;
  - gravam numa ramificação "claude/" do repositório;
  - **a rede é restrita, por padrão, a uma lista de domínios permitidos**, então as fontes brasileiras precisam entrar nessa lista;
  - o custo por execução não aparece na documentação, e o uso se lê em claude.ai/settings/usage.
- **Ajustes [PROPOSTA]:**
  - **Rotina na nuvem só para o que não pede pessoa:** buscas por API já aprovadas e tratamento de lotes de 15. Ela **abre uma proposta na ramificação "claude/" para Vicente revisar** e nunca grava direto na versão principal.
  - **Buscas assistidas ficam com pessoas.**
  - **Antes de confiar,** um teste com uma única rotina pequena num repositório de teste, anotando a rede permitida, o consumo, a ramificação e a conta que assina.
- **Guarda de orçamento medida de verdade:**
  - Vicente define um teto (lotes por semana ou parte da cota);
  - o uso em claude.ai/settings/usage é anotado antes e depois de cada rodada;
  - ao atingir o teto, tudo para com o estado salvo.
- **Revisão curta por lote:** um resumo de uma tela (o que entrou, o que ficou em quarentena, Faltas novas), que Vicente aprova ou devolve em poucos minutos.
- **Gatilhos de reabertura só marcam "a reabrir".** Nada roda sozinho: a reabertura entra na fila por prioridade.
- **Recortes nascem sob demanda,** nunca a grade inteira de combinações.
- **Captura-recaptura:** Spoor et al., BMJ 1996 (secundária). Exige fontes independentes, o que raramente acontece entre bases de bibliotecas, e dá intervalos largos. Fica só como informação.
- **Save Page Now:** a chave e os limites não foram conferidos. Pedir captura em ritmo baixo, com a chave da conta.

### 20. Tiers com ferramentas de ação, além de informar (§5.9, Passo 9)

**Resposta:** está considerado em parte (o planejador de aulas, D-006, Passo 9). O resto entra agora. [PROPOSTA]
- **Cada tier tem duas coisas:** o que vê primeiro e as **ferramentas de ação sob demanda** (princ. 15). Ferramenta não é controle de acesso: é pública, salvo o que já é restrito.
- **Grupos candidatos e suas ferramentas** (a pergunta 5 do §10 continua aberta):
  - **educadores, inclusive de escolas indígenas e quilombolas:**
    - planejador de aulas por CLB ou por conjunto;
    - kits de fonte primária (FH-8);
    - materiais que já existem no eduCAPES e na Embrapa (PA-8);
    - alinhamento à BNCC, à LDB art. 26-A e às diretrizes da educação escolar indígena e quilombola (a conferir);
  - **comunidades e detentores:**
    - pedido de restrição, correção ou retirada;
    - devolutiva do que o projeto tem sobre elas;
    - inventário participativo (manual do IPHAN de 2016, a conferir);
    - modelo de pedido de registro com as exigências (a anuência da comunidade vem da Res. IPHAN 1/2006; secundária);
  - **pesquisadores:** dados abertos, citação e entrada no mutirão de escavação;
  - **gestores e legisladores:** kit com as leis existentes (fontes oficiais a conferir no Passo 4) e a moldura legal do Anexo C;
  - **praticantes e produtores:** cartilha de biossegurança quando o risco estiver verificado (princ. 12), com revisão profissional (Passo 9);
  - **comunicadores:** kit de pauta com fontes conferidas e "como citar".
- **Três jeitos de construir, sem backend:**
  1. **Gerador no navegador** a partir dos dados publicados das fichas verificadas e de modelos: sem IA, sem servidor e totalmente rastreável. É a base recomendada.
  2. **IA sob demanda por fila:** pedido → rotina do Claude, dentro da guarda de orçamento → validador → entrega.
  3. **"Traga sua IA":** pacote de dados e instruções para a IA que a pessoa já usa, com o aviso de que o resultado não foi conferido pelo projeto.
- **Regras:**
  - só conteúdo verificado, e as Faltas ficam visíveis;
  - o que é jurídico ou sanitário passa por profissional antes de circular;
  - toda saída é carimbada com as fichas, as evidências, a versão, a data e o "como citar";
  - nada é guardado automaticamente;
  - um plano de aula testado pode voltar como contribuição, com crédito: é o ciclo coletivo.

**Lote A (15/10): conferências e ajustes do revisor**
- **BNCC (oficial):**
  - o código de habilidade do Ensino Fundamental é etapa + ano ou bloco de anos + componente + posição. Ex.: EF05HI04 = Ensino Fundamental, 5º ano, História, 4ª habilidade;
  - a Educação Infantil e o Ensino Médio seguem outra regra;
  - não há API oficial do MEC; o bncc.dev é um projeto independente.
- **Res. CNE/CEB 5/2012 (Educação Escolar Indígena; secundária):** prevê unir conhecimentos científicos e tradicionais e envolver "os sábios, especialistas nos conhecimentos tradicionais".
- **Ainda não conferidos:** LDB art. 26-A, Res. 8/2012 e o manual do IPHAN.
- **Ajustes [PROPOSTA]:**
  - **Começar com 1 grupo e 1 ferramenta:** educadores, com um kit de fonte primária numa página estática. Ampliar só depois de uso real.
  - **Jeito 1** é a base. **Jeito 2** fica adiado até haver demanda real. **Jeito 3** leva o aviso dentro do próprio pacote: "saída gerada fora do CLB, não conferida".
  - **BNCC:** uma tabela estática com os códigos, tirada do PDF do MEC com a página citada. Aparecem como "habilidades sugeridas", interpretação do CLB, nunca alinhamento oficial.
  - **Inventário participativo:** só o link e um resumo. Se uma comunidade quiser, ela conduz, e o CLB documenta o que ela entregar, com crédito.
  - **Modelo de pedido de registro:** **descartado**. Vira uma página "o que a lei pede", com as citações literais da CF art. 216 e do Decreto 3.551 e o aviso "não é orientação jurídica".
  - **Cartilha de biossegurança:** só com risco verificado e um profissional revisor identificado. Até lá, a ficha mostra a Falta "risco sanitário não verificado" e o link do órgão oficial.
  - **Escolas indígenas e quilombolas:** antes de qualquer material, registrar como Falta se a comunidade foi ouvida.
  - **Carimbo mínimo comum:** fichas com versão, nível, Faltas, data, "como citar" e o aviso "não é orientação jurídica nem sanitária".
  - **Medição de uso:** só contagem agregada, sem identificar pessoas.

---

### 21. Grafo 4D real, com interações reais (§2 princ. 3, §5.7, Passo 7)

**Onde está hoje:** o §2 e o §5.7 da v0.1 o preveem, e o Passo 7 o gera por script. A primeira entrega são páginas e tabelas, e a "interface mais rica só se Vicente sentir falta". Vicente o mencionou para conferir se o tema tinha sido tratado, porque ele pode **ajudar muito na visualização, nas interconexões e na pesquisa**. **Fica fora da revisão de essencialidade.**

**O que esta rodada acrescenta [PROPOSTA]:**
- **Os dados nascem em 4D desde a fase 1.** Cada elemento de prática tem X, Y, Z e W (item 2), e as relações têm tipo: sustenta, tensão, transformação de W, correção. Assim a visualização é uma leitura dos dados, nunca um desenho feito à mão (P61 e P66).
- **Uma primeira vista navegável na fase 1,** gerada por script a partir dos dados do caso-piloto:
  - **nós:** os elementos de prática;
  - **arestas:** as relações, com tensões e Faltas à vista, e Faltas como nós vazios;
  - **filtros** por Z e por W; a cor mostra o estado.
  - Cada nó e cada aresta leva à ficha e à evidência. É o circuito wiki ↔ grafo (P11).
- **O gerador de site previsto (Quartz) mostra só ligações entre notas** (conferido na página oficial), e não as quatro dimensões. A vista 4D precisa de um componente próprio, que o Passo 6 ou 7 avalia.
- **O que o grafo dará à pesquisa:** achar tensões, lacunas por região e período, e relações entre bebidas e técnicas que nenhuma ficha mostra sozinha.

**Pergunta para compreender:** que pergunta de pesquisa você gostaria de responder olhando esse grafo? A resposta decide se a vista entra já na fase 1 ou fica para o Passo 7.

### 22. Agentes com harness qualificado, modelos por tarefa e logs (Passo 1)

**O que é "harness"** (em português simples): tudo o que ajuda um agente a acertar, mesmo num modelo barato: instruções claras, formato de entrada e de saída, validadores por script, exemplos reais de entrada e saída esperada, listas de conferência, limite de passos e de custo, critério de parada e registro do que fez.

**Os agentes que ajudaram a planejar** (Plan, general-purpose etc.) **fazem parte da ferramenta, não do projeto.** Os agentes do projeto serão criados no Passo 1, com harness qualificado. **[VIGENTE pela fala de Vicente de 16/10; o desenho é PROPOSTA]**

**Diretrizes de harness [PROPOSTA]:**
- **Cada habilidade traz:** contrato de entrada e saída, validador por script, pares de exemplo reais do caso-piloto, lista de conferência, teto de custo e de passos, critério de parada e a declaração do que ela não faz.
- **Teste no modelo-alvo:** a habilidade roda nos modelos candidatos sobre os pares de exemplo, e fica o mais barato que passar. Só é "aprovada" quando o resultado passa nos validadores. Se falhar, reforça-se o harness primeiro; sobe de modelo só se não bastar.
- **Logs:** cada agente grava um registro por execução, sem dados pessoais e no Git, em `trilhas/`: quem, modelo, habilidade, versão do harness, entrada, buscas feitas, o que foi aceito, descartado ou posto em quarentena (e por quê), tokens gastos, tempo e erros. Um resumo curto por lote é o que Vicente lê.
- **Verificador independente:** um agente verificador, com harness e modelo diferentes do produtor, mais os scripts e a amostra sorteada de Vicente.

**Modelos (essência confirmada em 16/10) [VIGENTE]:**
- **Planejamento** (a conversa de 15 e 16/10): Opus 5.5, esforço máximo, ultracode e thinking.
- **Execução** (o brief, numa janela nova): Opus 5.5 com **esforço médio**, com harness e sem ultracode. Os subagentes de conferência e de verificação rodam em Sonnet 5.5 alto, sugestão apoiada nas medições de 15 e 16/10.
- **Depois disso,** os modelos por tarefa são os que os **testes** indicarem. Cada habilidade roda nos modelos candidatos sobre os exemplos reais do caso-piloto, e fica o mais barato que passar nos validadores. Hipóteses de partida, a testar e não decididas: ajustes em Sonnet 5.5 (esforço alto) e rotinas automáticas em Haiku 5.5.
- **Regra de aviso:** antes de executar, o agente diz qual é o modelo indicado. Se a sessão estiver em outro, avisa e para para a troca.
- **Orçamento:** mantido. Medir e parar antes de acabar, com o estado salvo. A execução do planejamento deve levar duas janelas (estimativa a medir). O teto provisório de 300 mil tokens por semana em agentes vale para a operação da fase 1.
- **A verificar no Passo 1:** como definir o modelo de cada rotina na nuvem e de cada subagente.

---

## Descartado ou reformulado (trilha)

- **Fatia vertical antes do Passo 1:** reabria a P36. Virou o caso-piloto dentro do Passo 1.
- **"Menos agentes":** era simplificação (P79). Virou "cada habilidade declara quem a executa"; ganhou-se um papel, o Jurídico.
- **Fluxograma como ilustração:** violaria a D-014.
- **"Glossário = termos, fichas = CLB":** decidia a pergunta 6 no lugar de Vicente. O modelo fica M:N.
- **W como matriz da fonte e como "âncora" num campo:** substituído pela definição de Vicente. W é uma dimensão, com registro próprio e Falta quando não captada.
- **Regra de evidência contrária que pesava contra a proposição:** substituída por "não julgamos; fonte contrária documenta".
- **"Sustentação (juízo)" como eixo de status:** virou "fidelidade da leitura", que confere a nossa leitura e não a prática.
- **Consulta jurídica externa antes dos Passos 4 e 6:** substituída pelo agente Jurídico de precaução.
- **Critérios de prática cultural criados no caso-piloto:** substituídos pelos critérios da legislação (CF, art. 216; Convenção de 2003; Decreto 3.551).
- **Apps Script como camada fixa:** sai. O Google só fica se for necessário para os canais de pessoas (Passo 4).
- **Hospedagem do site:** adiada para o Passo 6.
- **RSS de busca do Google Notícias e feeds do Google Alertas:** saem, porque o robots.txt e os termos do Google vedam a leitura automática. Os Alertas chegam por e-mail.
- **Hospedar RSS-Bridge, RSSHub ou changedetection.io, ou usar instâncias públicas:** sai. No lugar, geradores próprios em Python.
- **Coleta automática em Instagram, Facebook e TikTok:** sai. Esses conteúdos entram só por link enviado por pessoa.
- **Contornar a proteção da Hemeroteca (recurso do pyHDB):** sai.
- **Filtros de país e de idioma nas buscas acadêmicas:** viram anotação, não recorte.
- **Modelo de pedido de registro no IPHAN:** descartado, porque seria quase assessoria jurídica. Vira a página "o que a lei pede".
- **Hash do ID de vídeo do YouTube:** retirado, porque não protege nada num ID público. Guarda-se o ID público e nunca o canal nem o @.
- **Páginas por bioma:** saem. O bioma vira filtro.
- **Quatro níveis de colaborador desde o início:** viram dois níveis.
- **Mapa no Passo 6:** começa por tabelas.
- **IA sob demanda (jeito 2) desde o começo:** adiada até haver demanda real.
- **"O portão faz do projeto um editor":** saiu, porque não tem base conferida.
- **"Guardar cópia não é republicar" como regra geral:** virou "limites estreitos, caso a caso".
- **Editores sem código (Pages CMS, Decap CMS):** não adotados agora.
- **Cinco adaptadores de busca de saída:** viram "só os que as fontes reais pedirem".
- **Conformidade com o PRISMA:** virou "inspirado em".
- **Rotina na nuvem gravando direto na versão principal:** saiu. Ela abre proposta para revisão.
- **Reverificação independente das três frentes concluídas e as sete frentes restantes como pesquisa na web:** adiadas para não estourar o limite de uso. Os fatos marcados "a conferir" são conferidos em lotes na implementação.

## Decisões que ainda ficam com Vicente (vão para o §8 da v0.2)

### As decisões que bloqueiam o próximo passo (estado em 16/10)

**Resolvidas:** 3 (fase 1 sem contribuições externas), 4 (portão combinado + validador + logs dos agentes; não há segunda pessoa), 5 (responsável: Vicente, pessoa natural) e 6 (orçamento mantido: o teto provisório de 300 mil tokens por semana em agentes, a confirmar o ajuste do item 22). **Em aberto e bloqueando:** só a 1 (caso-piloto). A 2 não impede o início.

1. **Caso-piloto:** qual CLB e quais as 2 ou 3 primeiras fontes reais.
2. **Enquadramento e Lei 13.123:**
   - o projeto se apresenta como pesquisa ou como documentação cultural independente? Isso decide se a Res. CNS 510 o alcança;
   - que caminho seguir para desfazer as Faltas da Lei 13.123: cadastro no SisGen, consentimento, consulta ao CGen, ou nenhum por ora? Sem caminho, o modo de fazer das CLB com planta nativa fica retido.
3. **Escopo da fase 1: resolvida em 16/10.** A fase 1 não recebe contribuições externas (ponto 3 aprovado). A consulta jurídica pontual fica para antes da fase 2.
   - **Nota sobre a decisão 2:** ela **não bloqueia o início da fase 1**. A fase 1 não faz entrevistas, então a Res. CNS 510 não entra, e trabalha em repositório privado. A Lei 13.123 só pede cadastro antes da "divulgação". A decisão 2 bloqueia o que for **publicado** (o kit e o wiki) e pesa na escolha do caso-piloto.
4. **Portão no GitHub e segunda pessoa:**
   - combinado (grátis), plano Pro ou Team, ou acervo liberado em repositório público?
   - **Decidido em 16/10:** não há segunda pessoa. Só Vicente e os agentes trabalham, e os agentes gravam logs.
   - **Consequência:** a segunda leitura vem do validador, de agentes verificadores com harness e modelo diferentes dos do produtor, e da amostra sorteada de Vicente. Evita a falha nº 7 do legado ("auditor igual ao produtor").
   - Portão: combinado + validador; rever na fase 2.
5. **Responsável:**
   - a conta Indalt é pessoal de Vicente, e ainda não há empresa por trás. O responsável é Vicente, pessoa natural;
   - se o projeto ganhar uma empresa ou organização, rever mais adiante.
6. **Orçamento:** qual o teto de consumo por semana? A rotina na nuvem fica para a fase 2, depois de um teste.

As decisões abaixo ficam para o passo em que entram, e nenhuma se perde. Na v0.2 elas viram perguntas de compreensão (acordo 1), não escolhas binárias.

**Perguntas para compreender (vão para o §10):**
- Quem decide que uma fonte é "revisionismo", e com que critério, sem julgar a prática? É uma regra de Vicente, então precisa de um critério operacional.
- "W só se ancora na fala de quem pratica" (FH-5) ainda é proposta. Uma etnografia que descreve a prática como comum basta?

- Qual CLB vai para o caso-piloto.
- Se e quando seguir uma das formas de desfazer a Falta da Lei 13.123 (cadastro no SisGen, consentimento, consulta ao CGen). Enquanto isso, vale a precaução.

**Da Parte 2:**
- **Acesso e coleta:**
  - confirmar a regra de nunca contornar proteção anti-robô;
  - pedir acesso a dados às instituições (ex.: BN)?
  - aceitar a leitura dos termos do GitHub Actions ou mover a coleta para a rotina do Claude?
  - criar a chave do OpenAlex e o e-mail do projeto (onde?);
  - buscar vínculo acadêmico para vias como a Meta Content Library?
- **Pessoas e oralidade:**
  - reabrir a P48 para entrevistas feitas pelo projeto?
  - ouvir depoimentos que já estão em acervos cabe agora?
  - o nome do depoente publicado por um acervo é autoria ou dado pessoal?
  - uma URL com @perfil conta como dado pessoal?
  - uma etnografia que descreve a prática como comum basta para ancorar W?
  - uma transcrição por IA ainda não conferida aparece no wiki com selo próprio?
- **Coletivo:**
  - sob que forma jurídica o projeto funciona: pessoa natural, associação, Ponto de Cultura ou parceria com universidade? (item 16-J);
  - abrir o mutirão de escavação, e para quais grupos?
  - licença das contribuições e do acervo;
  - quem é a segunda pessoa de referência.
- **Enquadramento e pessoas (lote A):**
  - o projeto se apresenta como pesquisa (com universidade ou publicação científica) ou como documentação cultural independente? Isso decide se a Res. CNS 510 o alcança;
  - já existe uma comunidade ou pessoa concreta que o projeto pretende ouvir?
  - onde fica a tabela que liga os códigos aos nomes, fora do Git?
  - há algum profissional jurídico ou sanitário que possa revisar, mesmo de vez em quando?
  - quem é o primeiro público real: uma escola, uma comunidade, um pesquisador?
- **Coletivo e jurídico (lote B):**
  - **portão único:** no GitHub gratuito privado não há revisão obrigatória. Seguir com portão combinado (grátis), pagar o plano Pro ou Team, ou tornar público só o acervo liberado?
  - a **Indalt** é empresa ou conta pessoal sua? Isso define quem responde;
  - contribuições de outras pessoas já na fase 1, ou só a sua curadoria por enquanto?
  - o acervo aberto pode ter **uso comercial** (editora, bar), ou isso preocupa as comunidades? Isso decide entre CC BY e CC BY-NC-SA;
  - fazer a **consulta jurídica pontual de 1 a 2 h** antes do primeiro contribuinte externo, ou seguir só com o agente Jurídico?
  - a **rotina na nuvem** traz achados para sua revisão (recomendado) ou grava direto? Qual teto de consumo por semana?
  - quais são as **2 ou 3 primeiras fontes reais** do caso-piloto? Elas decidem quais adaptadores nascem primeiro.
- **Lugar (lote A):**
  - uma "região cultural" ("do sertão", "da beira do rio") nasce na primeira menção ou só depois de várias fontes?
  - o mapa é para Vicente explorar ou para o público?
  - para comunidades, a precisão padrão é UF ou município até haver consentimento?
- **Wiki e ferramentas:**
  - o bioma é porta de entrada ou filtro? (o revisor recomenda filtro)
  - a ordem de prioridade dos recortes e quando vale pagar o custo do folheio;
  - a tabela de domínio público da BN vira regra de precaução para imagens em material didático?
- Onde vivem os dados pessoais dos canais de pessoas (Passo 4).
- Quando agendar a rotina do Claude, depois de medir o custo.

---

## Implementação (depois da aprovação): Fundação v0.2 + GitHub

**Como executar:** a partir do **brief de execução** (`C:\Users\alqui\.claude\plans\clb-execucao-v0.2-brief.md`), numa janela nova, em Opus 5.5 com esforço médio e sem ultracode, com subagentes em Sonnet 5.5 alto. A execução não para para aprovar o que já foi decidido (D-028).

**Execução em lotes, com guarda de orçamento.**
- **Por que isto:** em 15/10, 1,4 milhão de tokens de subagentes bastaram para atingir o limite da sessão.
- **Teto:** 600 mil tokens de subagentes por janela de uso, menos da metade do que se viu hoje. Ao chegar perto, eu paro, salvo o estado e aviso.
- **Ordem e pontos de retomada:**
  1. **Git e GitHub:** não usa agentes.
  2. **Conferência dos fatos:** lotes temáticos, um agente por tema, em **Sonnet 5.5 com esforço alto** (sugestão; D-027), com teto de 15 a 20 aberturas de página por agente. O resultado de cada lote é gravado num arquivo de rascunho antes do lote seguinte, então uma interrupção perde no máximo um lote.
  3. **Edição do documento:** poucas substituições grandes, por seção, para gastar menos turnos. O progresso fica num checklist em `trilhas/`.
- **Estimativa, a medir:** cerca de 400 mil tokens no total, entre 3 e 4 lotes de conferência mais a edição.

0. **Salvar a pesquisa dentro do projeto** (para não pesquisar de novo):
   - tirar dos registros dos workflows `wf_89a76895-c9b`, `wf_5e7f9960-6a1` e `wf_c21065e2-8ff` as propostas FH, PA e MO, os catálogos de fontes, os fatos (com URL, nível e citação) e as revisões dos lotes A e B, mais o relatório do crítico;
   - gravar em `trilhas/2026-10-15_pesquisa/`, só texto e sem dado pessoal;
   - conferir a leitura dos arquivos antes de seguir.
1. **Preservar a v0.1:**
   - `git init -b main` e commit da v0.1;
   - conferir `git config user.name/email`; se faltar, configurar só neste repositório, com Vicente como autor.
2. **Criar o repositório privado no GitHub** (publicação aprovada por Vicente):
   - conferir `gh auth status`; se não houver login, pedir a Vicente que rode `gh auth login` num terminal;
   - o repositório nasce na conta Indalt (já decidido); passar para uma organização é decisão futura (decisão 5);
   - criar `cultura-liquida` como **privado** e enviar o commit da v0.1. Nenhum dado pessoal existe na pasta.
3. **Verificar os padrões e os serviços citados** (Web Annotation, SKOS, PROV-O, EDTF, CSL-JSON, TBX, JSON Schema, Flora e Funga do Brasil, CARE, Local Contexts, as bibliotecas Python, as rotinas agendadas do Claude e os limites do GitHub Actions):
   - **sai desta lista o que os lotes A e B já conferiram:** CNS 510 e 304, FUNAI IN 01/1995, códigos da BNCC, Creative Commons, CRediT, mapa do Quartz, Lei 5.765/1971, Decreto 6.583/2008, rotinas do Claude;
   - **ficam os que seguem abertos:** Lei 9.610 arts. 7º, 29, 46 II, 49 e 50; LGPD arts. 4º, 5º, 7º, 11, 18, 37, 41 e 46; Marco Civil art. 19 e a tese literal do STF de 2025; Código Civil arts. 20, 53 e 54; Lei 13.123 art. 2º, I; Lei 13.018 e suas alterações; LDB art. 26-A; Res. CNE/CEB 8/2012; manual do IPHAN; tabela de biomas do IBGE; Res. CD/ANPD 2/2022 art. 4º;
   - **testes reais:** feeds e APIs a partir do GitHub Actions; uma rotina de teste do Claude num repositório de teste; busca do IPHAN; SRU do LexML; plano gratuito × revisão obrigatória no repositório real;
   - entram também, da lista antiga, os "a conferir" da Parte 2 que não foram cobertos acima: Res. CNS 510/2016 e 304/2000, regra da FUNAI para pesquisa em terra indígena, Código Civil art. 20, Lei 9.610 art. 7º, LGPD arts. 11 e 18, estrutura dos códigos da BNCC, LDB art. 26-A (oficial), Res. CNE/CEB 5/2012 e 8/2012, manual do IPHAN de inventários participativos (2016), API de localidades e regiões de 2017 do IBGE, reformas ortográficas desde 1900, PRISMA 2020 e PRISMA-ScR, captura-recaptura em revisões, licenças Creative Commons, Linked Places, mapa no Quartz;
   - abrir a página oficial de cada um, em lotes, como descrito acima;
   - registrar o nível e a URL no novo **Anexo C.3**;
   - o que não for confirmado é escrito como tal.
4. **Editar `00_Fundacao_Cultura_Liquida.md` → v0.2:**
   - **Cabeçalho:** versão, data e "o que mudou".
   - **§0:** legenda das P-refs; acordo 6; regra PROPOSTA ≠ plano; diário em `trilhas/`.
   - **§2:** princípio 3 reescrito com W como dimensão, a Falta, "não julgamos" e a Proposição com as Evidências; ajustes nos princípios 1, 2, 4, 9 e 11.
   - **§5.1, §5.4, §5.5 e §5.7:** itens 7, 9, 10, 11 e 12.
   - **§6, reescrito:** Ambiente, Consulta, Execução, Entrada, Fonte (com perspectiva, `deriva_de` e Correção), Trecho, Evidência, Proposição, Termo, CLB situada (M:N), Elemento de prática (X, Y, Z, W), Compreensão local (W), Transformação, Falta, Insumo, Aresta, campos de proteção, eixos de status e IDs imutáveis.
   - **§7:**
     - Passo 0 feito;
     - Passo 1 com caso-piloto, contrato de Termo e o agente Jurídico no mapa;
     - Passo 2 com GitHub, validador no envio e teste de reconstituição;
     - Passo 3 como ambiente:
       - só entra o que for verificável e condizente com as regras novas, e o site não é aproveitado (D-024);
       - os termos do legado entram como candidatos, que servem de busca até ganharem abonação;
       - o Drive é exportado em .docx e convertido por script, sem as planilhas com dados pessoais;
     - Passo 4 com as duas camadas na nuvem e a decisão sobre os canais de pessoas;
     - critérios ajustados dos Passos 6 e 7.
   - **§8:** as decisões acima.
   - **§9, entradas com a essência confirmada por Vicente e a diretriz resultante (a fala original fica no Anexo de trilha):**
     - D-015: v0.2;
     - D-016: curadoria de 1 a 3 h;
     - D-017: exemplos;
     - D-018: dimensão W;
     - D-019: não julgamos / fonte contrária;
     - D-020: agente jurídico e Falta;
     - D-021: nuvem, GitHub sincronizado, Google só se necessário e publicação aprovada;
     - D-022: critérios de prática cultural vindos da legislação;
     - D-023: guarda de orçamento ("se deve medir para parar antes de acabarem");
     - D-024: legado só se for verificável e condizente com as regras novas; o site não é aproveitado;
     - D-025: regras proporcionais "de início", com revisão de essencialidade depois das coletas e verificações; biblioteca informativa com proposições, não réplica da legislação; barreira jurídica sempre com porquê e caminho assistido;
     - D-026: fase 1 só com Vicente e agentes, com logs; responsável é Vicente, pessoa natural (Indalt é conta pessoal);
     - D-027: o planejamento rodou em Opus 5.5 máximo, ultracode e thinking; a execução roda em Opus 5.5 com esforço médio, com harness e sem ultracode, e os subagentes em Sonnet 5.5 alto; depois, os modelos são escolhidos por teste; harness qualificado (item 22);
     - D-028: a execução não para para aprovar o que já foi revisado e decidido; para só em decisão nova, teto de orçamento ou bloqueio.
   - **Anexo C.1:** entram os textos conferidos em 15/10, com nível "oficial" e URL: CF arts. 215 e 216; Decreto 5.753/2006, arts. 2 e 13; Decreto 3.551/2000; Decreto 6.040/2007; Lei 13.123, arts. 2º, 8º, 9º, 10 e 12; Decreto 8.772, arts. 12 e 13; Resolução CGen 47/2025; Lei 9.610, arts. 8º, 41, 45 e 46.
     - A anuência da comunidade para o registro no IPHAN fica confirmada (Resolução IPHAN 1/2006, art. 4º, VII), mas em fonte secundária.
     - Ficam a conferir: o art. 2º, I, da Lei 13.123 (definição de patrimônio genético) e o caráter declaratório do cadastro no SisGen.
   - **§10:** pergunta 9 respondida; pergunta 7 respondida em parte; pergunta 6 reformulada; pergunta 13 relida à luz da Falta.
   - **§11:** cota de juízo.
   - **Anexo D (novo):** esta análise como trilha, com os descartados e as propostas completas FH, PA e MO.
   - **Anexo E (novo) — Ambientes candidatos:** o catálogo das cerca de 60 fontes conferidas em 15/10 (via de acesso, sintaxe, termos, uso, nível), tirado do registro do workflow `wf_89a76895-c9b`.
   - **Parte 2 no corpo do documento:**
     - §5.2 a §5.5: itens 13, 14 e 19;
     - §5.4 e §6: itens 15 e 16, com os tipos de evidência, os papéis de pessoas, o Recorte, o Lugar, os arquivos de estado e as reservas;
     - §5.7 e §5.9: itens 17 e 20;
     - §7: Passos 1, 2, 4, 5, 6, 9 e 10;
     - §10: perguntas novas para compreender;
     - §11: guarda de orçamento;
     - Anexo C.2: correções (Google, OpenAlex, termos do GitHub Actions).
   - **Fundir as camadas:** em cada item, corpo, ajustes dos lotes A e B e descartados viram um texto final único. O plano guarda as camadas; a v0.2 não.
   - **Textos que precisam ser escritos na v0.2:**
     - ajustes dos princípios 1, 2, 4, 9 e 11;
     - tabela de eixos de status × selos (item 4);
     - regras fixas do Jurídico (item 7);
     - perguntas novas do §10;
     - precondições dos Passos 4 e 6;
     - custódia do texto da fonte, dos dados pessoais e do áudio (itens 5 e 15);
     - fase 1 e fase 2.
   - **Marcadores:** as falas de Vicente entram como [VIGENTE]; o desenho de campos e as camadas, como [PROPOSTA].
5. **Commit da v0.2 e push para o GitHub.**
6. **Memória do Claude:** registrar três acordos com Vicente:
   - exemplos nunca limitam o trabalho;
   - todo termo novo é explicado na primeira vez em que aparece;
   - medir o custo em tokens contra o trabalho restante e parar antes de acabar: lotes com ponto de retomada, teto por agente, nada de rodadas grandes em paralelo sem estimativa.

## Verificação

- `git log` local e no GitHub mostram os commits da v0.1 e da v0.2, e os dois estão idênticos (`git status` limpo, `git log origin/main` igual).
- O repositório aparece como **Private** em `gh repo view`.
- A busca por "Versão 0.2", "D-015" a "D-028", "Anexo E", "Anexo D", "C.3", "Falta" e pela legenda das P-refs acha cada um.
- O §6 contém cada entidade dos itens 1 a 7.
- Cada item do C.3 tem URL e nível de verificação.
- A análise longa fica no Anexo D, fora da leitura padrão.
