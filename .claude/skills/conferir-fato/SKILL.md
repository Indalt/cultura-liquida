---
name: conferir-fato
description: Confere um lote de fatos na fonte (Cn), com URL, nível (oficial, secundária, não conferido) e citação literal, e entrega um JSON no formato de esquemas/conferencia.schema.json. Use quando um fato novo precisa entrar no projeto Cultura Líquida ou quando um item está "a conferir".
---

# conferir-fato

**Versão do harness:** 0.1.1 · **Quem usa:** auditor, juridico · **Rodada:** A

## Objetivo
Transformar perguntas de fato em respostas verificáveis: cada afirmação com a URL de onde veio, o nível de verificação e o trecho literal que a sustenta. O que não se confirmou fica escrito como "não conferido", nunca omitido nem completado.

## Quando usar / quando não usar
- **Usar:** conferências de lote (como C1 e C2 de 16/10); itens marcados "a conferir" na Fundação, no passo em que entram; reconferências.
- **Não usar:** para opinar sobre a prática cultural (D-019); para interpretar a lei além do texto (interpretação vai em `observacao`, marcada como tal); para fatos que não serão usados no passo corrente.

## Entradas e saídas
- **Entrada:** lista de perguntas com ID (`Cn.k`), o teto de chamadas e a data.
- **Saída:** um objeto JSON válido em `esquemas/conferencia.schema.json`, com o campo `resposta` que o esquema exige em cada item, em um de dois formatos por item:
  - nível no item (`nivel`, `url`, `citacao`), quando o item inteiro tem o mesmo nível (ver C1);
  - **preferido:** `partes`, uma por afirmação, cada uma com `afirmacao`, `citacao`, `url`, `nivel` (ver C2). Use partes sempre que só parte do item for oficial.
- O campo `nao_conferido` lista, por item, o que faltou e por quê.

## Passos
1. Leia as perguntas e anote o teto de chamadas (15 a 20), contado como o harness conta: cada ferramenta e cada pedido HTTP, mesmo agrupados num só comando, inclusive ToolSearch. **Reserve uma chamada** para a validação do passo 8.
2. Para cada pergunta, vá direto à página oficial (lei no planalto.gov.br; norma no portal do órgão; padrão na página de quem o mantém).
3. **Leis no Planalto:** `curl -sL -A "Mozilla/5.0" <url> | iconv -f latin1 -t utf-8 | grep -n "Art. 46"` e recorte as linhas do artigo. Nunca traga a página inteira. Se o Planalto cair, use os espelhos (www2.camara.leg.br/legin, normas.leg.br, legislacao.presidencia.gov.br).
4. Copie a citação **literal** da página crua, por `curl` e `grep -n`, como já se faz com as leis (passo 3), e a URL exata que abriu. O WebFetch serve só para localizar a página: ele devolve o trecho passado por um modelo pequeno, que pode parafrasear, e por isso nunca é a fonte da citação.
5. Atribua o nível: **oficial** só se a página oficial abriu e você leu o trecho; **secundária** se veio de outra fonte; **não conferido** se nada abriu. Resumo de busca não é leitura: é no máximo "secundária". O trecho devolvido pelo WebFetch também não é leitura literal.
6. Se só parte do item foi lida na fonte oficial, divida em `partes`.
7. Liste em `nao_conferido` o que ficou de fora e o motivo (403, PDF não aberto, teto de chamadas).
8. Antes de entregar, valide com a chamada reservada: `echo '<json>' | python scripts/validar.py conferencia -`. Se reprovar, corrija (o `resposta` de cada item é o erro mais comum) e entregue só o que passa.
9. Termine com o bloco LOG.

## Regras herdadas
- **Nível de verificação:** "oficial" exige URL http(s) e citação; nada de memória como se fosse conferido.
- **Essência:** não reescreva decisões de Vicente; fatos só informam.
- **Dado pessoal:** não registre e-mail, telefone, CPF ou @perfil de terceiros (só e-mails institucionais quando forem a via de acesso).
- **Anti-robô:** 403, captcha ou verificação de navegador nunca se contornam; registre e siga.
- **Falta dita:** o que não se conferiu é dito ("não conferido"), nunca completado por inferência.

## Teto e custo
- Chamadas: o teto informado pelo curador (15 a 20), com uma reservada para a validação. Ao chegar na penúltima, pare, valide e entregue o que tem.
- Tokens estimados: 60 a 85 mil por lote de 5 a 6 itens em Sonnet 5.5 alto (medidos: C1 = 81.852 com 19 chamadas; C2 = 77.351 com 19).

## Critério de parada
Todos os itens com nível atribuído, ou teto de chamadas atingido (os restantes vão para `nao_conferido`).

## O que não faz
Não decide se o projeto pode publicar algo (isso é Falta do juridico); não altera arquivos; não traz páginas inteiras para o contexto.

## Campos do log
`agente` (auditor ou juridico), `habilidade: "conferir-fato"`, `versao_harness: "0.1.1"`, `entrada_ref` (ID do lote), `acoes` (fontes abertas), `resultados` (itens e níveis), `decisoes` (cada item: aceito se oficial ou secundária com URL; falta se não conferido), `erros` (403, quedas), `alcance` (páginas abertas e o que não abriu; D-030).

## Exemplos e validador
- [exemplos/casos.json](exemplos/casos.json): C1 e C2 reais (passam); "oficial" sem URL e "oficial" sem citação (reprovam).
- Validador: `scripts/validar.py conferencia`.

## Histórico
- 0.1.1 (22/10/2026, K-101; insumo 17): uma chamada reservada no teto para validar a saída com `scripts/validar.py`, com o campo `resposta`; citação literal da página crua por `curl` e `grep -n`, e o WebFetch só para localizar a página; teto contado como o harness conta.
- 0.1.0 (16/10/2026): primeira versão, a partir das conferências C1 e C2.
