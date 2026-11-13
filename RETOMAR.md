# RETOMAR — K-125 (rotina com IA na API do Gemini; D-054)

Conversa 2 (13/11/2026, noite) parada pela **parada (c)**: a chave está num projeto do Google no nível gratuito.
O gemini-4-hydrogen tem 20 pedidos por dia; o gemini-4-argon não tem cota (limite 0). Sem a cobrança ligada,
a segunda leitura (argon), as provas do argon e a rodada no Actions não rodam. Passo de dono pedido a Vicente.

## Feito
- `scripts/gemini_agente.py` 0.3: ferramentas restritas, teto de chamadas, histórico encurtado, contador semanal
  (`trilhas/rotina-ia/consumo-gemini.jsonl`; `--semana`), cota diária (código 4), `--ler-tambem`, `--log`.
- `.github/workflows/rotina-ia-gemini.yml` (escrito, não testado), `rotina_ia.py` 0.2, vigia com o autor novo,
  `ambientes/rotinas-ia/rotinas.json` 0.2 (rotina "gemini", lote 5).
- Provas: ee/hydrogen rodada 1 reprova (300 mil de entrada); rodada 2 interrompida pela cota (57 mil); gg/argon recusada.
- Semana do Gemini (desde 11/11, 23h): 357.072 de entrada, 35.472 de saída.

## Falta, depois da cobrança
1. As provas: ee (hydrogen, rodada 3), rt e mf (hydrogen), gg e tj (argon), e as cinco no outro modelo, com o
   script de prova da conversa (preparar → `gemini_agente.py --tipo teste --proibir acervo/ entrada/ ambientes/ grafo/
   wiki-local/ testes/modelos/ trilhas/ --log "[teste de modelo] ..."` → `banco.py avaliar`). Vigiar o teto da semana (insumo 134).
2. Teste à mão do workflow: os passos dele numa ramificação local `claude/...` com `CL_GRAVADOR=rotina`, sem enviar.
3. Passo de dono: o segredo `GEMINI_API_KEY` no repositório (guiado).
4. `gh workflow run rotina-ia-gemini.yml`; a proposta em `claude/`, o portão e a junção; o consumo medido.

## Próximo comando
`python scripts/relatorio_dia.py`; `python scripts/gemini_agente.py --semana`; um pedido curto ao argon para ver se a cota abriu.
