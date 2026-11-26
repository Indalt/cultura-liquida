# K-011 · Revisão do Claude Code (26/11) e acordo para seguir até o K-004

Para Vicente e a Antigravity, pela passagem de bastão da D-060 (item 3). A Antigravity trabalhou de 24 a 26/11; aqui ficam o que a revisão confirmou, o que foi corrigido, o que segue para o passo 3 ou para a reunião e como continuar.

**Revisado:**
- os commits 4af882e (D-060), 47c3902 (K-011, passo 1) e 5afa49d (D-061, passo 2);
- `D-060.json`, `D-061.json` e `fundamentos.md`;
- as falas acrescentadas (22/11, falas 12 e 13; K-004, fala 7);
- o quadro, o checklist, o `AGENTS.md` e o `RETOMAR.md`;
- os logs EX-0166 a EX-0168.

**Rodado:** a suíte, o validador do acervo, o `checar_fundacao.py`, o `comparar_anexos.py`, o recálculo de μ e λ e a vistoria da casa (resultado na seção 7).

## 1. O que está certo

- **Acordo (D-060).** O Claude Code concorda com os sete itens como estão. A seção 6 só acrescenta práticas de trabalho, sem decisão nova.
- **Passos 1 e 2 do K-011.** Seguiram o desenho de 22/11:
  - lista fechada;
  - uma rodada só de confirmação;
  - uma decisão só (D-061), seguindo o alerta da fala 7 contra a decisão avulsa;
  - os três [ABERTO] mantidos sem completar;
  - o que surgiu fora da lista anotado em "depois", sem explorar.
- **`fundamentos.md`.** É fiel às falas. A conferência por amostra das linhas da Fundação citadas (541, 627, 865, 880 e 896) bate.
- **Quadro.** O K-126 foi encerrado sem execução e o K-127 voltou a "A fazer" até o K-011 fechar. Isso é coerente com a D-035 e com a D-061.
- **Casa.** Nenhum `.agents/` nem `GEMINI.md`. Nada mudou em scripts, esquemas, testes ou acervo.

## 2. Corrigido agora (só texto; nenhuma regra nem ferramenta muda)

- **`AGENTS.md`.** A D-029 ficou marcada como alterada pela D-060, e a D-057 como substituída pela D-061. As duas liam como vigentes, sem aviso, no arquivo que toda conversa e todo agente carregam.
- **`CLAUDE.md`.** A linha "só o Claude Code opera os agentes (D-029)" passou a dizer o que vale pela D-060.
- **Falas de 22/11.** O título "vira a D-060" foi corrigido: o número ficou com o acordo, e a essência foi para a D-061.
- **`fundamentos.md`.** A referência às falas na linha 10 foi acertada.
- **Quadro.** O "[ABERTO]" do K-127 sobre a ordem em relação ao K-126 foi tirado, porque o K-126 está encerrado.
- **`RETOMAR.md`.** O bastão foi atualizado, e os blocos de 20/11 e 22/11 marcados como superados.

## 3. Não corrigido: vai para o passo 3 ou para a reunião

1. **Os logs EX-0166 a EX-0168 gravam tokens 0 e chamadas 0, e isso quer dizer "não medido".**
   - O esquema do log só aceita null em agente de workflow. Por isso o 0 passou, e era a única saída válida. A tentativa de trocar por null reprovou no validador e foi desfeita.
   - O efeito: o `orcamento.py` usa a última medida inteira do mesmo agente e habilidade, e o 0 entraria como medida.
   - O conserto é no esquema (aceitar null com motivo para sessão de outra LLM). Isso muda um esquema, então fica para depois do K-011. Junta-se ao insumo 136.
2. **O `orcamento.py` e a volta do Claude.**
   - A D-060 previu descontinuar o `orcamento.py` quando o Claude voltasse, e o Claude voltou.
   - Descontinuar mexe nas regras de orçamento do `AGENTS.md` e em 6 casos da trava, que pela D-059 só mudam com a confirmação de Vicente.
   - Proposta: levar à reunião do K-004, sem cartão nem decisão avulsa. Até lá ele fica como está, e a leitura de uso vem da linha [Uso do plano].
3. **O estado "inconsistente" ainda dispara uma ação.**
   - A D-061 (4e) diz que μ, λ e o Para-analisador não são critério de veredito.
   - Hoje o estado "inconsistente" abre o cartão de conflito (D-037; `scripts/fila_curadoria.py`). Não é veredito, é o gatilho para chamar Vicente.
   - O passo 3 diz se esse gatilho continua.
4. **Os exemplos das habilidades.** As pastas `exemplos/` de `.claude/skills/` guardam casos reais do piloto, que funcionam como casos de prova. O passo 3 confere se algum deles funciona como lista fechada, à luz do fundamento 10 e do insumo 140.

## 4. Como seguir no passo 3 (proposta para a Antigravity e Vicente)

**Universo:** os 32 insumos que ficaram da limpeza de 20/11 e os insumos 142, 143 e 144. São 35.

**Duas perguntas fechadas por insumo** (D-061, 3):
1. Que fundamento de `fundamentos.md`, se estivesse claro, teria evitado este insumo? A resposta é "nenhum" ou o número do fundamento.
2. O que o insumo pede se resolve por qual via (D-060)? As opções são:
   - script;
   - habilidade ou agente;
   - os dois;
   - nenhum dos dois, porque é texto da Fundação ou regra de Vicente.

**Destinos possíveis:**
- dissolve-se num fundamento e vai à reunião como texto da Fundação;
- fica como problema da ferramenta, com a via dita;
- junta-se a outro insumo;
- já foi resolvido depois de 20/11, com o commit. Os lotes 3 e 4 do K-127 tocaram os insumos 105, 101, 102 e 135.

Cada linha traz a evidência: o arquivo e a linha, ou o commit.

**Papéis, como o quadro já diz:**
- A Antigravity propõe, e o Claude Code relê às cegas. São harnesses diferentes (D-026), e quem propõe não aprova (D-038).
- O Claude Code não abre a proposta antes de gravar a própria releitura. O `RETOMAR` falava em "proposta num ambiente e releitura no outro", sem dizer quem fazia o quê; vale o quadro.

**Formato:** uma linha JSON por insumo, igual nas duas leituras, com os campos `insumo`, `destino`, `fundamento`, `via`, `junta_a` e `evidencia`. Arquivos `passo3-proposta.jsonl` e `passo3-releitura.jsonl`, nesta pasta.

**Comparação e divergências:**
- A comparação é feita por script, sem IA.
- A divergência não vai a Vicente em separado. O insumo fica com o destino mais conservador ("fica como problema da ferramenta"), e a divergência entra no documento da reunião (D-037).

**Passo 4:** quem estiver com o bastão depois da comparação escreve o documento único, e o outro o relê antes da reunião.

**Custo:** a proposta e a releitura cabem numa conversa cada. A releitura do Claude só começa com a linha [Uso do plano] abaixo de 90%; em 26/11, a estimativa da semana estava acima disso, com calibração antiga (última leitura oficial em 19/11).

## 5. Os três [ABERTO] da D-061: posição inicial do Claude Code para o diálogo no K-004

1. **A lógica entra como regra ou como declaração?**
   - Declarar o quadro lógico agora.
   - Virar regra explícita só no lugar em que a voz própria de fato conclui algo e um caso real pede. No piloto, nenhuma Proposição ficou "inconsistente".
   - É o "só se absolutamente necessário" da fala 4.
2. **Como declarar os vieses no wiki inteiro?**
   - Uma página fixa com os vieses estruturais, os que não mudam com cada CLB: o lógico, o do quadro X/Y/Z/W, o da lei como definição, o da contagem, o da máquina e o da língua.
   - Um bloco gerado por script a partir do alcance já gravado nos logs (D-030). Esse bloco muda quando entra CLB nova.
   - Converge com a proposta da Antigravity (`fundamentos.md`, §2).
3. **O campo de ação precisa declarar viés?** Vicente pediu "me convença".
   - O Claude Code não consegue sustentar que todo artefato precisa de uma declaração própria: o link para a ficha já leva a observação.
   - Há um caso só em que ela é necessária: quando o artefato sustenta uma decisão de poder (política, salvaguarda, ensino; princípio 4) e um viés muda o que o artefato recomenda. Por exemplo, o viés do arquivo quando a prática é sobretudo oral.
   - Nesse caso basta uma nota curta, como a "nota só quando houver escolha interpretativa nova" que a Antigravity já propôs.
   - As duas LLMs convergem, e o ponto pode fechar rápido na reunião.

## 6. Práticas somadas ao acordo (modo de trabalhar, sem decisão nova)

- O número de decisão ou de cartão só aparece no registro. As devoluções dizem "vira uma decisão", sem número. Foi o que causou a troca da D-060.
- O que não se mediu se diz "não medido". Enquanto o esquema exigir número, a explicação vai no alcance do log.
- Quem mexe em arquivo escrito pela outra LLM diz no bastão o que mudou, como já pede a D-060 (item 3).
- Quem faz o commit envia, como pede o `CLAUDE.md`. Se o ambiente não tiver como enviar, diz isso no bastão. Os 3 commits de 24 a 26/11 estavam só na máquina.
- A suíte roda com o Python do projeto (`.venv`, que tem o `jsonschema`), o mesmo do pre-commit. Ver a §7.

## 7. Verificação de 26/11 (sem IA; nada mudou)

- **Suíte com o Python do projeto** (`.venv`, com `jsonschema`, o mesmo do pre-commit): 272 OK, 0 falha, 3 pendentes. Os pendentes são os 3 casos do kit, já conhecidos.
- **Suíte com o Python do sistema** (sem `jsonschema`): 1 falha, o caso "F-0024 completada por inferência" (triagem-juridica).
  - O caso espera a mensagem no formato do `jsonschema`; o validador mínimo diz a mesma coisa com outras palavras.
  - Não é regressão: o caso passa com o `.venv` (conferido).
  - Fica como fragilidade para o K-127, porque o `CLAUDE.md` diz que os scripts rodam com qualquer um dos dois Pythons, e este caso não roda.
- **Acervo e Fundação:** acervo válido (4.473 registros); o `checar_fundacao.py` passa; os Anexos A e B estão idênticos; μ e λ batem no recálculo (451).
- **Registros da Antigravity:** D-060 e D-061 passam no esquema de decisão; os três logs, no esquema de log.
- **Dado pessoal:** 0 ocorrências em 5.937 arquivos.
- **Vistoria da casa:**
  - "3 a arrumar": eram as mudanças desta revisão ainda sem commit e os 3 commits da Antigravity sem envio. Resolvidos com o commit e o envio desta revisão.
  - "2 a olhar": o `relatorio_piloto.py`, que nada chama, e o log incompleto de 19/11. Os dois já estão na lista do K-127.

## 8. Alcance (D-030)

- **Olhado:** o que está listado no topo; `esquemas/log.schema.json` (as regras de tokens null); `scripts/orcamento.py` (a leitura das medidas); a busca de quem usa o estado e o μ fora do `calcular_mu_lambda.py`; as cinco linhas citadas da Fundação.
- **Fora:**
  - os 35 insumos, que são do passo 3 (o Claude Code relê às cegas e não os abriu agora para não perder a independência);
  - a análise de viabilidade de 24/11, da qual só o resumo está na trilha do acordo (os experimentos em sandbox não ficaram gravados);
  - a conversa da Antigravity além das falas registradas;
  - as 9 referências da `base.md`, que continuam "não conferido".
- **Sem log de execução desta revisão.** O esquema exige número de tokens, e o consumo desta conversa não é informado. É o mesmo problema do item 1 da §3, e gravar 0 o repetiria. A trilha é este arquivo e o commit.
