# Serviço do K-004, primeiro momento: a ferramenta funcionando e as 5 aulas do caju

**Preparado em 27/11/2026** pelo Claude Code (Opus 5.5, esforço médio), a pedido de Vicente (fala 3, abaixo). **Estado: preparado. A execução começa com a autorização de Vicente.** Nada aqui é decisão nova: o que muda regra entra no O2, só com a confirmação dele (`registrar-decisao`).

**De onde vem:** a leitura de 27/11 na conversa com Vicente (o que impede a ferramenta de funcionar, o que a reunião pode fazer já, os módulos e o desenho das 5 aulas), feita só por leitura, sem agentes e sem mudar nada; e as falas abaixo.

## 0. Falas de Vicente (27/11), só para rastreabilidade
1. "[...] viabilizar o cultura liquida com rigor sem ter de finalizar todas as pendencias, e programando de forma organizada os melhoramentos. [...] A urgencia é ser capaz de bolar um programa de 5 aulas para falar sobre culturas liquidas brasileira começando com o caju [...] nao criar taferas novas para essa urgencia. já temos o plano disso em campo de acao, apenas dar foco. [...] a ideia é ficar pronto na primeira semana de dezembro."
2. "tenho 30% de tokens semanais do claude e 30% de tokens semanais do antigravity gemini para entregar a suite funcionando com as aulas do caju. O que daria pra realizar com isso sobre o que falta?"
3. "Prepare o serviço para voce realizar, diga o modelos, esforços, e os objetivos. o fim da linha não existe e por isso o funcionamento nao pode ser dependente do que falta. o que falta não pode ser esquecido durante o serviço, mas deve ser isolado dos objetivos. se o que falta precisar interagir com o serviço entra para o serviço. após o serviço que não precisa ir até o fim do prazo (poderia ser terminado antes e isso seria positivo) o gemini faz a auditoria e devolve. caso algo tenha ficado sem ser compreendido retorne para desambiguar."

## 1. Regra deste serviço (fala 3; a essência vira regra geral só pelo O2)
- Não existe fim da linha. O funcionamento não depende do que falta.
- O que falta não se esquece: fica na seção 5, isolado dos objetivos.
- O que falta entra no serviço só quando interage com ele, isto é, quando impede um objetivo de chegar ao seu "pronto quando".
- O que aparecer no caminho vira uma linha na seção 5, sem explorar (D-035).
- O serviço pode terminar antes de 5/12/2026. No fim, a Antigravity audita e devolve (seção 6).
- Um objetivo por vez (D-035; D-060, sem paralelismo). Commit e push ao fim de cada objetivo, com o RETOMAR em dia.

## 2. Orçamento
- **Leitura declarada por Vicente em 27/11:** restam 30% da semana do Claude e 30% da semana da Antigravity.
- **Claude:** a semana renova em 2/12/2026, 23h. Até lá cabem 20 pp até o teto de 90%. A partir de 80%, termina-se o passo em curso e grava-se o RETOMAR.
- **Previsto:** O1, de 1 a 2 pp; O2, de 2 a 4 pp; O3, de 4 a 6 pp. Total de 7 a 12 pp. Taxa do `orcamento.py`: 2 pp por conversa e 1,6 pp por 100 mil tokens de agente. O kit do K-114 mediu 103.960 tokens numa chamada do campo-de-acao.
- **Antigravity:** não há medida do gasto dela no projeto. A auditoria anota, no fim, quanto gastou.

## 3. Objetivos

| # | Objetivo | Quem, modelo e esforço | Custo | Pronto quando |
|---|---|---|---|---|
| O1 | A coleta diária volta a gravar | Claude Code, Opus 5.5, médio; sem agente | 1 a 2 pp | a próxima rodada diária grava "portão: passa" |
| O2 | Uma decisão só para o primeiro momento do K-004 | Claude Code, Opus 5.5, médio; sem agente | 2 a 4 pp | a decisão gravada e validada, com a confirmação de Vicente |
| O3 | O programa das 5 aulas do caju (K-121) | agente campo-de-acao, Sonnet 5.5, alto; o curador em Opus 5.5, médio | 4 a 6 pp | os 6 arquivos gravados, todas as marcas existindo no acervo, entregues a Vicente |

### O1 — A coleta diária volta a gravar
- **Por quê:** o portão da rotina diária reprovou todos os dias de 14 a 26/11; a última rodada aprovada foi a de 13/11. Nada dessas rodadas entrou no main.
  - De 14 a 20/11, a causa foram os 3 casos do kit (KeyError 'comando'), consertados no lote 1 do K-127.
  - De 21 a 26/11, foi "TRAVA: 20 problema(s)" (`trilhas/logs/2026-11-2x_portao-rotina.jsonl` na ramificação `rotinas`).
  - O lote 1 do K-127 tinha como "pronto quando" "o portão da rotina diária volta a passar", e isso não se cumpriu. Por isso o O1 não é tarefa nova.
- **Causa (conferida por script em 27/11):**
  - Em `scripts/trava_testes.py:65`, os arquivos de uma pasta citada por um caso são ordenados pelo próprio caminho.
  - No Windows, onde a trava foi gravada, essa ordem ignora maiúsculas; no Linux do GitHub, não.
  - Com a ordem do Linux, mudam exatamente 20 impressões, todas de `testes/coleta/casos.json`. É o número do log.
  - Localmente, num clone da ramificação `rotinas`, a suíte (272 OK, 0 FALHA, 3 PENDENTE) e a trava passam.
- **O quê:**
  - Ordenar por uma chave igual em qualquer sistema, que reproduz a ordem com que a trava foi gravada: `key=lambda x: tuple(s.lower() for s in x.relative_to(p).parts)`.
  - Nenhum caso nem impressão muda (conferido: 0 de 275). Por isso a trava não pede confirmação de Vicente (D-059).
  - A versão fica em `trava-testes-0.1`: as impressões e as fixtures não mudam. A razão vai no comentário e no commit.
- **Como provar:**
  1. A suíte local e a simulação da ordem do Linux, ambas com 0 diferenças.
  2. O pre-commit, que roda a suíte porque o commit toca código.
  3. Push.
  4. A rodada diária seguinte.
- **Se o que falta interagir:** se o portão reprovar depois por outra causa, essa causa entra no O1.

### O2 — Uma decisão só (primeiro momento do K-004)
- **Conteúdo proposto (essência a confirmar; seção 7, item 1):**
  - **(a) A pauta do K-004 passa a ser tornar a ferramenta viável com rigor, sem esperar o fim das pendências.**
    - Primeiro se resolve o que impede a coleta verificada, a organização e os planos de aula.
    - O resto vira módulos, programados de uma vez (Bloco 8, D-046).
    - A escrita da Fundação passa a ser um dos módulos, e não o "fim só" do K-004 (fala 6 de 20/11).
  - **(b) A regra da fala 3** (seção 1).
  - **(c) Os 3 [ABERTO] da D-061, pelas leituras em que as duas LLMs concordaram:**
    - declarar o quadro lógico agora, com a identidade no tempo como primeiro caso a observar;
    - uma página fixa de vieses no wiki e um bloco gerado por script, que vira módulo;
    - o carimbo mínimo basta no campo de ação, com uma nota de viés só quando o artefato sustenta decisão de poder.
  - **(d) Os insumos 143 e 144:** o 143 junta-se ao 144, e os dois se dissolvem no texto dos fundamentos 6 e 7; o código fica como está.
  - **(e) Opcional, só se Vicente quiser:** o [ABERTO] da D-058, isto é, se a operação com IA em escala é liberada com a fila montada ou só com ela resolvida.
- **Como:** pela `registrar-decisao`: a essência devolvida, as palavras conferidas e a confirmação de Vicente, com onde ele confirmou. Grava-se `trilhas/decisoes/D-062.json`, validado pelo esquema, e uma linha de essência no `AGENTS.md`. Uma decisão só: a fala 7 de 25/11 pede cuidado com mais um D-xx.
- **Não depende do O1 nem segura o O3.** Pode ser feito quando Vicente confirmar, em qualquer ponto do serviço.

### O3 — O programa das 5 aulas do caju (K-121, pedido real de Vicente)
- **Por que o K-121:**
  - O cartão já existe. O que ele pede: "Passo 9: campo de ação além do kit (planejador de aulas, guia do IPHAN, cartilha), sob demanda". O "pronto quando" dele: "um pedido real vira rascunho com fontes, revisado".
  - O campo-de-acao só é chamado depois do caso-piloto e quando Vicente pede um artefato. As duas condições valem.
- **Quem e como:**
  - O agente campo-de-acao (Sonnet 5.5, alto, harness 0.2.0), em 1 ou 2 chamadas, com teto de 25 turnos cada.
  - Ele lê a ficha (`acervo/fichas/CL-0001.md`), a camada Educação (`acervo/fichas/educacao/CL-0001.md`), o kit (`campo_de_acao/kit-fonte-primaria-cajuina.md`) e o desenho abaixo.
  - Grava item a item em `campo_de_acao/aulas-caju/`: `programa.md` e `aula-1.md` a `aula-5.md`, cada um marcado "rascunho, não publicado".
  - O curador grava o log de cada chamada (`scripts/registrar_log.py`).
- **Conferência pelo curador (script, sem IA):**
  - toda marca `[PR-nnnn]` e toda Fonte `FO-nnnn` citadas existem no acervo;
  - nenhum dado pessoal (`scripts/procurar_dado_pessoal.py`);
  - o carimbo mínimo em cada aula: versão da ficha, nível, Faltas, data, "como citar" e o aviso "não é orientação jurídica nem sanitária".
- **Quadro:** o K-121 entra em Fazendo durante o O3; o K-004 fica com o estado salvo no RETOMAR e volta depois (D-035).
- **Depois do O3:** a revisão de Vicente. Os ajustes podem cair na semana nova, de 3 a 4/12.

#### O pedido (o desenho das aulas, da leitura de 27/11)
**O fio:** cada aula segue uma dimensão da ferramenta (X insumo, Z tempo, Y processo, W compreensão local, e o hoje). Em toda aula se pratica o rigor da casa:
- separar "a fonte diz" de "eu digo" (fundamento 3);
- dizer a Falta em vez de completá-la (D-018);
- não julgar a prática (D-019).

Dizer o grau de cada frase também ensina: μ 0,5 é uma linhagem só.

| Aula | Conteúdo, com as marcas do acervo | Ceará e o hoje | Falta à vista | Tarefa |
|---|---|---|---|---|
| 1. O caju e o território (X) | acá-iu [PR-0022]; o pedúnculo [PR-0048; PR-0003]; o Delta do Parnaíba, terra dos Tremembé [PR-0411]; os nativos e o caju [PR-0011]; a safra [PR-0064], a chuva e o corte [PR-0261]; caju doce × clonado [PR-0142]; o pedúnculo jogado fora [PR-0032] | o caju como insumo de quem faz | o caju no Ceará de hoje (cajucultura, clone) não foi lido: 228 Entradas ficaram só como pegada (insumo 58) | registrar uma fonte primária de casa pelo kit, sem enviar |
| 2. Antes da cajuína: fermentar (Z) | a bebida indígena [PR-0020]; caoi ou caoim [PR-0011], cauim, caium (Termo candidato, insumo 91); a ascendência do vinho de caju, paracompleta [PR-0401; PR-0247; PR-0402]; o Rio Grande do Norte [PR-0113]; "mocororó" como nome da cajuína crua [PR-0130] e como outra bebida (CL-0003, candidata) | o uso por povo nomeado persiste no Ceará [PR-0412] | o detalhe fica fora (F-0033); vinho de caju, mocororó e caoi são candidatas (D-061) | fontes lado a lado sobre a ascendência, fechando com a Falta escrita |
| 3. O modo de fazer como conhecimento (Y) | o tanino no corte [PR-0093]; resina, cola e gelatina [PR-0058; PR-0006]; o filtro de tanino [PR-0099]; o banho-maria [PR-0103; PR-0117]; a cor [PR-0104]; a água, paracompleta [PR-0065] | Appert no Ceará, década de 1890 [PR-0235]; o farmacêutico e a vacina [PR-0408]; as redinhas de Pacajus [PR-0236] | todas com μ 0,5 (uma linhagem): dizer isso em aula | mapa do processo: o manual × a fala de quem faz |
| 4. Quem sabe e como se passa (W) | a casa e as mulheres [PR-0060; PR-0098]; as matriarcas nos rótulos [PR-0178]; a hospitalidade [PR-0349; PR-0254]; os cursos × a filtragem [PR-0116]; patroa e empregados [PR-0291; PR-0073]; o Iphan [PR-0054; PR-0056] | o livrinho de receitas do Ceará [PR-0240]; Piauí × Ceará [PR-0212; PR-0220]; Fortaleza, 1912 [PR-0238] | a W pouco captada (F-0027 a F-0031) | "quem me ensinou", com o consentimento do kit |
| 5. O caju hoje | a cajuína em pesquisa da UFC [PR-0036; PR-0037]; a bebida mista [PR-0008]; a IN 37/2018 [PR-0035]; o refrigerante [PR-0225]; o Crush Cajuína [PR-0137]; a padronização [PR-0138; PR-0143]; nativo × clonado [PR-0358]; o pequeno produtor [PR-0075]; Moçambique [PR-0045] | indústria, mercado e cultura (fala 7 de 25/11) | a cena atual da gastronomia cearense e o Guia Alimentar não estão no acervo | mini-ficha de um líquido da própria cultura alimentar, com uma proposta de ação |

**Cuidados nas 5 aulas:**
- nenhum nome de quem pratica (F-0032);
- povo nomeado sem detalhe ritual (F-0033; F-0024 na parte das outras bebidas);
- em escola indígena ou quilombola, a Falta da escuta vem antes;
- nada sanitário nem jurídico: não é receita; preparar ou provar em aula é escolha do educador;
- habilidades da BNCC só como sugestão, as do ensino médio (camada Educação); as do fundamental não foram lidas.

## 4. Ordem
1. **O1.** Não depende de nada.
2. **O3.** Depois das respostas da seção 7, ou com os valores provisórios ditos lá.
3. **O2.** Quando Vicente confirmar a essência; pode entrar antes, entre ou depois dos outros.
4. **Fim:** bastão à Antigravity para a auditoria (seção 6).

## 5. O que falta (isolado; não entra no serviço salvo se interagir)

| O que falta | Onde está | Entra no serviço se |
|---|---|---|
| Os 30 insumos, em 9 módulos (M1 relatórios: 46, 63, 111, 137, mais o aviso de reprovações seguidas; M2 escala: 70, 126, 128, 129, 132; M3 medida: 136, 139 e o fim do `orcamento.py`; M4 termos e outras CLB: 77, 87, 97, 123, 91, 131; M5 achar e ler: 49, 52, 53, 55, 58, 68, 69, 140; M6 receber: 61, 62, 112; M7 casa: 94, 104, 135; M8 menos IA: 141; M9 planejamento: Fundação v0.3, K-005, K-006, estacionados) | `saida-K-004.md` e `trilhas/insumos-planejamento.md` | algum deles impedir O1, O2 ou O3 (o M1 só entra se o O1 não puder ser provado sem ele) |
| O [ABERTO] da D-058 (liberar a leitura com IA em escala) | `trilhas/decisoes/D-058.json` | Vicente o incluir no O2 |
| Publicar: o K-010 e as Faltas "só para publicar" (F-0024 em parte, F-0025, F-0032, F-0033) | quadro, K-010 e K-203 a K-206 | o material das aulas for circular aberto (seção 7, item 3) |
| As Faltas de conteúdo das aulas (caju no Ceará hoje; a gastronomia cearense atual; o Guia Alimentar; as três CLB candidatas; a BNCC do fundamental) | seção 3, tabela das aulas | Vicente trouxer links: aí entram pela porta da entrada por link, com o avaliador (Haiku 5.5, alto) e o auditor (Sonnet 5.5, alto), de 4 a 6 pp, de preferência depois de 2/12 |
| Os acréscimos 1 e 2 da conferência dos exemplos | `reuniao.md`, seção 3 | nunca neste serviço (texto da Fundação, M9) |
| Depois (surgido no caminho) | — | — |

## 6. Auditoria da Antigravity (depois do serviço)
- **Quem:** a Antigravity (Gemini 4 Neon, o da releitura de 27/11), esforço alto. Ela não fez o serviço (D-038).
- **O que confere:**
  1. **O1:** a mudança é só a linha da ordenação; a trava tem 275 casos em ordem; o log da rodada diária mostra "portão: passa".
  2. **O2:** o texto da decisão é a essência confirmada, e não a transcrição da fala; não há exceção nova às regras vigentes (D-061, item 5).
  3. **O3:**
     - cada frase sobre a cajuína é fiel ao valor da Proposição marcada;
     - o grau é dito quando a Proposição é intermediária;
     - as Faltas e o carimbo estão em cada aula;
     - nenhum nome de quem pratica; nenhum detalhe ritual de povo nomeado;
     - nenhum fato sem fonte; nenhum exemplo virou regra (D-061, item 2).
  4. **Seção 5:** nada se perdeu e nada que falta entrou sem interagir.
- **Como devolve:** notas na seção 8 deste arquivo e o bastão no RETOMAR, para o Claude Code e Vicente. Valor provisório (seção 7, item 4): ela não corrige direto; quem fez corrige. No fim, anota quanto gastou.

## 7. A desambiguar com Vicente (cada item tem um valor provisório, para o serviço não depender da resposta)
1. **A essência do O2** (seção 3) está certa? Palavras a conferir:
   - "fim da linha": lido como o estado em que nada falta, que não existe;
   - "isolado": listado à parte, sem trabalho nele durante o serviço;
   - "interagir": quando o que falta impede um objetivo de chegar ao "pronto quando";
   - "suíte funcionando": a suíte de testes e a rotina diária gravando.
   - *Provisório:* o O2 espera; O1 e O3 seguem.
2. **Para quem são as 5 aulas, onde, e quanto tempo tem cada uma?**
   - *Provisório:* turma adulta de curso livre de gastronomia e cultura alimentar, aulas de 2 h em blocos de 30 min, e a BNCC como anexo para quem usar no ensino médio.
3. **O material das aulas fica com você e a turma, ou vai circular aberto?**
   - *Provisório:* rascunho para uso seu, não publicado. Se for circular, o K-010 entra no serviço.
4. **"A auditoria devolve":** a Antigravity só aponta, ou pode corrigir texto direto, como fez em 27/11 no `saida-K-004.md`?
   - *Provisório:* só aponta; quem fez corrige.

## 8. Auditoria da Antigravity (a preencher por ela)

## 9. Alcance (D-030)
- **Olhado em 27/11:**
  - `RETOMAR.md`, `reuniao.md`, `saida-K-004.md`;
  - a passagem de 15/11 e as falas de 14 a 25/11;
  - os 30 insumos no `trilhas/insumos-planejamento.md`;
  - a ficha e a camada Educação da cajuína, o kit, a Fundação (§5.9 e Passo 9), o quadro;
  - o acervo contado por script (Proposições por atributo, por Fonte e com o Ceará);
  - o log da rodada diária de 26/11 no GitHub Actions e os logs do portão de 14 a 21/11 na ramificação `rotinas`;
  - a trava rodada no main, numa cópia limpa e num clone da `rotinas`, e a simulação da ordem do Linux.
- **Fora:** as 2.544 Entradas brutas; nenhum fato externo conferido; o gasto desta conversa, que não foi medido.
