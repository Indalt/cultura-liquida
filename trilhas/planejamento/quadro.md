# Quadro das três frentes (D-036)

Lógica kanban: **A fazer → Fazendo → Concluído**. Cada sessão pega **um** cartão e o leva até "Concluído", ou o devolve a "A fazer" com o estado salvo e o motivo. Na operação, quem move os cartões são os agentes.

- **Formato do cartão:** ID, título, origem (decisão ou insumo) e destino (aonde se quer chegar).
- **Onde o quadro mora:** neste arquivo, até o K-001 decidir se ele migra para as Issues e o Projects do GitHub.

## Planejamento de melhorias

| Coluna | Cartão | Origem | Destino |
|---|---|---|---|
| A fazer | **K-001** Reunir tudo nas três frentes: mapear a Fundação v0.2, o roteiro, o brief de execuções, os insumos 1 a 14 e as decisões D-001 a D-037 em planejamento, desenvolvimento e operação; povoar este quadro; dizer o que vai para a próxima versão da Fundação | D-036 | um mapa das três frentes, este quadro completo e a lista do que entra na próxima versão |
| A fazer | **K-002** Escolher a IA da operação (assinatura ou API com teto mensal) e a cadência e o teto do planejamento | insumos 12 e 13 | a operação sem disputar a cota de Vicente; rodadas com custo previsto |
| Concluído | **K-000** Registrar as D-036 e D-037 e criar o quadro e o estado do planejamento (21/10/2026) | D-036, D-037 | este arquivo e `estado-planejamento.md` |

## Desenvolvimento

| Coluna | Cartão | Origem | Destino |
|---|---|---|---|
| A fazer | **K-101** Bloco 1 do brief de execuções: harness e operação. Aguarda a autorização de Vicente | brief de execuções | o harness pronto para a coleta do piloto |
| A fazer | **K-102** Script de menções incidentais. Ordem a definir no K-001 | D-037 | menções a outras CLB viram ligação no grafo e cartão de baixa prioridade |
| A fazer | **K-103** Habilidade `registrar-melhoria`. Ordem a definir no K-001 | D-036; insumo 10 | toda sessão e toda rotina anota insumos num formato fixo |

## Operação

| Coluna | Cartão | Origem | Destino |
|---|---|---|---|
| — | ainda vazia. A operação sem sessão começa com o Bloco 10. Depois disso, os agentes abrem aqui os cartões de conflito, de Falta a liberar, de CLB candidata e, na fase 2, de sugestão | D-036, D-037 | a ferramenta trabalhando sozinha, e Vicente chamado só por conflito |
