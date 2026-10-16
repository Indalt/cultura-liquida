---
name: montar-ficha
description: Monta a ficha de uma CLB do projeto Cultura Líquida a partir das Proposições e Evidências, com toda frase apontando para as afirmações que a sustentam, a compreensão local (W) antes da tradução e as Faltas à vista. Harness pendente do caso-piloto do Passo 1.
---

# montar-ficha

**Versão do harness:** 0.1.0 · **Quem usa:** arquivista · **Rodada:** B · **Estado:** papel, formato e passos escritos; **exemplos pendentes: caso-piloto (Passo 1)**.

## Objetivo
Uma ficha que qualquer pessoa leia e possa conferir até a fonte (princípio 1).

## Quando usar / quando não usar
- **Usar:** quando uma CLB situada tiver Proposições com Evidências.
- **Não usar:** para publicar (publicação passa pelo juridico e pelo portão); para preencher lacuna.

## Entradas e saídas [PROPOSTA, contrato no Passo 1]
- **Entrada:** CLB situada, Proposições, Evidências, Faltas.
- **Saída:** cabeçalho (id, termos, X insumos, Y processos, Z períodos com dupla marcação, W compreensão local, territórios, status, avisos) e seções (definição; modo de fazer; ilustração técnica; temporalidade; quem ensina e como se transmite; territórios; tensões; avisos; educação; fontes; como citar). Cada frase com a marca da afirmação que a sustenta (formato definido no Passo 1).

## Passos
1. Junte as Proposições da CLB situada.
2. Escreva primeiro a compreensão local (W), depois a tradução.
3. Tensões (documentação divergente) ficam lado a lado; Faltas aparecem como tais.
4. Passe a ficha pela `triagem-juridica` antes de qualquer publicação.
5. Termine com o bloco LOG.

## Regras herdadas
Nível de verificação; essência (D-018, D-019, D-020); dado pessoal ("quem ensinou" só com consentimento, senão papel e ID opaco); anti-robô; Falta dita.

## Teto e custo
A medir no caso-piloto.

## Critério de parada
Ficha com todas as seções preenchidas ou marcadas como Falta.

## O que não faz
Não preenche Falta, não escreve frase sem afirmação que a sustente, não publica.

## Campos do log
`agente: "arquivista"`, `habilidade: "montar-ficha"`, `entrada_ref` (ID da CLB situada).

## Exemplos e validador
**Pendente: caso-piloto (Passo 1).** Ver [exemplos/LEIA-ME.md](exemplos/LEIA-ME.md).

## Histórico
- 0.1.0 (16/10/2026): papel, formato e passos (D-029).
