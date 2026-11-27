# K-004 · Reunião (abertura em 27/11/2026)

**Quem:** Vicente, Claude Code (Opus 5.5, esforço médio) e Antigravity, em diálogo sequencial (D-060, D-061). **Cartão:** K-004 em `Fazendo` desde 27/11; o K-011 fechou nesta abertura.
**Material de entrada:** `trilhas/planejamento/rodadas/2026-11-25_K-011/saida-K-004.md` (relida pela Antigravity em 27/11, com 6 notas na §5), `trilhas/planejamento/rodadas/2026-11-15_antes-do-K-004/passagem.md` (§5: o K-004 em sete etapas), `trilhas/planejamento/rodadas/2026-11-20_K-004/` (etapa 1, a limpeza, feita em 20/11), `trilhas/decisoes/D-058.json`, `D-059.json`, `D-061.json`.
**Regra desta trilha:** nada aqui é decisão. O que Vicente confirmar se grava como decisão no fim do bloco, pela `registrar-decisao`; até lá, só leitura e proposta. Nenhuma mudança em código, esquemas, testes ou acervo nesta abertura.

---

## 1. Abertura (feita em 27/11, pelo Claude Code)

- `git pull`: main em `bac3e57`, já em dia. `scripts/relatorio_dia.py` (relatorio-dia-0.4): 0 Entradas novas hoje (2.578 no total), 0 ambientes rodados hoje, `origin/rotinas` 19 commits à frente do main, 44 Faltas, 35 vácuos de busca, 22 links quebrados (0 novos).
- Quadro: K-011 → Concluído (27/11/2026); K-004 → Fazendo. `RETOMAR.md` com o topo no K-004. Esta trilha criada.

## 2. As 6 notas da Antigravity (`saida-K-004.md`, §5) — leitura do Claude Code

| Nota | Leitura | Por quê |
|---|---|---|
| 1. Insumo 112 e o viés do arquivo | **Concordo, com um reparo.** | O que ficar fora de "intervenção humana" entra como declaração do viés do arquivo (fund. 9; `base.md` l. 70). Mas o [ABERTO] em si é o alcance de uma regra da D-049, e o fundamento não o resolve: continua pedindo uma leitura de Vicente. Destino: fica, via "regra de Vicente"; o fund. 9 diz para onde vai o que ficar fora. |
| 2. Insumo 62 e a oralidade | **Divirjo em parte.** | O insumo 62 (`trilhas/insumos-planejamento.md`, l. 68) tem duas partes. (a) A oralidade **já gravada em acervo público** é porta aberta da fase 1 (§5.4, localizador `t=início,fim`); sem transcrição, o trecho vira Falta "não verificável por máquina" e a W, que se ancora na fala de quem pratica, fica Falta. Isso é problema da ferramenta na fase 1 e a declaração do viés não o resolve. (b) O áudio mandado por pessoas e a entrevista própria estão adiados (P48, D-009; Fundação l. 816 e 844) e vão ao K-008. Proponho partir o 62 nas duas partes. A pergunta 21 do §10 (l. 895) segue aberta. |
| 3. Insumos 58, 132, 135 e 139 | **Concordo.** | 58 se trata junto com o 140 (mesmo mecanismo, outra etapa), mantendo os dois números visíveis; 132 e 139 caminham com o 136 depois da decisão sobre o `orcamento.py`; 135 fica só pela parte "quando a vistoria roda sozinha". |
| 4. [ABERTO] 1 e o 5º lugar | **Concordo, e corrijo a minha posição inicial.** | Escrevi "no piloto, nenhuma Proposição ficou inconsistente" como se isso dissesse que a regra não é necessária. A nota mostra que esse número só mede o eixo 3 da Eτ; a tensão de identidade (código `CL-nnnn` fixo e a prática que muda) já está na cajuína e nenhum contador a capta. O zero não serve de argumento. |
| 5. As cinco divergências de via | **Concordo.** | Não há desacordo de fundo: falta a regra antes (D-038), e quem a aplica já está mapeado. |
| 6. A hipótese "pouco a resolver para sair do piloto" | **Concordo com a contagem, com uma ressalva de leitura.** | Os 30 que ficam são problemas para a ferramenta cumprir a promessa da fase 1 (D-058, item 2), não necessariamente para "sair do piloto", que já foi entregue em 14/11 (D-061). Quais dos 30 impedem a operação com IA em escala ou a escrita da Fundação é a pergunta do Bloco 4; só então a hipótese fica testada inteira. |

## 3. Conferência dos exemplos das habilidades (`saida-K-004.md`, §5, item 6; segunda leitura, D-038)

**Feita em 27/11, só leitura, sem mudar nada.** Olhado: as 15 pastas `.claude/skills/*/exemplos/`, quem as lê (`grep -n exemplos` em `scripts/`) e os nomes de outras CLB nelas e nos `SKILL.md`.

- **Confirma a Antigravity:** nenhum script lê os exemplos em execução. Só `scripts/rodar_testes.py` (os `casos.json` e `casos-rodada-b.json`) e `scripts/trava_testes.py` os usam, como casos de prova; `scripts/manutencao.py:272` só confere se a pasta existe; `scripts/validar_acervo.py:216` trata outra coisa (a faixa de IDs dos exemplos de esquema). As listas fechadas estão nos scripts e em `esquemas/triagem-fixa.json`, como a Antigravity situou.
- **Confirma o nome antigo de guia:** `triagem-juridica/exemplos/falta-conhecimento-tradicional.json` aponta `G-sisgen-cadastro-de-acesso` (l. 15). Já está no "Depois" do K-127.
- **Acréscimo 1 (para a reunião, não conserto):** o fundamento 10 diz que exemplo não entra em teste. Os casos das habilidades são de outra natureza: dados reais do piloto (`real-*`) e mutações que devem reprovar (`erro-*`). Convém a Fundação dizer essa diferença (exemplo que explica ≠ caso de prova com dado real), para o fundamento 10 não ser lido contra a suíte.
- **Acréscimo 2 (para a reunião, não conserto):** dois textos que o agente lê em execução trazem nomes de outras CLB como ilustração: `.claude/skills/triagem-juridica/SKILL.md:45` ("vinho de caju, caoi, mocororó e outras", lista aberta) e `.claude/skills/consulta/SKILL.md:55` (o caso `cauim-totais.json`, real, de 15/10). Nenhum vira lista fechada; ficam como viés de exemplo a declarar ou a reescrever sem nome próprio, conforme a reunião decidir.

## 4. Pauta proposta em blocos (proposta do Claude Code; a ordem é de Vicente)

A ordem põe primeiro o que muda regra, porque a regra muda o destino dos insumos (D-038: a ferramenta decide os itens pela regra; Vicente decide as regras). Cada bloco fecha com a essência devolvida a Vicente, a confirmação e, se houver regra nova, a decisão gravada (uma por bloco, para nada ficar só no chat). **Bastão à Antigravity** onde está marcado ⇄.

| Bloco | Assunto | Quem faz o quê | Modelo e esforço |
|---|---|---|---|
| 1 | **Os fundamentos em aberto:** os 3 [ABERTO] da D-061 e o gatilho "inconsistente" (insumos 143 e 144) | Claude Code apresenta; Vicente delibera. ⇄ Antigravity relê o texto da decisão antes de gravar | Claude Opus 5.5 médio; Antigravity médio |
| 2 | **As regras que só Vicente dá:** as 6 divergências que pedem regra (77, 87, 97, 112, 123, 128), o 62 partido em dois, o [ABERTO] da D-049 (o 112), se arrumar a casa (94, 135) é parte da promessa, e o [ABERTO] da D-058 (a liberação espera a fila montada ou resolvida) | ⇄ Antigravity faz o contraponto de cada leitura **antes** de ir a Vicente (quem lê não aprova) | as duas, médio |
| 3 | **A medida:** a descontinuação formal do `orcamento.py` com os 6 casos da trava (fala 14; D-059), os logs com 0 que querem dizer "não medido" (mexe num esquema) e os insumos 132, 136 e 139 | Claude Code prepara a lista dos 6 casos e o que muda; Vicente confirma caso a caso (`trava_testes.py --confirmar` só depois). ⇄ Antigravity relê a lista contra a trava | Claude Opus 5.5 médio |
| 4 | **A fila dos 30 e as divergências restantes:** destino por família, com 58 e 135 e as 11 de fundamento, via ou junção; o que vai ao K-127, o que espera a operação com IA (70, 126, 128, 129, 132); a realocação dos alvos do K-126 (91, 131, nota do 99); quais dos 30 impedem a escrita da Fundação | Quem não propôs relê (D-038): se o Claude Code propõe, ⇄ a Antigravity relê às cegas, e a comparação é por script, como no K-011 | Claude Opus 5.5 médio; comparação sem IA |
| 5 | **Os estacionados:** K-125, K-115b, K-115c (o K-115c tem as habilidades da escrita da Fundação, 49% dos tokens de agentes do piloto) | Claude Code traz o estado salvo; Vicente decide | Claude Opus 5.5 médio |
| 6 | **A 3ª passada do K-005:** os números da D-038 e do registro calibrados com o que se mediu (e o piso dito onde não há medida: insumos 136, 138, 139) | ⇄ Antigravity relê os números | Claude Opus 5.5 médio |
| 7 | **O K-006:** o agente de melhorias e as três habilidades (consolidar, medir-custo, preparar-tarefa) | Claude Code apresenta o desenho; ⇄ Antigravity contraponto | as duas, médio |
| 8 | **Cartões novos, de uma vez (D-046),** e a volta do K-127 | Claude Code monta o quadro; ⇄ Antigravity relê | Claude Opus 5.5 médio |
| 9 | **Escrever a Fundação** (V-01 a V-39 de `proxima-versao.md`, os 12 fundamentos, as 9 referências da `base.md` §7 conferidas antes) | redator escreve por grupo de seções; ⇄ Antigravity verifica como harness diferente (D-026) | redator Opus 5.5 médio; auditor Sonnet 5.5 alto |
| 10 | **Conferir e fechar:** `checar_fundacao.py`, `comparar_anexos.py`, aprovação de Vicente | script; Vicente aprova | sem IA, e Opus 5.5 médio para o relatório |

Os blocos 1 a 8 são conversa de planejamento (cerca de 2 a 6 pp cada, sem agentes, pela medida da `passagem.md` §5). O bloco 9 é o único com agentes em escala (a v0.2 custou 1.227.342 tokens de agentes); antes dele, a conta de quantos e quanto (regra global, item 3).

## 5. Bloco 1 — os fundamentos em aberto (para a deliberação de Vicente)

Apresentado a Vicente em 27/11. As respostas e a essência confirmada entram abaixo quando vierem. Nada aqui está decidido.

**1.1 · Lógica na voz própria: regra explícita ou declaração do quadro ([ABERTO] i da D-061).**
- *Já decidido:* a ferramenta não ganha lógica nova (fund. 5); na voz própria, uma lógica não clássica pode valer como regra, declarada como viés (fund. 6); μ e λ só descrevem linhagens (fund. 7).
- *Leitura das duas LLMs:* declarar o quadro agora, na Fundação (os cinco lugares da `base.md` §4 e a família de da Costa como referência, conferida antes de entrar); virar regra explícita só onde a voz própria concluir algo e um caso real pedir.
- *O que a nota 4 da Antigravity muda:* o caso real já existe, a identidade da cajuína no tempo (código fixo, prática que muda). Proposta: a declaração nomeia esse caso como o primeiro a observar; a regra, se vier, trata de como a ficha diz "a mesma CLB" através do tempo. Nada muda no código agora.
- *Para compreender (pergunta a Vicente):* quando o sistema falar na voz própria (ficha, wiki), que tipo de afirmação te preocupa que saia sem regra?

**1.2 · Vieses no wiki inteiro ([ABERTO] ii).**
- *Leitura das duas LLMs:* uma página fixa com os vieses estruturais (o lógico, o da língua, o do quadro de coordenadas, o da lei como definição, o da contagem, o do que é uma CLB, o da identidade, o da máquina e o de valor; `base.md` §5) e um bloco gerado por script a partir do alcance dos logs, que muda quando entra CLB nova.
- *Consequência para a pauta:* a página fixa é texto (vai ao Bloco 9); o bloco gerado é código novo (vira cartão no Bloco 8).
- *Para compreender:* quem lê o wiki precisa encontrar "de onde se vê" uma vez, numa página, ou ao lado de cada página de CLB?

**1.3 · Viés no campo de ação ([ABERTO] iii).**
- *Leitura das duas LLMs:* o carimbo mínimo basta (link da ficha, Faltas, data, como citar, aviso legal). Uma nota curta de viés só quando o artefato sustenta decisão de poder (por exemplo, um pedido de registro) e um viés muda o que ele recomenda (princípio 4).
- *Para compreender:* para quem você imagina os primeiros artefatos do campo de ação, e algum deles sustentaria decisão de poder?

**1.4 · O gatilho "inconsistente" (insumos 143 e 144).**
- *Como está:* `scripts/fila_curadoria.py:58` abre o cartão de conflito quando uma Proposição fica "inconsistente" e chama Vicente para conferir a nossa leitura das Evidências, nunca a prática (D-037, D-038).
- *Leitura das duas LLMs:* é gatilho para reler, não veredito (fund. 7). Proposta: fica como está no código; a Fundação diz que o estado vem da descrição das linhagens e só chama a releitura; o 143 se junta ao 144 e os dois se dissolvem no texto do fund. 7 e do 6.
- *Para compreender:* esta leitura bate com o que você quis dizer ao trazer o 143?

**Ao fechar o bloco:** a essência devolvida a Vicente; com a confirmação, uma decisão só (pela `registrar-decisao`) que fecha os três [ABERTO] da D-061 e o destino de 143 e 144; ⇄ a Antigravity relê o texto antes de gravar (D-038).

## 6. Depois (sem explorar, D-035)

- Acréscimos 1 e 2 da seção 3 (exemplos × casos de prova; nomes de CLB em `SKILL.md`): levar ao bloco 2 ou ao 9, conforme a ordem.
