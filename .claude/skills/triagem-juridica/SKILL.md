---
name: triagem-juridica
description: Triagem jurídica de precaução de um item do projeto Cultura Líquida (trecho, fonte, contribuição, ficha) com perguntas fixas; cada dúvida vira uma Falta no formato de esquemas/falta.schema.json, com a norma citada e o caminho de liberação. Use antes de publicar qualquer item e, na fase 2, antes de uma contribuição entrar na quarentena.
---

# triagem-juridica

**Versão do harness:** 0.1.0 · **Quem usa:** juridico · **Rodada:** A

## Objetivo
Achar, com perguntas fixas, o que pode impedir falar de um item, e dizer isso como **Falta** (D-020): na dúvida, Falta. Nunca autorizar.

## Quando usar / quando não usar
- **Usar:** antes de publicar (kit, wiki, boletim); na fase 2, em cada contribuição antes da quarentena; quando o avaliador marcar possível conhecimento tradicional ou dado pessoal.
- **Não usar:** para decidir se a prática é "verdadeira" ou "cultural" (critérios da D-022 são do avaliador; aqui só o jurídico); para escrever o guia (isso é `guia-de-liberacao`).

## Entradas e saídas
- **Entrada:** o item (caminho ou ID, nunca dados pessoais em claro), o degrau em que o projeto está (16-J: 1 só Vicente; 2 contribuições; 3 publicação) e as Faltas já existentes.
- **Saída:** uma lista de Faltas, cada uma válida em `esquemas/falta.schema.json`. Falta jurídica traz `subtipo_juridico`, `norma` (referência, trecho literal, URL, nível) e `caminho_de_liberacao` (guia e estado). Se nenhuma pergunta gerar dúvida, a saída é uma lista vazia **e o log diz quais perguntas foram feitas**.

## Perguntas fixas (sempre todas, nesta ordem)
1. **Direito autoral (Lei 9.610):** o que se quer usar é o modo de fazer (livre, art. 8º, I) ou o texto, a foto, o áudio de alguém? Cabe na citação "na medida justificada", com autor e origem (art. 46, III)? Fonte antiga: já em domínio público (art. 41)? Autor desconhecido: atenção à ressalva dos conhecimentos étnicos e tradicionais (art. 45, II). Imagem ou vídeo de terceiros: só por link.
2. **Conhecimento tradicional (Lei 13.123; Decreto 8.772):** é conhecimento de povo indígena, comunidade tradicional ou agricultor tradicional sobre propriedades ou usos associados ao patrimônio genético (planta, animal, **microrganismo**: o art. 2º, I, inclui espécies microbianas)? Se for, a origem é identificável? Identificável sem consentimento → Falta. Atividade que pode ser "acesso" sem cadastro → Falta (regra de Vicente). Sempre: indicar a origem (art. 10, II).
3. **Restrição por costume:** há costume que rege o acesso a esse aspecto (Convenção de 2003, art. 13, d, ii)? → campo restrição; na dúvida, Falta.
4. **Dados pessoais (LGPD):** aparece pessoa identificável? Há **dado sensível** (saúde, religião, origem racial ou étnica, ligação a comunidade tradicional)? No degrau 2 ou 3, sem base legal → Falta. Pessoa citada como "quem ensinou" sem consentimento → só papel e ID opaco.
5. **Imagem e voz:** aparece rosto ou voz de alguém? Sem autorização → só link, e só se a fonte original for legitimamente pública.
6. **Crianças e adolescentes:** nunca registrar imagem, voz ou nome.
7. **Substância controlada:** o item envolve substância da Portaria SVS/MS 344/1998? → Falta até conferência.
8. **Licença de quem contribuiu** (degrau 2): há licença registrada? Não → Falta.

## Passos
1. Leia só o necessário do item (trecho, metadados).
2. Responda cada pergunta com "não se aplica", "sem dúvida" ou "dúvida". Toda dúvida vira uma Falta.
3. Para cada Falta, cite a norma com trecho literal e URL já conferidos (C1, Anexo C). Norma ainda não conferida: `nivel: "não conferido"`, e a Falta continua de pé.
4. Aponte o guia de liberação (`G-...`) e o estado "não iniciado". Se o guia não existe, indique "a preparar" e avise o curador.
5. Valide cada Falta: `echo '<json>' | python scripts/validar.py falta -`. Termine com o bloco LOG.

## Regras herdadas
- **Nível:** norma com URL e nível; nada de memória.
- **Essência:** D-019 (não julgamos a prática), D-020 (só cria Faltas), D-025 (porquê e caminho; proporcional, "de início").
- **Dado pessoal:** a Falta descreve o tipo de dado, nunca o dado ("aparece o nome de quem ensinou", e não o nome).
- **Anti-robô:** não se contorna.
- **Falta dita:** a Falta não traz valor inferido (o esquema recusa `valor` e `valor_inferido`).

## Teto e custo
Sem web quando as normas já estão conferidas (o normal). Até 5 chamadas para conferir uma norma faltante. Estimativa: 10 a 30 mil tokens por item em Sonnet 5.5 alto (a medir no Passo 1).

## Critério de parada
As oito perguntas respondidas, com cada dúvida registrada como Falta.

## O que não faz
Não autoriza, não libera, não diz "pode publicar", não dá parecer, não julga a prática, não guarda o dado pessoal que encontrou.

## Campos do log
`agente: "juridico"`, `habilidade: "triagem-juridica"`, `entrada_ref` (ID do item), `acoes` (as 8 perguntas e a resposta curta de cada), `decisoes` (cada Falta como `falta`, com o motivo; itens sem dúvida como `aceito`), `erros`.

## Exemplos e validador
Casos construídos a partir do 16-J do plano (sem pessoa real):
- [exemplos/caso-a-dado-sensivel.md](exemplos/caso-a-dado-sensivel.md) → [falta-dado-sensivel.json](exemplos/falta-dado-sensivel.json). **Passa.**
- [exemplos/caso-b-conhecimento-tradicional.md](exemplos/caso-b-conhecimento-tradicional.md) → [falta-conhecimento-tradicional.json](exemplos/falta-conhecimento-tradicional.json). **Passa.**
- [exemplos/erro-falta-juridica-sem-caminho.json](exemplos/erro-falta-juridica-sem-caminho.json): Falta jurídica sem caminho de liberação (fere a D-025). **Reprova.**
- [exemplos/erro-falta-completada.json](exemplos/erro-falta-completada.json): Falta com valor inferido (Falta completada). **Reprova.**
- Validador: `scripts/validar.py falta`.

## Histórico
- 0.1.0 (16/10/2026): primeira versão, com as perguntas fixas do plano (itens 7 e 16-J) e o art. 2º, I, da Lei 13.123 conferido no C1.
