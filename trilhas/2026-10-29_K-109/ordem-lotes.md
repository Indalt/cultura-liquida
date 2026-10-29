# K-109: ordem dos lotes da triagem (bloco 7)

**Regra (Vicente, 27/10; Fundação l. 512):** a prioridade é risco, depois a CLB do caso-piloto. Primeiro vêm as Entradas que citam cajuína no título ou no resumo. Se sobrar lote, vêm as de caju achadas pelos descritores das Consultas mistas (CO-0003, CO-0004) ou só pelos descritores (CO-0005). O resto segue na fila, sem descarte (princípio 10).

**Como se achou:** por script, sem IA. A busca procura `cajuina`, sem acento e sem caixa, no título e no resumo do cache local de metadados (`<TEMP>/cultura-liquida/cache/metadados/AM-0021.jsonl` e `AM-0029.jsonl`, de 24/10, fora do Git; D-045, camada 3), casando cada linha com a Entrada pelo identificador. Das 1.002 Entradas de trabalho (todas no estado "bruto", pré-triagem "segue"), **26** citam cajuína: 16 no título e 10 só no resumo. O campo `pretriagem.motivo` registra só o primeiro motivo e por isso mostra 8 delas. A triagem fixa (triagem-fixa-0.3, ato "ler") deu 0 Falta nas 26: "sem Falta pela regra" (D-042).

**Alcance (D-030):** só se olhou o título e o resumo que a fonte entrega. Não se olhou o texto integral, e a cajuína citada só no corpo fica fora desta ordem até a extração.

## Lote 1 (15)
1. O registro da cajuína no BCR (AM-0061), se a ficha de acesso testada de novo permitir trazê-lo pela via que mostrar. Sem ele, entra no lugar a EN-0438.
2. Com cajuína no título, saúde e bebida alcoólica primeiro (risco; a marca de aviso, saúde ou política é do avaliador): EN-1155, EN-1543, EN-0266, EN-1355.
3. Depois as que tratam da bebida e do modo de fazer: EN-0078, EN-1314, EN-1443, EN-1294, EN-1315, EN-1369, EN-1413, EN-0640, EN-0694, EN-1544.

## Lote 2 (15)
- As de título que restaram: EN-0438 (se não entrou no lote 1) e EN-0957.
- Só no resumo: EN-0036, EN-0186, EN-0200, EN-0271, EN-1265, EN-1370, EN-1442, EN-1461, EN-1518, EN-1565.
- Completam o lote as primeiras de caju pelos descritores (CO-0003, CO-0004, CO-0005), pela ordem do EN-nnnn.

## Lote 3, se sobrar conta
- As seguintes de caju pelos descritores, pela ordem do EN-nnnn.

## Fila
- As outras Entradas seguem no estado "bruto", sem descarte. Escala: insumo 60 (vai ao K-002).
