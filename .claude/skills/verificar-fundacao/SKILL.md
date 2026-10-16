---
name: verificar-fundacao
description: Verifica a Fundação do projeto Cultura Líquida (00_Fundacao_Cultura_Liquida.md) de forma mecânica e independente, um olhar por passada (mecânico; decisões D-015 a D-029; contradições; nível dos fatos e termos explicados), e entrega achados confirmados por grep ou script no formato de esquemas/achado-verificacao.schema.json. Use depois de cada grupo de seções escrito pelo redator.
---

# verificar-fundacao

**Versão do harness:** 0.1.0 · **Quem usa:** auditor · **Rodada:** A

## Objetivo
Quem produz não confere. Achar o que se perdeu ou se contradiz na Fundação, com prova mecânica: **cada achado só vale com o comando de `grep` ou de script que o confirma e, quando não é ausência, a linha citada**. Não se decide por votação nem por impressão.

## Quando usar / quando não usar
- **Usar:** depois de cada grupo de seções da v0.2 (Bloco 3 do brief); antes do commit final (Bloco 4); a cada nova versão da Fundação.
- **Não usar:** para reescrever o texto (o auditor só aponta; quem corrige é o redator, depois de o achado ser confirmado); para conferir fatos na web (isso é `conferir-fato`).

## Entradas e saídas
- **Entrada:** o arquivo, o grupo de seções (faixas de linhas), o olhar pedido e o teto de leitura.
- **Saída:** um relatório JSON válido em `esquemas/achado-verificacao.schema.json`. Achados com `tipo`, `descricao`, `linha`, `trecho`, `confirmacao` (`metodo`: grep ou script; `comando`; `saida`) e `estado` (`confirmado` ou `nao_confirmado`).

## Passos (um olhar por passada)
1. **Mecânico (sempre primeiro):**
   - `python scripts/checar_fundacao.py --essencias .claude/skills/escrever-secao-fundacao/referencias/essencias.json --falas .claude/skills/escrever-secao-fundacao/referencias/falas.json --saida <relatorio.json>` (marcadores, "Versão 0.2", D-015 a D-029, legenda das P-refs, Anexos D e E, C.3, entidades do §6, termos-chave de cada essência, transcrição no lugar da essência);
   - `python scripts/comparar_anexos.py` (Anexos A e B idênticos ao commit `e868a98`);
   - `python scripts/procurar_dado_pessoal.py 00_Fundacao_Cultura_Liquida.md`.
2. **(a) Decisões:** para cada D-015 a D-029, `grep -n "D-0nn"` e leia só a linha e as continuações; compare o **sentido** com a essência em `referencias/essencias.json` da habilidade `escrever-secao-fundacao`. Termo-chave presente não basta: o sentido não pode se inverter.
3. **(b) Contradições:** para cada afirmação forte do grupo, `grep -n` pelos termos dela no resto do arquivo; duas linhas que dizem o contrário viram achado com as duas linhas citadas.
4. **(c) Nível e termos:** fato novo sem URL e nível; termo técnico sem explicação na primeira vez que aparece (`grep -n` pela primeira ocorrência).
5. Para cada suspeita, rode o comando que a confirma e copie a saída. Sem confirmação → `nao_confirmado`.
6. Valide o relatório: `python scripts/validar.py achado-verificacao <relatorio.json>` (ou `-` pela entrada padrão). Termine com o bloco LOG.

## Regras herdadas
- **Nível:** o auditor também usa fontes verificáveis (princípio 9).
- **Essência:** a régua é a essência confirmada (seção 2 do brief), não a fala original nem a opinião do auditor.
- **Dado pessoal:** achado de dado pessoal cita a linha e o tipo, nunca repete o dado.
- **Anti-robô:** não se aplica (verificação local).
- **Falta dita:** ausência de algo exigido é achado; o auditor não preenche.

## Teto e custo
Leitura só por `grep -n` e faixas de linhas, nunca o arquivo inteiro. Até 3 passadas por grupo (uma por olhar). Estimativa: 30 a 60 mil tokens por passada em Sonnet 5.5 alto (a medir).

## Critério de parada
O olhar pedido percorrido no grupo inteiro, ou o teto de leitura atingido (dizer até onde chegou).

## O que não faz
Não corrige, não reescreve, não vota, não confere fato na web, não aceita achado sem comando que o confirme.

## Campos do log
`agente: "auditor"`, `habilidade: "verificar-fundacao"`, `entrada_ref` (arquivo e commit), `acoes` (comandos rodados), `resultados` (número de achados por tipo), `decisoes` (achado confirmado = `aceito`; não confirmado = `descartado`, com o motivo), `erros`.

## Exemplos e validador
- **v0.1 → as ausências conhecidas:** `checar_fundacao.py --commit e868a98` (a v0.1 gravada no Git, para o teste não mudar quando a v0.2 sair) dá 37 achados (D-015 a D-029, "Versão 0.2", Anexos D e E, C.3, legenda das P-refs e 17 entidades do §6). Reprova como esperado.
- **Divergência real de 16/10:** a D-018 tinha perdido "traduzível" ([exemplos/d018-sem-traduzivel.md](exemplos/d018-sem-traduzivel.md)). Reprova; a versão certa ([exemplos/d018-correta.md](exemplos/d018-correta.md)) passa.
- **Anexos intactos:** `comparar_anexos.py` na cópia atual. Passa.
- **Relatório com achado sem linha** ([exemplos/erro-achado-sem-linha.json](exemplos/erro-achado-sem-linha.json)). Reprova; o relatório de exemplo ([exemplos/relatorio-exemplo.json](exemplos/relatorio-exemplo.json)) passa.
- Casos: [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.0 (16/10/2026): primeira versão.
