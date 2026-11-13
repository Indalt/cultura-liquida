# RETOMAR — K-125 (rotina com IA na API do Gemini; D-054)

Conversa 1 (13/11/2026) fechada com a janela de 5 h acima de 70% (123% a 140%, estimada pelo hook): um lote só.

## Feito
- `scripts/gemini_agente.py` (gemini-agente-0.1): executor com ferramentas restritas, teto de chamadas e contador semanal em `trilhas/rotina-ia/consumo-gemini.jsonl`. `--semana` mostra a soma.
- Prova `ee-en1369-en1544` no gemini-4-hydrogen, rodada 1: reprova; 299.975 de entrada, 28.037 de saída (seção "Gemini" de `testes/relatorio-modelos.md`; checklist do piloto, seção do K-125).
- Insumos 133 (nível gratuito: HTTP 429 pela cota de 20 pedidos) e 134 (uma prova de 2 Entradas ≈ 300 mil de entrada; um lote de 15 passa do teto de 1 milhão).

## Falta
1. As outras nove provas (preparar com `testes/modelos/banco.py preparar <prova> --pasta <scratchpad>`; rodar com `gemini_agente.py --tipo teste --proibir acervo/ entrada/ ambientes/ grafo/ wiki-local/ testes/modelos/ trilhas/`; avaliar com `banco.py avaliar`). Antes, ver o insumo 134: as dez provas ficam perto de 3 milhões de entrada (o teto semanal é 1 milhão).
2. Workflow `.github/workflows/rotina-ia-gemini.yml` (quintas; `rotina_ia.py preparar` → executor avaliador/hydrogen → `registrar_log.py` → `filtrar` + gravação → `amostra` → executor auditor/argon → `fechar` → validar → commit e push em `claude/`), aviso no Issue #1 quando o executor sair com código 3; `ambientes/rotinas-ia/rotinas.json` com o executor e o lote calibrado.
3. Passo de dono guiado: segredo `GEMINI_API_KEY` no repositório.
4. Uma rodada no Actions, o portão e a junção do K-113.

## Próximo comando
`python scripts/relatorio_dia.py` e `python scripts/gemini_agente.py --semana`; depois, o item 1 (ou o 2, se Vicente decidir os insumos 133 e 134 antes).
