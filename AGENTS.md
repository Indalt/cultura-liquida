# AGENTS.md — regras do projeto Cultura Líquida

Resumo para qualquer agente que trabalhe nesta pasta. A fonte de verdade é `00_Fundacao_Cultura_Liquida.md` (hoje v0.1; a v0.2 está em escrita). Na dúvida, vale a Fundação; enquanto a v0.2 não sair, vale o brief em `trilhas/2026-10-15_pesquisa/clb-execucao-v0.2-brief.md`.

## O projeto em 5 linhas
- **Cultura Líquida Brasileira (CLB):** uma bebida e tudo o que a faz existir (insumos, modos de fazer, recipientes, tempos, lugares, pessoas, transmissão). Nativos primeiro, aculturados incluídos.
- **Propósito:** encontrar, organizar e devolver o que se pode saber sobre as CLB desde 1900, com cada informação rastreável até a origem.
- **Três movimentos:** rastrear (ambientes e consultas), organizar (wiki, termos, grafo 4D paraconsistente) e devolver e agir (educação, salvaguarda, campo de ação sob demanda).
- **Fase 1:** só Vicente e os agentes, com logs. Responsável: Vicente, pessoa natural (D-026).
- **Casa:** este repositório, `Indalt/cultura-liquida`, **público** (D-021).

## Regra de Ouro e acordos (§0 da Fundação)
- **Regra de Ouro (P38):** nenhum agente inventa solução fora do plano. Diante de dificuldade, recorre à Fundação e ao brief; se não resolverem, **para e pergunta a Vicente**.
- **Acordos:**
  1. Perguntas servem para compreender, nunca para direcionar com escolhas binárias.
  2. Nada de simulação apresentada como execução (P96): o que não foi feito não é relatado como feito.
  3. Não simplificar para conseguir executar (P79): se não couber, dizer e parar.
  4. Tudo deixa trilha: o que se buscou, onde, o que se achou, o que se descartou e por quê.
  5. O plano só muda com entrada no Registro de Decisões e nova versão da Fundação.
  6. Exemplos ilustram e nunca limitam (D-017).
- **[PROPOSTA] não é plano:** nenhum agente executa um item marcado [PROPOSTA] sem decisão registrada.
- **Comentário novo de Vicente:** captar a essência, conferir palavras ambíguas ("por princípio" pode ser "de início"), devolver o entendido, e só depois registrar como diretriz (nunca como transcrição).

## Princípios (§2, uma linha cada; "Pn" = pedido n de Vicente, Anexo A, buscar `#### Pn`)
1. Transparência e rastreabilidade: cada informação mostra de onde veio, link ou caminho (P90–P93, P97).
2. Ciência terminológica: termos e booleanos de baixo para cima; a variação é dado (P3, P23, P24).
3. Lógica paraconsistente no grafo 4D (X insumo, Y processo, Z tempo, W compreensão local): contradições convivem (P27–P29).
4. Rigor com o poder, hospitalidade com o vestígio: o que sustenta decisão exige fonte forte; fragmentos entram com selo (P22, P13).
5. Cânone rigoroso, aberto ao desconhecido (P5).
6. Nativos primeiro, aculturados incluídos (P6).
7. De baixo para cima: categorias nascem das fontes e das pessoas (P24).
8. Descritores processuais, não genéricos (P3).
9. Fontes reais e verificáveis para tudo, inclusive para o auditor (P90–P92).
10. Quarentena não descarta; valências equilibradas (P85–P87).
11. Persistência e reconstituição: tudo nesta pasta, legível por qualquer IA (P42).
12. Institucionalidade sem invasão: avisar, nunca apagar nem discriminar.
13. Leis brasileiras como moldura.
14. Tiers são grupos de interesse, não monetização.
15. Campo de ação sob demanda, nunca automático.
16. Infraestrutura simples, fidedigna e segura.

## Decisões vigentes (essência confirmada por Vicente)
- **D-015:** a Fundação passa à v0.2, com as melhorias da análise de 15–16/10.
- **D-016:** Vicente tem 1 a 3 h por semana de curadoria; os "15" nunca são teto de coleta.
- **D-017:** exemplos ilustram e nunca limitam o trabalho.
- **D-018:** W é a prática **comum** da região (conhecimento compartilhado), episteme própria **mas traduzível**, tratada como dimensão; o não captado é **Falta**, dita e nunca completada; o saber comum muda de forma autóctone ou por interação.
- **D-019:** **não julgamos.** Fonte contrária só documenta; se a fonte corrige, documenta-se a correção; não é preciso documentar tudo; prática que atende aos critérios é admitida e pode ignorar revisionismo.
- **D-020:** o agente Jurídico é de precaução: cria Faltas e nunca autoriza.
- **D-021:** GitHub na conta Indalt, sincronizado, commits de Vicente; repositório **público** (o que entra no Git é publicação aberta; legado e dados pessoais de terceiros ficam fora); Google só se necessário; nuvem a considerar.
- **D-022:** critérios de prática cultural vêm da lei: CF art. 216; Convenção UNESCO 2003 (Decreto 5.753/2006, art. 2); Decreto 3.551/2000.
- **D-023:** medir e parar antes de acabar, com o estado salvo; teto provisório de 300 mil tokens/semana em agentes na operação da fase 1.
- **D-024:** do legado, só entra o verificável e condizente com as regras novas; o resto não se apaga (Drive e `legado/`, só leitura); o site não é aproveitado.
- **D-025:** regras valem "de início" e são proporcionais; revisão de essencialidade depois da fase 1; nenhuma obrigação legal é desprezada e toda barreira jurídica traz porquê e caminho de liberação assistido; o grafo 4D fica fora da revisão.
- **D-026:** fase 1 só com Vicente e agentes, com logs; segunda leitura = validador + verificador de harness diferente + amostra sorteada.
- **D-027:** execução em Opus 5.5 médio com harness; subagentes em Sonnet 5.5 alto (sugestão medida); depois, modelos por tarefa escolhidos **por teste**.
- **D-028:** a execução não para para aprovar o que já foi decidido.
- **D-029:** os agentes, habilidades e harness ficam em `.claude/` antes da v0.2, que é escrita por eles, com logs; só o Claude Code os opera; o caso-piloto continua no Passo 1.

## Passo corrente
- **Feito:** Blocos 1 e 2 (repositório, conferências C1 e C2) e Bloco 2.5 (agentes, habilidades, harness).
- **Próximo:** Blocos 3 e 4 do brief (escrever a v0.2, conduzida pelos agentes). Depois, Passo 1 da Fundação (caso-piloto, testes de modelos).
- **Estado do trabalho:** `trilhas/2026-10-16_execucao-v0.2.md` (checklist). Leia-o antes de qualquer passo.

## Agentes e habilidades (`.claude/agents/`, `.claude/skills/`)
| Agente | Papel | Habilidades | Modelo inicial |
|---|---|---|---|
| curador | sessão principal: brief, decisões, checklist, orçamento, logs | executar-brief, registrar-decisao | Opus 5.5, médio |
| redator | escreve os textos (v0.2, Educação, boletim) | escrever-secao-fundacao | Opus 5.5, médio |
| auditor | verificação mecânica e independente | verificar-fundacao, conferir-fato | Sonnet 5.5, alto |
| juridico | precaução: cria Faltas, prepara guias de liberação | conferir-fato, triagem-juridica, guia-de-liberacao | Sonnet 5.5, alto |
| rastreador | ambientes, fichas de acesso, consultas, pegadas | ficha-de-acesso, consulta | Sonnet 5.5, alto (testar Haiku) |
| avaliador | valências, quarentena, evidência com trecho literal | extrair-evidencia | a definir no Passo 1 |
| arquivista | termos, fichas, grafo 4D | registrar-termo, montar-ficha, gerar-grafo | a definir no Passo 1 |
| campo-de-acao | ferramentas de ação sob demanda | kit-fonte-primaria | a definir |

Os modelos são provisórios até os testes do Passo 1. Avaliador, arquivista e campo-de-acao têm exemplos "pendente: caso-piloto (Passo 1)" e não devem ser chamados antes dele.

## Orçamento (D-023)
- Medir e parar antes de acabar. Antes de cada agente: consumido + estimativa ≤ teto da janela; não abrir lote se a folga for menor que 2× o maior lote já medido.
- Todo agente tem teto: pesquisa web, 15 a 20 chamadas; leitura só por `grep -n` e faixas de linhas.
- Para planejar: cerca de 60 mil tokens por agente Sonnet com teto (medidos: 34 a 82 mil).
- Todo agente grava log (`scripts/registrar_log.py`); o curador soma os tokens no checklist.

## Fatos e fontes
- Todo fato novo traz **URL e nível**: "oficial" só se a página oficial abriu; senão "secundária" ou "não conferido". Nada de memória apresentada como conferido.
- Fato que não se consegue conferir não é motivo de parada: marcar "não conferido" e seguir.
- **Proteções anti-robô nunca se contornam** (403, captcha, verificação de navegador).
- Leis no planalto.gov.br: extrair só o artigo (`grep -n` e recorte), nunca a página inteira.

## Onde está cada coisa
- `00_Fundacao_Cultura_Liquida.md`: a Fundação. Anexos A e B são intocáveis (conferir com `scripts/comparar_anexos.py`).
- `trilhas/`: diário, checklist, pesquisa (`2026-10-15_pesquisa/`, com `indice.md`), conferências (`2026-10-16_conferencias/`) e logs (`logs/`).
- `esquemas/`: JSON Schema de log, conferência, Falta, guia de liberação, achado e decisão.
- `scripts/`: registrar log, procurar dado pessoal, comparar anexos, checar a Fundação, validar JSON.
- `testes/`: relatórios das rodadas de teste dos validadores.
- `.claude/agents/`, `.claude/skills/<nome>/` (SKILL.md, `exemplos/`): agentes e habilidades.
- `legado/`: sistema anterior, **fora do Git e só leitura**.

## O que não fazer
- Não pôr dado pessoal de terceiros no Git (e-mail, telefone, CPF, @perfil, nome de quem não consentiu). O e-mail de Vicente, como responsável, é permitido. Rodar `scripts/procurar_dado_pessoal.py` antes de cada commit.
- Não processar o legado nem abrir os Docs antes do Passo 3.
- Não criar rotinas na nuvem nem GitHub Actions antes do Passo 4.
- Não publicar site.
- Não reabrir decisão vigente: registrar o conflito e perguntar a Vicente.
- Não completar Falta por inferência; não julgar a prática; o Jurídico nunca autoriza nem protocola em nome de Vicente.
- Não lançar agentes em paralelo sem teto; não usar Workflow sem pedido explícito de Vicente.
