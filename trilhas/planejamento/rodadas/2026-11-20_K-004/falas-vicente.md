# Falas de Vicente na conversa de planejamento de 20/11/2026 (K-004)

Trilha das falas (acordo 4). Uma essência só vale como diretriz depois de confirmada por Vicente (habilidade `registrar-decisao`); até lá, o que está aqui é leitura do curador.

## Fala 1 (abertura)

> analisar esses 142 insumos e procurar saber se estes 82 em aberto não podem ser problemas similares que foram se acumulando enquanto a ferramenta era construida e vamos buscar reduzir estes 82

Feito pela regra da D-058: `limpeza/resultado.md` (commit 5a2714c). Dos 82 abertos, ficam 32, em 12 famílias.

## Fala 2 (depois do resultado)

> Limpar e arrumar o sistema é o primeiro passo. vamos organizar o que e como? para que nao haja overthinkig, o que deve fazer tb e como evitar que os consertos gerem novos problemas por circularidade de pensamento?

Responde à pergunta do curador sobre os insumos 94 e 135 (se arrumar a casa é parte do que a ferramenta promete).

### Essência devolvida (à espera de confirmação)

Antes dos outros consertos, limpa-se e arruma-se a ferramenta: fica o que serve à forma final, pelo caminho mais simples já achado, e a casa passa a dizer a verdade sobre si mesma e a custar pouco para abrir. A limpeza tem uma lista fechada e uma hora de parar, e é feita de um jeito que não crie problema novo.

### Palavras a conferir

- **"o sistema"**: lido como a ferramenta e a casa (scripts, esquemas, habilidades, agentes, rotinas, AGENTS.md e CLAUDE.md, a raiz da pasta); não a base (acervo e Entradas) nem a trilha (logs, decisões, insumos, falas), que não se limpam.
- **"o primeiro passo"**: lido como o primeiro da fila de consertos, antes dos outros insumos que ficam. Em aberto: onde fica o K-126 (as três CLB candidatas, D-057) em relação à limpeza.
- **"o que deve fazer tb"**: lido como o que fazer, além da lista, para não haver overthinking (escopo fechado e regra de parada).

### Organização devolvida (proposta do curador, não decisão)

**O que.** Vistoria da casa de 20/11 (`scripts/manutencao.py`, sem IA): 5.889 arquivos, 21,5 MB; 3 a arrumar (a pasta `campo_de_acao/` na raiz; AGENTS.md e CLAUDE.md com 32.256 caracteres contra o limite de 24.000; o RETOMAR citando o K-126) e 5 a olhar (dois caminhos citados sem a pasta, no RETOMAR; `resumo_coleta.py` e `relatorio_piloto.py` que nada chama; um agente de 19/11 sem log completo). Com os insumos da família "casa e harness" (94, 105, 135) e os de "registros e relatórios fiéis" (46, 63, 111, 137):
1. tirar o que nada usa (script sem chamada, a ramificação que sobrou da rotina de 13/11, comentários e passos que só serviram ao caminho); sair do código não é apagar: fica no histórico do Git, com o porquê no commit;
2. enxugar o que toda conversa e todo agente carregam (AGENTS.md e CLAUDE.md): o histórico vai para o checklist, as essências das decisões ficam; o texto das decisões só Vicente muda;
3. cada coisa no seu lugar: os números provisórios que moram em scripts (cadência, 101; limites da vistoria, 135; ritmo do Internet Archive, 102) vão ao registro de valores, sem mudar o valor; a pasta da raiz;
4. a casa dizendo a verdade: o estado dos 69 ambientes (137), a contagem do relatório do dia (111), o relatório do lote (63), a Execução descartada no log (46), a checagem de agente ou habilidade que não carrega (105) e a vistoria rodando sozinha (135).
Fora da limpeza: o resto dos 32 (achar outras CLB, ler a fonte, receber, jurídico, pessoas, custo, rotina com IA), que vem depois, na fila.

**Como.** Inventário por script (quem chama cada script, esquema e habilidade), em uma lista de uma linha por item: fica, sai ou muda de lugar, com o porquê; essa lista é o escopo. Fica o que algo vivo usa (rotina, teste, habilidade, portão, wiki) e toda a trilha. Lotes pequenos por área; cada lote passa na suíte de testes, no validador do acervo e no portão da rotina antes do commit e do push, e um auditor confere que só mudou o que a lista dizia (D-038). Uma conversa de desenvolvimento, com teto em pp; agente só onde for preciso ler texto.

**Contra o overthinking.** A lista do começo é o escopo; o que aparecer no caminho vira uma linha em "depois", sem explorar (D-035). Cada lote tem um "pronto quando" de uma linha, medido por script; para quando a lista acaba, não quando fica perfeito. Nenhum documento de análise novo: a trilha é a lista e os commits.

**Contra a circularidade.** Pela limpeza da lista, 5 insumos nasceram do conserto de outro (100 do 76, 99 do 80, 53 do 32, 102 do 78, 97 do 89) e 3 cartões fecharam sem resolver o insumo (o 137 repete o 47; o 54, o 44; o 140, o 118). Daí:
1. limpar não muda comportamento: só tirar e mudar de lugar, sem lógica nova; a prova é a suíte e o portão iguais antes e depois;
2. o lote que quebra algo volta inteiro (git revert); não se conserta por cima;
3. o insumo fecha quando o seu "aonde se quer chegar" é conferido, numa linha (cumprido ou não), e não quando o cartão fecha;
4. regra ou número novo não nasce escondido num conserto: vai ao registro de valores como provisório e a Vicente como regra (D-038);
5. a regra da D-058 vale também na porta: só vira insumo o que é problema para a promessa; o resto é nota (proposta de regra nova, para Vicente).

## Fala 3 (resposta à organização)

> ok. adicione isso aos testes para que quando um teste nao passar por mudanças somos obrigados a verificar e confirmar antes de admitir a mudança

Leitura do curador: o "ok" confirma a essência e a organização devolvidas na fala 2, com as leituras de "o sistema", "o primeiro passo" e "o que deve fazer tb"; não responde ao lugar do K-126, que segue [ABERTO] (a resposta que confirma a lista não se lê como resposta a uma pergunta que ela não toca; insumo 142). Registrada como D-059 (`trilhas/decisoes/D-059.json`), com o cartão K-127.

O pedido da trava foi feito na mesma conversa (D-059, item 6): `scripts/trava_testes.py` guarda a impressão dos 271 casos da suíte; o `rodar_testes.py` (o que valida no GitHub e o portão da rotina) e o pre-commit reprovam caso mudado ou tirado sem confirmação; o pre-commit também roda a suíte quando o commit toca código, esquemas, testes ou harness.

Devolvido a Vicente como leitura, a confirmar: quem confirma a mudança de um teste é ele (a trava pede "--confirmado-por vicente" e onde ele confirmou); o caso novo entra sem confirmação; a suíte só roda no pre-commit quando o commit toca código, esquemas, testes ou harness.
