---
name: triagem-juridica
description: Triagem jurídica de precaução de um item do projeto Cultura Líquida (trecho, fonte, contribuição, ficha, política de um script) com perguntas fixas e reflexão antes da ação; cada dúvida que a regra não resolve vira uma Falta no formato de esquemas/falta.schema.json, com a norma citada, o vale_para (agora ou só publicar) e o caminho de liberação. Use antes da coleta de um ambiente ou de um script que copia, antes de publicar qualquer item e, na fase 2, antes de uma contribuição entrar na quarentena.
---

# triagem-juridica

**Versão do harness:** 0.2.0 · **Quem usa:** juridico · **Rodada:** A

## Objetivo
Achar, com perguntas fixas e **reflexão antes da ação** (D-042), o que pode impedir o projeto de fazer algo com um item, e dizer isso como **Falta** (D-020), com o que ela barra: o ato **agora** ou **só a publicação**. Nunca autorizar.

## A regra da informação pública e acessível (D-042, item 1)
**Regra de precaução de Vicente, não parecer de licitude.** Ler, localizar e linkar informação pública e acessível, e citar trecho curto com autor e origem (Lei 9.610, art. 46, III e VIII), **não gera Falta**. O nome do autor citado não é dado pessoal a barrar; o dado de acesso público segue a LGPD, art. 7º, §3º. A Falta fica para:
- proibição expressa nos termos de uso ou no robots.txt (barra **agora**);
- cópia além da citação de obra protegida (barra **agora**);
- dado pessoal, inclusive sensível e de criança ou adolescente (barra **agora**);
- conhecimento tradicional associado (Lei 13.123, que vale mesmo para o publicado; barra **só a publicação**, com a nota do art. 9º: de origem identificável, o detalhe não se aprofunda e espera numa pasta local até o K-010);
- substância controlada (barra **só a publicação**; **agora**, só o modo de obter ou de preparar, Lei 11.343, art. 33);
- licença ausente, que só vale diante de cópia ou de publicação (barra **só a publicação**).

Quando a regra resolve, a resposta da pergunta é "sem Falta pela regra" e o log diz isso, nunca "pode publicar".

## Quando usar / quando não usar
- **Usar:** antes da coleta de um ambiente ou de um script que guarda cópia (ex.: a política de cópias do `wayback.py`); antes de publicar (kit, wiki, boletim); na fase 2, em cada contribuição antes da quarentena; quando o avaliador marcar possível conhecimento tradicional ou dado pessoal.
- **Não usar:** para decidir se a prática é "verdadeira" ou "cultural" (critérios da D-022 são do avaliador; aqui só o jurídico); para escrever o guia (isso é `guia-de-liberacao`); para os casos óbvios em lote, que o `scripts/triagem_fixa.py` (triagem-fixa-0.3) já cobre pela regra.

## Entradas e saídas
- **Entrada:** o item (caminho ou ID, nunca dados pessoais em claro), o ato que se quer fazer com ele (ler, localizar, linkar e citar; copiar; publicar), o degrau em que o projeto está (16-J: 1 só Vicente; 2 contribuições; 3 publicação) e as Faltas já existentes.
- **Saída:** uma lista de Faltas, cada uma válida em `esquemas/falta.schema.json`. Falta jurídica traz `subtipo_juridico`, `norma` (referência, trecho literal, URL, nível), `vale_para` (`agora` ou `publicar`) e `caminho_de_liberacao` (guia e estado). Se nenhuma pergunta gerar Falta, a saída é uma lista vazia **e o log diz quais perguntas foram feitas e quais ficaram "sem Falta pela regra"**.

## Reflexão antes da ação (D-042, item 4)
Dentro de **cada** pergunta fixa que se aplica, antes de concluir, seis passos, nesta ordem:
1. **O que vamos fazer com a fonte?** (ler, localizar, linkar, citar trecho curto; copiar; publicar)
2. **É pública e acessível?** (abriu sem login, sem barreira, sem proibição expressa nos termos ou no robots.txt)
3. **Qual norma, com o texto conferido?** (trecho literal, URL, nível; o que não foi conferido fica "não conferido" e dito)
4. **O ato bate mesmo na norma?** (ex.: ler e linkar não é a reprodução do art. 29; a cópia de página inteira é)
5. **Barra agora ou só a publicação?** (pela lista da regra acima)
6. **Há um jeito de fazer sem Falta?** (ex.: link e citação curta no lugar da cópia; a captura que já existe no lugar da captura nova, D-043; o papel e o código no lugar do nome)

Se o passo 4 ou o 6 resolver pela regra, a pergunta fecha "sem Falta pela regra".

## Perguntas fixas (sempre todas, nesta ordem)
1. **Direito autoral (Lei 9.610):** o que se quer usar é o modo de fazer (livre, art. 8º, I) ou o texto, a foto, o áudio de alguém? Cabe na citação "na medida justificada", com autor e origem (art. 46, III), ou nos pequenos trechos (art. 46, VIII)? Há cópia além da citação (art. 29, I; **agora**)? Fonte antiga: já em domínio público (art. 41)? Autor desconhecido: atenção à ressalva dos conhecimentos étnicos e tradicionais (art. 45, II). Imagem ou vídeo de terceiros: só por link. A licença ausente só pesa diante de cópia ou de publicação (**publicar**).
2. **Conhecimento tradicional (Lei 13.123; Decreto 8.772):** é conhecimento de povo indígena, comunidade tradicional ou agricultor tradicional sobre propriedades ou usos associados ao patrimônio genético (planta, animal, **microrganismo**: o art. 2º, I, inclui espécies microbianas)? A lei vale mesmo para o publicado (art. 2º, IX). Se for, a origem é identificável? O cadastro vem antes da divulgação (art. 12, §2º) → Falta que vale para **publicar**; de origem identificável, o consentimento condiciona o acesso (art. 9º): o detalhe não se aprofunda e espera na pasta local até o K-010 (D-043). Sempre: indicar a origem (art. 10, II).
3. **Restrição por costume:** há costume que rege o acesso a esse aspecto (Convenção de 2003, art. 13, d, ii)? → campo restrição; na dúvida, Falta.
4. **Dados pessoais (LGPD):** aparece pessoa identificável? Há **dado sensível** (saúde, religião, origem racial ou étnica, ligação a comunidade tradicional)? Sem base legal → Falta (**agora**). O nome do autor citado numa referência não é dado a barrar (D-042); o dado de acesso público segue a finalidade, a boa-fé e o interesse público (art. 7º, §3º). Pessoa citada como "quem ensinou" sem consentimento → só papel e ID opaco.
5. **Imagem e voz:** aparece rosto ou voz de alguém? Sem autorização → só link, e só se a fonte original for legitimamente pública (CF, art. 5º, X; Código Civil, art. 20; ambos oficiais, conferidos no parecer do K-124).
6. **Crianças e adolescentes:** nunca registrar imagem, voz ou nome (**agora**).
7. **Substância controlada:** o item envolve substância ou planta das listas da Portaria SVS/MS 344/1998 (secundária, cópia de 2022; a lista oficial e atual não foi conferida)? → Falta que vale para **publicar**; o modo de obter ou de preparar barra **agora** (Lei 11.343, art. 33). Ayahuasca e jurema não aparecem pelo nome nas listas: entram como **dúvida**, não como controle certo.
8. **Licença de quem contribuiu** (degrau 2): há licença registrada? Não → Falta.

## Passos
1. Leia só o necessário do item (trecho, metadados) e diga o ato que se quer fazer.
2. Responda cada pergunta com "não se aplica", "sem Falta pela regra" ou "dúvida", passando pela reflexão antes da ação. Toda dúvida que a regra não resolve vira uma Falta.
3. Para cada Falta, cite a norma com trecho literal e URL já conferidos (C1, C5, parecer do K-124, `esquemas/triagem-fixa.json`). Norma ainda não conferida: `nivel: "não conferido"`, e a Falta continua de pé.
4. Preencha o `vale_para` (`agora` ou `publicar`) pela regra.
5. Aponte o guia de liberação (`G-...`) e o estado "não iniciado". Se o guia não existe, indique "a preparar" e avise o curador.
6. Valide cada Falta: `python scripts/validar.py falta <arquivo>` (o juridico devolve o JSON ao curador, que grava e valida). Termine com o bloco LOG.

## Regras herdadas
- **Nível:** norma com URL e nível; nada de memória.
- **Essência:** D-019 (não julgamos a prática), D-020 (só cria Faltas), D-025 (porquê e caminho; proporcional, "de início"), D-038 (Vicente decide as regras; o agente só aplica), D-042 (a regra da informação pública e a reflexão antes da ação), D-043 (o Wayback só com a captura existente; o padrão da F-0003 para o Git público).
- **Dado pessoal:** a Falta descreve o tipo de dado, nunca o dado ("aparece o nome de quem ensinou", e não o nome).
- **Anti-robô:** não se contorna.
- **Falta dita:** a Falta não traz valor inferido (o esquema recusa `valor` e `valor_inferido`).

## Teto e custo
Sem web quando as normas já estão conferidas (o normal). Até 5 chamadas para conferir uma norma faltante. Medido: 46.107 tokens e 9 chamadas na triagem da política de cópias (K-107); 82.949 tokens e 24 chamadas no parecer do K-124, com 13 consultas à web.

## Critério de parada
As oito perguntas respondidas, cada uma com a reflexão, e cada dúvida que a regra não resolve registrada como Falta.

## O que não faz
Não autoriza, não libera, não diz "pode publicar", não dá parecer de licitude (a regra da informação pública é de Vicente), não julga a prática, não guarda o dado pessoal que encontrou.

## Campos do log
`agente: "juridico"`, `habilidade: "triagem-juridica"`, `versao_harness: "0.2.0"`, `entrada_ref` (ID do item e o ato), `acoes` (as 8 perguntas e a resposta curta de cada; "sem Falta pela regra" quando a regra resolve), `decisoes` (cada Falta como `falta`, com o motivo e o vale_para; itens sem Falta como `aceito`, com o motivo "sem Falta pela regra (D-042)"), `erros`, `alcance`.

## Exemplos e validador
Casos construídos a partir do 16-J do plano e do K-124 (sem pessoa real):
- [exemplos/caso-a-dado-sensivel.md](exemplos/caso-a-dado-sensivel.md) → [falta-dado-sensivel.json](exemplos/falta-dado-sensivel.json). **Passa.**
- [exemplos/caso-b-conhecimento-tradicional.md](exemplos/caso-b-conhecimento-tradicional.md) → [falta-conhecimento-tradicional.json](exemplos/falta-conhecimento-tradicional.json). **Passa.**
- [exemplos/caso-c-f0004-relida.md](exemplos/caso-c-f0004-relida.md): a F-0004 relida pelo roteiro da reflexão (a captura nova é cópia além da citação; barra agora; o jeito sem Falta é a captura que já existe, D-043) → `acervo/faltas/F-0004.json`, com `vale_para: "agora"`. **Passa.**
- [exemplos/caso-d-link-e-citacao.md](exemplos/caso-d-link-e-citacao.md): link e citação curta com o autor citado → "sem Falta pela regra" (e o mesmo pela triagem fixa: `testes/nucleo/triagem/entrada-citacao-autor.json`). **Passa.**
- [exemplos/falta-ct-so-publicar.json](exemplos/falta-ct-so-publicar.json): conhecimento tradicional de origem identificável, só para publicar, com a nota do art. 9º. **Passa.**
- [exemplos/erro-falta-juridica-sem-caminho.json](exemplos/erro-falta-juridica-sem-caminho.json): Falta jurídica sem caminho de liberação (fere a D-025). **Reprova.**
- [exemplos/erro-falta-completada.json](exemplos/erro-falta-completada.json): Falta com valor inferido (Falta completada). **Reprova.**
- [exemplos/erro-vale-para-fora.json](exemplos/erro-vale-para-fora.json): `vale_para` fora do contrato ("depois"). **Reprova.**
- Os casos da regra na triagem fixa (cópia de página inteira, quem ensinou, receita de substância listada e conhecimento tradicional de origem identificável no ato publicar, que reprovam no portão; link e citação com o autor, e o conhecimento tradicional no ato ler, que passam) estão em `testes/nucleo/casos.json`.
- Validador: `scripts/validar.py falta`; `scripts/triagem_fixa.py --ato <ato> --portao`.

## Histórico
- 0.2.0 (24/10/2026, K-124): a regra da informação pública e acessível (D-042, regra de Vicente, não parecer de licitude); a reflexão antes da ação, em seis passos, dentro das oito perguntas, que ficam; o `vale_para` (agora ou só publicar) em toda Falta jurídica; a CF, art. 5º, X, e o Código Civil, art. 20, conferidos; a substância pela Lista E e pelas substâncias, com ayahuasca e jurema como dúvida; o Wayback só com a captura existente (D-043); casos novos, com a F-0004 relida.
- 0.1.0 (16/10/2026): primeira versão, com as perguntas fixas do plano (itens 7 e 16-J) e o art. 2º, I, da Lei 13.123 conferido no C1.
