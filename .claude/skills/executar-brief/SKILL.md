---
name: executar-brief
description: Conduz um brief de execução do projeto Cultura Líquida passo a passo (retomada, conta do orçamento, delegação a um agente por vez, log, checklist, commit e push, paradas e relatório de uma tela). Use ao abrir cada janela de trabalho e a cada passo de um bloco autorizado por Vicente.
---

# executar-brief

**Versão do harness:** 0.1.0 · **Quem usa:** curador (sessão principal) · **Rodada:** A

## Objetivo
Executar o que Vicente autorizou, sem parar para aprovar o já decidido (D-028), medindo e parando antes de acabar (D-023), com tudo registrado e no GitHub.

## Quando usar / quando não usar
- **Usar:** na primeira mensagem de cada janela e em cada passo dos blocos autorizados.
- **Não usar:** para decidir o que o brief não cobre (isso é parada, caso a); para executar bloco não autorizado (memória "plano não é execução").

## Entradas e saídas
- **Entrada:** o brief (`trilhas/2026-10-15_pesquisa/clb-execucao-v0.2-brief.md` ou o vigente), o checklist (`trilhas/2026-10-16_execucao-v0.2.md`), a mensagem de autorização de Vicente (blocos e percentual de uso).
- **Saída:** passos feitos; checklist atualizado (passo, estado, consumo, modelo e esforço, observação); logs em `trilhas/logs/`; commits e push; relatório de uma tela.

## Passos
1. **Modelo:** confira o ID da sessão. Se não for o indicado (hoje `claude-opus-5-5`), avise e pare.
2. **Retomada:** leia o checklist; rode `git log --oneline`, `git remote -v`, `gh repo view Indalt/cultura-liquida --json name,visibility || true`. Pule o que já foi feito; nunca crie um segundo repositório.
3. **Registre** no checklist a autorização e o percentual de uso informado ("não informado" se vier em branco).
4. **Para cada passo:**
   1. Se o passo usa agente: rode `python scripts/orcamento.py --teto 600000 --medidos <consumos da janela> --estimativa <est>`. Código 1 → parada (caso b).
   2. Delegue a **um** agente do projeto por vez, com o teto de chamadas no pedido e só as faixas de linhas necessárias.
   3. Valide a saída do agente com `scripts/validar.py <esquema>` e grave-a no lugar indicado.
   4. Grave o log completo: monte o JSON (formato `esquemas/log.schema.json`, com `tokens` e `chamadas` do retorno do Agent) e rode `python scripts/registrar_log.py <arquivo>`.
   5. Atualize o checklist.
   6. `python scripts/procurar_dado_pessoal.py --git`; commit (mensagem em português, linha de atribuição da sessão) e **push**.
5. **Paradas** (só quatro): (a) decisão nova; (b) orçamento; (c) bloqueio que só Vicente resolve; (d) conflito com decisão vigente. Fato não conferido **não** para: marque "não conferido" e siga. Comentário novo de Vicente: use `registrar-decisao`.
6. **Fim do bloco:** checklist, commit e push; relatório de uma tela (o que foi feito, consumo, o que ficou "não conferido", próximos passos).

## Regras herdadas
- **Nível:** todo fato novo com URL e nível; o curador não pesquisa na web, delega.
- **Essência:** decisões pela essência confirmada; não reconfirmar o que a seção 2 do brief já traz.
- **Dado pessoal:** nada de terceiros no Git; rodar a busca antes de cada commit.
- **Anti-robô:** nunca contornar.
- **Falta dita:** o que não se fez ou não se conferiu é dito no relatório.

## Teto e custo
Teto da janela para subagentes: 600 mil tokens; folga mínima de 2× o maior lote medido. Para planejar: cerca de 60 mil por agente Sonnet com teto. A escrita da sessão principal não entra nessa conta, por isso as paradas obrigatórias por bloco.

## Critério de parada
Fim dos blocos autorizados, ou um dos quatro casos de parada. Sempre com o estado salvo (checklist, commit, push).

## O que não faz
Não lança agentes em paralelo, não usa Workflow sem pedido, não reabre decisão, não executa bloco não autorizado, não confere o próprio trabalho como verificação final.

## Campos do log
`agente: "curador"`, `habilidade: "executar-brief"`, `entrada_ref` (brief e bloco), `acoes` (passos), `resultados` (commits), `decisoes` (o que foi feito, pulado ou deixado "não conferido", com motivo), `tokens` e `chamadas` dos agentes da janela, `erros`, `alcance` (o que se olhou e o que ficou fora).

## Exemplos e validador
- **Conta real da janela 1** (antes do C2): consumido 81.852, maior lote 81.852, estimativa 60.000 → folga 518.148 ≥ 163.704 → **pode** (`scripts/orcamento.py`, passa).
- **Conta que manda parar:** consumido 500.000 (lotes de 300 e 200 mil) → folga 100.000 < 2 × 300.000 → **parar** (reprova como esperado).
- **Log real do teste do Bloco 2.5** ([exemplos/log-teste-auditor.json](exemplos/log-teste-auditor.json)) passa no esquema; um log com e-mail de terceiro ([exemplos/erro-log-com-email.json](exemplos/erro-log-com-email.json)) é recusado pelo `registrar_log.py --simular`.
- Casos: [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.0 (16/10/2026): primeira versão, a partir das janelas 1 e 2.
