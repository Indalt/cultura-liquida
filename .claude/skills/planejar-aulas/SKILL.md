---
name: planejar-aulas
description: Planeja, sob demanda, um programa de aulas sobre uma cultura líquida brasileira (a bebida e tudo o que a faz existir), com a nota do educador e o kit do professor. A aula ensina a bebida e a ciência com que ela se conhece; o sistema que produziu o material não é assunto da aula. Usada pelo campo-de-acao quando Vicente pede aulas.
---

# planejar-aulas

**Versão do harness:** 0.1.0 (28/11/2026, D-063) · **Quem usa:** campo-de-acao · **Estado:** sem exemplos reais aprovados ainda (o primeiro par é o programa do caju, depois da revisão de Vicente).

## Objetivo
Fazer aulas que um professor dá com gosto e uma turma acompanha com interesse: sobre a bebida, seu insumo, seu modo de fazer, seu tempo, quem sabe e o hoje, e sobre **como se sabe** o que se diz dela. A ciência entra como modo de olhar, com o nome que tem na área. O sistema que reuniu as fontes fica fora da sala de aula.

## Entradas
- O pedido (assunto, número de aulas, duração, público ou "público em aberto").
- A ficha da bebida e a camada Educação (`acervo/fichas/`), as Proposições (`acervo/proposicoes/`) e as Fontes (`acervo/fontes/`), como base de conteúdo e rastreio.
- O desenho de conteúdo que o curador passar (quais afirmações por aula), sem o vocabulário interno.

## Saídas (na pasta que o curador indicar)
1. **`aula-1.md` a `aula-n.md`**, o texto que o professor usa em sala.
2. **`nota-do-educador.md`**: o rastreio e os cuidados, aula por aula, com espaço para anotar.
3. **`kit-do-professor.md`**: a explicação breve ao professor e, no fim, a aula ao grande público sobre como o programa foi feito.

Cada arquivo começa com a marca "rascunho, não publicado" enquanto o pedido não disser outra coisa.

## Regras da aula (o texto da sala)
1. **O assunto é a bebida e a ciência.** Nada sobre o sistema: nem o nome dele, nem os códigos, os graus numéricos, os nomes de objetos internos, as decisões ou as pastas. Teste: um professor que nunca ouviu falar do sistema entende cada linha sem consultar nada?
2. **A ciência pelo nome da área, em palavras simples.** Por exemplo (ilustram, não limitam): fonte primária e secundária, sempre "em relação a qual pergunta"; quem fala na fonte e de que lugar; fontes independentes que concordam, ou uma que copia a outra; fontes que divergem, lado a lado, sem dizer quem tem razão; o que nenhuma fonte diz, dito em voz alta e não completado por palpite.
3. **O grau de apoio em palavras:** "uma fonte só, ainda sem confirmação independente"; "fontes independentes concordam"; "as fontes divergem"; "nenhuma fonte diz". Nunca símbolo ou número de grau.
4. **Fontes citadas como a ciência cita:** no texto, (Autor, ano) ou (Instituição, ano); no fim da aula, a lista de referências (AUTOR. Título. Instituição ou editora, ano. Link). Sem autor registrado: título, instituição, ano e link. "Possivelmente" e outras ressalvas da fonte ficam como estão.
5. **A aula 1 abre com o programa** (D-063): em tópicos, no máximo 15 minutos, para encantar quem vai seguir. Uma pergunta, um objeto ou uma imagem que acorda a curiosidade; o caminho das aulas em uma linha cada; e, em poucas palavras, como se sabe o que se sabe (o item 2 acima). O resto da aula 1 é o assunto dela.
6. **Cada aula cuida só do seu assunto.** Não recapitula a outra além de uma frase de ligação; não antecipa o conteúdo da seguinte.
7. **Roteiro em minutos** que caiba na duração pedida, com tempo real para a tarefa (a tarefa não se apresenta em poucos minutos se tem muitos campos).
8. **Tarefa possível com o que o estudante tem.** Se for registrar uma fonte de casa, os campos servem a um objeto ou papel de casa (o que é, quem fez, quando, onde fica guardado, sem endereço) e também a um site ou vídeo (link, data de acesso, página ou minuto). Uma afirmação por linha; "a fonte diz" e "eu digo" em colunas; "não dito" no que não se sabe; a pergunta "primária ou secundária para a pergunta da aula?"; uma linha para o que a fonte não diz.
9. **Pessoas:** nunca imagem, voz ou nome de criança ou adolescente; pessoas de casa por código (P-1) e só com consentimento, com um texto de consentimento curto e simples que o estudante possa ler a quem o ensinou ("é uma tarefa da escola, não será gravada nem publicada; posso anotar o que você me contou, sem o seu nome?"). Explicar que o código protege enquanto não há consentimento, e não apaga a autoria de quem sabe.
10. **Povos e comunidades:** nomear o povo pode; o detalhe do rito ou do preparo ritual não entra. Em escola indígena ou quilombola, a escuta da comunidade vem antes da aula (dito na nota do educador).
11. **Nada sanitário nem jurídico:** o que a fonte diz de composição, preparo, norma ou risco aparece como "a fonte diz", sem dose, tempo ou temperatura para reproduzir. Provar a bebida em aula é escolha do educador.
12. **Nenhum fato fora das fontes.** O que não está nas fontes reunidas é dito como "ainda não se sabe" ou "as fontes que temos não dizem"; nunca completado por memória.

## A nota do educador
Por aula: a tabela "frase da aula → código da afirmação (PR) → fonte (FO) → página", para quem quiser conferir; os cuidados em palavras simples (as Faltas que valem, com o código entre parênteses); o "Ajuste ao público:" vazio quando o público está em aberto; habilidades da BNCC só como sugestão, se a camada Educação as traz; e um bloco **Anotações** com linhas em branco (`______`) para escrever à mão e um espaço para digitar. No fim, o carimbo mínimo do campo de ação: versão da ficha, nível, Faltas, data, como citar e o aviso "não é orientação jurídica nem sanitária". É o único arquivo onde os códigos aparecem.

## O kit do professor
1. **Para o professor (breve e simples, uma ou duas páginas):** o que é o programa, como usar as aulas e a nota, os cuidados com pessoas, como citar, e onde o material ainda é frágil (uma fonte só em muitas afirmações, pouca voz de quem pratica), dito sem códigos.
2. **No fim, uma aula ao grande público:** "como este programa de aulas foi feito com base nas ciências". Em tom humilde: os métodos existem, qualquer pessoa pode usá-los na sua área, e aplicar método reforça o que se sabe. Para cada escolha mostrada (poucas, não todas): o problema que ela resolve, o nome do método e o que ainda não se sabe. Um breve comentário sobre a didática usada (o modelo pedagógico escolhido e por quê). Não menciona o sistema.

## Modelos pedagógicos de referência (escolher e dizer qual; nível: de memória, não conferido)
Ilustram, não limitam (D-017). Ao usar um, cite-o no kit do professor com o nível "não conferido" até o auditor conferir.
- **Leitura de fontes como na história:** perguntar de onde vem a fonte, situá-la no contexto, corroborar com outras independentes e ler com atenção (o modelo do Stanford History Education Group, "Reading Like a Historian").
- **Educação patrimonial:** observar, registrar, explorar e se apropriar do bem cultural (Guia Básico de Educação Patrimonial, Iphan, 1999); inventários participativos (Iphan, 2016).
- **Tema gerador e diálogo (Paulo Freire):** partir do que a turma vive (o cajueiro do quintal, a garrafa na geladeira) e voltar a ele.
- **Ensino por investigação:** uma pergunta, hipóteses da turma, fontes como dados, conclusão com o grau de apoio (sequências de ensino investigativo, Anna Maria Pessoa de Carvalho).
- **Sequência didática:** cada aula com começo, meio e fim ligados ao conjunto (Antoni Zabala).
- **Estações e trabalho em grupo:** grupos com conjuntos diferentes de fontes que depois se comparam.
- **Aprendizagem por projeto:** para a última aula, uma proposta de ação da turma.

## Autoconferência (antes de entregar; é a conferência da habilidade, sem segunda leitura)
1. Releia cada aula como um professor de fora: há alguma palavra que só faz sentido dentro do sistema? Reescreva.
2. Toda afirmação de fato tem citação na aula e linha na nota do educador; todo código da nota existe no acervo (`ls acervo/proposicoes/PR-nnnn.json`, `acervo/fontes/FO-nnnn.json`).
3. A abertura da aula 1 cabe em 15 minutos e encanta; nenhuma aula faz o trabalho de outra; o roteiro soma a duração pedida.
4. `python scripts/procurar_dado_pessoal.py <arquivos>` sem ocorrência.
5. A nota do educador tem o carimbo e o espaço de anotações.

## Teto e custo
Uma chamada por dois ou três arquivos (teto de 25 turnos do agente); grave cada arquivo assim que terminar.

## O que não faz
Não produz sem pedido (princípio 15); não publica; não dá parecer jurídico nem sanitário; não ensina o preparo ritual; não completa o que as fontes não dizem.

## Campos do log
`agente: "campo-de-acao"`, `habilidade: "planejar-aulas"`, `entrada_ref` (o pedido e a pasta de saída).

## Histórico
- 0.1.0 (28/11/2026, D-063): primeira versão, depois da revisão das aulas do caju por Vicente.
