# Tabela de municípios do IBGE com o bioma predominante (cópia local)

Base do bioma derivado do Lugar (Fundação, §5.7, l. 538 e 543: "os códigos do IBGE ficam em cópia local"). Gravada no cartão K-106 (bloco 4 do brief de execuções), em 23/10/2026.

| Campo | Valor |
|---|---|
| Arquivo | `Bioma_Predominante_por_Municipio_2024.csv`, cópia sem alteração (bytes do IBGE; `-text` no `.gitattributes`) |
| Fonte | IBGE, *Bioma Predominante por Município para Fins Estatísticos*, edição 2024 |
| Baixado de | https://geoftp.ibge.gov.br/informacoes_ambientais/estudos_ambientais/biomas/documentos/Bioma_Predominante_por_Municipio_2024.csv (HTTP 200, `text/csv`, 209.074 bytes, em 23/10/2026; data do arquivo na listagem oficial: 2024-07-01 14:36) |
| SHA-256 | `192dfa72717b541a6dc9963ec12ba6d71df5e3c597c4247c2ac28ee51c4c75d5` |
| Publicação | https://biblioteca.ibge.gov.br/visualizacao/livros/liv102097.pdf |
| Nível | **oficial**: o PDF da publicação e a listagem do diretório abriram ao auditor no lote C6 (EX-0017, `trilhas/2026-10-23_K-106/conferencia-C6.json`); a página do produto no ibge.gov.br deu verificação anti-robô (403), não contornada. Resolve a marcação dividida do Anexo C, F-23 (l. 1701 e 1808) para esta tabela. |
| Formato | UTF-8 com BOM, separador `;`; colunas `Geocódigo`, `Nome do município`, `Sigla da UF`, `Bioma predominante`; 5.572 linhas de dados (Mata Atlântica 2.741, Caatinga 1.095, Cerrado 1.062, Amazônia 503, Pampa 162, Pantanal 9; 224 no PI), seguidas de um dicionário de campos no fim do arquivo (contado pelo curador em 23/10/2026) |
| Limites e malha | limites dos biomas do IBGE de 2019 (escala 1:250.000) e Malha Municipal Digital de 2022, pela publicação (oficial); a revisão de limites de 2025 não aparece nela |
| Interbiomas | 963 municípios em dois ou mais biomas, pela publicação (oficial); a tabela dá só o predominante, com fim estatístico |

**Uso:** o bioma é filtro e contagem, não página (l. 543), e é dado derivado: o Lugar guarda o nome literal da fonte e o geocódigo; o bioma sai desta tabela, com a edição. **Não conferido:** a versão XLSX (não baixada); o número de municípios da API de Localidades (respondeu 200 em 23/10, sem contagem exata).
