# Conferência do teste de reconstituição do K-111 (31/10/2026)

O curador conferiu a resposta (`reconstituicao-resposta.md`, da conversa nova aberta por Vicente em 30/10 e terminada em 31/10) pelos seis critérios de `reconstituicao-pedido.md`.

| # | Critério | Resultado | Onde está na resposta |
|---|---|---|---|
| 1 | Projeto e piloto | **passa** | Item 1: CLB, com rastreabilidade; a cajuína como CL-0001; o piloto é teste e não publicação (D-031, D-032). |
| 2 | Ponto salvo | **passa** | Item 2: o K-111 em Fazendo (quadro, l. 34); os lotes 1 a 3, o auditor (EX-0097) e o relatório da rodada B; falta a reconstituição, a conferência dela e a aprovação de Vicente. |
| 3 | Próximo passo | **passa** | Item 3: o K-112 na sua vez; o K-113 à espera da aprovação e do K-002; o K-115 à espera da aprovação; o K-002 no planejamento; o K-207 na operação, sem chamar Vicente. |
| 4 | Testes | **passa** | Item 4: OK 241 · FALHA 0 · PENDENTE 1, só no kit-fonte-primaria (bloco 11), com o porquê. A nova execução na conferência deu o mesmo total: OK 241 · FALHA 0 · PENDENTE 1. |
| 5 | Fora do Git | **passa** | Item 5: tabela de pessoas, conhecimento tradicional, legado, wiki local, bruto da coleta e pasta temporária, sem conteúdo; o gancho ligado. |
| 6 | Sem invenção | **passa** | Cada item com o arquivo de origem; o que não achou está dito (item 6); só o arquivo de resposta foi criado (`git status`: um arquivo novo). |

**Resultado: passa.**

## Observações (não mudam o resultado)

- **Item 6.2:** o `relatorio_dia.py` mostra "61 pp de 50" sem a suspensão dos tetos que Vicente deu nesta semana. Já está no insumo 98 (K-002).
- **Item 6.6:** a resposta leu a l. 390 do brief como se fosse do bloco 11, mas ela é a entrada do bloco 12. O bloco 11 (l. 381-387) não espera a aprovação do bloco 9, e o quadro está certo. Foi um erro de leitura da conversa nova, apontado como dúvida e não como fato; o repositório não precisa de reparo.
- **Item 6.7:** a suíte levou mais de 10 minutos na conversa nova. Nas execuções do K-111, levou de 3 a 5 minutos, quase todo o tempo no `validar_acervo.py` e nas cópias da rodada B. O tempo não tem valor de referência no repositório.
