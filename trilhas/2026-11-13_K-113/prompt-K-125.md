# Prompt da conversa do K-125 (preparado no fechamento do K-113, 13/11/2026)

Colar numa conversa nova do Claude Code, na pasta do projeto, com Opus 5.5 e esforço médio.

---

Autorizo o cartão K-125 (rotina com IA na API do Gemini), pela D-054. Opus 5.5, esforço médio. Retome pelo quadro e mova o cartão para Fazendo.

Antes de tudo:
- Orçamento pela D-040: o projeto até 60 pp por semana e o desenvolvimento até 50; a semana da conta vai até 18/11, às 23h. A leitura de uso vem da linha [Uso do plano] do hook; não me pergunte a porcentagem. Acima de 70% da janela de 5 h, um lote só, e a conversa fecha com o estado salvo. Commit e push a cada lote, só dos seus arquivos e depois de git pull.
- A rotina diária sem IA está na operação: não mexa nela, salvo se uma falha vier de algo que você mudou. A rotina do Claude do K-113 fica pausada (D-054).
- A chave da API do Gemini está no `.env` da pasta, fora do Git. Nunca a escreva em arquivo versionado, log, commit ou mensagem.

O que já está decidido (não pergunte de novo):
- D-054: a automatização roda pela API do Gemini; o Claude só nas sessões abertas por mim. Modelos: gemini-4-hydrogen onde o K-115a passou em Haiku (extrair-evidencia, registrar-termo, montar-ficha); gemini-4-argon onde pediu Sonnet (gerar-grafo, triagem-juridica e a segunda leitura do auditor); o gemini-4-carbon nunca. Teto da automatização: 1 milhão de tokens de entrada e 2 milhões de saída por semana; ao passar, para e me avisa; se o teto não couber no trabalho, me avise.
- As provas do banco do K-115a (`testes/modelos/`) são a métrica para os modelos do Gemini.
- Do K-113 seguem: a fila (`scripts/fila_ia.py`), o portão da camada 2 (`scripts/portao_camada2.py`), a junção pelo Actions (`.github/workflows/rotina-ia-juncao.yml`, quem propõe não aprova), o vigia do main e a cadência às quintas.

O que fazer:
1. Um executor sem dependência do Claude (`scripts/gemini_agente.py`, nome provisório): chama a API do Gemini com o harness da habilidade (o SKILL.md e o pedido) e um laço de ferramentas restritas (ler arquivo por faixa, grep, gravar arquivo na pasta de trabalho e rodar só os scripts do projeto que a habilidade usa, como `localizar_trecho.py`, `juntar_saida.py` e `validar.py`), com teto de chamadas e o contador de tokens que a API informa, gravado por rodada e somado na semana.
2. As cinco provas do banco do K-115a rodadas no gemini-4-hydrogen e no gemini-4-argon, pelo executor, com o resultado e os tokens de cada uma em `testes/relatorio-modelos.md` (seção nova do Gemini). Se um modelo reprovar onde a D-054 o pôs, anote e siga a regra da l. 698 (reforço do harness), sem trocar de modelo por conta própria.
3. A rotina semanal no GitHub Actions com o executor: um lote de `entrada/` pela fila, extrair-evidencia no hydrogen, a segunda leitura no argon, a proposta numa ramificação `claude/`, o portão e a junção do K-113. O contador para a rodada antes do teto e avisa no Issue do relatório do dia.
4. O meu passo de dono, guiado, só depois do 1 ao 3 testados à mão: guardar a chave como segredo do repositório no GitHub.
5. Meça os tokens de cada rodada e de cada prova e grave no log.

Pronto quando: as provas rodaram no Gemini, com a tabela; uma rodada da rotina no Actions propôs em `claude/` com a segunda leitura, e o portão decidiu; o consumo da semana medido e abaixo do teto; a configuração versionada em `ambientes/rotinas-ia/`. O que não couber vai a insumo.

Paradas: só as da seção 0 do brief (o passo do segredo é a parada c, guiada). O que surgir fora disso vai a insumo (D-046). Eu não rodo workflow nem confiro execução; a mim, só passo de dono, guiado.
