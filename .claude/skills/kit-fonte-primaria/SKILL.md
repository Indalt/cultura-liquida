---
name: kit-fonte-primaria
description: Produz, sob demanda, o kit de fonte primária do projeto Cultura Líquida — o material que ensina alguém a registrar e enviar uma fonte primária (documento, depoimento já gravado, objeto) com trilha, consentimento e sem dado pessoal exposto. Harness pendente; só com pedido de Vicente e depois do caso-piloto.
---

# kit-fonte-primaria

**Versão do harness:** 0.1.0 · **Quem usa:** campo-de-acao · **Rodada:** B · **Estado:** papel, formato e passos escritos; **exemplos pendentes: caso-piloto (Passo 1)**.

## Objetivo
Ferramenta de ação (plano, item 20): ajudar quem tem uma fonte primária a registrá-la de modo que o projeto possa conferi-la, respeitando a fonte e as pessoas.

## Quando usar / quando não usar
- **Usar:** só quando Vicente pedir (princípio 15) e depois de decididas as portas de admissão (fase 1 não recebe contribuições externas).
- **Não usar:** como formulário de coleta automática; para publicar sem a triagem jurídica.

## Entradas e saídas [PROPOSTA, a definir no passo em que entra]
- **Entrada:** o pedido de Vicente (público, tier, formato).
- **Saída:** o kit (passos de registro, localizador, consentimento, licença de quem contribui, o que não enviar), revisado pelo juridico.

## Passos
1. Confirme o pedido e o público.
2. Monte o kit a partir das portas de admissão vigentes e dos tipos de evidência (plano, item 15).
3. Passe pela `triagem-juridica`; o que for Falta fica fora ou com o caminho de liberação.
4. Termine com o bloco LOG.

## Regras herdadas
Nível de verificação; essência (D-020, D-025); dado pessoal (crianças e adolescentes: nunca imagem, voz ou nome); anti-robô; Falta dita.

## Teto e custo
A medir.

## Critério de parada
Kit pronto pelos critérios do pedido.

## O que não faz
Não produz sem pedido; não dá parecer jurídico ou sanitário; não publica site.

## Campos do log
`agente: "campo-de-acao"`, `habilidade: "kit-fonte-primaria"`, `entrada_ref` (pedido).

## Exemplos e validador
**Pendente: caso-piloto (Passo 1).** Ver [exemplos/LEIA-ME.md](exemplos/LEIA-ME.md).

## Histórico
- 0.1.0 (16/10/2026): papel, formato e passos (D-029).
