# Resultado da rotina de teste (K-113, bloco 10b) — 2026-11-13

## 1. CLAUDE.md
- Marca de teste no contexto inicial: **CAJU-7319** (sim).
- Texto do AGENTS.md no contexto: sim. Título: "AGENTS.md — regras do projeto Cultura Líquida"; primeira seção: "O projeto em 5 linhas".

## 2. Agentes e habilidades
- Agent oferece: arquivista, auditor, avaliador, campo-de-acao, claude, claude-code-guide, curador, Explore, general-purpose, juridico, nimble:nimble-analyst, nimble:nimble-researcher, Plan, rastreador, redator, statusline-setup.
- Habilidades do projeto no contexto: conferir-fato, consulta, escrever-secao-fundacao, executar-brief, extrair-evidencia, ficha-de-acesso, gerar-grafo, guia-de-liberacao, kit-fonte-primaria, montar-ficha, registrar-decisao, registrar-melhoria, registrar-termo, triagem-juridica, verificar-fundacao (além de muitas de plugins).
- `ls .claude/agents`: arquivista, auditor, avaliador, campo-de-acao, curador, juridico, rastreador, redator (.md). `ls .claude/skills`: as mesmas 15 habilidades acima. Coincidem.

## 3. Git e conta
- Ramificação inicial: main
- Remoto: origin https://github.com/Indalt/cultura-liquida-teste-rotina (fetch e push), sem credencial visível
- user.name: Claude; user.email: noreply@anthropic.com
- gh: /usr/local/bin/gh existe

## 4. Rede (código HTTP ou erro)
- bdtd.ibict.br: erro curl 56, CONNECT 403 (proxy, fora da lista)
- oasisbr.ibict.br: erro curl 56, CONNECT 403
- infoteca.cnptia.embrapa.br: erro curl 56, CONNECT 403
- bcr.iphan.gov.br: erro curl 56, CONNECT 403
- api.openalex.org: erro curl 56, CONNECT 403
- web.archive.org: erro curl 56, CONNECT 403
- pypi.org/simple/jsonschema/: 200
- github.com/: 400
- HTTP_PROXY/http_proxy: vazias; HTTPS_PROXY/https_proxy: host 127.0.0.1
- python3 3.11.18; `pip install jsonschema`: funcionou (rc 0, só aviso de root)

## 5. Auditor
- Chamada pela ferramenta Agent funcionou. Resposta: primeira linha com D-038 em AGENTS.md = 21 (conferi por grep: confere).
- Modelo informado pelo próprio agente: claude-sonnet-5-5. Uma chamada de 3 (Grep). Tokens e chamadas na notificação final: 29.864 tokens, 2 usos de ferramenta (o relato do agente dizia 1 chamada).

## 6. Ramificação e principal
- Ramificação `claude/teste-rotina` criada; commit e `git push -u origin claude/teste-rotina`: **aceito** (nova ramificação).
- Teste na principal: commit vazio numa cópia local de main e `git push origin HEAD:main`: **ACEITO**, sem recusa e sem mensagem de erro (`9a3008b..85a4711  HEAD -> main`). A principal NÃO está protegida contra gravação direta por esta conta. Nenhum outro caminho foi tentado. Observação: o commit vazio "teste: a rotina tenta gravar na principal" agora está em main.
- Autor e committer do commit na ramificação: `Claude <noreply@anthropic.com> | Claude <noreply@anthropic.com>`.

## 7. Tabela
| Passo | O que se viu |
|---|---|
| 1 | Marca CAJU-7319 e AGENTS.md no contexto |
| 2 | 16 tipos de agente; 15 habilidades do projeto; ls coincide |
| 3 | main; remoto Indalt/cultura-liquida-teste-rotina; Claude <noreply@anthropic.com>; gh presente |
| 4 | Só pypi (200) e github.com (400); os outros 6 domínios, 403 de proxy; pip jsonschema ok; Python 3.11.18 |
| 5 | Auditor funcionou, linha 21, claude-sonnet-5-5, 29.864 tokens |
| 6 | Push em ramificação aceito; push na main aceito (sem proteção) |

