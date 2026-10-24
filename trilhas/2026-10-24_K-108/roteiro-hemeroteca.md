# Roteiro da busca assistida na Hemeroteca Digital (AM-0001 × CO-0002, cajuína)

Para Vicente. A Hemeroteca segue na via humana pela D-044 (3): no teste do juridico de 24/10/2026, o robô identificado levou 403 em memoria.bn.gov.br e desafio do Cloudflare em hemerotecadigital.bn.gov.br (`triagem-hemeroteca.json`). Este roteiro descreve a tela pelo que o projeto sabe dela (ficha do K-106, sintaxe do Anexo E); **a tela não foi conferida por robô**: onde ela for diferente, vale a tela, e a diferença vai numa linha de "observações".

## Antes de começar
- **Formulário:** `C:\Users\alqui\AppData\Local\Temp\cultura-liquida\assistido\AM-0001_CO-0002_2026-10-24.json` (fora do Git). Gere outro por período com `python scripts/assistido.py modelo --ambiente AM-0001 --consulta CO-0002 --periodo 1950-1959`.
- **Limite:** até **1 h por sessão**. Ao parar, deixe `"terminou": false` e a última página vista em `paginas` (o cursor); a próxima sessão começa da página seguinte.
- **Horas:** anote o início e o fim de cada sessão; entram no bloco 13 como busca assistida.
- **Nada de nome de pessoa** nas observações.

## Passo a passo
1. Abra `https://hemerotecadigital.bn.gov.br/` no navegador e, se vier a verificação do Cloudflare, passe por ela como pessoa (é a via humana).
2. Entre na pesquisa por acervo (aba ou botão de pesquisa da Hemeroteca, que abre `hdb/periodico.aspx`).
3. Deixe **Periódico** em todos (ou o que a tela pedir) e escolha **Período** (a década). No campo **Pesquisa**, cole a sintaxe do formulário:
   `(cajuína/"caju-ína"/"cajuí-na"/"ca-juína"/cajuyna)` (acento indiferente; `/` é "ou").
4. **Primeira passada, só para contar:** para cada década, anote o número de ocorrências que a tela mostra, numa tabela simples (década → ocorrências). Isso define a ordem.
5. **Ordem dos Recortes (valor provisório):** do período com menos ocorrências para o com mais. **Acima de 50 ocorrências** numa década, ela já é o Recorte (não junte décadas); abaixo, pode juntar décadas vizinhas num Recorte só, até 50.
6. Para cada Recorte, abra os resultados. A lista mostra os periódicos com a quantidade de ocorrências; abra cada um no leitor (DocReader), que leva à página com o termo destacado.
7. **Link permanente da página:** copie o endereço do leitor na barra do navegador quando a página estiver aberta (a forma esperada é `.../DocReader/docreader.aspx?bib=<código>&pagfis=<página>`; se a tela oferecer um botão de link ou "copiar endereço", use-o). Cole em `itens[].link_permanente`.
8. **Localizador:** periódico, data da edição e página, e onde na página (coluna, seção), por exemplo `"Jornal X, 12/03/1958, p. 4, coluna 2"`. Cole em `itens[].localizador`. O código `bib` vai em `id_na_fonte`.
9. **Página de resultados:** para cada página da lista de resultados, cole o link dela em `paginas[].link_permanente` e o número de resultados vistos.
10. No fim do Recorte, ponha `total_informado` (o total da tela) e `"terminou": true`. Avise o curador para registrar: `python scripts/assistido.py registrar <formulário>`.
