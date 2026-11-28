---
name: planejar-aulas
description: Planeja, sob demanda, um programa de aulas sobre uma cultura líquida brasileira (CLB) — a bebida e tudo o que a faz existir — com qualquer número de aulas, a nota do educador e o kit do professor. A IA escreve só os blocos de texto; o script montar_programa.py prepara o material fechado, monta as aulas, as referências e a nota, e barra a invenção. A aula ensina a bebida e a ciência com que ela se conhece, nunca o sistema. Usada pelo campo-de-acao quando Vicente pede aulas.
---

# planejar-aulas

**Versão do harness:** 0.2.0 (28/11/2026, D-063) · **Quem usa:** campo-de-acao · **Script:** `scripts/montar_programa.py` (montar-programa-0.1) · **Estado:** casos de teste do script em `exemplos/casos.json`; sem par real aprovado ainda (o primeiro é o programa da cajuína, depois da revisão de Vicente).

## Objetivo
Aulas que um professor dá com gosto e uma turma acompanha com interesse: sobre a CLB (no programa da cajuína, o caju entra como parte dela: o insumo), seu modo de fazer, seu tempo, quem sabe e o hoje, e sobre **como se sabe** o que se diz dela. A ciência entra como modo de olhar, com o nome que tem na área. O sistema que reuniu as fontes fica fora da sala de aula.

## Divisão do trabalho (o que é da IA e o que é do script)
| Quem | Faz |
|---|---|
| **IA (esta habilidade)** | divide o assunto em blocos e escreve o texto de cada bloco e do kit; adapta ao público e ao educador quando o pedido os define |
| **`montar_programa.py material`** | o material fechado de cada bloco: só as afirmações do bloco, com o grau em palavras e a citação curta prontos |
| **`montar_programa.py conferir`** | barra a invenção: marca fora do material, data, número ou nome próprio que não aparece no material, dado pessoal |
| **`montar_programa.py montar --aulas N`** | as N aulas a partir das montagens, a lista de referências de cada aula, a nota do educador (rastreio, cuidados, carimbo, ajuste, espaço para anotar) e o kit com referências |

**Não faça à mão o que o script faz:** não abra as fichas do acervo para escrever referências, tabelas, graus ou carimbos, e não escreva a nota do educador.

## Passos
1. **O programa (`programa.json` na pasta do programa).** Divida o assunto em blocos (cada um com id, título, minutos e as afirmações `PR-nnnn` que ele usa, escolhidas da ficha da CLB e do desenho que o curador passar). O primeiro bloco é a **abertura**: o programa apresentado em tópicos, em até 15 minutos (menos quando o programa é curto), para encantar quem vai seguir. Declare as **montagens**: quais blocos formam cada aula para cada número de aulas pedido (1, 3, 5 ou outro), sem passar da duração da aula. Cuidados e "o que as fontes ainda não dizem" em palavras simples, com o código da Falta entre parênteses só aqui. O carimbo (versão da ficha, nível, data, como citar).
2. **O material:** `python scripts/montar_programa.py material <programa.json>`. Leia só `material/<bloco>.md`.
3. **Os blocos:** escreva `blocos/<id>.md`, um por bloco, e `blocos/kit.md`. Depois de cada frase com fato, a marca invisível `<!-- PR-nnnn -->`. Grave cada arquivo assim que terminar.
4. **A conferência:** `python scripts/montar_programa.py conferir <programa.json>`. Corrija cada ponto reprovado no texto (não no material). Se um nome ou número vier de fato do material com outra grafia, use a grafia do material.
5. **A montagem:** `python scripts/montar_programa.py montar <programa.json> --aulas N` para o número pedido.
6. **A autoconferência** (abaixo) e o bloco LOG.

## Regras do texto dos blocos
1. **O assunto é a CLB e a ciência.** Nada sobre o sistema: nem o nome dele, nem códigos (fora da marca invisível), graus numéricos, nomes de objetos internos, decisões ou pastas. Teste: um professor que nunca ouviu falar do sistema entende cada linha sem consultar nada?
2. **Só o material.** O que não está no material do bloco não entra: nem data, nem número, nem nome, nem relação de causa ("por isso", "sempre") que a afirmação não diz. O que falta se diz: "as fontes que temos não dizem".
3. **A ciência pelo nome da área, em palavras simples.** Por exemplo (ilustram, não limitam): fonte primária e secundária, sempre "em relação a qual pergunta"; quem fala na fonte e de que lugar; fontes independentes que concordam, ou uma que copia a outra; fontes que divergem, lado a lado, sem dizer quem tem razão; o que nenhuma fonte diz, dito e não completado.
4. **O grau e a citação como o material traz:** "uma fonte só, ainda sem confirmação independente", "fontes independentes concordam", "as fontes divergem", "as fontes não bastam para afirmar nem negar"; a citação curta entre parênteses. "Possivelmente" e outras ressalvas da fonte ficam.
5. **Cada bloco cuida só do seu assunto.** Uma frase de ligação basta; não recapitula nem antecipa outro bloco.
6. **Roteiro em minutos** dentro do bloco, com tempo real para a tarefa.
7. **Tarefa possível com o que o estudante tem.** Registro de fonte: campos que servem a um objeto ou papel de casa (o que é, quem fez, quando, onde fica guardado, sem endereço) e a um site ou vídeo (link, data de acesso, página ou minuto); uma afirmação por linha; "a fonte diz" e "eu digo" em colunas; "não dito" no que não se sabe; "primária ou secundária para a pergunta da aula?"; uma linha para o que a fonte não diz.
8. **Pessoas:** nunca imagem, voz ou nome de criança ou adolescente; pessoas de casa por código (P-1) e só com consentimento, com um texto curto que o estudante possa ler a quem o ensinou (é tarefa da escola, não será gravada nem publicada; posso anotar sem o seu nome?). O código protege enquanto não há consentimento e não apaga a autoria de quem sabe.
9. **Povos e comunidades:** nomear o povo pode; o detalhe do rito ou do preparo ritual não entra.
10. **Nada sanitário nem jurídico:** o que o material marca como aviso aparece só como "a fonte diz", sem dose, tempo ou temperatura para reproduzir. Provar a bebida em aula é escolha do educador.

## Adaptar ao público e a qualquer educador
O pedido pode descrever o público (idade, escola, lugar) e o educador (formação, lugar, pertencimento, língua, se ele mesmo é quem sabe fazer a bebida). Com isso, a linguagem, o tempo das atividades, as tarefas e a posição do material mudam: quando o educador ou a turma são detentores do saber, a aula abre espaço para essa voz entrar como voz própria, e a comunidade decide o que pode ser dito; a escuta dela vem antes. Sem descrição no pedido, faz-se a versão geral e a adaptação fica com o educador, no campo de ajuste da nota (o script o põe), sem mudar o programa.

## O kit do professor (`blocos/kit.md`)
1. **Para o professor, breve e simples:** o que é o programa, como usar as aulas e a nota, como montar 1, 3 ou 5 aulas, os cuidados com pessoas, onde o material ainda é frágil (uma fonte só em muitas afirmações, pouca voz de quem pratica), sem códigos.
2. **No fim, uma aula ao grande público:** como este programa foi feito com base nas ciências. Tom humilde: os métodos existem, qualquer pessoa pode usá-los na sua área, e aplicar método reforça o que se sabe. Poucas escolhas, cada uma com o problema que resolve, o nome do método e o que ainda não se sabe; um breve comentário sobre a didática usada. Não menciona o sistema.

## Modelos pedagógicos de referência (escolher e dizer qual no kit; nível: de memória, não conferido)
Ilustram, não limitam (D-017).
- **Leitura de fontes como na história:** de onde vem a fonte, contexto, corroboração, leitura atenta (Stanford History Education Group, "Reading Like a Historian").
- **Educação patrimonial:** observar, registrar, explorar, apropriar-se (Guia Básico de Educação Patrimonial, Iphan, 1999); inventários participativos (Iphan, 2016).
- **Tema gerador e diálogo (Paulo Freire):** partir do que a turma vive e voltar a ele.
- **Ensino por investigação:** pergunta, hipóteses, fontes como dados, conclusão com o grau de apoio (Anna Maria Pessoa de Carvalho).
- **Sequência didática** (Antoni Zabala); **estações e grupos**; **aprendizagem por projeto** para a última aula.

## Autoconferência (antes de entregar; sem segunda leitura)
1. `conferir` passa.
2. Releia cada bloco como um professor de fora: há palavra que só faz sentido dentro do sistema? Há relação ou conclusão que o material não diz? Reescreva.
3. A abertura encanta e cabe no tempo; nenhum bloco faz o trabalho de outro; cada montagem cabe na duração.

## Teto e custo
Uma chamada para o programa e o material e os primeiros blocos; outra para o resto, o kit, a conferência e a montagem (teto de 25 turnos do agente). Grave cada arquivo ao terminar.

## O que não faz
Não produz sem pedido (princípio 15); não publica; não dá parecer jurídico nem sanitário; não ensina o preparo ritual; não completa o que as fontes não dizem; não escreve o que o script faz.

## Campos do log
`agente: "campo-de-acao"`, `habilidade: "planejar-aulas"`, `entrada_ref` (o pedido e a pasta do programa).

## Histórico
- 0.2.0 (28/11/2026, D-063): número de aulas livre (montagens); o programa é da CLB; adaptação a qualquer público e educador; a IA escreve só os blocos e o `montar_programa.py` faz material, montagem, referências, nota e conferência contra invenção.
- 0.1.0 (28/11/2026, D-063): primeira versão.
