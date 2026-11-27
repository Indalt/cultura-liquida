# K-011 · Passo 4 — Saída única para a reunião do K-004

**Data:** 26/11/2026 (relido em 27/11/2026) · **Escrito por:** Claude Code (Opus 5.5, esforço médio), que tinha o bastão depois da comparação · **Relido por:** Antigravity (Gemini 4 Neon, esforço alto) em 27/11/2026 (D-038; D-060; `revisao-claude-26-11.md`, §4).

Este é o documento único que o cartão K-011 pede (`trilhas/2026-11-22_logica/falas-vicente.md`, passo 4): os fundamentos confirmados, o destino de cada insumo e a contagem do que resta. A `trilhas/2026-11-22_logica/base.md` se absorve aqui (seções 3 e 4). **Nada aqui é decisão nova:** o que muda regra é da reunião (D-046, D-061).

**Fontes:** `fundamentos.md` (Passos 1 e 2), `trilhas/decisoes/D-061.json`, `revisao-claude-26-11.md`, `passo3-proposta.jsonl` (Antigravity), `passo3-releitura.jsonl` (Claude Code, gravada sem abrir a proposta), `comparacao.md` e `comparacao.json` (gerados por `comparar_passo3.py`, sem IA) e `base.md`.

---

## 1. Os fundamentos confirmados (D-061)

O enunciado inteiro, a fonte e as linhas da Fundação de cada um estão em `fundamentos.md` (§1). Aqui, só a essência.

| # | Fundamento | Estado |
|---|---|---|
| 1 | O sistema faz mais que buscar, encontrar e devolver: acolher, situar, organizar, afirmar na voz própria, agir, proteger, auditar a si mesmo, durar e mudar (lista aberta) | confirmado; "dão conta no momento" |
| 2 | O rigor é não dizer mais do que as fontes permitem: o observado, a Falta e o alcance | confirmado |
| 3 | Duas vozes: a da atribuição ("a fonte F diz P no trecho T") e a própria ("o sistema diz"), onde mora a escolha lógica | confirmado |
| 4 | Regimes de saber situados têm tensões formais ou políticas, não inconsistência; resolvem-se situando ou predicando | confirmado |
| 5 | A ferramenta não precisa de lógica não clássica nova | confirmado |
| 6 | Uma lógica não clássica pode valer como regra do sistema, na voz própria, declarada como viés | confirmado como desenhado na `base.md` §4; **[ABERTO]** regra explícita ou declaração do quadro |
| 7 | μ e λ descrevem linhagens documentais; não são a lógica do sistema nem veredito | confirmado |
| 8 | Cultura muda; o modelo de dados (código fixo, identificação pelo termo) pressupõe identidade estática, em tensão com a lei e com a Transformação de W | confirmado |
| 9 | Usar qualquer conhecimento é um viés, e o viés se declara | confirmado em parte (observação nas fichas); **[ABERTO]** wiki inteiro e campo de ação |
| 10 | Exemplo e termo de explicação não entram no sistema, no código, nas listas fixas, nos testes nem no escopo | confirmado |
| 11 | A cajuína sozinha basta para o piloto; o K-126 não roda; as outras CLB seguem candidatas | confirmado (substitui a D-057) |
| 12 | Trabalhar para chegar a algum lugar, sem exceção às regras vigentes nem decisão avulsa | confirmado |

**Os três [ABERTO] da D-061 vão à reunião.** As posições iniciais das duas LLMs estão em `revisao-claude-26-11.md`, §5:
1. Lógica como regra ou como declaração. Posição do Claude Code: declarar o quadro agora e só virar regra onde a voz própria concluir algo e um caso real pedir. No piloto, nenhuma Proposição ficou "inconsistente".
2. Vieses no wiki inteiro. As duas LLMs convergem: uma página fixa com os vieses estruturais e um bloco gerado por script a partir do alcance dos logs, que muda quando entra CLB nova.
3. Viés no campo de ação. As duas LLMs convergem: basta o carimbo mínimo (link da ficha, Faltas, data, como citar, aviso legal). Uma nota curta só quando o artefato sustenta decisão de poder e um viés muda o que ele recomenda.

---

## 2. O destino de cada insumo (Passo 3)

**Como se chegou:** a Antigravity propôs e o Claude Code releu às cegas (D-038). O `comparar_passo3.py` comparou as duas leituras. Onde o destino diverge, fica o mais conservador ("fica como problema da ferramenta"). Toda divergência vem para a reunião (D-037).

**Concordância:** 18 dos 35 insumos concordam em tudo. O destino diverge em 6, e 11 divergem só em fundamento, via ou junção.

**Destino final:**

| Destino | Quantos | Insumos |
|---|---|---|
| fica como problema da ferramenta | 30 | os demais |
| já resolvido depois de 20/11 | 2 | 101 (commit 1ce9c4a), 105 (commit c16feab) |
| dissolve-se num fundamento e vai à reunião como texto da Fundação | 2 | 142 (fundamento 10), 144 (fundamento 6) |
| junta-se a outro insumo | 1 | 143, ao 144 (fundamento 7) |

### 2.1 Divergências no destino (6): ficaram como problema da ferramenta

| Insumo | Proposta (Antigravity) | Releitura (Claude Code) | O que a reunião olha |
|---|---|---|---|
| 58 (pré-triagem só lê os Termos) | junta-se ao 140 (fund. 10, os dois) | fica (fund. 10, script) | As duas leituras veem o mesmo mecanismo do 140. A releitura o separou por ser outra etapa (a pré-triagem, não a Consulta). |
| 62 (oralidade não transcrita) | dissolve-se no fund. 9 (viés do arquivo) | fica (os dois) | Se declarar o viés basta ou se a ferramenta precisa transcrever. |
| 112 ([ABERTO] da D-049, "intervenção humana") | dissolve-se no fund. 9 | fica (regra de Vicente) | As duas concordam que a via é "nenhum dos dois". O [ABERTO] é da D-049, não de um fundamento. |
| 132 (custo da rotina com IA) | junta-se ao 136 | fica (script) | Se a medida da sessão da rotina e a calibração do lote cabem no conserto da medida única (136). |
| 135 (vistoria da casa) | já resolvido (c16feab, 1ce9c4a, 814c2b5) | fica (script) | Quatro das cinco partes foram resolvidas. Falta decidir quando a vistoria roda sozinha (`trilhas/2026-11-20_K-127/lista.md`, proposto a Vicente). |
| 139 (duas cópias de `numero()`) | junta-se ao 136 (fund. 12) | fica (fund. 2, script) | Depende da descontinuação do `orcamento.py` (seção 5, item 3). O `relatorio_piloto.py` fica para o K-007. |

### 2.2 Divergências só em fundamento, via ou junção (11)

Nenhuma muda o destino. Os itens seguem a tabela em `comparacao.md`. O padrão principal:
- **Fundamento.** A Antigravity ligou mais insumos a um fundamento: o 2 nos insumos 68, 69, 77 e 123; o 8 no 97; o 10 no 87; o 11 no 141; o 1 no 136 (onde a releitura marcou o 2). A releitura só ligou onde o fundamento claro teria evitado o insumo, e marcou "nenhum" nos defeitos de código.
- **Via.** Em 77, 87, 97, 123 e 128, a releitura leu "nenhum dos dois": falta primeiro uma regra de Vicente (D-038), e só depois habilidade ou script a aplicam. A proposta leu a via de quem aplicaria a regra.
- **Outros casos:** 104 (proposta "nenhum dos dois"; releitura "script"), 141 (os dois ou script) e 142 (proposta "nenhum dos dois"; releitura "habilidade ou agente": o texto da `registrar-decisao`).

### 2.3 Os 30 que ficam como problema da ferramenta, por família da limpeza de 20/11

| Família | Insumos | Via (quando as duas leituras concordam) |
|---|---|---|
| A. Medida e custo | 132, 136, 139, 141 | 136: script; os outros divergem |
| B. Rotinas | 70, 104, 126, 129 | script (104 diverge) |
| D. Achar outras CLB | 58, 140 | 140: os dois (fund. 10); 58: via diverge (fund. 10) |
| E. Ler a fonte | 68, 69 | script |
| F. Coleta | 49, 55 | script |
| G. Registros e relatórios | 46, 63, 111, 137 | script (lote 5 do K-127) |
| H. Acesso às fontes | 52, 112 | 52: os dois; 112: regra de Vicente |
| I. Jurídico | 53, 87 | 53: os dois (fund. 10); 87 diverge |
| J. Pessoas citadas | 77, 128 | divergem |
| K. Receber | 61, 62 | 61: script; 62 diverge |
| L. Organização | 97, 123 | divergem |
| M. Casa e harness | 94, 135 | script (94 no K-127) |

**Contagem por via:**

| Via | Quantos | Insumos |
|---|---|---|
| script | 15 | 46, 49, 55, 61, 63, 68, 69, 70, 94, 111, 126, 129, 135, 136, 137 |
| os dois | 3 | 52, 53, 140 |
| regra de Vicente, nenhum dos dois | 1 | 112 |
| via divergente | 11 | à reunião |

**Leituras das duas, sem decisão:**
- Cinco dos 30 tocam a operação com IA em escala, que a D-058 libera depois da fila: 70, 126, 128, 129 e 132 (`trilhas/planejamento/rodadas/2026-11-20_K-004/limpeza/resultado.md`, leitura do curador).
- Cinco estão no escopo já escrito do K-127: 46, 63, 111 e 137 (lote 5) e 94 (passo de limpeza).

---

## 3. A lógica que o sistema pede (absorve a `base.md`, §2 a §4)

A `base.md` era a base escrita em 22/11 para esta reunião. As essências que ela marcava "a confirmar" entraram na D-061 (fundamento 1 confirmado; fundamento 9 confirmado em parte, com wiki inteiro e campo de ação ainda [ABERTO]). O texto dela entra aqui, resumido. A tabela dos atos fica na `base.md`, §2, como trilha.

- **Cada ato pressupõe algo, e o que ele pressupõe é o seu viés.**
  - Buscar só acha o que se sabe nomear.
  - Encontrar supõe a leitura fiel.
  - Situar parte de um quadro X, Y, Z, W escolhido antes dos dados.
  - Afirmar na voz própria é o salto de "a fonte diz" para "o sistema diz".
  - Agir e proteger lidam com normas que colidem.
- **Onde a lógica comum basta:** encontrar, acolher e auditar, que falam na voz da atribuição; e situar, pela lógica de contextos (McCarthy, 1993: `ist(c, p)`).
- **Os cinco lugares onde ela não basta** (fundamento 6):
  1. a voz própria, que não afirma sem documentação nem explode diante de fontes opostas (lógica não-alética, da Costa, 1989; ou os quatro valores de Belnap);
  2. o alcance parcial (quase-verdade, Mikenberg, da Costa e Chuaqui, 1986);
  3. o rigor com o poder (Lógicas da Inconsistência Formal, Carnielli, Coniglio e Marcos);
  4. as normas em conflito (deôntica paraconsistente, da Costa e Carnielli, 1986; Coniglio, 2007);
  5. a identidade no tempo (lógicas não-reflexivas de da Costa e Krause, ou a não-alética na fronteira da transformação; fundamento 8).
- **Leitura da `base.md`, §4.** Só a linha de da Costa cobre os cinco lugares numa família só. O traço que mais combina com o projeto é a negação clássica onde a fórmula é bem-comportada e não clássica só onde a documentação obriga. O que menos combina é o Para-analisador da Eτ, usado no piloto como instrumento de decisão. Daí o fundamento 7.
- **Todas as referências seguem "não conferido".** Só o resumo de busca de 22/11 foi lido. Elas estão na `base.md`, §7, e precisam de conferência antes de entrar no texto da Fundação (`fundamentos.md`, §3).

---

## 4. Vieses a declarar (absorve a `base.md`, §5)

Declarar não corrige o viés: diz de onde se vê (Haraway, 1988, "não conferido"). A lista de 14 vieses, com o efeito de cada um e se já é dito hoje, está na `base.md`, §5. Ficaram decididos e em aberto estes pontos:
- **Decidido pela D-061:** o viés se declara como observação nas fichas.
- **Em aberto:** o wiki inteiro e o campo de ação (seção 1, itens 2 e 3).
- **Não ditos hoje nem como viés:** o lógico, o da língua, o do quadro de coordenadas, o da lei como definição, o da contagem, o do que é uma CLB e o da identidade. São o núcleo da página fixa proposta para o wiki (junto com o da máquina e o de valor — este já dito hoje como princípio, não como viés; `base.md`, §5; `revisao-claude-26-11.md`, §5, item 2).

---

## 5. Pontos que só a reunião resolve

1. **Os três [ABERTO] da D-061** (seção 1).
2. **As 17 divergências do Passo 3** (seções 2.1 e 2.2). Seis delas pedem uma leitura de Vicente sobre regra: 77, 87, 97, 112, 123 e 128.
3. **A descontinuação formal do `orcamento.py`,** com a confirmação de Vicente para os 6 casos da trava (fala 14; D-059). Ela mexe nos insumos 132, 136 e 139.
4. **Logs com tokens 0 que querem dizer "não medido".** O esquema só aceita null em script, rotina, pessoa e agente de workflow. O conserto muda um esquema e se junta ao 136 (`revisao-claude-26-11.md`, §3, item 1).
5. **O estado "inconsistente", que abre o cartão de conflito** (`scripts/fila_curadoria.py:58`). Leitura das duas leituras do Passo 3: é gatilho para chamar Vicente, não veredito (fundamento 7). Fica como está até a reunião (insumo 143, junto ao 144).
6. **Os exemplos das habilidades** (`.claude/skills/*/exemplos/`), à luz do fundamento 10. Na proposta do Passo 3 (`passo3-proposta.jsonl`, linhas 14 e 31; `fundamentos.md`, §3 e §4), a Antigravity conferiu as 15 pastas `exemplos/` e registrou que funcionam como casos de prova, e não como lista fechada em execução (salvo o nome antigo de guia em `triagem-juridica/exemplos/falta-conhecimento-tradicional.json:15`), situando as listas fechadas nos scripts (`gerar_termo.py`, `pretriagem.py`, `mencoes_incidentais.py`, `triagem_fixa.py`) e em `esquemas/triagem-fixa.json`. Falta a segunda conferência independente pelo Claude Code (D-038; insumos 53, 87 e 140).
7. **O resto da pauta do K-004, sem mudança:** o K-006, a 3ª passada do K-005 e os estacionados (K-125, K-115b, K-115c). Também a pergunta a Vicente (levantada pelo agrupador cego da limpeza de 20/11) sobre se arrumar a casa (insumos 94 e 135) é parte da promessa da ferramenta.

### Notas da releitura da Antigravity (27/11/2026 — discordâncias de leitura e posição para a reunião, D-038)

1. **Insumo 112 ([ABERTO] da D-049, "intervenção humana"):** concorda em mantê-lo para decisão de Vicente (`via: "nenhum dos dois"`), mas discorda da leitura da §2.1 de que o ponto seria alheio a um fundamento: a `base.md` (§5, l. 70) inclui expressamente a D-049 (sem conta nem cadastro) e a D-044 (robôs barrados) no **viés do arquivo (fundamento 9)**. A reunião decide o alcance de "intervenção humana" já sabendo que o que ficar fora entra como declaração desse viés, não como contorno na ferramenta.
2. **Insumo 62 (oralidade não transcrita):** discorda de tratá-lo como problema da ferramenta na fase 1; P48 e entrevistas orais estão adiados na Fundação (`00_Fundacao_Cultura_Liquida.md`, l. 816, 844 e 895; K-008, fase 2). Na fase 1, vale declarar o viés do arquivo (fundamento 9, `base.md`, l. 70); a transcrição pertence à decisão da fase 2 (K-008), não à saída do piloto.
3. **Insumos 58, 132, 135 e 139 (divergências de destino):** aceita a regra conservadora que mantém todos visíveis para a reunião (D-037) e **concorda com o reparo do Claude Code no 135** (faltou 1 das 5 partes: decidir quando a vistoria roda sozinha, `trilhas/2026-11-20_K-127/lista.md`, l. 152). Mantém para a reunião que o 58 convém ser tratado junto ao 140 (mesmo fundamento 10 em pré-triagem e Consultas) e que 132 e 139 convém caminhar com o 136 após a descontinuação formal do `orcamento.py`.
4. **Posição inicial sobre o [ABERTO] 1 da D-061 (lógica como regra ou como declaração, §1):** converge com a posição do Claude Code (declarar o quadro lógico agora e só virar regra explícita onde a voz própria concluir algo e um caso real pedir), com um acréscimo para a reunião: separar o 5º lugar (**identidade no tempo**, fundamento 8) da contagem de `"inconsistente"` da Eτ, porque 0 `"inconsistente"` no piloto mede só contradição do eixo 3, enquanto a tensão de identidade (`CL-nnnn` fixo vs. transformação da prática) já está presente na própria cajuína (fala 10 de 22/11).
5. **Padrão das cinco divergências de via (77, 87, 97, 123 e 128):** não há desacordo real entre `script` e `habilidade`; o Claude Code marcou `"nenhum dos dois"` por faltar primeiro a regra de Vicente (D-038), e a Antigravity apontou quem a executa depois de decidida. Assim, fixada a regra na reunião, o executor já está mapeado.
6. **Teste da hipótese "pouco a resolver para sair do piloto" (D-061, palavras conferidas; `trilhas/2026-11-22_logica/falas-vicente.md`, l. 94 e 121):** a contagem mostra que os fundamentos sozinhos não esvaziaram a maior parte dos 35 insumos — 2 se dissolvem direto em texto da Fundação, 1 se junta, 2 já foram resolvidos e **30 (em 12 famílias)** seguem abertos, dos quais 5 já estão no escopo escrito do K-127, 5 tocam a liberação da operação com IA em escala (D-058) e 6 pedem antes uma regra de Vicente. Fica dito explicitamente para a reunião (P96, D-030).

---

## 6. Depois (sem explorar, D-035)

- Reconferir as 9 referências da `base.md`, §7, antes de entrarem no texto da Fundação.
- No K-127:
  - o caso "F-0024 completada por inferência" com o Python sem `jsonschema`;
  - o nome do guia em `.claude/skills/triagem-juridica/exemplos/falta-conhecimento-tradicional.json:15` (`fundamentos.md`, §3).
- A primeira versão do `comparar_passo3.py`, no commit 91edbc0, apagava os campos concordantes quando o destino divergia. Foi corrigida neste passo. A contagem de divergências não mudou.
- Na etapa 5 do K-004, realocar os alvos que a limpeza de 20/11 apontou para o K-126 (encerrado sem execução pela D-061): insumos 91, 131 e a nota do 99 (`trilhas/planejamento/rodadas/2026-11-20_K-004/limpeza/resultado.md`, l. 114, 123 e 175).

## 7. Alcance (D-030)

- **Olhado:**
  - `fundamentos.md`, `revisao-claude-26-11.md` e `base.md`;
  - as falas de 22/11 (passos do K-011 e falas 12 a 14);
  - a proposta, a releitura e a comparação;
  - o `resultado.md` da limpeza;
  - a lista do K-127;
  - na releitura da Antigravity (27/11): conferência cruzada de `saida-K-004.md` contra `fundamentos.md`, `comparacao.md`, `comparacao.json`, `comparar_passo3.py`, `passo3-proposta.jsonl`, `passo3-releitura.jsonl`, `base.md`, `D-061.json`, `revisao-claude-26-11.md` e `limpeza/resultado.md`.
- **Fora:**
  - a conferência independente pelo Claude Code dos exemplos das habilidades (conferidos na proposta da Antigravity, ainda sem segunda leitura pela D-038);
  - alteração de código, esquemas, testes ou acervo;
  - os textos completos das referências lógicas;
  - o consumo desta conversa, que não foi medido: o esquema de log exige número, e não se grava 0.
