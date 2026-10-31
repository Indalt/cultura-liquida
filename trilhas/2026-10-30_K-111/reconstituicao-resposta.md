# Teste de reconstituição do K-111 — resposta

Conversa nova, aberta em 30/10/2026 e terminada em 31/10/2026 (a suíte de testes levou mais de 10 minutos). Usei só o repositório e, para o item 5, só a existência das pastas fora do Git nesta máquina, sem abrir o conteúdo delas. Não lancei agentes, não fiz commit e não alterei outro arquivo além deste.

O pedido e o critério estão em `trilhas/2026-10-30_K-111/reconstituicao-pedido.md`. Li o critério, mas cada resposta abaixo vem do arquivo de origem citado, não dele.

## 1. O projeto e o caso-piloto

- **O projeto:** Cultura Líquida Brasileira (CLB). É uma ferramenta para encontrar, organizar e devolver o que se pode saber sobre as bebidas do Brasil e tudo o que as faz existir (insumos, modos de fazer, recipientes, tempos, lugares, pessoas e transmissão), desde 1900, com cada informação rastreável até a fonte (`README.md:3`; `00_Fundacao_Cultura_Liquida.md:74`, Propósito; `AGENTS.md`, "O projeto em 5 linhas").
- **Os três movimentos:** rastrear, organizar e devolver e agir (`README.md:9-13`).
- **Fase 1:** só Vicente e os agentes, com logs. O repositório `Indalt/cultura-liquida` é público (`README.md:5`; `AGENTS.md`, D-021 e D-026).
- **A fonte de verdade:** a Fundação v0.2. A exceção são as linhas da seção 6A do brief de execuções (D-034, D-035), conforme `AGENTS.md` (topo) e `README.md:17,23`.
- **O caso-piloto:** a cajuína, CL-0001 (`README.md:15`; `trilhas/decisoes/D-031.json:4-5`). O trabalho começa pelo caju, o insumo (D-031). O piloto é um teste da ferramenta inteira e não é publicação (`README.md:15`; `trilhas/decisoes/D-032.json:5`; `AGENTS.md`, D-032).

## 2. O ponto salvo

- **O cartão em curso:** K-111, bloco 9 ("pares reais, rodada B, README e reconstituição"). Está na coluna **Fazendo desde 30/10/2026** (`trilhas/planejamento/quadro.md:34`). A parada do cartão é a aprovação de Vicente do harness pronto. O destino é FALHA 0 e PENDENTE 0 nas habilidades dos blocos 4 a 8, com a reconstituição passando.
- **O que já está feito** (`trilhas/planejamento/quadro.md:34`; `trilhas/2026-10-17_execucao-piloto.md:334-342`):
  - lote 1: `gravar_extracao` 0.3 com `--clb`, as Evidências separadas na CL-0002 e a PR-0011 movida para a CL-0004 (commit `857d672`);
  - lote 2: os pares reais da rodada B (`testes/rodada-b/caso_real.py` e os `casos-rodada-b.json` das habilidades) e o harness 0.2.0 com Histórico (commit `1f8fe34`);
  - lote 3: o `README.md` e o pedido com o critério da reconstituição (checklist, l. 340);
  - a segunda leitura do auditor: EX-0097, com 82.846 tokens e 17 chamadas, e os achados A1, A2, A3 e A9 corrigidos (checklist, l. 341; `trilhas/2026-10-30_K-111/achados-auditor.json`);
  - o relatório da rodada B, com OK 146 · FALHA 0 · PENDENTE 1 (`testes/relatorio-rodada-B.md:6`), e a tela dele em `trilhas/2026-10-30_K-111/relatorio-rodada-B-tela.md` (checklist, l. 342).
- **O que falta para fechar** (checklist, l. 343; quadro, l. 34; brief, `trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md:353-354`):
  1. esta reconstituição;
  2. a conferência dela pelo critério, feita pela conversa do K-111;
  3. a aprovação de Vicente do harness pronto, pela tela do relatório da rodada B. É a parada (a) do bloco 9, e o padrão é "aprovar se os números baterem com o critério".

## 3. O próximo passo em cada frente, pela ordem do quadro

- **Desenvolvimento** (`trilhas/planejamento/quadro.md:35-38`):
  - O próximo é o **K-112**, bloco 10a: as rotinas sem IA, pela D-048. As paradas são os termos do Actions e, se valer a D-033, o fornecedor de outra nuvem. Ele entra na sua vez, depois do bloco 9, e não espera a aprovação (brief, l. 9 e 354).
  - O **K-113** (bloco 10b) espera a aprovação do K-111 **e** o K-002.
  - O **K-114** (bloco 11, o kit) é a linha seguinte do quadro.
  - O **K-115** (bloco 12) espera a aprovação do K-111.
- **Planejamento:** o **K-002**, que vem antes do K-113 (`trilhas/planejamento/quadro.md:15`). O K-006 e a 3ª passada do K-005 entram na reunião do K-004, depois do K-116, pela D-046 (quadro, l. 16-18).
- **Operação:** o **K-207**, a lista das CLB candidatas. É de baixa prioridade e não chama Vicente (`trilhas/planejamento/quadro.md:70`). Os K-201, K-203 a K-206 (Faltas jurídicas a liberar) esperam o K-010 (quadro, l. 64-69). Hoje nenhum cartão chama Vicente: o `relatorio_dia.py` mostra "0 cartão(ões) à espera de Vicente".

## 4. Os testes

- **`scripts/relatorio_dia.py`** (relatorio-dia-0.3, rodado em 30/10):
  - **0 Entradas novas** (1006 no total: bruto 972, extraído 28, quarentena 6) e **24 Recortes** (7 abertos, 17 percorridos pela busca);
  - **30 Faltas** (2 novas hoje) e **18 vácuos**;
  - 9.782 pegadas, em 4.013 arquivos e 12,5 MB, abaixo do alarme;
  - fila de curadoria com 0 cartão à espera de Vicente e 6 itens que pedem cartão;
  - 0 propostas de rotina à espera de junção.

  O relatório não traz OK, FALHA nem PENDENTE. Sobre o consumo, ele diz "desenvolvimento 61 pp de 50"; ver o item 6.
- **`scripts/rodar_testes.py`** (sem argumentos, a suíte inteira): **OK: 241 · FALHA: 0 · PENDENTE: 1**, com código de saída 0.
  - **O único pendente:** `kit-fonte-primaria`, caso "exemplos do caso-piloto". O critério diz: "pendente: caso-piloto (Passo 1). O primeiro pedido real de Vicente e os critérios de aceitação dele." (`.claude/skills/kit-fonte-primaria/exemplos/casos.json:7-8`; `testes/relatorio-rodada-B.md:74`).
  - **O porquê:** o kit é do bloco 11 (K-114), sob demanda, e fica fora do critério do bloco 9, que cobre os blocos 4 a 8 (brief, l. 353: "a do kit sai no bloco 11").
  - O total bate com o do checklist, "Suíte inteira: OK 241 · FALHA 0 · PENDENTE 1" (`trilhas/2026-10-17_execucao-piloto.md:342`).

## 5. O que vive fora do Git

A tabela vem de `README.md:46-58` (e `AGENTS.md`, "Passo corrente"). Nesta máquina, conferi só se cada pasta existe, sem abrir o conteúdo.

| O quê | Onde fica | Nesta máquina |
|---|---|---|
| Tabela de pessoas (código → nome) | `C:/Antigravity/Cultura Liquida - privado/pessoas/` (ou `CL_PRIVADO`, que não está definida) | a pasta existe |
| Conhecimento tradicional em detalhe (D-043) | `C:/Antigravity/Cultura Liquida - privado/conhecimento-tradicional/` | a pasta existe |
| Legado (só leitura, D-024) | `legado/` (ignorado pelo Git) | a pasta existe |
| Wiki local (Quartz) | `wiki-local/` (ignorado pelo Git) | a pasta existe |
| Bruto da coleta (D-045) | fora do repositório: a fonte o guarda e o Recorte o refaz. O cache de `metadados.py` fica em `<TEMP>/cultura-liquida/cache/metadados` (`scripts/guarda.py:9-10`; `scripts/metadados.py:4,46`) | o cache existe |
| Pasta temporária das fontes (descartável) | `<TEMP>/cultura-liquida/fontes` (ou `CL_FONTES_TMP`) | a pasta existe |
| Arquivos de tiers e de coleta cidadã | ignorados pelo `.gitignore` | não conferi |

- **O gancho:** `git config core.hooksPath` responde `.githooks`, então o pre-commit está ligado (`README.md:39`).
- **Conclusão:** nada do que é preciso para retomar falta nesta máquina, até onde a existência das pastas mostra. Não conferi se o conteúdo delas está completo. A tabela de pessoas, por regra, não está no repositório (brief, l. 246).

## 6. O que não consegui achar ou confirmar só com o repositório

1. **O uso atual da conta** (semanal e janela de 5 h): só Vicente o informa. A linha do K-111 na tabela "Semana da conta" está com "a informar" (`trilhas/2026-10-17_execucao-piloto.md:401`).
2. **Uma divergência no consumo:** o `relatorio_dia.py` mostra "desenvolvimento 61 pp de 50" na semana de 28/10 a 04/11. O checklist registra que Vicente suspendeu, nesta semana, os tetos de 60 pp e de 50 pp, e que ficam a linha de 90% e a regra da janela de 5 h (checklist, l. 336 e 401). O script não mostra essa suspensão. Não decido nada sobre isso, só aponto.
3. **A aprovação de Vicente do harness pronto:** não há registro dela no repositório, o que é coerente com o K-111 em Fazendo.
4. **O conteúdo das pastas privadas:** não abri, de propósito. Por isso não sei se a tabela de pessoas cobre os 34 códigos do K-110.
5. **Os arquivos de tiers e de coleta cidadã:** não conferi se existem nesta máquina.
6. **Uma pendência para o K-114:** o quadro põe o K-114 entre o K-113 e o K-115 sem dizer se ele espera a aprovação do K-111. O brief diz que o bloco 11 precisa do bloco 9 aprovado (`brief-execucoes-v0.1.md:390`, "Entrada: o bloco 9 aprovado; para o kit, o bloco 11").
7. **O tempo da suíte:** o `rodar_testes.py` levou mais de 10 minutos nesta máquina. Não achei no repositório o tempo esperado.
