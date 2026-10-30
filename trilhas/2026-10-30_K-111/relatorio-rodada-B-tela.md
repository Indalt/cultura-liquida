# K-111 — Relatório da rodada B (uma tela, para a aprovação do harness pronto)

Bloco 9 do brief (l. 346-353). Validador: `rodar_testes.py --rodada B --relatorio testes/relatorio-rodada-B.md` → **OK 146 · FALHA 0 · PENDENTE 1**. Suíte inteira: **OK 241 · FALHA 0 · PENDENTE 1**. O único PENDENTE é o kit-fonte-primaria, que sai no bloco 11 (K-114) e fica fora do critério. Segunda leitura: auditor, EX-0097 (82.846 tokens, 17 chamadas). Os 3 achados que pediam correção foram corrigidos (`achados-auditor.json`).

| Habilidade | Par real que passa | Caso real que reprova (erro do brief e outros) | Custo medido nos logs |
|---|---|---|---|
| registrar-termo | TE-0002 cajuína + TE-0004 (forma dividida marcada) | forma de OCR como variante; "mocororó" sem a marca de termo ambíguo (insumos 26, 88) | 3 execuções, 149.782 tokens, 32 chamadas |
| extrair-evidencia | TR-0001; TR-0101 com ligadura (insumo 83); PR-0001; PR-0002 | TR-0034 com "fresco", de outro trecho, marcado como localizado; leitura divergente contada (A1); marca de saúde perdida (A3); "mocororó" num trecho que não traz a palavra (insumo 88) | 7 lotes, 1.212.590 tokens, 155 chamadas |
| montar-ficha | ficha CL-0001; camada Educação (insumo 80) | frase factual sem Proposição; habilidade da BNCC sem página | 1 execução, 111.618 tokens, 18 chamadas |
| gerar-grafo | PR-0016 (duas linhagens); PR-0065 (tensão interna) | duas fontes da mesma linhagem contadas como duas; tensão interna apagada | 1 execução, 104.796 tokens, 15 chamadas (μ e λ por script) |
| ficha-de-acesso | Hemeroteca (AM-0001, 403, via humana) | 403 com decisão "aceito" | 2 execuções, 203.060 tokens, 25 chamadas |
| consulta | Recorte RC-0010 (K-108) | total visto acima do informado, sem explicação | 1 execução, 51.898 tokens, 8 chamadas |
| triagem-juridica | F-0033; F-0024 | sem caminho de liberação; Falta completada por inferência | 4 execuções, 286.179 tokens, 47 chamadas (mais 3 combinadas com conferir-fato ou guia, 408.802) |
| guia-de-liberacao | guia da Lei 9.610 (K-109) | sem limites; passo "oficial" sem URL | 3 execuções, 278.283 tokens, 47 chamadas |

**Regras fixas do Jurídico reprovando os casos de teste:** a `triagem_fixa.py` sobre a Entrada real EN-0009 passa no ato de ler, localizar, linkar e citar (D-042: sem Falta pela regra) e **barra** a cópia além da citação. Os 9 casos fixos do núcleo também dão o esperado: dado sensível, quem ensinou sem consentimento, receita de substância controlada, conhecimento tradicional ao publicar.

**O que o piloto não deu e não se inventou (seção 6C, item 7):**
- nenhuma Proposição inconsistente ou falsa: o cartão de conflito segue só com exemplo de esquema;
- nenhuma língua de designação nas fontes;
- nenhuma Falta preenchida numa ficha;
- os achados A2 (voz) e A4 (qualificativo) do K-109 ficam com a leitura do auditor: nenhum script os pega.

**Insumos no harness 0.2.0:**
- 26, 29, 35, 71, 72, 74, 76, 80, 83, 86 e 88: feitos;
- 82: só a regra no texto da habilidade e do arquivista, sem conferência por script;
- 89 e 92: parciais, pela regra; o que ficou fora está no checklist e nos insumos 97 a 100;
- o insumo 84 não entrou (vai à reunião do K-004).

**Reconstituição:** aguardando a conversa nova. O pedido e o critério estão em `trilhas/2026-10-30_K-111/reconstituicao-pedido.md`.
