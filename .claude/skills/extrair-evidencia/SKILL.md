---
name: extrair-evidencia
description: Triagem por valências, quarentena e extração de Evidências com trecho literal (texto exato, antes, depois, localizador e voz) ligadas a Proposições, no projeto Cultura Líquida. Harness pendente do caso-piloto do Passo 1; não usar antes dele.
---

# extrair-evidencia

**Versão do harness:** 0.1.0 · **Quem usa:** avaliador · **Rodada:** B · **Estado:** papel, formato e passos escritos; **exemplos pendentes: caso-piloto (Passo 1)**.

## Objetivo
De uma Entrada, tirar Evidências verificáveis — cada uma um trecho da fonte — e ligá-las a Proposições (CLB situada × atributo × valor × período), sem julgar a prática (D-019).

## Quando usar / quando não usar
- **Usar:** a partir do caso-piloto, em lotes de até 15 Entradas.
- **Não usar:** antes do caso-piloto; para conferir trecho por IA (a localização é por script).

## Entradas e saídas [PROPOSTA, contrato no Passo 1]
- **Entrada:** Entrada (ID, fonte, texto lido no momento da extração ou cópia do Wayback).
- **Saída:** Evidências no formato do seletor de citação da W3C Web Annotation (texto exato, um pedaço antes, um depois, localizador), mais: voz (autor, pessoa citada em fala direta, instituição, anúncio), hash do texto lido, data; Proposição ligada; eixo "localização do trecho" (localizado / não localizado / não verificável por máquina); triagem por valências; quarentena com `PENDENTE_JULGAMENTO` quando não passa.

## Passos
1. Leia a Entrada e aplique a triagem por valências (P85–P87), sem zerar um critério ao ajustar outro.
2. O que não passa vai para a quarentena; nada é descartado (princípio 10).
3. Marque os trechos candidatos e rode o script de localização (Passo 2); abaixo do limiar, Falta "não verificável por máquina" para a cota humana.
4. Registre a voz do trecho; W só se ancora na fala de quem pratica ([PROPOSTA], FH-5).
5. Ligue cada Evidência a uma Proposição; fonte contrária documenta, não corrige (D-019).
6. Termine com o bloco LOG.

## Regras herdadas
Nível de verificação; essência (D-018, D-019); dado pessoal (pessoas só por papel e ID opaco); anti-robô; Falta dita.

## Teto e custo
A medir no caso-piloto.

## Critério de parada
Fim do lote ou teto informado.

## O que não faz
Não julga a prática, não confere trecho por IA, não descarta, não ancora W sem a fala de quem pratica.

## Campos do log
`agente: "avaliador"`, `habilidade: "extrair-evidencia"`, cada Entrada em `decisoes` (aceito, descartado, quarentena ou falta, com motivo).

## Exemplos e validador
**Pendente: caso-piloto (Passo 1).** Ver [exemplos/LEIA-ME.md](exemplos/LEIA-ME.md).

## Histórico
- 0.1.0 (16/10/2026): papel, formato e passos (D-029).
