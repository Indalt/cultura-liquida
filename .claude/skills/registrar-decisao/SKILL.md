---
name: registrar-decisao
description: Registra um comentário novo de Vicente no projeto Cultura Líquida como decisão (D-nnn) — capta a essência, confere palavras ambíguas, devolve o entendido para confirmação e só então escreve a diretriz, no formato de esquemas/decisao.schema.json. Use sempre que Vicente fizer um comentário que mude ou acrescente regra.
---

# registrar-decisao

**Versão do harness:** 0.2.0 · **Quem usa:** curador · **Rodada:** A

## Objetivo
Que o texto de trabalho registre o **sentido** do que Vicente decidiu, confirmado por ele, e não a transcrição. A fala original fica só na trilha, por referência (plano, item 8).

## Quando usar / quando não usar
- **Usar:** comentário novo de Vicente que crie, mude ou substitua uma regra; decisão que o brief e o plano não cobrem (parada, caso a), depois da resposta dele.
- **Não usar:** para reconfirmar essências já confirmadas (seção 2 do brief); para decisões que não são de Vicente; para opiniões do agente.

## Entradas e saídas
- **Entrada:** a fala de Vicente (na conversa) e onde ela fica guardada na trilha.
- **Saída:** um objeto válido em `esquemas/decisao.schema.json`: `id`, `data`, `essencia`, `diretriz`, `confirmada_por_vicente: true`, `data_confirmacao`, `fala_original_ref`, `palavras_conferidas`, `substitui` (se for o caso), `marcador`. Depois, a entrada vai para o §9 da Fundação na próxima versão (acordo 5).

## Passos
1. **Capte a essência** em uma ou duas frases, no vocabulário do projeto.
2. **Confira as palavras ambíguas.** "Por princípio" pode ser "de início" (caso real, D-025); "talvez" é hipótese, não decisão; "privado" e "público" mudam regras (caso real, D-021). Anote cada uma em `palavras_conferidas`.
3. **Devolva a Vicente** o que entendeu e peça confirmação, com uma pergunta para compreender (acordo 1), nunca binária para direcionar.
4. **Só depois da confirmação**, escreva a diretriz (o que muda na prática) e preencha `confirmada_por_vicente: true` e `data_confirmacao`.
5. Se a decisão substitui outra, preencha `substitui` e registre o conflito no checklist.
6. Grave a fala original na trilha (checklist ou diário) e aponte-a em `fala_original_ref` (arquivo e seção).
7. Valide: `python scripts/validar.py decisao <arquivo>`. Grave o log.

## Regras herdadas
- **Nível:** a decisão não traz fato novo; se trouxer, com URL e nível.
- **Essência:** é o centro desta habilidade; nada de transcrição como diretriz.
- **Dado pessoal:** a fala de Vicente pode conter nomes de terceiros: eles não entram no registro.
- **Anti-robô:** não se aplica.
- **Falta dita:** o que Vicente não decidiu fica [PENDENTE] ou [ABERTO], nunca completado.

## Teto e custo
Sem web e sem subagente. Custo só da sessão principal.

## Critério de parada
Decisão confirmada e registrada; ou Vicente ainda não confirmou (fica pendente, sem diretriz).

## O que não faz
Não registra decisão sem confirmação, não interpreta sozinho palavra ambígua, não reabre decisão vigente por conta própria.

## Campos do log
`agente: "curador"`, `habilidade: "registrar-decisao"`, `entrada_ref` (ID da decisão), `acoes` (essência devolvida, confirmação), `decisoes` (`aceito` com o motivo "confirmada por Vicente em AAAA-MM-DD"), `erros`.

## Exemplos e validador
- [exemplos/d025-de-inicio.json](exemplos/d025-de-inicio.json): o "por princípio" que era "de início" (caso real de 16/10). **Passa.**
- [exemplos/d021-publico.json](exemplos/d021-publico.json): a D-021, que passou a público depois da janela 1 (caso real de 16/10). **Passa.**
- [exemplos/erro-sem-confirmacao.json](exemplos/erro-sem-confirmacao.json): diretriz escrita sem a confirmação de Vicente. **Reprova.**
- Validador: `scripts/validar.py decisao`. Casos: [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.2.0 (30/10/2026, K-111): versão do conjunto, sem mudança de regra.
- 0.1.0 (16/10/2026): primeira versão.
