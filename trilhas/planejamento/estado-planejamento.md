# Estado do planejamento de melhorias

Este arquivo é a memória da frente de planejamento (D-036). Toda rodada começa por ele, pelo quadro e pelos insumos; nenhuma depende da memória de uma conversa. Tamanho máximo: duas páginas. O que for longo vai para um arquivo próprio em `trilhas/planejamento/` e fica só apontado aqui.

## Como uma rodada acontece
1. **Sessão nova:** Opus 5.5 com esforço máximo, ultracode e thinking, que é a configuração do planejamento (D-027).
2. **Kit de leitura:**
   - `AGENTS.md`, este arquivo e `quadro.md`;
   - de `trilhas/insumos-planejamento.md`, só as entradas abertas;
   - as decisões citadas no cartão (`trilhas/decisoes/`);
   - a Fundação, só pelas seções que o cartão pede.
3. **Pegar um cartão** da coluna "A fazer" da frente de planejamento e movê-lo para "Fazendo".
4. **Trabalhar dentro do teto da rodada:** 300 mil tokens de agentes, valor provisório até o insumo 13. Medir antes de lançar cada agente, como manda a D-023.
5. **Gravar o resultado:**
   - o resultado da rodada vai para `trilhas/planejamento/`;
   - decisões novas vão para `trilhas/decisoes/`, pela habilidade `registrar-decisao` (essência confirmada, não transcrição);
   - insumos novos vão para `insumos-planejamento.md`.
6. **Fechar:** mover o cartão, atualizar este arquivo, fazer o commit e o push.

## Estado em 21/10/2026
- **Fundação v0.2:** concluída e verificada em 16 e 17/10.
- **Roteiro e brief de execuções** (`trilhas/2026-10-17_caminhos/`): aprovados em 17/10.
- **Caso-piloto:** cajuína, começando pelo caju (D-031). O piloto testa a ferramenta inteira (D-032).
- **Desenvolvimento:** Bloco 0 feito. O próximo é o Bloco 1 (harness e operação), que aguarda a autorização de Vicente.
- **Decisões vigentes:** até a D-037.
- **Insumos abertos:** de 1 a 14 (`trilhas/insumos-planejamento.md`).
- **Próxima rodada:** o cartão K-001, reunir tudo nas três frentes.

## Falas originais (20 e 21/10/2026), para a trilha
Elas ficam aqui só por rastreabilidade. O texto de trabalho usa a essência registrada nas D-036 e D-037.

- **20/10:** "manter a sessao de planejamento de melhorias, com ferramentas para isso, manter as sessoes para acoes relativas ao desenvolvimento da ferramenta, mas que a execucao e o trabalho da ferramenta nao dependa das sessoes de trabalho." Na mesma mensagem: "essa sessão de melhoramento seria constante? e quando a memoria encher? como usar essa sessao de forma constante sem gastar o que vem sendo gasto de tokens".
- **20/10:** "estamos construindo uma base de conhecimento. bases de conhecimento não precisam de revisao a nao ser que uma das dimensoes veja conflito sobre essa base de conhecimento. acho que isso entra na trilha de melhorias da aplicacao." Ainda: "quem a olha a base pode sugerir para a base, assim como as buscas e escavaçoes podem perceber isso"; "uma historia de uma pessoa sozinha pode testemunhar outros detalhes de culturas liquidas [...] na historia da cajuina se fala de mocororo como sendo o suco do caju, mas mocororo também é uma clb em si. esses pontos nao sao prioritarios, poderia haver apenas um script com roteiro simples de checagem durante o processamento normal da clb"; "o modo como as sessoes sao pensadas, executadas e implementadas na logica kaban de (a fazer, fazendo e concluido)"; "Isso poderia ser usado como interação de outras pessoas que querem contribuir"; "ser necessario reunir tudo nestas 3 frentes".
- **21/10:** "tokens renovados. podemos seguir." Esta fala aprovou as essências e a leitura da amostra sorteada como auditoria da ferramenta.
