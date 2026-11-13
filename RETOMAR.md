# RETOMAR — K-115a (parada em 12/11/2026, 23h, janela de 5 h em 97%, lida por Vicente)

**Cartão:** K-115a segue em Fazendo (quadro). Conversa parada pela regra da janela de 5 h (D-040), com o estado salvo.

## Feito
- Base do teste: C115 (o modelo por chamada na ferramenta Agent, oficial; `trilhas/2026-11-12_K-115a/conferencia-c115.json`); `orcamento.py` ignora os registros `[teste de modelo]`; banco de provas `testes/modelos/banco.py` (banco-0.1, base congelada 288c4b0, insumo 119) com 5 provas e `casos.json` (OK 10 · FALHA 0); `testes/modelos/relatorio.py`; `testes/relatorio-modelos.md` (cabeçalho, sem a tabela ainda).
- Haiku 5.5: extrair-evidencia passa na rodada 3 (harness 0.2.1: cobertura e voz do autor que cita; rodadas 1 e 2 reprovaram na cobertura); registrar-termo passa (r1); montar-ficha passa (r1). Logs e `testes/modelos/resultados/`.
- Suíte: OK 257 · FALHA 0 · PENDENTE 1 (antes do banco).

## Falta
1. gerar-grafo em Haiku (a rodada foi parada no meio; refazer: `banco.py preparar gg-pr0042-cadeia --pasta <scratchpad>/k115a/gg-haiku`, depois o Agent arquivista com `model: haiku` e o pedido em `<pasta>/pedido.md`; `banco.py avaliar ... --modelo claude-haiku-5-5 --rodada 1 --resumo`; log com `[teste de modelo]` e `rodada 1`).
2. triagem-juridica em Haiku (prova `tj-tr0018`, agente juridico).
3. Sonnet 5.5 só onde o Haiku não passar depois do reforço do harness (regra da l. 698).
4. Segunda leitura do auditor (Sonnet 5.5 alto) das saídas que passaram, com os pontos dos logs: EE r3 (20 Evidências de 10 Trechos, marcas "por cautela"), RT (abonou a EV-0004 divergente), MF (frases sobre as Faltas F-0027 a F-0031). As pastas das saídas ficam no scratchpad desta sessão e se perdem; refazer a prova se a leitura pedir a saída.
5. `python testes/modelos/relatorio.py`; o texto do relatório; frontmatter do avaliador e do arquivista para `claude-haiku-5-5` (se passarem), com Histórico; checklist, quadro, insumos (registrar-melhoria: o banco fora da suíte do portão; o SKILL.md carregado com o agente pode não ser o do disco); commit e push.

## Próximo comando
`python scripts/relatorio_dia.py`, depois o item 1 acima.
