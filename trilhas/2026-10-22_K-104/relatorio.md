# K-104 (bloco 2): relatório

**Data:** 22/10/2026. **Quem fez:** o curador (Opus 5.5, esforço médio). **Quem conferiu:** o auditor (Sonnet 5.5, esforço alto). Este relatório não pede aprovação (D-037).

## O que entrou
- **Registro de valores provisórios:** `esquemas/valores-provisorios.json`, com o esquema dele. A estrutura que a D-038 fixa fica separada dos valores, que podem mudar. Os esquemas leem o registro por `$ref`, e os scripts por `carregar_valores()`. Ninguém guarda cópia.
- **Contratos do §6 em `esquemas/`:** 18 contratos, de Termo a Pessoa, mais `comum`, `ficha-acesso` e `estado-consulta`. O Insumo do §6 ficou como `insumo-x`, porque `insumo.schema.json` já é o esquema do planejamento.
- **Exemplos:** `esquemas/exemplos/` tem 40 casos, que rodam em `rodar_testes.py`.
  - Usam dado real do mapa de 17/10 os exemplos de Termo, Proposição, Fonte, Ambiente, Recorte, Trecho e Lugar. Os outros levam a marca "exemplo de esquema".
  - Os IDs dos exemplos ficam na faixa 900000-999999, que nenhum gravador usa.
- **Rastreador:** os 4 casos reais saíram de PENDENTE.
  - Reprovam como esperado: a ficha com 403 e decisão "aceito"; o total visto acima do informado sem explicação.
  - A segunda é uma regra entre campos, aplicada em `validar.py`.
- **Parada (c):** valeu o padrão de Vicente. A tabela código → nome fica numa pasta da máquina dele, fora da pasta versionada.
  - Caminho padrão: `C:/Antigravity/Cultura Liquida - privado/pessoas/`.
  - Se a variável `CL_PRIVADO` estiver definida, ela vale no lugar do caminho padrão.

## O que o auditor achou
Os 5 achados foram corrigidos (`achados-auditor.json`):
- **A-001:** a retirada passa a ficar sem o conteúdo.
- **A-002 e A-003:** os campos de proteção ficam obrigatórios na Pessoa e permitidos em todos os contratos.
- **A-004:** "não calculado" sai do eixo 4. Até o cálculo, a Proposição fica sem o campo de estado.
- **A-005:** a Aresta ganha `estado_detalhe`.

Os estados da busca que ele deixou em quarentena entraram no registro (`estados_busca`).

Lote C4 (`conferencia-C4.json`):
- **SKOS:** oficial, conferido no w3.org.
- **TBX:** oficial pelo tbxinfo.
- **ISO 30042:** não conferida, porque a página da ISO deu 403.

## Quarentena e Faltas novas
Não há: o bloco não processa itens da base.

## Não conferido
- A ISO 30042 na página da ISO.
- A equivalência campo a campo do Termo com TBX e SKOS.
- Uma segunda leitura independente das correções A-001 a A-005.

## Insumos
- **29:** agente sem Write não consegue validar JSON por heredoc.
- **30:** o Termo não guarda a língua das designações.
- **31:** o User-Agent do projeto não está definido.

## Consumo
- **Agentes:** 143.833 tokens (auditor, 20 chamadas). A semana de 19 a 25/10 soma 217.297.
- **Próximo auditor:** pela regra de folga (`orcamento.py`), só cabe na semana de 26/10.
