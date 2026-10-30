# K-102 — Script de menções incidentais (30/10/2026)

Cartão do desenvolvimento entre os blocos 8 e 9 (brief de execuções, l. 338-344; D-037, diretriz 4; D-039). Sem agentes. Autorização de Vicente em `trilhas/2026-10-29_K-110/falas-vicente.md`, última seção (versão revista).

## O que se fez
- **`scripts/mencoes_incidentais.py`** (regra mencoes-0.1), sem IA, com dois atos e uma conferência:
  - **candidatas** (`--separadas`): das Evidências que o K-110 separou como outra CLB (l. 419 b), nasce Termo candidato e CLB candidata quando a forma declarada está no texto exato de um Trecho localizado (eixo 3) e o registro não a tem; a forma de um Termo declarado ambíguo se desdobra (D-039); sem a forma no trecho, nada se grava;
  - **varredura** (`--textos`): o texto lido (pasta temporária, fora do Git) contra as designações e variantes do registro de Termos do momento; a menção a outra CLB vira ligação em `grafo/mencoes-incidentais.json`; o termo ambíguo vai marcado, sem ligação; grava só IDs, forma, contagens e localizadores, nunca o texto;
  - **`--conferir`**: menção sem ligação, ligação de termo ambíguo, CLB candidata sem linha com a origem no cartão de lista ou cartão por CLB reprovam.
- **`fila_curadoria.py` 0.2:** a linha do cartão de lista traz a forma do Termo e a menção de origem (a nota da CLB candidata) e acompanha as candidatas a cada `--abrir-cartoes`; "espera" sem distinguir maiúscula.
- **Casos** em `testes/mencoes/` (trecho real: o TR-0513 do dossiê, já no Git como citação curta): 2 que passam e 4 que reprovam como esperado.

## O que a regra deu
- **Candidatas (EX-0085):** **TE-0003 "vinho de caju" e CL-0002**, das separadas a5-35, a5-36, a5-39 e a5-40 ("vinho" no texto exato delas; a forma inteira no de TR-0491 e TR-0513); **TE-0004 "mocororó" e CL-0003**, desdobrados do termo ambíguo do TE-0002 (D-039), com a forma e o povo no texto exato de TR-0494, a proteção que guarda o detalhe na pasta local (F-0033) e sem ligação à a5-47, cujo trecho não traz a palavra. As a5-31 a a5-34 não nomeiam a bebida: ficam sem termo (o nome não se infere).
- **Cartão de lista (EX-0086):** **K-207**, único, de baixa prioridade, que não chama Vicente, com as duas linhas em `trilhas/planejamento/clb-candidatas.md`.
- **Varredura (EX-0087):** 34 textos, 4 Termos, 6 formas; **7 ligações** CL-0001 → CL-0002 ("vinho de caju", 43 ocorrências em 7 textos); **5 menções ambíguas** de "mocororó" (41 ocorrências em 5 textos), marcadas e sem ligação; 2.537 menções da própria CLB e 1.998 de "caju" (Termo sem CLB), só contadas. `--conferir`: conferido.

## Fora (D-030)
- Toda CLB cujo termo não está no registro do momento; as formas de busca; as formas que as fontes usam e o registro ainda não tem ("vinho do caju", "vinho-de-caju"; insumo 91).
- Seis textos sem CLB de origem (cinco Entradas sem Proposição e a BNCC): as menções só contam.
- Atestar o TE-0003 e o TE-0004 (arquivista, fora deste cartão); as Evidências das CLB candidatas no acervo (insumo 92); as Proposições de outra CLB que ficaram na CL-0001 (insumo 89).

## Validador
`rodar_testes.py`: OK 204 · FALHA 0 · PENDENTE 5; `validar_acervo.py`: 2.849 registros, válido.
