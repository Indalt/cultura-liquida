# Casos do gravar_extracao.py (K-109)

- `raiz/`: um acervo mínimo para os testes. Tem a Entrada EN-1155 como estava antes da triagem (commit 792a793) e o Termo TE-0002.
- `trecho-EN-1155-1.json`: a saída real do `localizar_trecho.py --saida` para um trecho de EN-1155, de 29/10/2026. É citação curta, sem nome de pessoa.
- `manifesto-ok/`: o manifesto do `ler_fonte.py` com o hash do texto lido igual ao do Trecho. `manifesto-outro/` tem outro hash.
- `saida-ok.json` passa. `erro-saida-sentido.json` (sentido fora do contrato da Evidência) reprova, e a saída boa com o manifesto de outro hash também reprova.
