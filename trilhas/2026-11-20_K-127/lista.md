# Inventário do K-127 (D-059), por script, sem IA

Gerado por `inventario.py`. 'Usado por' conta arquivos que citam o nome fora da trilha. Sem uso vivo = candidato a sair (fica no histórico do Git); a decisão de cada linha vai na lista do lote.

## Scripts

| Item | Usado por | Proposta |
|---|---|---|
| `scripts/_acervo.py` | scripts 11, testes 2 | fica |
| `scripts/_coleta.py` | scripts 15, testes 1, esquemas 1 | fica |
| `scripts/_comum.py` | scripts 47, testes 4, esquemas 1 | fica |
| `scripts/adaptador_cursor.py` | scripts 1, testes 1 | fica |
| `scripts/adaptador_oai.py` | scripts 1, testes 1 | fica |
| `scripts/adaptador_tainacan.py` | scripts 1, testes 1 | fica |
| `scripts/adaptador_vufind.py` | scripts 2 | fica |
| `scripts/agendar.py` | scripts 1, testes 1, rotinas 1 | fica |
| `scripts/assistido.py` | scripts 4, testes 14, harness 5, esquemas 1, rotinas 1, regras 1 | fica |
| `scripts/calcular_mu_lambda.py` | scripts 1, testes 12, harness 7, esquemas 1 | fica |
| `scripts/checar_fundacao.py` | harness 9, esquemas 1 | fica |
| `scripts/comparar_anexos.py` | harness 5, regras 1 | fica |
| `scripts/deduplicar.py` | workflows 1, scripts 14, testes 3 | fica |
| `scripts/entrada_link.py` | scripts 1, testes 1 | fica |
| `scripts/feed.py` | workflows 1, scripts 4, testes 3 | fica |
| `scripts/fila_curadoria.py` | scripts 5, testes 1, esquemas 1 | fica |
| `scripts/fila_ia.py` | workflows 1, scripts 1 | fica |
| `scripts/gemini_agente.py` | workflows 1, testes 1 | fica |
| `scripts/gerar_anexo_e.py` | scripts 1 | fica |
| `scripts/gerar_termo.py` | scripts 3, testes 54, harness 2, esquemas 1 | fica |
| `scripts/gravar_extracao.py` | workflows 1, scripts 4, testes 9, harness 3 | fica |
| `scripts/guarda.py` | scripts 11, testes 4, harness 9, esquemas 3, regras 2 | fica |
| `scripts/hook_subagent_stop.py` | harness 1 | fica |
| `scripts/juntar_saida.py` | workflows 1, scripts 2, testes 4, harness 9 | fica |
| `scripts/ler_fonte.py` | scripts 5, testes 5 | fica |
| `scripts/localizar_trecho.py` | workflows 1, scripts 5, testes 14, harness 1, esquemas 1, regras 1 | fica |
| `scripts/manutencao.py` | scripts 2, testes 3, esquemas 1, regras 1 | fica |
| `scripts/mencoes_incidentais.py` | scripts 2, testes 2, harness 5 | fica |
| `scripts/metadados.py` | scripts 5, testes 7, harness 3, esquemas 1, regras 1 | fica |
| `scripts/migrar_entradas.py` | scripts 1, testes 1 | fica |
| `scripts/nomes_provaveis.py` | scripts 1, testes 3, harness 4 | fica |
| `scripts/orcamento.py` | scripts 2, testes 3, harness 3, esquemas 2, regras 1 | fica |
| `scripts/pegadas.py` | workflows 1, scripts 13, testes 8, harness 5, esquemas 3, regras 2 | fica |
| `scripts/portao.py` | workflows 2, scripts 1 | fica |
| `scripts/portao_camada2.py` | workflows 1 | fica |
| `scripts/pretriagem.py` | scripts 8, testes 1, esquemas 1 | fica |
| `scripts/procurar_dado_pessoal.py` | workflows 2, scripts 7, harness 3, regras 2 | fica |
| `scripts/reavaliar_pegadas.py` | testes 1 | fica |
| `scripts/recorte.py` | scripts 8, testes 16, harness 4, esquemas 3, regras 1 | fica |
| `scripts/registrar_log.py` | scripts 5, harness 10, esquemas 2, regras 2 | fica |
| `scripts/registrar_melhoria.py` | harness 2, esquemas 1 | fica |
| `scripts/relatorio_dia.py` | scripts 2, testes 1, harness 2, esquemas 1, regras 2 | fica |
| `scripts/relatorio_piloto.py` | — | olhar: sem uso vivo |
| `scripts/resumo_coleta.py` | — | olhar: sem uso vivo |
| `scripts/rodar_testes.py` | workflows 1, gancho 1, scripts 3, testes 8, harness 1, regras 1 | fica |
| `scripts/rotina_diaria.py` | workflows 1, scripts 1, testes 1 | fica |
| `scripts/rotina_ia.py` | workflows 1 | fica |
| `scripts/semear_ambientes.py` | testes 20 | fica |
| `scripts/sortear_amostra.py` | scripts 2, testes 4, esquemas 1 | fica |
| `scripts/testar_no_runner.py` | workflows 1 | fica |
| `scripts/trava_testes.py` | gancho 1, scripts 1, testes 2, regras 2 | fica |
| `scripts/triagem_fixa.py` | testes 5, harness 4, esquemas 1 | fica |
| `scripts/validar.py` | workflows 2, scripts 6, testes 4, harness 19, esquemas 2, regras 2 | fica |
| `scripts/validar_acervo.py` | workflows 2, gancho 1, scripts 5, testes 20, harness 15, esquemas 3 | fica |
| `scripts/verificar_links.py` | scripts 2 | fica |
| `scripts/wayback.py` | scripts 6, testes 53, harness 3, esquemas 4, regras 1 | fica |

## Esquemas

| Item | Usado por | Proposta |
|---|---|---|
| `esquemas/achado-verificacao.schema.json` | scripts 2, testes 1, harness 2 | fica |
| `esquemas/ambiente.schema.json` | scripts 20, testes 24, harness 3, esquemas 4 | fica |
| `esquemas/aresta.schema.json` | scripts 1, testes 1, esquemas 1 | fica |
| `esquemas/clb.schema.json` | scripts 7, testes 68, esquemas 3 | fica |
| `esquemas/compreensao-local.schema.json` | scripts 1 | fica |
| `esquemas/comum.schema.json` | scripts 2, harness 1, esquemas 21 | fica |
| `esquemas/conferencia.schema.json` | scripts 1, testes 1, harness 2, esquemas 1 | fica |
| `esquemas/consulta.schema.json` | scripts 12, testes 10, harness 9, esquemas 2 | fica |
| `esquemas/decisao.schema.json` | scripts 5, testes 16, harness 10, esquemas 3 | fica |
| `esquemas/elemento.schema.json` | scripts 1, testes 1 | fica |
| `esquemas/entrada.schema.json` | workflows 1, scripts 25, testes 13, harness 10, esquemas 3 | fica |
| `esquemas/estado-consulta.schema.json` | scripts 1, harness 2 | fica |
| `esquemas/evidencia.schema.json` | scripts 2 | fica |
| `esquemas/falta.schema.json` | scripts 11, testes 26, harness 8, esquemas 3 | fica |
| `esquemas/ficha-acesso.schema.json` | testes 1, harness 4, esquemas 1 | fica |
| `esquemas/fonte.schema.json` | scripts 8, testes 78, harness 2, esquemas 3 | fica |
| `esquemas/guia-liberacao.schema.json` | testes 1, harness 5 | fica |
| `esquemas/insumo-x.schema.json` | scripts 1 | fica |
| `esquemas/insumo.schema.json` | scripts 1, harness 7 | fica |
| `esquemas/log.schema.json` | scripts 3, harness 10, esquemas 1 | fica |
| `esquemas/lugar.schema.json` | scripts 2, testes 16, esquemas 2 | fica |
| `esquemas/pegada.schema.json` | scripts 2, esquemas 1 | fica |
| `esquemas/pessoa.schema.json` | scripts 8, testes 18, esquemas 3 | fica |
| `esquemas/processo.schema.json` | scripts 1, testes 22 | fica |
| `esquemas/proposicao.schema.json` | scripts 4, testes 78, esquemas 2 | fica |
| `esquemas/recorte.schema.json` | scripts 3, testes 1, harness 3, esquemas 2 | fica |
| `esquemas/termo.schema.json` | scripts 8, testes 72, harness 3, esquemas 4 | fica |
| `esquemas/transformacao.schema.json` | scripts 1 | fica |
| `esquemas/trecho.schema.json` | scripts 8, testes 89, harness 12, esquemas 6 | fica |
| `esquemas/triagem-fixa.json` | scripts 1, testes 1, harness 1 | fica |
| `esquemas/valores-provisorios.json` | scripts 9, testes 1, esquemas 23 | fica |
| `esquemas/valores-provisorios.schema.json` | esquemas 1 | fica |

## Habilidades

| Item | Usado por | Proposta |
|---|---|---|
| `.claude/skills/conferir-fato` | scripts 1, testes 2, harness 6, esquemas 1, regras 1 | fica |
| `.claude/skills/consulta` | scripts 18, testes 46, harness 14, esquemas 4, rotinas 1, regras 1 | fica |
| `.claude/skills/escrever-secao-fundacao` | testes 2, harness 6, regras 1 | fica |
| `.claude/skills/executar-brief` | scripts 1, testes 2, harness 3, esquemas 1, regras 1 | fica |
| `.claude/skills/extrair-evidencia` | workflows 1, scripts 3, testes 11, harness 11, esquemas 1, regras 1 | fica |
| `.claude/skills/ficha-de-acesso` | testes 4, harness 7, esquemas 2, regras 1 | fica |
| `.claude/skills/gerar-grafo` | testes 10, harness 8, regras 1 | fica |
| `.claude/skills/guia-de-liberacao` | scripts 1, testes 5, harness 8, esquemas 2, regras 1 | fica |
| `.claude/skills/kit-fonte-primaria` | testes 3, harness 4, regras 1 | fica |
| `.claude/skills/montar-ficha` | scripts 2, testes 8, harness 9, esquemas 1, regras 1 | fica |
| `.claude/skills/registrar-decisao` | scripts 1, testes 2, harness 6, esquemas 1, regras 1 | fica |
| `.claude/skills/registrar-melhoria` | scripts 2, testes 2, harness 7, esquemas 1, regras 1 | fica |
| `.claude/skills/registrar-termo` | scripts 1, testes 31, harness 8, regras 1 | fica |
| `.claude/skills/triagem-juridica` | testes 11, harness 15, regras 1 | fica |
| `.claude/skills/verificar-fundacao` | workflows 1, scripts 2, testes 2, harness 9, esquemas 1, regras 1 | fica |

## Agentes

| Item | Usado por | Proposta |
|---|---|---|
| `.claude/agents/arquivista.md` | scripts 1, testes 35, harness 4, esquemas 1, regras 2 | fica |
| `.claude/agents/auditor.md` | scripts 8, testes 11, harness 14, esquemas 2, regras 2 | fica |
| `.claude/agents/avaliador.md` | workflows 1, scripts 4, testes 11, harness 5, esquemas 1, regras 2 | fica |
| `.claude/agents/campo-de-acao.md` | harness 2, regras 2 | fica |
| `.claude/agents/curador.md` | scripts 8, testes 444, harness 19, esquemas 2, regras 2 | fica |
| `.claude/agents/juridico.md` | scripts 2, testes 10, harness 12, regras 2 | fica |
| `.claude/agents/rastreador.md` | scripts 1, testes 26, harness 6, esquemas 1, regras 2 | fica |
| `.claude/agents/redator.md` | scripts 1, harness 4, regras 2 | fica |

## Sem uso vivo

- Scripts: scripts/relatorio_piloto.py
- Scripts: scripts/resumo_coleta.py

## Decisões por item (o escopo do K-127, D-059)

| Item | Decisão | Por quê | Lote |
|---|---|---|---|
| 3 casos do kit (K-114) | voltam a "pendente" | sem comando nem esquema, quebravam a suíte e o portão da rotina (17 a 19/11); confirmado por Vicente (fala 4) | 1 (594b82f) |
| `scripts/resumo_coleta.py` | sai (fica no histórico do Git) | nada o chama desde o K-108 (insumo 135; vistoria) | 2 |
| `scripts/relatorio_piloto.py` | fica | o relatório do piloto se refaz no K-007 (gatilho da fase 2, com 4 semanas medidas) | 2 |
| ramificação remota `claude/rotina-ia-2026-11-13` | sai como ramificação; os commits ficam na etiqueta `rotina-ia-2026-11-13` | sobra da rotina com IA de 13/11 (insumo 135); a trilha da rodada não se perde | 2 |
| cabeçalho de agente ou habilidade que não carrega | checagem por script na suíte | insumo 105 | 3 |
| números provisórios em scripts | vão ao registro de valores, sem mudar valor | insumos 101, 102 e 135 | 4 |
| relatórios que não dizem a verdade | consertar | insumos 137, 111, 63 e 46 | 5 |
| texto das decisões no AGENTS.md; quando a vistoria roda sozinha; `campo_de_acao/` na raiz; lugar do K-126 | proposto a Vicente, não aplicado | só Vicente decide (D-059, item 4) | — |

## Depois (o que surgiu no caminho; sem explorar)

