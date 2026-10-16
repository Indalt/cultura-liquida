---
name: guia-de-liberacao
description: Prepara um guia de liberação assistido para uma Falta jurídica do projeto Cultura Líquida: por que está barrado (norma citada), o que destravaria, quem pode fazer, passo a passo com onde e como preencher, documentos, limites e o que não foi conferido. Use quando o juridico cria uma Falta jurídica ou quando Vicente quer destravar uma.
---

# guia-de-liberacao

**Versão do harness:** 0.1.0 · **Quem usa:** juridico · **Rodada:** A

## Objetivo
Barrar não basta (D-025): toda Falta jurídica traz o porquê e um caminho de liberação. O guia orienta e prepara; **Vicente decide, assina e protocola**.

## Quando usar / quando não usar
- **Usar:** para cada tipo de Falta jurídica recorrente (ordem de provável uso: SisGen e consentimento prévio informado, Lei 13.123; licença de texto, imagem e áudio, Lei 9.610; consentimento e atendimento ao titular, LGPD; registro de bem imaterial no IPHAN, Decreto 3.551 e Res. IPHAN 1/2006).
- **Não usar:** para dizer que algo "está liberado"; para dar parecer; para casos que a lei reserva a profissional habilitado (o guia diz isso e o passo vira "contratar ou consultar").

## Entradas e saídas
- **Entrada:** a Falta (formato `esquemas/falta.schema.json`) ou o tipo de barreira; as conferências já feitas (ex.: `trilhas/2026-10-16_conferencias/lote-C1.json`).
- **Saída:** objeto JSON válido em `esquemas/guia-liberacao.schema.json`: `por_que_barrado` (explicação simples + norma + trecho literal + URL + nível), `o_que_destravaria`, `quem_pode_fazer` (com nível), `passos` (n, o que fazer, onde, como preencher, nível, URL), `documentos`, `exige_profissional`, `limites`, `estado`, `nao_conferido`, `versao`, `data`.

## Passos
1. Parta das normas já conferidas no projeto (C1, Anexo C); só confira de novo se faltar (habilidade `conferir-fato`, com teto).
2. Escreva o porquê em português simples, seguido do trecho literal e da URL.
3. Liste o que destravaria (cadastro, consentimento, licença, parecer, consulta).
4. Escreva os passos na ordem real. Cada passo tem o nível do que afirma: o que é lei pode ser "oficial"; **tela de sistema só é "oficial" se a página oficial do sistema ou o manual atual foi aberto**; senão, "não conferido".
5. Para cada campo de formulário conhecido pela norma, diga como preencher no caso do projeto (sem inventar dado).
6. Liste os limites (nunca autoriza, nunca protocola, revisão profissional quando a lei exige) e o que não foi conferido.
7. Valide: `echo '<json>' | python scripts/validar.py guia-liberacao -`. Termine com o bloco LOG.

## Regras herdadas
- **Nível:** "oficial" exige URL e leitura da página oficial; o resto é "secundária" ou "não conferido".
- **Essência:** D-020 (cria Faltas, nunca autoriza) e D-025 (porquê e caminho; nenhuma obrigação desprezada; biblioteca informativa, não réplica da lei).
- **Dado pessoal:** nenhum dado de terceiro no guia; os modelos de documento ficam com campos em branco para Vicente.
- **Anti-robô:** sistemas com login ou bloqueio não se contornam; o passo fica "não conferido".
- **Falta dita:** o guia não fecha a Falta; só o comprovante real muda o estado para "liberado".

## Teto e custo
Até 10 chamadas web por guia quando é preciso conferir algo novo; 0 quando as normas já estão conferidas. Estimativa: 20 a 50 mil tokens em Sonnet 5.5 alto (a medir no Passo 1).

## Critério de parada
Todos os campos do esquema preenchidos, ou teto atingido (o que faltar vai para `nao_conferido`).

## O que não faz
Não autoriza, não protocola, não preenche cadastro em nome de Vicente, não dá parecer, não publica guia antes de os formulários e prazos serem conferidos no portal oficial.

## Campos do log
`agente: "juridico"`, `habilidade: "guia-de-liberacao"`, `versao_harness`, `entrada_ref` (ID da Falta ou do guia), `acoes` (normas usadas), `resultados` (passos e níveis), `decisoes` (passos sem conferência oficial = `falta`), `erros`.

## Exemplos e validador
- [exemplos/guia-sisgen.json](exemplos/guia-sisgen.json): o SisGen. Cadastro declaratório que pessoa natural pode fazer (Lei 13.123, art. 2º, XII; Decreto 8.772, arts. 22 e 22-A; C1, oficial). As telas não foram conferidas e estão marcadas assim. **Passa.**
- [exemplos/erro-tela-oficial-sem-url.json](exemplos/erro-tela-oficial-sem-url.json): um passo de tela marcado "oficial" sem URL. **Reprova.**
- [exemplos/erro-sem-limites.json](exemplos/erro-sem-limites.json): guia sem a lista de limites (o que o agente não faz). **Reprova.**
- Validador: `scripts/validar.py guia-liberacao`.

## Histórico
- 0.1.0 (16/10/2026): primeira versão, com o caso SisGen do C1.
