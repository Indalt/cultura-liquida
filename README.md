# Cultura Líquida Brasileira

Este repositório é a casa do projeto **Cultura Líquida Brasileira (CLB)**: uma ferramenta para encontrar, organizar e devolver o que se pode saber sobre as bebidas do Brasil e tudo o que as faz existir (os insumos, os modos de fazer, os recipientes, os tempos, os lugares, as pessoas e a forma como o saber passa de uma geração a outra), desde 1900, com cada informação rastreável até a fonte de onde veio.

Responsável: Vicente (fase 1: só ele e os agentes de IA, com registro de tudo). O repositório é **público**: o que entra aqui é publicação aberta.

## O que a ferramenta faz

A ferramenta trabalha em três movimentos:

1. **Rastrear:** busca em bibliotecas, repositórios e acervos (os "ambientes"), com consultas montadas a partir dos nomes das bebidas, e guarda o que viu, mesmo o que não usou.
2. **Organizar:** de cada fonte tira trechos literais (as "Evidências"), liga cada trecho a uma afirmação (a "Proposição"), monta os termos (os nomes das bebidas e as variantes), a ficha de cada bebida e um grafo que mostra o que as fontes dizem a favor e o que dizem de diferente, sem esconder as contradições e sem julgar a prática.
3. **Devolver e agir:** a ficha, uma camada para educadores e, quando Vicente pedir, materiais de ação.

O caso-piloto é a **cajuína** (CL-0001), um teste da ferramenta inteira. O piloto não é publicação.

As regras do projeto estão na **Fundação** (`00_Fundacao_Cultura_Liquida.md`) e, em resumo, no `AGENTS.md`. Uma regra de ouro: nenhum agente inventa solução fora do plano; diante de dificuldade, para e pergunta.

## Onde está cada coisa

| Pasta ou arquivo | O que guarda |
|---|---|
| `00_Fundacao_Cultura_Liquida.md` | A Fundação: o plano e as regras. Vale sobre tudo, com as exceções que o `AGENTS.md` diz. |
| `AGENTS.md`, `CLAUDE.md` | O resumo das regras e das decisões, e as notas para quem opera os agentes. |
| `ambientes/` | Os lugares de busca (`AM-nnnn`), as consultas (`consultas/`), as passadas de busca (`recortes/`) e as pegadas, que são o registro compacto de tudo o que se viu (`pegadas/`). |
| `entrada/` | O que chegou de cada busca e segue em trabalho (`EN-nnnn`). |
| `acervo/` | O conhecimento organizado: fontes, trechos, evidências, proposições, termos, bebidas (`clb/`), lugares, pessoas só por código, Faltas (o que não se sabe ou não se pode usar ainda) e as fichas (`fichas/`, com a camada Educação em `fichas/educacao/`). |
| `grafo/` | O grafo gerado pelos scripts: pontos, ligações e tabelas. |
| `esquemas/` | Os formatos de cada registro e os valores provisórios. |
| `scripts/` | Os programas que fazem o trabalho sem IA: buscar, localizar trechos, calcular, validar, montar relatórios. |
| `testes/` | Os casos de teste, com o relatório das rodadas A e B (`relatorio-rodada-B.md`). |
| `trilhas/` | O diário de tudo: o checklist do piloto, uma pasta por cartão de trabalho, as decisões de Vicente (`decisoes/`), os registros dos agentes (`logs/`), os insumos para melhorar o plano e o quadro de trabalho (`planejamento/quadro.md`). |
| `.claude/` | Os agentes de IA e as habilidades que eles usam, com exemplos reais. |
| `.githooks/` | O gancho que confere o acervo antes de cada gravação. |

## Como se retoma o trabalho

1. Abra uma conversa nova com o Claude Code nesta pasta. Ele lê o `CLAUDE.md` e o `AGENTS.md` sozinho.
2. Numa cópia nova do repositório, ligue o gancho uma vez: `git config core.hooksPath .githooks`. Sem ele, o acervo não é conferido antes de cada gravação; o relatório do dia avisa quando está desligado.
3. O ponto salvo está em três lugares: o quadro (`trilhas/planejamento/quadro.md`: o cartão em "Fazendo" é o que está em curso), o checklist do piloto (`trilhas/2026-10-17_execucao-piloto.md`) e a pasta do cartão em `trilhas/`.
4. Cada conversa de trabalho abre com `scripts/relatorio_dia.py` (o estado do dia) e `scripts/rodar_testes.py` (os testes).
5. Diga qual cartão autoriza e quanto da conta já usou na semana e na janela de 5 horas. O trabalho segue o brief de execuções (`trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md`).

Os programas rodam com Python 3.12; as dependências estão em `requirements.txt` (no Windows, o projeto usa o ambiente `.venv`).

## O que vive fora do Git, e por quê

O repositório é público. Por isso, algumas coisas ficam só na máquina de Vicente e nunca entram aqui:

| O quê | Onde fica | Por quê |
|---|---|---|
| A tabela de pessoas (código → nome) | `C:/Antigravity/Cultura Liquida - privado/pessoas/` (ou a pasta da variável `CL_PRIVADO`) | No acervo, as pessoas aparecem só por código (`P-nnnn`) e papel. Nome de terceiro é dado pessoal e não vai a um repositório público. |
| O conhecimento tradicional em detalhe | `C:/Antigravity/Cultura Liquida - privado/conhecimento-tradicional/` | O que uma Falta jurídica marca como conhecimento tradicional de um povo nomeado espera numa pasta local até a revisão jurídica (D-043). No Git ficam só o link, o localizador, o hash e a Falta. |
| O legado (o sistema anterior) | `legado/` (ignorado pelo Git) | Só leitura. Do legado entra só o que for verificável e condizente com as regras novas (D-024). |
| O wiki local | `wiki-local/` (ignorado pelo Git) | Uma visualização das fichas na máquina, para leitura. O piloto não publica site. |
| O bruto da coleta | fora do repositório | A fonte guarda o original e a busca o refaz; no Git ficam as pegadas e as Entradas de trabalho (D-045). |
| Os arquivos de tiers e de coleta cidadã | ignorados pelo `.gitignore` (`Controle_Usuarios_e_Tiers*`, `Respostas_Coleta_Cidada_Tier1*`) | Trazem dados de pessoas. |
| A pasta temporária das fontes | a pasta temporária do sistema, em `cultura-liquida/fontes` (ou `CL_FONTES_TMP`) | O texto integral das fontes, lido para localizar os trechos. É descartável: numa cópia nova pode não existir, e os scripts a refazem lendo a fonte de novo. O texto integral nunca entra no repositório. |

## Regras que não mudam sem decisão de Vicente

- Toda informação mostra de onde veio (link ou caminho).
- O que não se sabe fica dito como Falta, nunca completado por suposição.
- Nenhuma proteção contra robôs é contornada.
- Nenhum dado pessoal de terceiros entra no repositório.
- O plano só muda com uma decisão registrada em `trilhas/decisoes/`.
