---
name: executar-brief
description: Conduz um brief de execução do projeto Cultura Líquida passo a passo, um cartão do quadro por vez (retomada pelo quadro, conta do orçamento, delegação a um agente por vez, log, checklist, insumos, commit e push, paradas e relatório de uma tela). Use ao abrir cada conversa de trabalho e a cada passo de um cartão autorizado por Vicente.
---

# executar-brief

**Versão do harness:** 0.2.0 · **Quem usa:** curador (sessão principal) · **Rodada:** A

## Objetivo
Executar o cartão que Vicente autorizou, sem parar para aprovar o já decidido (D-028), medindo e parando antes de acabar (D-023), com tudo registrado e no GitHub.

## Quando usar / quando não usar
- **Usar:** na primeira mensagem de cada conversa de trabalho e em cada passo do cartão autorizado.
- **Não usar:** para decidir o que o brief não cobre (isso é parada, caso a); para executar cartão não autorizado (memória "plano não é execução").

## Entradas e saídas
- **Entrada:** o quadro (`trilhas/planejamento/quadro.md`) e o estado do planejamento (`trilhas/planejamento/estado-planejamento.md`); o brief de execuções (`trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md`: os quadros de ajustes do início, as seções 0 e 4 e o bloco do cartão); o checklist do piloto (`trilhas/2026-10-17_execucao-piloto.md`); a mensagem de autorização de Vicente (cartão e percentual de uso).
- **Saída:** passos feitos; checklist atualizado (passo, estado, consumo, modelo e esforço, observação); logs em `trilhas/logs/`; insumos novos; o cartão movido no quadro; commits e push; relatório de uma tela.

## Passos
1. **Modelo:** confira o ID da sessão. Se não for o indicado (hoje `claude-opus-5-5`, esforço médio), avise e pare.
2. **Retomada (brief, seção 1):** `git pull`, `git log --oneline -10`, `git status --short`, `git remote -v`, `gh repo view Indalt/cultura-liquida --json name,visibility || true`. Leia o quadro e o estado do planejamento; pegue o cartão autorizado, na ordem do quadro, e **mova-o para Fazendo**. Leia o checklist do piloto (com a tabela "Semana da conta" no fim); rode `scripts/rodar_testes.py` (a partir do bloco 5, `scripts/relatorio_dia.py`, que avisa se o gancho de pre-commit está desligado nesta cópia: `git config core.hooksPath .githooks`; insumo 35). Pule o que já foi feito; nunca crie um segundo repositório.
3. **Registre** no checklist a autorização e o uso informado (semanal e da janela de 5 h; "não informado" se vier em branco), e abra a linha da conversa na tabela "Semana da conta" (semana, frente, cartão, A0; D-040). A leitura de abertura fecha a linha da conversa anterior (A1 e pp), se ela ficou "a informar". Com a janela de 5 h acima de 70%, só um lote e a conversa fecha.
4. **Para cada passo:**
   1. Se o passo usa agente: rode `python scripts/orcamento.py --a0 <uso semanal ao abrir> --janela <uso da janela de 5 h> --agente <agente> --habilidade <habilidade> --medidos-conversa <tokens de cada agente já rodado nesta conversa>` (D-040). O script lê o que o desenvolvimento já usou na semana da conta pela tabela do checklist e a estimativa nos logs (a última medida do mesmo agente com a mesma habilidade; sem medida, 96.520). Código 1 → parada (caso b). No planejamento, `--frente planejamento`.
   2. Delegue a **um** agente do projeto por vez, só com os tipos de `.claude/agents/` (insumo 7): fato trazido por outro tipo de agente ou outro modelo entra como "não conferido" até a reconferência. O pedido traz a entrada (arquivos e faixas de linhas), a habilidade, o critério de parada, o esquema da saída e o **teto de chamadas contado como o harness conta** e, a agente sem Write, a pasta de saída com o `juntar_saida.py` e a validação por arquivo (insumos 29, 71, 74) (cada ferramenta e cada pedido HTTP, mesmo agrupados num só comando), com margem.
   3. Valide a saída do agente com `scripts/validar.py <esquema>` e grave-a no lugar indicado.
   4. Grave o log completo **por arquivo**: monte o JSON com a ferramenta Write (formato `esquemas/log.schema.json`, com `alcance`) e rode `python scripts/registrar_log.py <arquivo>`, sem heredoc. Os `tokens` e as `chamadas` são os do retorno do Agent, o número oficial, nunca a soma pelo transcript (insumo 5).
   5. Atualize o checklist (o passo e a linha da conversa: tokens de agentes e chamadas).
   6. Anote os insumos novos do lote com a habilidade `registrar-melhoria` (K-103).
   7. `python scripts/procurar_dado_pessoal.py --git`; commit (mensagem em português, linha de atribuição da sessão) e **push**.
5. **Relatório de cada lote:** uma tela (o que entrou, o que ficou em quarentena, as Faltas novas), gravada na trilha como relatório, **sem pedir aprovação** (ritual da l. 512 relido pela D-037; A-02). O que, no conteúdo, precisa de Vicente vira cartão de conflito ou de Falta jurídica a liberar na frente de operação (D-037, diretriz 1); o resto vai à `registrar-melhoria`.
6. **Paradas** (só quatro): (a) decisão nova; (b) orçamento; (c) bloqueio que só Vicente resolve; (d) conflito com decisão vigente. Fato não conferido **não** para: marque "não conferido" e siga. Comentário novo de Vicente: use `registrar-decisao`.
7. **Fim do cartão:** checklist (a linha da conversa fica com A1 "a informar" até Vicente dar o uso), quadro (o cartão vai a Concluído, ou de volta a A fazer com o estado salvo e o motivo; D-036, diretriz 2), log do curador, commit e push; relatório de uma tela (o que foi feito, consumo, o que ficou "não conferido", próximos passos).

## Regras herdadas
- **Nível:** todo fato novo com URL e nível; o curador não pesquisa na web, delega.
- **Essência:** decisões pela essência confirmada; não reconfirmar o que a seção 2 do brief já traz. A ferramenta decide os itens pela regra; Vicente decide as regras (D-038).
- **Dado pessoal:** nada de terceiros no Git; rodar a busca antes de cada commit.
- **Anti-robô:** nunca contornar.
- **Falta dita:** o que não se fez ou não se conferiu é dito no relatório.

## Teto e custo
Em pontos percentuais (pp) do limite semanal da conta (D-040; brief, seção 0; registro, `orcamento`): o projeto até 60 pp por semana, somadas as três frentes; o desenvolvimento até 50; o planejamento o resto; a conta nunca acima de 90%. A folga da conversa é H = o menor entre (50 − o desenvolvimento já usado na semana), (60 − o projeto já usado) e (90 − A0); abre-se o lote se 2 + 1,6 × (tokens já rodados na conversa ÷ 100 mil) + 1,6 × (estimativa ÷ 100 mil) ≤ H, sem folga de 2× nem margem: a conversa não para antes do teto. A guarda é não perder trabalho: commit e push a cada lote. Os tokens de agentes seguem medidos e somados no checklist.

## Critério de parada
Fim do cartão autorizado, ou um dos quatro casos de parada. Sempre com o estado salvo (checklist, quadro, commit, push).

## O que não faz
Não lança agentes em paralelo, não usa Workflow sem pedido, não reabre decisão, não executa cartão não autorizado, não confere o próprio trabalho como verificação final, não pede aprovação de rotina do conteúdo da base.

## Campos do log
`agente: "curador"`, `habilidade: "executar-brief"`, `entrada_ref` (cartão, brief e bloco), `acoes` (passos), `resultados` (commits), `decisoes` (o que foi feito, pulado ou deixado "não conferido", com motivo), `tokens` e `chamadas` dos agentes da conversa, `erros`, `alcance` (o que se olhou e o que ficou fora). O `id` da Execução é dado pelo `registrar_log.py`.

## Exemplos e validador
- **Conta do exemplo do K-105 (D-040):** A0 = 37%, desenvolvimento já com 8 pp, lote sem medida (96.520) → H = 23; 2 + 1,54 ≤ 23 → **pode**.
- **Lote que não cabe:** A0 = 58%, lote de 159.897 → H = 2; 2 + 2,56 > 2 → **parar** (reprova como esperado). Com A0 = 89%, a linha da conta dá H = 1 → parar; com a janela de 5 h em 75%, o script avisa "só um lote".
- **A tabela da semana da conta e os logs:** o script soma só a semana da última linha, tira as linhas "fora do projeto" e acha a última medida do agente com a habilidade (`testes/orcamento/`).
- **Log real do teste do Bloco 2.5** ([exemplos/log-teste-auditor.json](exemplos/log-teste-auditor.json)) passa no esquema; um log com e-mail de terceiro ([exemplos/erro-log-com-email.json](exemplos/erro-log-com-email.json)) é recusado pelo `registrar_log.py --simular`.
- **Log sem alcance** ([exemplos/erro-log-sem-alcance.json](exemplos/erro-log-sem-alcance.json)) é recusado pelo `registrar_log.py`; log de agente de workflow com tokens nulos e sem o motivo reprova, com o motivo passa; log de script sem alcance reprova, com alcance passa; decisão automática sem a versão da regra reprova; os logs antigos seguem válidos.
- Casos: [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.2.0 (30/10/2026, K-111): gancho de pre-commit em cada cópia, conferido na retomada (insumo 35); nomes prováveis e `--clb` na gravação (insumos 76, 92); pedido a agente sem Write com o `juntar_saida.py` (insumos 29, 71, 74).
- 0.1.2 (23/10/2026, K-123): a conta da conversa em pp da conta (D-040), com o `orcamento.py` novo (A0, janela de 5 h, tabela "Semana da conta" do checklist, estimativa pelos logs com 96.520 sem medida, sem a folga de 2×); a linha da conversa no checklist; os casos da conta trocados.
- 0.1.1 (22/10/2026, K-101): retomada pelo quadro e pelo estado do planejamento, com o cartão movido no começo e no fim (D-036, diretriz 2; A-01); entrada no brief de execuções e no checklist do piloto; conta com `--teto 300000` por semana; teto de chamadas contado como o harness conta; log por arquivo, sem heredoc; tokens do retorno do Agent, nunca pelo transcript (insumo 5); Agent só com os tipos de `.claude/agents/` (insumo 7); relatório de lote sem aprovação (D-037; A-02); insumos pela `registrar-melhoria` (K-103; insumo 27); casos novos do esquema de log.
- 0.1.0 (16/10/2026): primeira versão, a partir das janelas 1 e 2.
