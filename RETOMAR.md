# RETOMAR — K-125 (rotina com IA na API do Gemini; D-054)

Conversa 2, continuação (13/11/2026, noite): Vicente trouxe a tela de limites da chave (nível gratuito) e pediu
"buscar viabilizar com coerência ao sistema". **Aguarda** a confirmação da leitura da essência (registrar-decisao):
a rotina no nível gratuito, com a vaga do argon (sem cota) pelo modelo com cota que passar nas provas do banco.
Até lá, nenhuma troca de modelo na rotina nem no `rotinas.json`.

## Feito
- `scripts/gemini_agente.py` 0.4: ferramentas restritas, teto de chamadas, histórico encurtado, contador semanal
  (`trilhas/rotina-ia/consumo-gemini.jsonl`; `--semana`), cota diária (código 4), `--ler-tambem`, `--log` e o
  **ritmo** pelos limites da tela do dono (`ambientes/rotinas-ia/limites-gemini.json`).
- `.github/workflows/rotina-ia-gemini.yml` (escrito, não testado), `rotina_ia.py` 0.2, vigia com o autor novo,
  `ambientes/rotinas-ia/rotinas.json` 0.2 (rotina "gemini", lote 5).
- Provas: ee/hydrogen rodada 1 reprova; rodada 2 interrompida pela cota; gg/argon recusada (sem cota);
  gg/gemini-3.8-flash reprova (gastou o teto sem gravar; EX-0147).
- Semana do Gemini (desde 11/11, 23h): 478.557 de entrada (48% do teto), 43.678 de saída.

## Falta, depois da confirmação
1. Reforço do harness para o Gemini pela l. 698 (a ponte do executor: gravar cedo, não explorar a raiz) e as provas:
   ee, rt e mf no hydrogen; gg, tj e a segunda leitura no candidato da vaga do argon (até 20 pedidos por dia por
   modelo: espalhar por dias). Script de prova da conversa: preparar → `gemini_agente.py --tipo teste --proibir
   acervo/ entrada/ ambientes/ grafo/ wiki-local/ testes/modelos/ trilhas/` → `banco.py avaliar`.
2. Lote da rotina medido em pedidos (cabe em 20 por modelo na quinta); teste à mão do workflow numa ramificação local.
3. Passo de dono: o segredo `GEMINI_API_KEY` no repositório (guiado).
4. `gh workflow run rotina-ia-gemini.yml`; a proposta em `claude/`, o portão e a junção; o consumo medido.

## Próximo comando
`python scripts/relatorio_dia.py`; `python scripts/gemini_agente.py --semana`.
