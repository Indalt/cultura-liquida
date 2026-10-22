---
name: executar-brief
description: Conduz um brief de execução do projeto Cultura Líquida passo a passo, um cartão do quadro por vez (retomada pelo quadro, conta do orçamento, delegação a um agente por vez, log, checklist, insumos, commit e push, paradas e relatório de uma tela). Use ao abrir cada conversa de trabalho e a cada passo de um cartão autorizado por Vicente.
---

# executar-brief

**Versão do harness:** 0.1.1 · **Quem usa:** curador (sessão principal) · **Rodada:** A

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
2. **Retomada (brief, seção 1):** `git pull`, `git log --oneline -10`, `git status --short`, `git remote -v`, `gh repo view Indalt/cultura-liquida --json name,visibility || true`. Leia o quadro e o estado do planejamento; pegue o cartão autorizado, na ordem do quadro, e **mova-o para Fazendo**. Leia o checklist do piloto; rode `scripts/rodar_testes.py` (a partir do bloco 5, `scripts/relatorio_dia.py`). Pule o que já foi feito; nunca crie um segundo repositório.
3. **Registre** no checklist a autorização e o percentual de uso informado ("não informado" se vier em branco).
4. **Para cada passo:**
   1. Se o passo usa agente: rode `python scripts/orcamento.py --teto 300000 --medidos <consumo de cada agente já rodado na semana> --estimativa <N>` (semana de segunda a domingo, pela data do log; N = a última medida do mesmo agente com a mesma habilidade, ou 60 mil). Código 1 → parada (caso b).
   2. Delegue a **um** agente do projeto por vez, só com os tipos de `.claude/agents/` (insumo 7): fato trazido por outro tipo de agente ou outro modelo entra como "não conferido" até a reconferência. O pedido traz a entrada (arquivos e faixas de linhas), a habilidade, o critério de parada, o esquema da saída e o **teto de chamadas contado como o harness conta** (cada ferramenta e cada pedido HTTP, mesmo agrupados num só comando), com margem.
   3. Valide a saída do agente com `scripts/validar.py <esquema>` e grave-a no lugar indicado.
   4. Grave o log completo **por arquivo**: monte o JSON com a ferramenta Write (formato `esquemas/log.schema.json`, com `alcance`) e rode `python scripts/registrar_log.py <arquivo>`, sem heredoc. Os `tokens` e as `chamadas` são os do retorno do Agent, o número oficial, nunca a soma pelo transcript (insumo 5).
   5. Atualize o checklist.
   6. Anote os insumos novos do lote com a habilidade `registrar-melhoria` (K-103).
   7. `python scripts/procurar_dado_pessoal.py --git`; commit (mensagem em português, linha de atribuição da sessão) e **push**.
5. **Relatório de cada lote:** uma tela (o que entrou, o que ficou em quarentena, as Faltas novas), gravada na trilha como relatório, **sem pedir aprovação** (ritual da l. 512 relido pela D-037; A-02). O que, no conteúdo, precisa de Vicente vira cartão de conflito ou de Falta jurídica a liberar na frente de operação (D-037, diretriz 1); o resto vai à `registrar-melhoria`.
6. **Paradas** (só quatro): (a) decisão nova; (b) orçamento; (c) bloqueio que só Vicente resolve; (d) conflito com decisão vigente. Fato não conferido **não** para: marque "não conferido" e siga. Comentário novo de Vicente: use `registrar-decisao`.
7. **Fim do cartão:** checklist, quadro (o cartão vai a Concluído, ou de volta a A fazer com o estado salvo e o motivo; D-036, diretriz 2), log do curador, commit e push; relatório de uma tela (o que foi feito, consumo, o que ficou "não conferido", próximos passos).

## Regras herdadas
- **Nível:** todo fato novo com URL e nível; o curador não pesquisa na web, delega.
- **Essência:** decisões pela essência confirmada; não reconfirmar o que a seção 2 do brief já traz. A ferramenta decide os itens pela regra; Vicente decide as regras (D-038).
- **Dado pessoal:** nada de terceiros no Git; rodar a busca antes de cada commit.
- **Anti-robô:** nunca contornar.
- **Falta dita:** o que não se fez ou não se conferiu é dito no relatório.

## Teto e custo
Teto semanal para subagentes: 300 mil tokens (brief, seção 0; D-023), somando o consumo que o retorno de cada Agent informa; folga mínima de 2× o maior lote medido. Para planejar: cerca de 60 mil por agente Sonnet com teto. As rodadas de planejamento têm teto próprio e ficam fora desta soma até o K-002 (A-13). A escrita da sessão principal não entra nessa conta, mas é medida pelo uso da conta que Vicente lê.

## Critério de parada
Fim do cartão autorizado, ou um dos quatro casos de parada. Sempre com o estado salvo (checklist, quadro, commit, push).

## O que não faz
Não lança agentes em paralelo, não usa Workflow sem pedido, não reabre decisão, não executa cartão não autorizado, não confere o próprio trabalho como verificação final, não pede aprovação de rotina do conteúdo da base.

## Campos do log
`agente: "curador"`, `habilidade: "executar-brief"`, `entrada_ref` (cartão, brief e bloco), `acoes` (passos), `resultados` (commits), `decisoes` (o que foi feito, pulado ou deixado "não conferido", com motivo), `tokens` e `chamadas` dos agentes da conversa, `erros`, `alcance` (o que se olhou e o que ficou fora). O `id` da Execução é dado pelo `registrar_log.py`.

## Exemplos e validador
- **Conta da semana com o teto de 300 mil:** semana sem agente medido, estimativa 60.000 → pode (`scripts/orcamento.py`, passa).
- **Conta real da janela 1** (teto de 600 mil da v0.2, antes do C2): consumido 81.852, estimativa 60.000 → folga 518.148 ≥ 163.704 → **pode**.
- **Conta que manda parar:** consumido 500.000 (lotes de 300 e 200 mil) → folga 100.000 < 2 × 300.000 → **parar** (reprova como esperado).
- **Log real do teste do Bloco 2.5** ([exemplos/log-teste-auditor.json](exemplos/log-teste-auditor.json)) passa no esquema; um log com e-mail de terceiro ([exemplos/erro-log-com-email.json](exemplos/erro-log-com-email.json)) é recusado pelo `registrar_log.py --simular`.
- **Log sem alcance** ([exemplos/erro-log-sem-alcance.json](exemplos/erro-log-sem-alcance.json)) é recusado pelo `registrar_log.py`; log de agente de workflow com tokens nulos e sem o motivo reprova, com o motivo passa; log de script sem alcance reprova, com alcance passa; decisão automática sem a versão da regra reprova; os logs antigos seguem válidos.
- Casos: [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.1 (22/10/2026, K-101): retomada pelo quadro e pelo estado do planejamento, com o cartão movido no começo e no fim (D-036, diretriz 2; A-01); entrada no brief de execuções e no checklist do piloto; conta com `--teto 300000` por semana; teto de chamadas contado como o harness conta; log por arquivo, sem heredoc; tokens do retorno do Agent, nunca pelo transcript (insumo 5); Agent só com os tipos de `.claude/agents/` (insumo 7); relatório de lote sem aprovação (D-037; A-02); insumos pela `registrar-melhoria` (K-103; insumo 27); casos novos do esquema de log.
- 0.1.0 (16/10/2026): primeira versão, a partir das janelas 1 e 2.
