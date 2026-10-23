---
name: registrar-termo
description: Registra um Termo do projeto Cultura Líquida como entrada terminológica (conceito, designações, variantes com uso no lugar e no tempo, abonações com fonte, booleanos derivados), nascendo candidato e virando atestado com a primeira abonação localizada. Harness pendente do caso-piloto do Passo 1.
---

# registrar-termo

**Versão do harness:** 0.1.1 · **Quem usa:** arquivista · **Rodada:** B · **Estado:** papel, formato e passos escritos; contrato em `esquemas/termo.schema.json` (0.2.0); **exemplos pendentes: caso-piloto (Passo 1)**.

## Objetivo
Que o glossário seja o motor de busca: um único registro de Termo gera, por script, os booleanos, os links do wiki e o glossário (princípio 2; plano, item 6).

## Quando usar / quando não usar
- **Usar:** ao achar uma designação ou variante nova numa fonte; ao migrar termos do legado (entram como candidatos, Passo 3).
- **Não usar:** para formas de busca (OCR, grafia truncada), que vão só ao booleano.

## Entradas e saídas
- **Entrada:** designação, fonte e trecho localizado (quando houver).
- **Saída:** Termo no modelo conceito → designações → variantes (tipo de variação: regional, étnica, histórica, grafia antiga; lugar; período) → abonações (Evidências com fonte), exportável para SKOS e TBX; estado candidato ou atestado; booleanos derivados. **Esquema:** `esquemas/termo.schema.json` (0.2.0). Cada designação é um objeto `{"forma": ...}`; quando a fonte der a língua, `lingua` (etiqueta BCP 47, como `pt-BR`) e `lingua_fonte` (a Evidência ou a URL que a dá), o mesmo na variante (insumo 30: no TBX, a seção de língua; no SKOS, o rótulo com a etiqueta). Validar: `.venv/Scripts/python.exe scripts/validar.py termo <arquivo>`.

## Passos
1. Procure o conceito existente; se não houver, crie o Termo candidato.
2. Separe variante linguística de forma de busca.
3. Dê a língua da designação e da variante **só quando a fonte a der**, com `lingua_fonte`; sem ela, deixe sem língua (a exportação usa `und`). Nunca infira a língua.
4. Ligue a abonação (trecho localizado) e mude para atestado.
5. Gere os booleanos por script (`scripts/gerar_termo.py`, regra termo-0.2) e sinalize ao rastreador a busca nova.
6. Termine com o bloco LOG.

## Regras herdadas
Nível de verificação; essência (D-017: termos não limitam a busca; D-018); dado pessoal; anti-robô; Falta dita.

## Teto e custo
A medir no caso-piloto.

## Critério de parada
Termo registrado com estado, variantes e abonações disponíveis.

## O que não faz
Não impõe taxonomia de cima; não trata a variação como ruído; não atesta sem abonação localizada.

## Campos do log
`agente: "arquivista"`, `habilidade: "registrar-termo"`, `entrada_ref` (ID do termo).

## Exemplos e validador
**Pendente: caso-piloto (Passo 1).** Ver [exemplos/LEIA-ME.md](exemplos/LEIA-ME.md).

## Histórico
- 0.1.1 (23/10/2026, K-106): contrato do Termo 0.2.0 com a língua da designação e da variante só quando a fonte a der, e de onde ela veio (insumo 30); passo 3 novo; booleanos pelo `gerar_termo.py` (termo-0.2).
- 0.1.0 (16/10/2026): papel, formato e passos (D-029).
