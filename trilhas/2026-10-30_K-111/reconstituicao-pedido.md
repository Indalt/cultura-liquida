# Teste de reconstituição do K-111 (princípio 11; Fundação, l. 709 e 726)

Uma conversa nova, só com o repositório, retoma o trabalho do ponto salvo. Vicente abre a conversa nova nesta pasta e cola o pedido abaixo; a conversa grava a resposta em `trilhas/2026-10-30_K-111/reconstituicao-resposta.md`; depois, a conversa do K-111 (esta ou a seguinte) confere pelo critério.

## O pedido (colar na conversa nova, sem mudar)

```
Teste de reconstituição (princípio 11). Use só o que está neste repositório: não use o que você lembrar de outras conversas nem pesquise na web. Não altere nenhum arquivo do repositório além do arquivo de resposta, não lance agentes e não faça commit.

Responda, com o caminho do arquivo (e a linha, quando der) de onde tirou cada coisa:
1. O que é este projeto e qual é o caso-piloto.
2. Qual é o ponto salvo: o cartão em curso, o que dele já está feito e o que falta para fechá-lo.
3. Qual é o próximo passo depois dele, em cada frente, pela ordem do quadro.
4. Rode scripts/relatorio_dia.py e scripts/rodar_testes.py e diga os totais (OK, FALHA, PENDENTE) e o que estiver pendente, com o porquê.
5. O que vive fora do Git, onde fica e se falta algo disso nesta máquina para retomar.
6. O que você não conseguiu achar ou confirmar só com o repositório.

Grave a resposta em trilhas/2026-10-30_K-111/reconstituicao-resposta.md e mostre-a aqui.
```

## O que conta como passar

A conferência marca cada item como passa ou não passa, com o trecho da resposta e o arquivo de origem:

1. **Projeto e piloto:** diz que é a Cultura Líquida Brasileira (encontrar, organizar e devolver o que se sabe sobre as bebidas e o que as faz existir, com rastreabilidade) e que o piloto é a cajuína (CL-0001), teste da ferramenta, sem publicação.
2. **Ponto salvo:** acha o K-111 em "Fazendo" no quadro; diz o que está feito (pares reais da rodada B, relatório da rodada B, harness 0.2.0, README) e o que falta (a reconstituição conferida e a aprovação de Vicente do harness pronto, a parada do bloco 9).
3. **Próximo passo:** pelo quadro, no desenvolvimento, o K-112 (bloco 10a) na sua vez e o K-113 e o K-115 à espera da aprovação do K-111 (o K-113 também do K-002); no planejamento, o K-002; na operação, o K-207, de baixa prioridade, sem chamar Vicente.
4. **Testes:** roda os dois scripts e dá os totais que eles imprimem, com FALHA 0 e o único PENDENTE no kit-fonte-primaria (bloco 11, fora do critério do bloco 9). Os números têm de bater com uma nova execução na conferência.
5. **Fora do Git:** nomeia a tabela de pessoas, a pasta de conhecimento tradicional, o legado, o wiki local, o bruto da coleta e a pasta temporária das fontes (descartável), sem trazer conteúdo delas.
6. **Sem invenção:** cada resposta tem o arquivo de origem; o que não achou, diz que não achou; não muda arquivo além da resposta, não decide nada novo, não lança agente.

**Passa** quando os seis itens passam. Um item que não passa vira o motivo, com o que faltou no repositório para a conversa nova achar; o reparo entra no K-111 antes da aprovação, e o teste se repete.
