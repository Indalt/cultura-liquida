# Brief de execução: Fundação v0.2 da Cultura Líquida

**Para quem:** a sessão do Claude Code que vai executar o planejamento, numa janela nova, aberta em `C:\Antigravity\Cultura Líquida`, sem memória da conversa de 15 e 16/10/2026. E para Vicente, que acompanha.
**Fechado em:** 16/10/2026. Foi revisado por dois revisores independentes, cujas correções já estão aplicadas.

**Precedência:** se o brief e o plano divergirem, **vale o brief**. Depois dele, vale o estado das decisões no plano ("As decisões que bloqueiam o próximo passo (estado em 16/10)"); por último, o resto do plano. As divergências conhecidas estão na seção 6.

---

## 0. Autorização, modelo e regras

**Autorização (D-028):** a primeira mensagem de Vicente na janela nova autoriza explicitamente os blocos indicados nela. Essa autorização vale para todos os passos desses blocos.
- **As memórias "plano não é execução" e "registrar a essência" não pedem nova autorização** para o que este brief já cobre.
- **As essências da tabela da seção 2 já foram confirmadas por Vicente,** e não se reconfirmam. Pedir confirmação de essência vale só para **comentários novos**.
- **Janelas (atualizado em 16/10, D-029):**
  - **janela 1** = Blocos 1 e 2 (**feita**);
  - **janela 2** = **Bloco 2.5** (agentes, habilidades e harness);
  - **janela 3** = Blocos 3 e 4 (a v0.2, conduzida pelos agentes).
  - Se a regra de orçamento mandar parar, a janela 3 continua numa quarta, pela retomada.

**Modelos desta execução (D-027):**
- **Sessão principal:** Opus 5.5, **esforço médio**, **sem ultracode**. O ultracode, o esforço máximo e o thinking foram a configuração do **planejamento**, não da execução.
  - O `~/.claude/settings.json` já fixa `effortLevel: "medium"` para `claude-opus-5-5`.
  - A sessão confere o ID do modelo. Se não for `claude-opus-5-5`, avisa e para.
- **Subagentes** (conferências do Bloco 2 e verificadores do Bloco 3): **Sonnet 5.5, esforço alto**, chamados pela ferramenta Agent, **um por vez**, com `model: "sonnet"` e `effort: "high"` explícitos.
  - Depois do Bloco 2.5, os subagentes são **os agentes do projeto** (`.claude/agents/`). Cada um declara o seu modelo; os valores iniciais estão no Bloco 2.5.
  - **Por que este modelo:** é a sugestão do planejamento, apoiada nas medições de 15 e 16/10. Agentes Sonnet com teto fizeram conferência na web com qualidade, gastando de 34 a 54 mil tokens cada.
  - **Registro:** anote no checklist o modelo e o esforço de cada agente.
- **Sem Workflow nesta execução:** sem ultracode, a sessão não orquestra rodadas de vários agentes.
- **Depois desta execução,** os modelos por tarefa são escolhidos por teste no Passo 1. As hipóteses de partida são Sonnet 5.5 (alto) para ajustes e Haiku 5.5 para rotinas.

**Regras de execução:**
1. **Não pare para aprovar o que já foi decidido.** Pare só em quatro casos:
   - (a) uma decisão nova, que o brief e o plano não cobrem;
   - (b) a regra de orçamento (item 2);
   - (c) um bloqueio que só Vicente resolve (login, permissão);
   - (d) um conflito que mude o sentido de uma decisão vigente.

   Um fato que não se consegue conferir **não é motivo de parada**: marque "não conferido" e siga.
2. **Orçamento (D-023). Meça e pare antes de acabar.**
   - **"Janela" é a janela de uso da conta** (o limite que zera de tempos em tempos), não o contexto da conversa.
   - **Medida inicial:** na primeira mensagem, Vicente informa o percentual de uso de claude.ai/settings/usage, e a sessão registra o número no checklist.
   - **Contagem:** por janela, some o consumo informado por cada Agent. **Teto: 600 mil tokens de subagentes.**
   - **Antes de cada agente,** a conta tem que fechar: consumido + estimativa ≤ 600 mil. Não abra um lote se a folga for menor que **2× o maior lote já medido**.
   - **Estimativas medidas em 15 e 16/10:**
     - agente Opus que lê arquivos, sem teto: 118 e 142 mil tokens;
     - agente Sonnet com teto de chamadas: de 34 a 54 mil;
     - agente Opus de pesquisa web, sem teto: de 200 a 450 mil;
     - o custo por chamada é parecido entre os modelos, de 2 a 3 mil tokens.
     - **Para planejar, conte cerca de 60 mil por agente Sonnet com teto** (estimativa; os medidos ficaram entre 34 e 54 mil).
   - **Todo agente tem teto.** Pesquisa web: até 15 a 20 chamadas, somando todas as ferramentas. Leitura: só os trechos necessários, via `grep -n` e leitura por faixa de linhas.
   - **Parada obrigatória no fim do Bloco 2.** Os Blocos 3 e 4 ficam para a janela seguinte, porque a escrita roda quase toda na conversa principal e não aparece nessa contagem.
   - **Compactação:** se o contexto for compactado, releia este brief e o checklist antes de continuar.
   - **O teto de 300 mil tokens por semana vale para a operação da fase 1**, não para esta execução.
3. **Todo fato novo traz URL e nível.** "Oficial" só se a página oficial abriu; senão, "secundária" ou "não conferido". Nada vem de memória como se fosse conferido.
   - **Leis no planalto.gov.br:** use `curl -sL <url> | iconv -f latin1 -t utf-8` e extraia **só o artigo**, com `grep -n "Art. 46"` e um recorte de linhas. **Nunca traga a página inteira para o contexto.**
   - **Se o Planalto derrubar a conexão,** use espelhos: www2.camara.leg.br/legin (a página "publicacaooriginal" traz o texto), normas.leg.br ou legislacao.presidencia.gov.br.
   - **Proteções anti-robô** nunca se contornam.
4. **Comentários novos de Vicente:** capte a essência, confira as palavras ambíguas ("por princípio" quis dizer "de início"), devolva o que entendeu e registre como diretriz, não como transcrição.
5. **Dados pessoais de terceiros nunca entram no Git.** O e-mail de Vicente, como autor e responsável, é permitido. A pasta `legado/` fica fora do Git.
6. **Ambiente Windows:**
   - o Python real é `C:/Users/alqui/AppData/Local/Programs/Python/Python312/python.exe`; o `python` do PATH é um atalho da Microsoft Store que falha;
   - use `PYTHONUTF8=1`;
   - em buscas que podem não achar nada, acrescente `|| true`;
   - no Git Bash, caminhos de API vão **sem a barra inicial** (`repos/...`), para não virarem caminho do Windows.
7. **Commits:**
   - autor configurado **só neste repositório**: `Vicente <vicente@dacaatinga.com.br>`. "Assinados" no plano quer dizer **autoria, não assinatura GPG**;
   - mensagem em português, terminando com a linha de atribuição que o sistema indicar na sessão;
   - **push depois de cada commit.**

---

## 1. Estado de partida e retomada

**Estado em 16/10:**
- **Pasta do projeto:**
  - `00_Fundacao_Cultura_Liquida.md` (v0.1, 1.430 linhas). O Anexo A fica nas linhas 696–1359 e o Anexo B em 1360–1388, ambos **intactos na v0.2**;
  - `legado/`: um .zip com 45 verbetes `.md.docx`, `Feed_Mestre_Completo_Rastreabilidade_69.csv.docx` e `grafo_dados_v7.json.docx`. As planilhas com dados pessoais não vieram;
  - `.claude/settings.local.json`;
  - **ainda não é um repositório Git**.
- **GitHub e Git:** o `gh` (2.102) está logado na conta **Indalt**, conta pessoal de Vicente, com escopo `repo`. O `git` (2.56) está sem autor configurado. O `gh` ainda não é o gerenciador de credenciais do git.
- **Pesquisa salva** em `C:\Users\alqui\.claude\plans\clb-pesquisa-2026-10-15\`. São JSON, que se leem com Python, nunca inteiros no contexto:
  - `w16qvy0xk.output.json`: frentes FH (fontes históricas), PA (acadêmicas) e MO (mídia e oralidade gravada), com cerca de 60 fontes, propostas e fatos com URL, nível e citação;
  - `wviefxn3h.output.json`: **lote A** (fontes oficiais, admissão, tiers, região, reconferência);
  - `w5h6fn1l0.output.json`: **lote B** (jurídico do coletivo, coletivo operacional, métodos);
  - `wf_*.journal.jsonl`: os mesmos resultados, uma linha por agente.
- **Plano completo:** `C:\Users\alqui\.claude\plans\vamos-planejar-com-as-modular-kurzweil.md`, com cerca de 1.010 linhas. Ache as seções com `grep -n "^### "` e não o leia inteiro.

**Estado depois da janela 1 (16/10):**
- Blocos 1 e 2 feitos (ver o checklist).
- O repositório `Indalt/cultura-liquida` é **público**.
- A proteção do `main` está ligada (1 aprovação, `enforce_admins: false`): o dono grava direto, e assim fica.
- As conferências C1 e C2 estão em `trilhas/2026-10-16_conferencias/` e custaram 82 mil e 77 mil tokens, com 19 chamadas cada.
- O commit 1, base da comparação dos anexos, é `e868a98`. A cópia de trabalho usa CRLF, então a comparação normaliza os fins de linha.

**Retomada: sempre, ao abrir uma janela, antes de qualquer passo:**
1. Se `trilhas/2026-10-16_execucao-v0.2.md` existir, leia esse checklist.
2. Rode `git log --oneline`, `git remote -v` e `gh repo view Indalt/cultura-liquida --json name,visibility || true`.
3. **Pule o que já foi feito.** Nunca crie um segundo repositório. Se `Indalt/cultura-liquida` existe e é o remote deste projeto, use-o.

---

## 2. Decisões vigentes: a essência confirmada

| ID | Essência |
|---|---|
| D-015 | A Fundação passa a v0.2, com as melhorias desta análise |
| D-016 | Vicente tem de 1 a 3 h por semana para curadoria humana. Os "15" **nunca** são teto de coleta. A separação em lote de máquina (P94) e cota humana (P84) é [PROPOSTA] |
| D-017 | Exemplos ilustram e nunca limitam o trabalho |
| D-018 | W é o modo como se entende o que se coleta: a prática **comum** (conhecimento compartilhado) da região, não a de um indivíduo. É uma episteme própria, **mas traduzível**, e deve ser tratada como dimensão. O que não foi captado é Falta, dita e nunca completada. O saber comum muda de forma autóctone ou por interação com outras comunidades. O registro próprio de W ("Compreensão local") é [PROPOSTA] |
| D-019 | **Não julgamos.** Fonte contrária não corrige, só documenta; se a fonte corrige, documenta-se a correção. Não é preciso documentar tudo. A prática que atende aos critérios de prática cultural **é admitida como evidência** e pode ignorar tentativas de revisionismo |
| D-020 | O agente Jurídico é de precaução: cria Faltas e nunca autoriza |
| D-021 | GitHub na conta Indalt, sincronizado, com commits de Vicente. **O repositório é público** (essência confirmada em 16/10, depois da janela 1): o que entra no Git é publicação aberta, e o legado e os dados pessoais de terceiros continuam fora. A proteção do `main` fica como está, com o dono liberado. **Futuro:** depois de tudo ajeitado, pensar em fechar o repositório e abrir só para quem Vicente quiser. Google só se for necessário. **Considerar** a nuvem para buscas e para tratamentos com IA, sem compromisso firme |
| D-022 | Os critérios de prática cultural vêm da lei: CF art. 216; Convenção UNESCO 2003 (Decreto 5.753/2006, art. 2); Decreto 3.551/2000 |
| D-023 | Medir e parar antes de acabar, com o estado salvo. Teto provisório de 300 mil tokens por semana em agentes **na operação da fase 1** |
| D-024 | Do legado, só entra no acervo o que for verificável e condizente com as regras novas. **O resto não se apaga**: fica como está (Drive e `legado/`, só leitura), o que concilia com o princípio 10. O site não é aproveitado |
| D-025 | As regras valem "de início" e são proporcionais. Depois das coletas e verificações da fase 1, há uma revisão de essencialidade (jurídico, colaboração, organização). **Nenhuma obrigação legal é desprezada**, e toda barreira jurídica traz o porquê e um caminho de liberação assistido. É uma biblioteca informativa com proposições, não uma réplica da legislação. **O grafo 4D fica fora dessa revisão** |
| D-026 | Na fase 1 trabalham só Vicente e os agentes, com logs; não há segunda pessoa. A segunda leitura vem do validador, de um verificador com harness diferente e da amostra sorteada. O responsável é Vicente, pessoa natural |
| D-027 | O **planejamento** rodou em Opus 5.5 com esforço máximo, ultracode e thinking. A **execução** roda em Opus 5.5 com esforço médio, com harness e sem ultracode, e os subagentes em Sonnet 5.5 alto (sugestão apoiada em medições). Depois, os modelos por tarefa são escolhidos **por teste**: a v0.2 não fixa modelo-alvo, e Sonnet 5.5 alto (ajustes) e Haiku 5.5 (rotinas) são hipóteses de partida. Harness qualificado |
| D-028 | A execução não para para aprovar o que já foi decidido |
| D-029 | **Antes da v0.2,** os agentes, suas habilidades e seus harness ficam na pasta do projeto, e a v0.2 é escrita **por eles**, com logs (16/10). **Só o Claude Code opera** os agentes (pasta `.claude/`, sem espelho `.agents/`), o que responde a pergunta 15. O **caso-piloto continua no Passo 1**: o Avaliador e o Arquivista nascem com os exemplos marcados como pendentes até ele |

---

## 3. Sequência de execução

### Bloco 1: preparação (sem agentes)
1. Crie o checklist `trilhas/2026-10-16_execucao-v0.2.md`, com passo, estado, consumo, modelo e esforço de cada agente, e observação. Registre o percentual de uso inicial informado por Vicente. Atualize o checklist ao fim de cada passo.
2. Crie `trilhas/2026-10-15_pesquisa/`:
   - copie para lá os 6 arquivos da pasta de pesquisa, **este brief e o plano completo**, para que entrem no Git;
   - gere por script um `indice.md`: fontes do catálogo (nome, via de acesso, uso, nível), propostas (ID, título, resumo) e fatos (afirmação, nível, URL);
   - procure dado pessoal de terceiros (e-mail, telefone, CPF, @perfil) e retire o que achar.
3. Crie o `.gitignore` com:
   - `legado/`
   - `.venv/`
   - `.claude/settings.local.json`
   - `Controle_Usuarios_e_Tiers*`
   - `Respostas_Coleta_Cidada_Tier1*`
   - arquivos de sistema (`Thumbs.db`, `desktop.ini`)
4. Rode `git init -b main` e configure o autor **local** (`git config user.name "Vicente"`; `git config user.email "vicente@dacaatinga.com.br"`). Faça dois commits:
   - commit 1: só a v0.1 e o `.gitignore`. Anote o hash no checklist, porque o Bloco 3 usa esse commit para comparar os anexos;
   - commit 2: a pasta `trilhas/`.
5. Rode `gh auth setup-git` e depois `gh repo create Indalt/cultura-liquida --private --source . --remote origin --push`. Confira com `gh repo view Indalt/cultura-liquida --json visibility`, que deve dizer `PRIVATE`. Se o nome já existir **e não for deste projeto**, use `cultura-liquida-clb` e registre.
6. **Teste da revisão obrigatória.** Rode:
   ```
   echo '{"required_status_checks":null,"enforce_admins":false,"required_pull_request_reviews":{"required_approving_review_count":1},"restrictions":null}' | gh api -X PUT repos/Indalt/cultura-liquida/branches/main/protection --input -
   ```
   - **403** (pede upgrade): é o limite do plano gratuito, como o lote B achou. O portão segue "combinado". Registre a mensagem literal.
   - **422:** é erro no corpo do pedido. Corrija e repita uma vez.
   - **200:** o recurso existe. Remova a proteção com `gh api -X DELETE repos/Indalt/cultura-liquida/branches/main/protection`, porque só Vicente trabalha, e registre que dá para ligar.

### Bloco 2: conferências essenciais (subagente Sonnet 5.5 com esforço alto, um por vez, teto de 15 a 20 chamadas)
Rode um agente por vez. Salve o resultado em `trilhas/2026-10-16_conferencias/lote-Cn.json` e `.md`, faça o commit e o push, e só então abra o próximo. **O C1 roda primeiro e serve para medir o custo.**

- **C1. Jurídico essencial da fase 1, com citação literal:**
  - Lei 9.610/1998, art. 7º (em que inciso estão as obras orais) e art. 46, II;
  - LGPD, art. 4º, I e II, b;
  - Lei 13.123/2015, art. 2º, I: patrimônio genético inclui microrganismos?
  - SisGen: o cadastro é declaratório? Pessoa natural pode cadastrar? Passos, campos e documentos, que alimentam o guia de liberação;
  - Res. CGen 47/2025: URL oficial e como pedir a consulta voluntária;
  - Res. IPHAN 1/2006: texto oficial e se ainda vigora.
- **C2. Padrões e serviços essenciais:**
  - TK Labels e como convivem com licenças abertas;
  - CARE (página oficial da GIDA);
  - Flora e Funga do Brasil: o campo de origem (nativa, naturalizada, cultivada);
  - rotinas do Claude Code: rede permitida, escolha de modelo, custo;
  - Save Page Now: chave e limites.
- **Ficam para o passo em que entram,** marcados "a conferir" na v0.2, com o passo indicado:
  - Marco Civil art. 19 e a tese do STF;
  - Código Civil arts. 20, 53 e 54;
  - os demais artigos da LGPD e da Lei 9.610;
  - Res. CD/ANPD 2/2022, art. 4º;
  - LDB art. 26-A; Res. CNE/CEB 8/2012; o manual do IPHAN;
  - Cultura Viva; FUNAI 1.401/2026;
  - W3C, SKOS, TBX, PROV, EDTF, CSL-JSON, JSON Schema, Linked Places;
  - as reconferências pendentes (termos do Google, Hemeroteca, Wikisource, tabela de biomas do IBGE, BHL);
  - os testes reais (IPHAN, LexML, Querido Diário, BDTD, OpenAlex).

**Parada obrigatória:** atualize o checklist, faça o commit e o push, e entregue a Vicente um relatório de uma tela (o que foi feito, o consumo, o que ficou "não conferido").

### Bloco 2.5: agentes, habilidades e harness (janela 2; sessão principal em Opus 5.5 com esforço médio)

**Objetivo (D-029):** pôr na pasta do projeto os agentes, suas habilidades e seus harness, para que a v0.2 (janela 3) e todo o trabalho seguinte sejam conduzidos por eles, com logs. **Harness** é tudo o que faz um agente acertar mesmo num modelo barato: instruções claras, formato de entrada e saída, validadores por script, exemplos reais, limites de custo e de passos, critério de parada e registro do que fez.

**Fontes para escrever o harness.** Ler por `grep -n` e faixas de linhas, nunca os arquivos inteiros:
- **v0.1:** §0 (Regra de Ouro e acordos), §2 (princípios), §6 (modelo de dados) e §7, Passo 1 (mapa de agentes, por volta das linhas 479–511);
- **plano** (`trilhas/2026-10-15_pesquisa/vamos-planejar-com-as-modular-kurzweil.md`), itens 1 a 8, 15, 16, 16-J, 19 e 22;
- `trilhas/2026-10-16_conferencias/` (C1 e C2) e `trilhas/2026-10-15_pesquisa/indice.md`.

**Passo 2.5.1: conferir os formatos oficiais do Claude Code** (no máximo 6 chamadas web; registrar o nível no checklist):
- frontmatter de subagente em `.claude/agents/` (`name`, `description`, `tools`, `model`; aceita `effort`?);
- estrutura de habilidade em `.claude/skills/<nome>/SKILL.md`;
- eventos de hook (existe `SubagentStop`? que JSON chega na entrada padrão?);
- importação de arquivo no `CLAUDE.md` (`@AGENTS.md`).

Fontes: as páginas oficiais em code.claude.com/docs (sub-agents, skills, hooks, memory). **O que não se confirmar fica pelo jeito mais simples que funcione**, e isso é registrado.

**Passo 2.5.2: regras do projeto**
- **`AGENTS.md`** (até 150 linhas):
  - o projeto em 5 linhas;
  - os princípios e as decisões D-015 a D-029, pela essência, uma linha cada;
  - a Regra de Ouro e os acordos;
  - o passo corrente;
  - uma tabela curta de agentes e habilidades;
  - o orçamento;
  - onde está cada coisa;
  - o que não fazer.
- **`CLAUDE.md`:** importa o `AGENTS.md` e traz só as notas do Claude Code: Python real, `PYTHONUTF8`, `|| true`, os modelos por agente, e os commits (autor Vicente local; push depois de cada commit; linha de atribuição).

**Passo 2.5.3: base comum**
- **`.venv`:** criada com o Python real, com `jsonschema`. Se a instalação falhar, use validação mínima em Python puro e registre.
- **`esquemas/`:** JSON Schema só do que esta rodada usa: log, resultado de conferência, Falta (com caminho de liberação), guia de liberação, achado de verificação.
- **`scripts/`:**
  - `registrar_log.py`: acrescenta uma linha validada em `trilhas/logs/AAAA-MM-DD_<agente>.jsonl`, com data e hora, agente, habilidade, versão do harness, modelo, esforço, referência da entrada, ações, resultados, decisões (cada item: aceito, descartado, quarentena ou Falta, com o motivo), tokens, chamadas, duração e erros. **Reprova dado pessoal de terceiros**;
  - `procurar_dado_pessoal.py`;
  - `comparar_anexos.py`: compara os Anexos A e B com o commit `e868a98`, normalizando CRLF;
  - `checar_fundacao.py`: marcadores, D-015 a D-029, legenda das P-refs e entidades do §6;
  - `validar.py`: confere um JSON contra um esquema.

**Passo 2.5.4: agentes e habilidades.** Um arquivo por agente em `.claude/agents/`, com:
- papel;
- quando é chamado;
- ferramentas permitidas (o mínimo necessário);
- modelo e esforço;
- habilidades que usa;
- o que não faz;
- critério de parada;
- **log obrigatório** (via `registrar_log.py`);
- as regras herdadas do `AGENTS.md`.

**Os modelos são iniciais e provisórios** até os testes do Passo 1 (D-027).

| Agente | Rodada | Papel | Habilidades | Modelo inicial |
|---|---|---|---|---|
| **curador** | A | conduz o brief e o plano; cuida do Registro de Decisões, do checklist, do orçamento e dos logs; para quando o plano não resolve (Regra de Ouro). Na prática, é a sessão principal | `executar-brief`, `registrar-decisao` | sessão principal (Opus 5.5, médio) |
| **redator** | A | escreve os textos do projeto: agora a v0.2; depois, a camada Educação e o boletim | `escrever-secao-fundacao` | Opus 5.5, médio |
| **auditor** | A | faz as verificações mecânicas e independentes, porque quem produz não confere: relatórios calculados e achados confirmados por `grep` ou script | `verificar-fundacao`, `conferir-fato` | Sonnet 5.5, alto |
| **juridico** | A | precaução: cria Faltas e nunca autoriza. Confere normas e prepara guias de liberação com porquê, passo a passo, documentos e modo de preencher (D-025) | `conferir-fato`, `triagem-juridica`, `guia-de-liberacao` | Sonnet 5.5, alto |
| **rastreador** | B | ambientes, fichas de acesso, consultas, recortes e pegadas | `ficha-de-acesso`, `consulta` | Sonnet 5.5, alto (a testar contra o Haiku) |
| **avaliador** | B | triagem por valências, quarentena e extração de evidência com trecho literal | `extrair-evidencia` | a definir no Passo 1 |
| **arquivista** | B | termos, fichas e grafo 4D | `registrar-termo`, `montar-ficha`, `gerar-grafo` | a definir no Passo 1 |
| **campo-de-acao** | B | ferramentas de ação sob demanda, como o kit de fonte primária | `kit-fonte-primaria` | a definir |

**Harness de cada habilidade.** Cada `.claude/skills/<habilidade>/` tem:
- **`SKILL.md`**, com:
  - frontmatter no formato conferido;
  - objetivo; quando usar e quando não usar;
  - entradas e saídas (apontando para `esquemas/`);
  - passos numerados;
  - regras herdadas: nível de verificação, essência, dado pessoal, anti-robô, Falta dita;
  - teto de chamadas e de tokens estimados;
  - critério de parada;
  - o que não faz;
  - campos do log;
  - versão do harness e histórico de mudanças;
- **`exemplos/`** com pares reais: entrada e saída esperada, ou critérios de aceitação;
- um **validador**, comum ou próprio.

**Exemplos reais por habilidade:**
- **`conferir-fato`:** C1 e C2. O validador tem que **passar** nos JSON reais e **reprovar** um caso com "oficial" sem URL.
- **`guia-de-liberacao`:** o SisGen. Cadastro declaratório, que pessoa natural pode fazer (Decreto 8.772, arts. 22 e 22-A; C1, oficial). As telas não foram conferidas e ficam marcadas assim.
- **`triagem-juridica`:** os casos do 16-J (dado sensível; conhecimento tradicional de origem identificável).
- **`verificar-fundacao`:** as divergências reais que os revisores acharam em 16/10. Por exemplo, a D-018 tinha perdido "traduzível".
- **`registrar-decisao`:** dois casos reais: o "por princípio" que era "de início", e a D-021, que passou a público.
- **`escrever-secao-fundacao`:** as essências da seção 2. O caso de reprovação é uma transcrição literal no lugar da essência.
- **`ficha-de-acesso` e `consulta` (rodada B):**
  - Hemeroteca respondendo 403; a API da BDTD funcionando; o Querido Diário instável;
  - "cauim": 54 resultados no OpenAlex, 10 na BDTD, 30 no Oasisbr e 12 na Crossref, mais a bola de neve do artigo do Boletim Goeldi.

  Tudo isso está nos JSON da pesquisa.
- **Avaliador, Arquivista e Campo de Ação (rodada B):** papel, formato e passos escritos; **exemplos marcados "pendente: caso-piloto (Passo 1)"**.

**Passo 2.5.5: log automático**
- **Se o formato conferido permitir,** um hook `SubagentStop` no `.claude/settings.json` do projeto grava uma linha mínima a cada fim de subagente. É uma rede de segurança: o log completo continua sendo gravado pelo curador, via `registrar_log.py`, depois de cada chamada, porque é ele quem tem os tokens.
- **Teste:** uma chamada curta ao **auditor**, que roda `checar_fundacao.py` na v0.1 e cujo resultado esperado são as ausências conhecidas. Confira se as duas linhas de log foram gravadas.

**Passo 2.5.6: testes e fechamento**
- Rode os validadores sobre todos os exemplos e registre em `testes/relatorio-rodada-A.md` o que passou, o que reprovou como esperado e o que ficou pendente.
- **Comparação entre modelos** (Haiku × Sonnet × Opus): **não é agora**. Ela vem no Passo 1, com o caso-piloto e os logs reais.
- Commit e push a cada passo, com o checklist atualizado.

**Parada obrigatória no fim do Bloco 2.5,** com relatório de uma tela a Vicente.

**Pronto quando:**
- cada agente tem o seu arquivo, com todos os campos;
- cada habilidade da rodada A passa nos exemplos reais e reprova o exemplo com erro;
- o teste de log gravou as linhas;
- o `AGENTS.md` tem até 150 linhas;
- nada com dado pessoal de terceiros entrou no Git;
- tudo está no GitHub.

**Estimativa:** de 200 a 300 mil tokens, quase tudo de escrita na sessão principal. Subagente, só o do teste. A regra de orçamento vale.

### Bloco 3: escrever a v0.2 (janela 3; conduzida pelos agentes do Bloco 2.5)

**Quem faz o quê (D-029):**
- o **curador**, que é a sessão principal, orquestra pelo mapa abaixo, grava os logs, controla o orçamento e faz um commit por grupo;
- o **redator** escreve cada grupo de seções direto no arquivo. Ele recebe só as faixas de linhas necessárias: a seção da v0.1, as essências da seção 2 e as fontes no plano;
- o **auditor** verifica cada grupo depois de escrito;
- o **juridico** confere os trechos jurídicos (§5, §7, §8 e o Anexo C).

**Grupos de seções:**
1. cabeçalho, §0 e §1;
2. §2;
3. §3, §4 e §5;
4. §6;
5. §7 a §11;
6. Anexos C, D e E.

Se o orçamento apertar, pare no fim de um grupo; a retomada continua do próximo.
**Base:** a v0.1, este brief, o mapa abaixo e os resultados do Bloco 2. Use a lista de edição do plano ("Implementação", passo 4, por volta das linhas 938–994) como **lista de conferência**. Faça um commit e um push por grupo de seções.

| Seção da v0.2 | O que fazer | Fonte no plano |
|---|---|---|
| Cabeçalho | versão 0.2, data, "o que mudou" em até 10 linhas | — |
| §0 | legenda das P-refs ("Pn = pedido n de Vicente, Anexo A; buscar `#### Pn`"); acordo 6 (exemplos não limitam); PROPOSTA ≠ plano; diário em `trilhas/`; registro de comentários pela essência | 8 |
| §1 | os três movimentos permanecem; trocar "RSS" pelo modelo monitoramento × escavação; a casa é o repositório | 10, 11 |
| §2 | princípios 1 (custódia do texto da fonte), 2 (Termo), 3 (W, Falta, "não julgamos", Proposição e Evidência, linhagens), 4, 9 e 11 (reconstituição) | 1–6 |
| §3 | o legado conforme a D-024 (o resto não se apaga, só não entra); §3.5 resolvido (exportado em 16/10); o site não é aproveitado | D-024 |
| §4 | manter as tabelas e atualizar o status das P-refs afetadas (P26, P48, P73, P84, P94, P95, P14) | — |
| §5 | 5.1: GitHub e custódia; 5.2–5.3: Consulta, Recorte, ficha de acesso; 5.4: portas de admissão e degraus do 16-J; 5.5: camadas de nuvem, sem Apps Script como agendador; 5.7: Lugar, ferramentas por tier, grafo 4D (21); 5.9: tiers | 10, 13–17, 20, 21 |
| §6 (reescrito) | as entidades da linha 943 do plano, mais Recorte, Lugar e papéis de pessoa; Falta com caminho de liberação; IDs imutáveis; tabela de eixos de status × selos | 1–6, 15, 17, 18 |
| §7 | Passo 0 (feito; despublicar o site e arquivar o App da Web); 1 (caso-piloto, harness, logs, Jurídico com regras fixas e guias, testes de modelos); 2 (validador, `.gitignore`, reconstituição, sem cópia do Apps Script); 3 (legado como ambiente, D-024); 4 (precondições: guias e consentimento; duas camadas); 5; 6 (precondição: a Lei 13.123 resolvida para o que se publica); 7 (grafo 4D); 8; 9 (guias assistidos); 10; fase 1, fase 2 e gatilho | 7, 9, 19, 21, 22; fase 1/2 |
| §8 | pendências: o caso-piloto, que é o único bloqueio; o caminho na Lei 13.123, que bloqueia publicar; as demais, por passo | decisões |
| §9 | D-015 a D-028, pela essência da seção 2 deste brief | — |
| §10 | perguntas 6, 7, 9 e 13 atualizadas; novas: critério de revisionismo; W e etnografia; a pergunta de pesquisa do grafo 4D | decisões |
| §11 | cota, guarda de orçamento e medidas reais | 9, 19 |
| Anexo C | C.1 com os textos conferidos (seção 5 e Bloco 2); C.2 com as correções (Google, OpenAlex, termos do Actions); C.3 novo, com o nível de cada item | 13, Bloco 2 |
| Anexo D (novo) | a trilha da análise, resumida, apontando para `trilhas/2026-10-15_pesquisa/` | — |
| Anexo E (novo) | os ambientes candidatos, em tabela gerada do catálogo | 13 |

**Regras de escrita:**
- funda as camadas do plano num texto final único;
- as essências vêm da seção 2;
- explique cada termo técnico na primeira vez que aparece;
- mantenha curtas as seções de leitura padrão e leve o que for longo para os anexos;
- marque [VIGENTE] o que Vicente decidiu e [PROPOSTA] o desenho;
- **os Anexos A e B não mudam.**

**Verificação:**
1. **Mecânica, por script:**
   - o trecho entre `## Anexo A` e `## Anexo C` é idêntico ao do commit 1 (`git show <hash>:00_Fundacao_Cultura_Liquida.md`);
   - a busca por "Versão 0.2", "D-015" a "D-028", "Anexo D", "Anexo E", "C.3", "Falta" e pela legenda das P-refs acha cada um;
   - o §6 contém cada entidade da lista.
2. **Independente:** o **auditor** (habilidade `verificar-fundacao`), em até três passadas, uma por olhar, com teto de leitura por `grep`. Os trechos jurídicos passam também pelo **juridico**. Os olhares:
   - (a) as decisões D-015 a D-028 têm o sentido certo;
   - (b) não há contradições;
   - (c) todo fato tem nível e todo termo tem explicação.

   **Cada achado só é corrigido depois de ser confirmado por `grep` ou script, com a linha citada.** Não se decide por votação. A independência vem do harness diferente (D-027) e da confirmação mecânica.

### Bloco 4: fechamento
1. Faça o commit final e o push. Confira que o `git status` está limpo e que `git log origin/main` é igual ao local.
2. **Relatório curto a Vicente:**
   - o que foi feito;
   - o consumo medido por bloco;
   - o que ficou "não conferido";
   - as decisões abertas: caso-piloto; caminho na Lei 13.123; pergunta do grafo; critério de revisionismo; W e etnografia; P48 para entrevistas; licença do acervo;
   - **ações de Vicente:** arquivar a implantação do "App da Web" do Apps Script e despublicar o Google Site (D-024);
   - o próximo passo: Passo 1, com harness qualificado, logs e testes de modelos.
3. **Memória:** os acordos já estão registrados (exemplos não limitam; termos explicados; orçamento; plano ≠ execução; registrar a essência). Não duplique.

---

## 4. Não fazer nesta execução
- Não completar o harness do avaliador, do arquivista e do campo-de-acao sem o caso-piloto: isso fica para o Passo 1. No Bloco 2.5 eles ganham papel, formato e passos, com os exemplos marcados como pendentes.
- Não processar o legado nem abrir os Docs. Isso é o Passo 3.
- Não criar rotinas na nuvem nem workflows do GitHub Actions. Isso é o Passo 4 e a fase 2.
- Não publicar site nenhum.
- Não reabrir decisão vigente. Se encontrar conflito, registre e pergunte (caso d).

## 5. URLs dos textos legais conferidos em 15/10 (Anexo C.1)
- **CF:** https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm (arts. 215 §1º e 216)
- **Decreto 5.753/2006** (Convenção UNESCO 2003): https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/decreto/d5753.htm (arts. 2 e 13)
- **Decreto 3.551/2000:** https://www.planalto.gov.br/ccivil_03/decreto/d3551.htm
- **Res. IPHAN 1/2006** (secundária): https://www.legisweb.com.br/legislacao/?id=103301
- **Decreto 6.040/2007:** https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6040.htm
- **Lei 13.123/2015:** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13123.htm (arts. 1º, 2º, 4º, 8º, 9º, 10 e 12)
- **Decreto 8.772/2016:** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/d8772.htm (arts. 12 e 13)
- **Lei 9.610/1998:** https://www.planalto.gov.br/ccivil_03/leis/l9610.htm (arts. 8º, 41, 45 e 46, III)
- **Res. CGen 47/2025:** URL a localizar no C1.
- **CNS 510/2016, CNS 304/2000, FUNAI IN 01/1995, BNCC, Res. CD/ANPD 2/2022, termos do GitHub e os demais:** URLs completas nos JSON dos lotes A e B.

## 6. Divergências conhecidas entre o plano e este brief (vale o brief)
- **"Outra pessoa aprova", "duas pessoas", "segunda pessoa":** na fase 1 não há segunda pessoa. A segunda leitura vem do validador, do verificador e da amostra (D-026).
- **Decisões já resolvidas que o plano ainda lista como abertas:** o estado em 16/10 é o que vale.
- **"Testes via GitHub Actions":** não acontecem nesta execução.
- **"Anexo D com as propostas completas":** o Anexo D é um resumo; as propostas ficam em `trilhas/`.
- **"Aqui o Haiku 5.5" (item 22):** os modelos-alvo são decididos por teste.
- **"Commits assinados":** quer dizer autoria, não assinatura GPG.
- **Agentes depois da v0.2 (o plano e o §7 da v0.1):** a D-029 mudou. Os agentes vêm **antes** da v0.2, no Bloco 2.5, e o caso-piloto continua no Passo 1.
- **"Repositório privado":** a D-021 mudou. O repositório é **público**, e fechá-lo é uma decisão futura.
