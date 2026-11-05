# Entender o K-002 (para leitura de Vicente; não decide nada)

Conversa de planejamento de 05/11/2026. Junta o que o plano já diz sobre o cartão K-002, para começar a entendê-lo antes de decidir. Nenhum agente foi usado; o que não foi conferido está dito.

## O que é e por que agora

O K-002 escolhe como a operação vai rodar quando a ferramenta trabalhar sozinha e quanto ela pode gastar (quadro, linha do K-002; D-040). Ele vem antes do K-113, a rotina com IA: sem o K-002, o K-113 não começa.

Agora há tempo para entender sem pressa. Os 7 dias de relatório do K-112 começam em 06/11, e o K-114 e o K-115 vêm antes do K-113.

## As quatro perguntas do cartão

### 1. Que IA trata as Entradas novas na operação (insumo 12)
- **Hoje:** nenhuma. A rotina sem IA traz as Entradas novas (5 na primeira rodada, em 05/11), e elas esperam uma conversa de trabalho para virar Evidência, ficha e grafo (brief, "Depois do bloco 14").
- **Opção A: a rotina do Claude Code, na sua assinatura.** Roda na nuvem da Anthropic, na sua conta, e gasta a mesma cota semanal das conversas (brief, seção 3b). Pelo brief:
  - o intervalo mínimo entre rodadas é de 1 hora;
  - a rede só alcança os domínios liberados;
  - cada rodada deixa uma proposta numa ramificação `claude/`.

  Não conferido: se o seu plano da conta tem rotinas e quanto cada rodada gasta.
- **Opção B: a API, com teto mensal em dinheiro.** Não disputa a sua cota, mas pede pagamento e um fornecedor nomeado por decisão (D-033). A D-049 trata de fontes e não decide isto.
- **O que ajuda a escolher:**
  - quantas Entradas novas chegam por semana (os 7 dias do K-112 mostram);
  - quanto gasta a rotina de teste do K-113 (bloco 10b).

### 2. A configuração de cada frente (insumo 19; mapa das três frentes, A-12)
- **Desenvolvimento:** Opus 5.5 com esforço médio, e os subagentes em Sonnet 5.5 com esforço alto (D-027; `CLAUDE.md`). Está fixada.
- **Planejamento:** Opus 5.5 com esforço máximo e ultracode. Repete o jeito como a v0.2 foi feita, e nenhuma decisão a fixa.
- **Operação:** a definir. O K-115 diz qual é o modelo mais barato que passa em cada habilidade.
- **Dado de 05/11:** esta conversa de planejamento gastou uns 6 pp em duas revisões independentes (5 agentes), que acharam erros reais antes de gravar a D-049.

### 3. A cadência e o teto do planejamento (insumos 8, 13 e 37; mapa, A-13; D-040)
- **Quando há rodada:** quando os insumos se acumulam ou em datas fixas? (insumo 13)
- **Teto:** pela D-040, o planejamento fica com o que sobra dos 60 pp do projeto, e o desenvolvimento usa até 50.
- **Medidas:**
  - K-001: 8 pp. K-003: 11 pp. Fechamento do K-003: 6 pp (insumo 37).
  - A rodada de replanejamento de outubro gastou 57% dos tokens de agentes da semana (insumo 8).

### 4. O teto de manutenção (D-040)
Do fim do K-113 em diante, os 60 pp por semana do piloto dão lugar a um teto de manutenção. Ele depende das perguntas 1 (quanto gasta a IA da operação) e 3 (quanto gasta o planejamento). É também a pergunta 16 do §10 da Fundação: "como você quer distribuir o consumo quando houver rotinas na nuvem?"

## Junto com as quatro
- **Como medir (insumos 15, 16 e 38):**
  - o Workflow e o Agent contam tokens de modos diferentes: em 05/11, o Workflow informou 360 mil, e os transcritos dos agentes somam 402 mil;
  - a estimativa de cada lote deve sair dos logs, por script;
  - o uso da conta só existe quando você o informa.
- **O lote semanal de Entradas (insumo 24):** entre o fim do piloto e a IA ligada, nenhum cartão trata as Entradas novas.
- **A junção da proposta da rotina com IA (insumo 20):**
  - a D-048 resolveu a da camada 1: o portão junta sem esperar você;
  - a da camada 2 vem no K-113;
  - a proteção do `main`, que recusou a primeira junção do K-112, é o mesmo obstáculo ali.
- **Pergunta 10 do §10:** "Se a IA saísse de cena, com que ferramentas você se sentiria à vontade para manter o sistema?" Ela pesa na escolha da IA da operação.

## Perguntas para entender (sem escolher ainda)
- O que você espera que a operação faça sozinha numa semana comum, depois do piloto?
- Que parte da sua cota semanal você imagina para a ferramenta, e que parte para você?
- Se a IA saísse de cena, com que ferramentas você se sentiria à vontade para manter o sistema (pergunta 10)?
