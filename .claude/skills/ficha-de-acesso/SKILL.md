---
name: ficha-de-acesso
description: Monta ou atualiza a ficha de acesso de um ambiente de busca do projeto Cultura Líquida (hemeroteca, repositório, API, acervo) — via de acesso, sintaxe, endpoint, link permanente, termos de uso, robots, cobertura, uso (monitoramento ou escavação), nível e o resultado do último teste de acesso. Use antes de buscar num ambiente novo e quando um ambiente mudar de comportamento.
---

# ficha-de-acesso

**Versão do harness:** 0.1.1 · **Quem usa:** rastreador · **Rodada:** B

## Objetivo
Saber, antes de buscar, **como** cada ambiente pode ser lido, o que ele permite e o que respondeu no último teste, para não repetir erro nem contornar proteção.

## Quando usar / quando não usar
- **Usar:** ambiente novo; ambiente que mudou (erro, bloqueio, nova API); reconferências pendentes (termos do Google, Hemeroteca, Wikisource, tabela de biomas do IBGE, BHL).
- **Não usar:** para coletar conteúdo (isso é `consulta`); para ambientes que só pessoas podem usar, além de registrar que são de via humana.

## Entradas e saídas
- **Entrada:** nome do ambiente e o que já se sabe: o Anexo E da Fundação (ambientes candidatos) e a ficha em `ambientes/`, que é a fonte de trabalho a partir do bloco 2 do brief; o catálogo da pesquisa (`trilhas/2026-10-15_pesquisa/indice.md`, seção 1) fica como trilha.
- **Saída:** uma ficha com os campos do catálogo da pesquisa: `nome`, `tipo`, `acesso`, `como_buscar`, `endpoint`, `link_permanente`, `texto_integral`, `termos`, `robots`, `cobertura`, `uso` (monitoramento, escavação ou ambos), `nivel`, `teste` (data, pedido, resposta HTTP, observação). **Esquema:** pendente; o contrato de Ambiente (§6) é entrega do Passo 1. Até lá, valem os critérios de aceitação abaixo.

## Passos
1. Leia a linha do ambiente no Anexo E (`grep -n "<nome>" 00_Fundacao_Cultura_Liquida.md`) e a ficha em `ambientes/`, se houver; na falta dela, o índice da pesquisa.
2. Abra a página oficial de ajuda, API ou termos (WebFetch), e o `robots.txt`.
3. Faça **um** pedido de teste pequeno (`curl -s -o /dev/null -w "%{http_code}"` ou a API com `limit` baixo), com o robô identificado.
4. Registre a resposta tal como veio: 200, 403, captcha, erro de servidor, SSL. Se for bloqueio, **pare ali**: a via passa a ser humana.
5. Preencha a ficha; cada afirmação com URL e nível. Termine com o bloco LOG.

## Critérios de aceitação
- Todo campo preenchido ou marcado "não conferido", inclusive `robots` e `cobertura`.
- O teste traz data, pedido e resposta literal (código HTTP ou mensagem).
- Bloqueio anti-robô registrado como fato e **nunca contornado**.
- Uso classificado (monitoramento × escavação) e termos de uso citados com URL.

## Regras herdadas
- **Nível:** "oficial" só com a página oficial aberta.
- **Essência:** D-016 (sem teto de coleta), D-017 (exemplos não limitam: os ambientes do catálogo não são a lista fechada).
- **Dado pessoal:** só e-mails institucionais quando forem a via de acesso.
- **Anti-robô:** nunca se contorna.
- **Falta dita:** ambiente inacessível vira Falta "fonte inacessível" com a via humana indicada.

## Teto e custo
Até 6 chamadas por ambiente. Estimativa: 15 a 30 mil tokens em Sonnet 5.5 alto (a testar contra o Haiku 5.5 no Passo 1).

## Critério de parada
Ficha completa pelos critérios, ou bloqueio registrado, ou teto atingido.

## O que não faz
Não contorna proteção, não coleta conteúdo, não usa instâncias públicas de terceiros para driblar bloqueio, não guarda texto integral.

## Campos do log
`agente: "rastreador"`, `habilidade: "ficha-de-acesso"`, `entrada_ref` (nome do ambiente), `acoes` (pedidos feitos), `resultados` (códigos de resposta), `decisoes` (ambiente aceito como via automática, ou `falta` com a via humana), `ambientes` (o ID do ambiente), `erros`, `alcance` (páginas abertas e o que não abriu; D-030).

## Exemplos (reais, da pesquisa de 15/10)
- [exemplos/hemeroteca-403.json](exemplos/hemeroteca-403.json): a Hemeroteca Digital Brasileira recusou o leitor automático (403) → via humana.
- [exemplos/bdtd-api.json](exemplos/bdtd-api.json): a API do VuFind da BDTD funcionando, sem cadastro.
- [exemplos/querido-diario-instavel.json](exemplos/querido-diario-instavel.json): a API do Querido Diário funcionou em 3 de 5 chamadas.
- Casos (validador pendente): [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.1 (22/10/2026, K-101): entrada pelo Anexo E e por `ambientes/`; `robots` e `cobertura` nos três exemplos, com "não conferido" onde faltava dado; Ambientes e alcance no log.
- 0.1.0 (16/10/2026): papel, formato, passos e exemplos reais; esquema pendente do Passo 1.
