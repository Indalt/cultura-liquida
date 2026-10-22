# Estado do planejamento de melhorias

Este arquivo é a memória da frente de planejamento (D-036). Toda rodada começa por ele, pelo quadro e pelos insumos; nenhuma depende da memória de uma conversa. Tamanho máximo: duas páginas. O que for longo vai para um arquivo próprio em `trilhas/planejamento/` e fica só apontado aqui.

## Como uma rodada acontece
1. **Sessão nova:** Opus 5.5 com esforço máximo, ultracode e thinking. É a configuração que o planejamento da v0.2 usou (D-027); nenhuma decisão a fixa para a frente, e ela vale até o K-002 dizer a de cada frente.
2. **Kit de leitura:**
   - `AGENTS.md`, este arquivo e `quadro.md`;
   - de `trilhas/insumos-planejamento.md`, só as entradas abertas (o cartão de cada uma está no mapa, seção 6);
   - as decisões citadas no cartão (`trilhas/decisoes/`);
   - a Fundação, só pelas seções que o cartão pede; o mapa das três frentes (`mapa-tres-frentes.md`) diz onde está cada coisa.
3. **Pegar um cartão** da coluna "A fazer" da frente de planejamento, na ordem do quadro, e movê-lo para "Fazendo".
4. **Trabalhar dentro do teto da rodada:** 300 mil tokens de agentes, valor provisório até o K-002. Medir antes de lançar cada agente, como manda a D-023, com a estimativa tirada da última medida do mesmo agente com a mesma habilidade (brief, l. 40; insumo 16).
5. **Gravar o resultado:**
   - o resultado da rodada vai para `trilhas/planejamento/` (os arquivos de trabalho, em `rodadas/AAAA-MM-DD_K-nnn/`);
   - decisões novas vão para `trilhas/decisoes/`, pela habilidade `registrar-decisao` (essência confirmada, não transcrição);
   - insumos novos vão para `insumos-planejamento.md`;
   - o que a próxima versão da Fundação deve levar vai para `proxima-versao.md`.
6. **Fechar:** mover o cartão, atualizar este arquivo, gravar os logs, fazer o commit e o push.

## Estado em 22/10/2026
- **Fundação v0.2:** concluída e verificada em 16 e 17/10. A próxima versão é o K-004, depois do relatório do piloto (D-035); a lista do que ela leva está em `proxima-versao.md` (V-01 a V-38).
- **Roteiro e brief de execuções** (`trilhas/2026-10-17_caminhos/`): aprovados em 17/10. As D-036 e D-037 entraram neles pelo K-003 (22/10): o quadro "Ajustes das D-036 e D-037" no início do brief, os ajustes no lugar e uma nota no roteiro, aprovados por Vicente em 22/10 com a D-038 e ajustados pela D-039.
- **K-003 concluído em 22/10:** Vicente aprovou os quatro padrões e as leituras (D-038, com a regra-mãe "a ferramenta decide os itens pela regra; Vicente decide as regras") e decidiu a CLB do piloto e o lugar da fonte institucional (D-039: a CLB se identifica pelo termo; nenhuma fonte é verdade única, nem a institucional; só CLB de outro termo vira candidata, num único cartão de lista). As marcas de aprovação saíram do brief e do roteiro; o que muda em `.claude/` está no bloco 1 do brief, para o K-101 gravar. Relatório, falas originais e checagens em `rodadas/2026-10-22_K-003/`.
- **K-001 concluído em 22/10:** `mapa-tres-frentes.md`, o quadro completo (35 cartões nas três frentes) e `proxima-versao.md`; relatório em `rodadas/2026-10-21_K-001/relatorio.md`. O quadro fica neste arquivo na fase 1, pelo plano (princípios 11 e 16, D-026; mapa, seção 9).
- **Caso-piloto:** cajuína, começando pelo caju (D-031). O piloto testa a ferramenta inteira (D-032).
- **Desenvolvimento:** bloco 0 feito (K-100). K-103 concluído em 22/10: a habilidade `registrar-melhoria`, o esquema de insumo e o script sem IA que grava o insumo na lista e no mapa; o primeiro uso real é o insumo 27. K-101 concluído em 22/10: o harness 0.1.1 (bloco 1), com o auditor sem divergência do pedido (`trilhas/2026-10-22_K-101/`). K-104 concluído em 22/10: o registro de valores provisórios e os contratos do §6 (bloco 2), com o auditor (5 achados, corrigidos; `trilhas/2026-10-22_K-104/`). Pela ordem do quadro, vem o K-105 (bloco 3).
- **Decisões vigentes:** até a D-039.
- **Insumos abertos:** de 1 a 31 (`trilhas/insumos-planejamento.md`); os 15 a 19 nasceram no K-001, os 20 a 26 no K-003, o 27 no K-103, já pela `registrar-melhoria`, o 28 no K-101 e os 29 a 31 no K-104.
- **Consumo da rodada K-001:** 299.042 tokens de agentes (lote C3, 31.342; verificação, 267.700), pelo número da ferramenta, dentro do teto. A conta pelo transcript daria mais (insumo 15). Uso da conta: 4% no início e 12% no fim, lidos por Vicente.
- **Consumo da rodada K-003:** 214.004 tokens de agentes (verificação, dois auditores, 30 chamadas), pelo número da ferramenta, dentro do teto; pelo transcript, com a saída do último turno, 251.736. O fechamento, numa conversa sem agentes, a pedido de Vicente, somou 0. Uso da conta, lido por Vicente: 12% no início e 23% ao abrir a conversa de fechamento; o fim dela, a informar.
- **Próxima rodada:** o K-002 (a IA da operação, a configuração e o teto de cada frente), pela ordem do quadro. Ele leva também os insumos 20 (juntar a proposta da rotina sem Vicente; a D-038 fixa que o papel de quem aprova é trocável) e 24. O uso da conta que Vicente der ao abrir essa rodada fecha a conta do K-003, como no K-001.

## Falas originais (20 e 21/10/2026), para a trilha
Elas ficam aqui só por rastreabilidade. O texto de trabalho usa a essência registrada nas D-036 e D-037.

- **20/10:** "manter a sessao de planejamento de melhorias, com ferramentas para isso, manter as sessoes para acoes relativas ao desenvolvimento da ferramenta, mas que a execucao e o trabalho da ferramenta nao dependa das sessoes de trabalho." Na mesma mensagem: "essa sessão de melhoramento seria constante? e quando a memoria encher? como usar essa sessao de forma constante sem gastar o que vem sendo gasto de tokens".
- **20/10:** "estamos construindo uma base de conhecimento. bases de conhecimento não precisam de revisao a nao ser que uma das dimensoes veja conflito sobre essa base de conhecimento. acho que isso entra na trilha de melhorias da aplicacao." Ainda: "quem a olha a base pode sugerir para a base, assim como as buscas e escavaçoes podem perceber isso"; "uma historia de uma pessoa sozinha pode testemunhar outros detalhes de culturas liquidas [...] na historia da cajuina se fala de mocororo como sendo o suco do caju, mas mocororo também é uma clb em si. esses pontos nao sao prioritarios, poderia haver apenas um script com roteiro simples de checagem durante o processamento normal da clb"; "o modo como as sessoes sao pensadas, executadas e implementadas na logica kaban de (a fazer, fazendo e concluido)"; "Isso poderia ser usado como interação de outras pessoas que querem contribuir"; "ser necessario reunir tudo nestas 3 frentes".
- **21/10:** "tokens renovados. podemos seguir." Esta fala aprovou as essências e a leitura da amostra sorteada como auditoria da ferramenta.
