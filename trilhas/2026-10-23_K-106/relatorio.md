# K-106 — Bloco 4: fichas de acesso, Termos e Consultas do caju (23/10/2026)

Relatório de uma tela, sem pedido de aprovação (D-037). Autorização de Vicente, com o insumo 30, no checklist do piloto.

## O que entrou
- **Termo 0.2.0 (insumo 30):** cada designação é `{forma, lingua?, lingua_fonte?}`; a língua (BCP 47) só quando a fonte a der, com de onde veio; sem ela, a exportação usa `und`. A primeira designação de cada língua é a do `skos:prefLabel` (SKOS: no máximo um por etiqueta de língua, oficial no C6.3). `gerar_termo.py` em termo-0.2; `registrar-termo` 0.1.1.
- **Termos candidatos:** TE-0001 caju e TE-0002 cajuína, sem abonação, sem variante e sem língua, com as formas de busca por família (l. 433) e o glossário gerado.
- **Consultas:** CO-0001 e CO-0002 (termo), CO-0003 e CO-0004 (mistas, com 4 descritores processuais tirados das fontes) e CO-0005 (só descritores). Tradução de cada uma nas quatro fontes em `ambientes/traducao-consultas.json`.
- **Fichas testadas e datadas:** BDTD (API v1 em UTF-8; totais 1306, 1441, 80, 83 e 10), Infoteca-e (OAI-PMH, 59.357 registros; a busca por texto é vedada ao robô), Hemeroteca (403 de novo, via humana) e BCR (nome fora do DNS em 23/10).
- **Lugares:** a tabela do bioma predominante por município do IBGE (2024), oficial, em `acervo/lugares/ibge/`.

## Em quarentena
- As citações do BCR e da USCS do mapa de 17/10 (vieram de leitor de página, não do PDF).
- As formas de busca de hífen na BDTD (ruído anotado, não apagado; insumo 39).
- A licença do item 748513 da Infoteca-e (CC BY-NC-ND 4.0 pelo rodapé do site).

## Faltas
- **BCR, fonte inacessível:** `bcr.iphan.gov.br` não existe no DNS em 23/10/2026; via humana ou reteste (insumo 40).
- **Infoteca-e, busca por texto** e **Hemeroteca:** via humana, com as traduções para a busca de Vicente.
- Não conferidos: TBX, o destino SKOS das variantes e formas de busca, a XLSX do IBGE, os termos de uso próprios das fontes.

## Consumo
263.700 tokens de agentes em 33 chamadas (arquivista 56.779 e 8; rastreador 152.214 e 14; auditor 54.707 e 11). Estimativa da D-040, não medida: 6,2 pp, dentro de H = 7. Insumos 39 a 43.
