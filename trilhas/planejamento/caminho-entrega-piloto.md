# Caminho curto para entregar o piloto — [PROPOSTA]

**Estado:** proposta de 14/11/2026, escrita a pedido de Vicente. **Não é plano**: só vale depois da decisão
dele registrada (seria a D-056). Até lá valem a D-053, a D-054 e a D-055 como estão.

**Alcance desta leitura:** o quadro, o `RETOMAR.md`, os blocos 11 e 14 do brief, a tabela de
`testes/relatorio-modelos.md`, os insumos 133 e 134, a fila (`fila_ia.py --resumo`) e a contagem das
pastas. Não foram relidos o checklist inteiro, a Fundação nem os logs.

## 1. O que o piloto precisa mostrar e o que já mostra

O piloto é o teste da ferramenta inteira com a cajuína (D-032, D-035; brief, l. 12). São cinco verbos:

| A ferramenta precisa | Está feito? | Onde |
|---|---|---|
| coletar | sim | K-108, K-108b, K-112: rotina diária sem IA (BDTD, Infoteca-e, Oasisbr, BCR) |
| receber pelas formas da fase 1 | sim | K-107, K-110: o registro do IPHAN entrou por link de Vicente |
| organizar no wiki | sim | K-110: ficha CL-0001, camada Educação, wiki local |
| gerar o grafo 4D | sim | K-110: `grafo/`, μ e λ batendo com o recálculo |
| criar proposta sob demanda | **não** | K-114: o kit de fonte primária (1 a 2 chamadas e a revisão de Vicente) |
| relatório do piloto | **não** | K-116: redator e auditor (2 chamadas) |

Falta, para entregar: **o kit e o relatório**. O resto da fila não é função do piloto.

## 2. O que está tomando o tempo e não é o piloto

- **K-125 (a IA da operação no Gemini).** A chave está no nível gratuito: 20 pedidos por dia, sem cota no
  modelo de raciocínio. As provas do modelo leve reprovaram, e uma prova de 2 Entradas gastou 300 mil
  tokens de entrada (insumo 134), com o teto semanal em 1 milhão. As próximas provas só depois de 18/11.
  É a escolha de **quem paga a IA da operação**, não o piloto.
- **K-115b e K-115c (testes de modelo).** Procuram o modelo mais barato que passa em cada habilidade. Os
  agentes já funcionam nos modelos que têm. É **economia da operação**, não o piloto.

Nenhum dos dois toca o rigor da base. Os dois gastam a conta que o kit e o relatório pedem.

## 3. O que não se toca

O trecho literal localizado por script; o `validar_acervo.py` no pre-commit; o portão; "quem propõe não
aprova" (segunda leitura por outro agente); a triagem jurídica e as Faltas; o log com alcance; a busca de
dado pessoal antes de cada commit; a rotina diária sem IA. É isto que faz a ferramenta ser melhor que uma
busca ou uma pergunta a uma IA, e é isto que a mantém de pé com qualquer IA: os dados são JSON e Markdown
validados por esquema, as regras são scripts sem IA, e a IA só **propõe**; quem aceita é a regra. O
executor do K-125 já mostrou que o proponente pode ser trocado de fornecedor sem mexer no resto.

## 4. A proposta, em três movimentos

1. **Estacionar, com o estado salvo, o que é economia da operação.** O K-125 fecha no ponto em que está
   (executor, workflow desligado, medidas e provas gravados). O K-115b e o K-115c saem do caminho do
   piloto. Os três vão à reunião do K-004 (D-046) com o que já ensinaram (insumos 119 a 134 e a tabela de
   modelos). O teste de modelo do kit (D-051) sai do K-114. Nada se apaga.
2. **A IA da operação, enquanto não houver financiamento:** a rotina do Claude do K-113, que foi testada e
   fechada em 13/11, dentro dos tetos da D-050 (20% da semana, 50% da janela de 5 h): o avaliador propõe
   (Haiku 5.5, que passou no K-115a), o auditor relê, o portão decide. O Gemini volta quando houver cota
   paga, pela mesma lógica da D-049. Isto muda a D-054 e a D-055: é decisão de Vicente.
3. **Entregar:** o K-114 (kit, rascunho com fontes, revisado por Vicente, sem publicar) e depois o K-116
   (relatório do piloto, com o que foi estacionado dito às claras e os números do que a ferramenta já
   processou). Com o relatório conferido, o piloto está entregue e abre-se a reunião do K-004.

**A primeira execução em escala** (a fila tem 2.544 Entradas, de todas as CLB) é o primeiro ato da
operação, pela rotina semanal, e não condição da entrega. Se Vicente quiser lotes antes do relatório, cada
lote de 15 Entradas custa, por estimativa a medir no primeiro, 3 a 4 pp da semana (avaliador e segunda
leitura).

## 5. A conta (estimativa; base: 2 pp por conversa e 1,6 pp por 100 mil tokens de agente, D-040)

| Passo | Chamadas | Custo estimado |
|---|---|---|
| K-114, kit | 1 a 2 | 4 a 5 pp |
| K-116, relatório | 2 | cerca de 5 pp |

Em 14/11 a semana da conta estava em cerca de 81% (estimado), com a linha em 90% e a virada em 18/11, 23h.
Cabe **um** dos dois passos antes da virada e o outro logo depois: a entrega fica para 19 ou 20/11. O que
limita a semana é a conta, não o plano.

## 6. O que Vicente confirma ou corrige (essência para a D-056)

> O piloto se entrega com o kit (K-114) e o relatório (K-116). O K-125, o K-115b e o K-115c ficam
> estacionados, com o estado salvo, e vão à reunião do K-004; o teste de modelo do kit sai do K-114. Até
> haver financiamento, a IA da operação é a rotina do Claude do K-113, nos tetos da D-050; o Gemini volta
> com cota paga. O rigor (trecho localizado, validador, portão, segunda leitura, triagem jurídica, logs)
> fica como está. A primeira execução em escala é da operação, depois da entrega.

## 7. O que fica para a reunião do K-004

- Os três cartões estacionados e a tabela de modelos por fechar.
- As decisões D-015 a D-055 no `AGENTS.md` (16,8 mil caracteres, carregados em toda conversa e em todo
  agente): entram na próxima versão da Fundação e saem de lá; só Vicente pode encurtar as essências.
- Quando a vistoria da casa (`scripts/manutencao.py`) roda sozinha (insumo de 14/11).
