---
name: gerar-grafo
description: Gera o grafo 4D paraconsistente do projeto Cultura Líquida (pontos com X, Y, Z e W; arestas com as afirmações que as sustentam) e calcula por script os graus de evidência μ e λ por linhagens independentes, mais Dc e Dct.
---

# gerar-grafo

**Versão do harness:** 0.2.0 · **Quem usa:** arquivista · **Rodada:** B · **Estado:** exemplos reais do piloto (rodada B, K-111).

## Objetivo
Um grafo em que contradições convivem sem trivializar o sistema (princípio 3): μ e λ descrevem quanta documentação há a favor e quanta divergente foi registrada; não são veredito.

## Quando usar / quando não usar
- **Usar:** no Passo 7, com conteúdo verificado; em testes, no caso-piloto.
- **Não usar:** para estimar μ e λ por IA; antes de haver Evidências com linhagem.

## Entradas e saídas [PROPOSTA, contrato no Passo 1]
- **Entrada:** Proposições, Evidências com `deriva_de` (linhagem), Compreensões locais, Transformações.
- **Saída:** pontos (elemento de prática com X, Y, Z, W), arestas (origem, destino, tipo, afirmações, Z, W, μ, λ), e os graus Dc = μ − λ e Dct = μ + λ − 1; estado (verdadeiro, falso, inconsistente = há documentação divergente, paracompleto = Falta, e intermediários).

## Passos
1. Agrupe as Evidências por linhagem independente (dez textos que copiam o mesmo autor contam como um).
2. Calcule μ e λ por script, sem peso por tipo de fonte ([PROPOSTA] do plano, item 3).
3. Calcule Dc e Dct e o estado.
4. Coordenada W não captada = Falta (paracompleto à vista).
5. O Z e o X de cada Elemento vêm de Proposição que os diga; o Z é o do gesto descrito, não o da história contada; sem ela, Falta (insumo 82).
6. Termine com o bloco LOG.

## Regras herdadas
Nível de verificação; essência (D-018, D-019; o grafo 4D fica fora da revisão de essencialidade, D-025); dado pessoal; anti-robô; Falta dita.

## Teto e custo
Script; IA só para o que exige juízo. Medido no piloto (logs, arquivista): 1 execução, 104.796 tokens e 15 chamadas; o cálculo de μ e λ é por script, sem tokens.

## Critério de parada
Grafo gerado e conferido pelos scripts.

## O que não faz
Não estima graus por IA, não julga, não esconde a contradição nem a Falta.

## Campos do log
`agente: "arquivista"`, `habilidade: "gerar-grafo"`, `entrada_ref` (commit dos dados).

## Exemplos e validador
**Rodada B (K-111):** pares reais do piloto em [exemplos/casos-rodada-b.json](exemplos/casos-rodada-b.json), rodados pelo `testes/rodada-b/caso_real.py` sobre uma cópia do acervo do momento; o que o piloto não deu está no [exemplos/LEIA-ME.md](exemplos/LEIA-ME.md). Relatório: `testes/relatorio-rodada-B.md`.

## Histórico
- 0.2.0 (30/10/2026, K-111): exemplos reais da rodada B (PR-0016 e PR-0065); Z e X do Elemento por Proposição que os diga (insumo 82); custo medido.
- 0.1.0 (16/10/2026): papel, formato e passos (D-029).
