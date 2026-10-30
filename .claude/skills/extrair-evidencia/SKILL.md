---
name: extrair-evidencia
description: Triagem por valências, quarentena e extração de Evidências com trecho literal (texto exato, antes, depois, localizador e voz) ligadas a Proposições, no projeto Cultura Líquida. Exemplos reais do caso-piloto (rodada B).
---

# extrair-evidencia

**Versão do harness:** 0.2.0 · **Quem usa:** avaliador · **Rodada:** B · **Estado:** exemplos reais do piloto (rodada B, K-111).

## Objetivo
De uma Entrada, tirar Evidências verificáveis — cada uma um trecho da fonte — e ligá-las a Proposições (CLB situada × atributo × valor × período), sem julgar a prática (D-019).

## Quando usar / quando não usar
- **Usar:** a partir do caso-piloto, em lotes de até 15 Entradas.
- **Não usar:** antes do caso-piloto; para conferir trecho por IA (a localização é por script).

## Entradas e saídas [PROPOSTA, contrato no Passo 1]
- **Entrada:** Entrada (ID, fonte, texto lido no momento da extração ou cópia do Wayback).
- **Saída:** Evidências no formato do seletor de citação da W3C Web Annotation (texto exato, um pedaço antes, um depois, localizador), mais: voz (autor, pessoa citada em fala direta, instituição, anúncio), hash do texto lido, data; Proposição ligada; eixo "localização do trecho" (localizado / não localizado / não verificável por máquina); triagem por valências; quarentena com `PENDENTE_JULGAMENTO` quando não passa; a marca "sustenta aviso, saúde ou política" quando o item sustenta um deles (D-038; l. 473).

## Passos
1. Leia a Entrada e aplique a triagem por valências (P85–P87), sem zerar um critério ao ajustar outro. A escala de valências é a do registro de valores do bloco 2: mede lastro, trecho localizado e voz, e não dá peso a uma fonte por ser institucional (D-039). Toda fonte, inclusive a institucional, nasce candidata e passa pela regra (D-039).
2. Marque o item que sustenta aviso, saúde ou política: ele vai ao auditor da segunda leitura, fora da amostra sorteada (D-038; l. 473).
3. O que não passa vai para a quarentena; nada é descartado (princípio 10). A saída da quarentena é pela regra versionada do registro de valores, pelo portão, nunca por veredito item a item; cada saída se registra como Execução, com a versão da regra e o motivo em `decisoes` (`automatica: true`, `versao_regra`) (padrão A-05, D-038).
4. Marque os trechos candidatos e rode o script de localização (bloco 3 do brief); abaixo do limiar, o trecho fica Falta "não verificável por máquina", dita e nunca completada (D-018), sem ir a ninguém nem à cota humana; a busca assistida pode resolvê-la como fato novo (leitura A-06, D-038).
5. Registre a voz do trecho; W só se ancora na fala de quem pratica ([PROPOSTA], FH-5).
6. Ligue cada Evidência a uma Proposição; fonte contrária documenta, não corrige (D-019).
7. **Leitura fiel** (insumo 72): a Proposição diz só o que o trecho diz, sem palavra de outro trecho e sem perder qualificativo; a voz é a de quem fala no trecho; a marca de aviso, saúde ou política vale igual para todas e vai à Proposição.
8. **Outra CLB no ato** (insumos 88 e 89): o trecho que nomeia outra bebida sai separado, com a forma no texto exato (o rótulo só com a palavra que o trecho traz); sem o termo no trecho, sai "sem termo". O curador grava com `mencoes_incidentais.py --separadas` e `gravar_extracao.py --clb`; o que uma Falta de conhecimento tradicional marca fica na pasta local (D-043, 3).
9. **Nomes** (insumo 76): `scripts/nomes_provaveis.py` sobre os Trechos do lote antes de devolver.
10. Grave a saída item a item e valide por arquivo (agente, seção "Gravar a saída").
11. Termine com o bloco LOG.

## Regras herdadas
Nível de verificação; essência (D-018, D-019); dado pessoal (pessoas só por papel e ID opaco); anti-robô; Falta dita.

## Teto e custo
Medido no piloto (logs, avaliador): 7 lotes, 1.212.590 tokens e 155 chamadas; de 126.968 a 212.245 tokens por lote de até 15 Entradas.

## Critério de parada
Fim do lote ou teto informado.

## O que não faz
Não julga a prática, não confere trecho por IA, não descarta, não ancora W sem a fala de quem pratica, não tira item da quarentena por veredito, não dá peso a uma fonte por ser institucional, não manda Falta abaixo do limiar à cota humana.

## Campos do log
`agente: "avaliador"`, `habilidade: "extrair-evidencia"`, cada Entrada em `decisoes` (aceito, descartado, quarentena ou falta, com motivo; nas decisões pela regra, `automatica: true` e a `versao_regra` aplicada, D-038); `alcance` (D-030).

## Exemplos e validador
**Rodada B (K-111):** pares reais do piloto em [exemplos/casos-rodada-b.json](exemplos/casos-rodada-b.json), rodados pelo `testes/rodada-b/caso_real.py` sobre uma cópia do acervo do momento; o que o piloto não deu está no [exemplos/LEIA-ME.md](exemplos/LEIA-ME.md). Relatório: `testes/relatorio-rodada-B.md`.

## Histórico
- 0.2.0 (30/10/2026, K-111): exemplos reais da rodada B (TR-0001, TR-0034, TR-0101, PR-0001, PR-0002, TR-0505); leitura fiel com os achados A1 a A5 do K-109 (insumo 72); rótulo só com a palavra do trecho (insumo 88); outra CLB separada no ato e gravada com `gravar_extracao.py --clb` (insumos 89 e 92); nomes prováveis (insumo 76); saída item a item (insumos 29, 71, 74); custo medido.
- 0.1.1 (22/10/2026, K-101): abaixo do limiar, Falta "não verificável por máquina" dita e nunca completada, sem cota humana (leitura A-06, D-038); quarentena e saída pela regra versionada, registrada com a versão da regra (padrão A-05, D-038); escala de valências do registro do bloco 2, sem peso institucional (D-039); marca do item que sustenta aviso, saúde ou política, que vai ao auditor fora da amostra (D-038; l. 473).
- 0.1.0 (16/10/2026): papel, formato e passos (D-029).
