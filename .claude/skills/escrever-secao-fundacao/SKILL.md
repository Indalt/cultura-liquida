---
name: escrever-secao-fundacao
description: Escreve um grupo de seções da Fundação do projeto Cultura Líquida (00_Fundacao_Cultura_Liquida.md), fundindo as camadas do plano num texto final único, com as essências confirmadas por Vicente (nunca a transcrição da fala), marcadores [VIGENTE] e [PROPOSTA], termos explicados e fatos com nível. Use no Bloco 3 do brief, um grupo de seções por vez.
---

# escrever-secao-fundacao

**Versão do harness:** 0.1.0 · **Quem usa:** redator · **Rodada:** A

## Objetivo
Produzir o texto final de um grupo de seções que qualquer sessão de IA leia e siga, curto nas seções de leitura padrão e com o longo nos anexos.

## Quando usar / quando não usar
- **Usar:** na v0.2 (grupos: cabeçalho, §0 e §1; §2; §3–§5; §6; §7–§11; Anexos C, D e E) e nas versões seguintes.
- **Não usar:** para criar ou mudar decisão (isso é `registrar-decisao`, com Vicente); para os Anexos A e B (intocáveis); para conferir fatos.

## Entradas e saídas
- **Entrada (do curador):** o grupo; as faixas de linhas da v0.1; a linha do mapa do Bloco 3 (o que fazer, fonte no plano); as essências ([referencias/essencias.json](referencias/essencias.json)); os resultados das conferências (C1, C2) quando o grupo usa fatos.
- **Saída:** o texto escrito direto no arquivo, no lugar das seções do grupo; e o bloco LOG.

## Passos
1. Leia só as faixas indicadas (`grep -n "^## \|^### "` para achar; `sed -n 'a,bp'` para ler).
2. Para cada item do mapa, escreva **um** texto final que funde corpo, ajustes dos lotes A e B e descartados. O plano guarda as camadas; a Fundação, não.
3. **Decisões:** use a essência de `referencias/essencias.json`. Nunca cole a fala original (as frases de [referencias/falas.json](referencias/falas.json) não podem aparecer literalmente).
4. Marque [VIGENTE] o que Vicente decidiu e [PROPOSTA] o desenho. Nenhum item [PROPOSTA] vira plano sem decisão.
5. Explique cada termo técnico na primeira vez que aparece (uma oração simples). Pn: "pedido n de Vicente, Anexo A; buscar `#### Pn`".
6. Fato: com URL e nível, ou "a conferir no Passo n". Nada de memória.
7. **Autoconferência antes de entregar:**
   - `python scripts/checar_fundacao.py <arquivo> --so-essencias --essencias .claude/skills/escrever-secao-fundacao/referencias/essencias.json --falas .claude/skills/escrever-secao-fundacao/referencias/falas.json`;
   - `python scripts/comparar_anexos.py`.
   Se algo reprovar, corrija antes de entregar. A verificação final é do auditor.
8. Termine com o bloco LOG.

## Regras herdadas
- **Nível de verificação:** todo fato com URL e nível.
- **Essência:** a régua é a seção 2 do brief; palavra ambígua de Vicente não se interpreta sozinho ("por princípio" foi "de início"): na dúvida, pergunte ao curador.
- **Dado pessoal:** nenhum dado de terceiro no texto.
- **Anti-robô:** não se aplica (sem web).
- **Falta dita:** o que não se sabe aparece como Falta ou "a conferir", nunca preenchido.

## Teto e custo
Um grupo por chamada; até 40 turnos. Estimativa: 40 a 120 mil tokens por grupo em Opus 5.5 médio (a medir no Bloco 3).

## Critério de parada
Grupo escrito e autoconferência passando; ou lacuna que o brief e o plano não resolvem (devolver a pergunta ao curador, sem inventar).

## O que não faz
Não altera os Anexos A e B; não muda o sentido de decisão; não transcreve falas; não lê o legado; não confere o próprio texto como verificação final.

## Campos do log
`agente: "redator"`, `habilidade: "escrever-secao-fundacao"`, `entrada_ref` (grupo e faixas de linhas), `acoes` (seções escritas), `resultados` (linhas resultantes, resultado da autoconferência), `decisoes` (itens do plano fundidos = `aceito`; descartados do plano = `descartado`, com o motivo), `erros`.

## Exemplos e validador
- [exemplos/secao9-boa.md](exemplos/secao9-boa.md): as D-015 a D-029 pelas essências da seção 2 do brief. **Passa.**
- [exemplos/secao9-transcricao.md](exemplos/secao9-transcricao.md): a D-018 escrita como transcrição literal da fala de Vicente, no lugar da essência. **Reprova** (transcrição e perda de "traduzível").
- Validador: `scripts/checar_fundacao.py --so-essencias --essencias ... --falas ...`. Casos: [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.0 (16/10/2026): primeira versão.
