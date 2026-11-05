# Passo a passo: deixar a rotina juntar a ramificação `rotinas` ao `main` (K-112; D-048)

**Para quem:** Vicente, dono do repositório `Indalt/cultura-liquida`. Não é decisão nova: é o ajuste que
só o dono faz para a junção pelo portão, que a D-048 já decidiu.

## Por que precisa

- A proteção do `main` pede uma revisão aprovada antes de cada junção (`required_approving_review_count: 1`)
  e não vale para administradores (`enforce_admins: false`; conferido pela API em 04/11/2026).
- O token que o próprio workflow recebe (`GITHUB_TOKEN`) não é administrador: o envio dele ao `main`
  é barrado. Sem o ajuste, a rotina segue gravando todo dia na ramificação `rotinas`, com o portão rodado,
  e o `main` fica para trás (o relatório do dia mostra quantos commits).
- Com um token seu, só com permissão de conteúdo deste repositório, guardado como segredo, a rotina
  envia `rotinas` ao `main` **só quando o portão da camada 1 passa** (`scripts/portao.py`: validador,
  deduplicação, dado pessoal e a suíte de testes). Quem propõe (a rotina) não aprova: o portão é script,
  com a versão gravada no log de cada junção (D-038).

## Passos (uns 5 minutos)

1. Abra <https://github.com/settings/personal-access-tokens/new> (token de acesso fino, "Fine-grained").
2. **Token name:** `cultura-liquida-rotinas`. **Expiration:** a maior que a página oferecer (o GitHub
   avisa por e-mail antes de vencer; vencido, a rotina volta a gravar só em `rotinas`, sem perder nada).
3. **Resource owner:** Indalt. **Repository access:** *Only select repositories* → `Indalt/cultura-liquida`.
4. **Permissions → Repository permissions:** *Contents* → **Read and write**. Nada mais.
5. **Generate token** e copie o valor (ele só aparece uma vez).
6. Abra <https://github.com/Indalt/cultura-liquida/settings/secrets/actions> → **New repository secret**.
   **Name:** `ROTINAS_TOKEN`. **Secret:** cole o valor. **Add secret**.
7. Pronto. Na rodada seguinte, o passo "Junção ao main pelo portão" do workflow `rotinas` diz
   "junção: main em dia com rotinas" no comentário do relatório do dia.

## Para desfazer

Apague o segredo `ROTINAS_TOKEN` (mesma página do passo 6) ou revogue o token em
<https://github.com/settings/personal-access-tokens>. A rotina volta a gravar só em `rotinas`.

## O que fica não conferido

- Se o envio com o seu token ao `main` passa pela proteção como passa o seu `git push` de hoje (o aviso
  "Bypassed rule violations" é o esperado); confere-se na primeira junção, e o resultado vai à trilha.
- Se o commit do workflow conta como atividade contra a desativação de 60 dias dos workflows agendados
  em repositório público (C112.5, não conferido pela documentação; confere-se pelo próprio GitHub,
  que avisa por e-mail antes de desativar).
