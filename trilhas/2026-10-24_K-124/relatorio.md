# K-124 — O juridico calibrado antes da coleta (24/10/2026)

Cartão do desenvolvimento, criado e executado nesta conversa a pedido de Vicente, antes do K-108. Sem agentes: o parecer prévio do juridico já estava feito (EX-0026; `parecer-juridico.md`).

## Falas originais de Vicente

Guardadas aqui por referência; o registro de decisões traz só a essência (registrar-decisao).

- Sobre a informação pública: "talvez o juridico tenha de refletir sobre informacoes que ja sao publicas e acessiveis"; depois, "meu comentario foi para que o juridico assimilasse isso"; e "algo sobre reflexao antes de acao".
- Sobre o parecer: "concordo com as posicoes do juridico e nao tenho objecoes".
- Sobre o Wayback: "C: só a captura existente".
- O pedido do cartão, com as seis regras já ajustadas ao parecer, está na mensagem de abertura desta conversa (24/10/2026), resumida nas D-042 e D-043.

## Palavras conferidas

- **"talvez"**: na primeira fala era hipótese; a segunda ("para que o juridico assimilasse isso") e o pedido do cartão fazem dela regra do juridico.
- **"reflexão antes da ação"**: não é pergunta nova; são seis passos dentro das oito perguntas fixas, que ficam.
- **"agora"**: barra o ato já, na coleta e no que se grava, antes de qualquer publicação; "publicar" barra só a publicação (K-010).
- **"C"**: a terceira opção do Wayback, só a captura que já existe; nenhuma captura nova no piloto.

## O que foi feito

- **Decisões:** D-042 (o juridico reflete antes de agir; a informação pública e acessível; agora ou só a publicação; a triagem fixa) e D-043 (o Wayback só com a captura existente; a proteção da Entrada; o padrão da F-0003), em `trilhas/decisoes/`.
- **Contrato:** `vale_para` com o valor "agora" no `falta.schema.json` ("captura", o nome antigo, segue aceito e é lido como "agora").
- **Harness:** juridico 0.2.0; `triagem-juridica` 0.2.0 (a regra, a reflexão em seis passos dentro das oito perguntas, o `vale_para`, os casos C e D); `guia-de-liberacao` 0.1.1.
- **Scripts:** `triagem_fixa.py` com a regra `triagem-fixa-0.3` (`--ato`, `--portao`, "sem Falta pela regra"); `wayback.py` 0.2 (Availability API, sem captura nova, Falta "sem cópia arquivada", proteção da Entrada).
- **Faltas:** F-0004 relida (agora; o pedido de captura nova fora do `wayback.py`); F-0005 com a nota; o K-202 fechado como "mantida com o porquê".
- **Testes:** `rodar_testes.py` OK 175 · FALHA 0 · PENDENTE 5 (eram 162); `validar_acervo.py` 173 registros, válido; fila de curadoria 0 de 15.

## Fora do alcance e não conferido

A Portaria 344 oficial e atual, as ADI 4815 e 4274, a Resolução CONAD 1/2010 e os termos do Internet Archive, como o parecer disse; a documentação e a resposta real da Availability API (nenhuma rodada real do `wayback.py`; insumo 51); o fim do art. 20 do Código Civil vem da citação do parecer, não da extração.

## Insumos

50 a 53 (`trilhas/insumos-planejamento.md`).
