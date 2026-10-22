"""Funções comuns aos scripts do projeto Cultura Líquida.

- RAIZ: pasta do projeto.
- carregar_json / carregar_esquema.
- validar_objeto: usa `jsonschema` se estiver instalado (.venv); senão, um
  validador mínimo em Python puro que cobre o subconjunto usado em `esquemas/`.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESQUEMAS = RAIZ / "esquemas"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def carregar_json(caminho: Path | str):
    return json.loads(Path(caminho).read_text(encoding="utf-8"))


def carregar_esquema(nome: str) -> dict:
    """Aceita 'log', 'log.schema.json' ou um caminho. Os $ref para outro arquivo de
    esquemas/ (ex.: "comum.schema.json#/$defs/data" ou "valores-provisorios.json#/valores/...")
    são resolvidos na carga e postos no lugar: o registro de valores provisórios é lido
    daqui, sem cópia nos esquemas (brief, bloco 2)."""
    p = Path(nome)
    if not p.exists():
        base = nome if nome.endswith(".schema.json") else f"{nome}.schema.json"
        p = ESQUEMAS / base
    return _embutir(carregar_json(p), None, p.parent)


def carregar_valores() -> dict:
    """O registro único de valores provisórios (esquemas/valores-provisorios.json)."""
    return carregar_json(ESQUEMAS / "valores-provisorios.json")


def _ponteiro(raiz, ponteiro: str):
    no = raiz
    for parte in [x for x in ponteiro.lstrip("/").split("/") if x]:
        no = no[parte.replace("~1", "/").replace("~0", "~")]
    return no


def _embutir(no, raiz_externa, pasta: Path, arq_externo: str = "", vistos: tuple = ()):
    """Troca cada $ref externo pelo conteúdo apontado. Dentro de um pedaço vindo de
    outro arquivo, também os $ref locais (#/...) desse arquivo. Os $ref locais do
    esquema principal ficam como estão."""
    if isinstance(no, list):
        return [_embutir(x, raiz_externa, pasta, arq_externo, vistos) for x in no]
    if not isinstance(no, dict):
        return no
    ref = no.get("$ref")
    if isinstance(ref, str) and (not ref.startswith("#") or raiz_externa is not None):
        arq, _, ponteiro = ref.partition("#")
        if arq:
            raiz = carregar_json(pasta / arq)
        else:
            raiz, arq = raiz_externa, arq_externo
        chave = f"{arq}#{ponteiro}"
        if chave in vistos:
            raise ValueError(f"$ref circular: {chave}")
        alvo = _embutir(_ponteiro(raiz, ponteiro), raiz, pasta, arq, vistos + (chave,))
        resto = {k: _embutir(v, raiz_externa, pasta, arq_externo, vistos) for k, v in no.items() if k != "$ref"}
        return {"allOf": [alvo, resto]} if resto else alvo
    return {k: _embutir(v, raiz_externa, pasta, arq_externo, vistos) for k, v in no.items()}


def validar_objeto(obj, esquema: dict, minimo: bool = False) -> list[str]:
    """Devolve a lista de erros (vazia = válido)."""
    if not minimo:
        try:
            import jsonschema  # type: ignore

            v = jsonschema.Draft202012Validator(esquema)
            return [
                f"{'/'.join(str(x) for x in e.absolute_path) or '(raiz)'}: {e.message}"
                for e in sorted(v.iter_errors(obj), key=lambda e: list(map(str, e.absolute_path)))
            ]
        except ImportError:
            pass
    erros: list[str] = []
    _MiniValidador(esquema).validar(obj, esquema, "", erros)
    return erros


class _MiniValidador:
    """Validador mínimo (subconjunto do JSON Schema 2020-12): type, enum, const,
    required, properties, additionalProperties=false, items, minItems, minLength,
    minimum, maximum, minProperties, maxProperties, propertyNames, uniqueItems, pattern, $ref local
    (os externos chegam já embutidos por carregar_esquema), allOf, anyOf, oneOf, not, if/then/else."""

    TIPOS = {
        "object": dict, "array": list, "string": str, "boolean": bool,
        "null": type(None),
    }

    def __init__(self, raiz: dict):
        self.raiz = raiz

    def _tipo_ok(self, obj, t) -> bool:
        if t == "integer":
            return isinstance(obj, int) and not isinstance(obj, bool)
        if t == "number":
            return isinstance(obj, (int, float)) and not isinstance(obj, bool)
        return isinstance(obj, self.TIPOS[t])

    def _resolver(self, ref: str) -> dict:
        assert ref.startswith("#/"), f"só $ref local: {ref}"
        no = self.raiz
        for parte in ref[2:].split("/"):
            no = no[parte]
        return no

    def ok(self, obj, esq) -> bool:
        e: list[str] = []
        self.validar(obj, esq, "", e)
        return not e

    def validar(self, obj, esq, caminho, erros):
        if esq is True or esq == {}:
            return
        if "$ref" in esq:
            self.validar(obj, self._resolver(esq["$ref"]), caminho, erros)
        c = caminho or "(raiz)"
        if "type" in esq:
            tipos = esq["type"] if isinstance(esq["type"], list) else [esq["type"]]
            if not any(self._tipo_ok(obj, t) for t in tipos):
                erros.append(f"{c}: tipo esperado {tipos}")
                return
        if "enum" in esq and obj not in esq["enum"]:
            erros.append(f"{c}: {obj!r} fora de {esq['enum']}")
        if "const" in esq and obj != esq["const"]:
            erros.append(f"{c}: esperado {esq['const']!r}")
        if isinstance(obj, str):
            if len(obj) < esq.get("minLength", 0):
                erros.append(f"{c}: texto curto demais")
            if "pattern" in esq and not re.search(esq["pattern"], obj):
                erros.append(f"{c}: não casa com {esq['pattern']}")
        if isinstance(obj, (int, float)) and not isinstance(obj, bool):
            if "minimum" in esq and obj < esq["minimum"]:
                erros.append(f"{c}: menor que {esq['minimum']}")
            if "maximum" in esq and obj > esq["maximum"]:
                erros.append(f"{c}: maior que {esq['maximum']}")
        if isinstance(obj, dict):
            for r in esq.get("required", []):
                if r not in obj:
                    erros.append(f"{c}: falta o campo obrigatório '{r}'")
            props = esq.get("properties", {})
            for k, v in obj.items():
                if k in props:
                    self.validar(v, props[k], f"{caminho}/{k}", erros)
                elif esq.get("additionalProperties") is False:
                    erros.append(f"{c}: campo não previsto '{k}'")
                elif isinstance(esq.get("additionalProperties"), dict):
                    self.validar(v, esq["additionalProperties"], f"{caminho}/{k}", erros)
            if "propertyNames" in esq:
                for k in obj:
                    self.validar(k, esq["propertyNames"], f"{caminho}/{k}", erros)
            if len(obj) < esq.get("minProperties", 0):
                erros.append(f"{c}: campos de menos")
            if "maxProperties" in esq and len(obj) > esq["maxProperties"]:
                erros.append(f"{c}: campos demais")
        if isinstance(obj, list):
            if len(obj) < esq.get("minItems", 0):
                erros.append(f"{c}: itens de menos")
            if esq.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in obj}) < len(obj):
                erros.append(f"{c}: itens repetidos")
            if "items" in esq:
                for i, v in enumerate(obj):
                    self.validar(v, esq["items"], f"{caminho}/{i}", erros)
        for sub in esq.get("allOf", []):
            self.validar(obj, sub, caminho, erros)
        if "anyOf" in esq and not any(self.ok(obj, s) for s in esq["anyOf"]):
            erros.append(f"{c}: não atende a nenhuma opção de anyOf")
        if "oneOf" in esq:
            n = sum(self.ok(obj, s) for s in esq["oneOf"])
            if n != 1:
                erros.append(f"{c}: atende a {n} opções de oneOf (esperado 1)")
        if "not" in esq and self.ok(obj, esq["not"]):
            erros.append(f"{c}: atende ao que 'not' proíbe")
        if "if" in esq:
            if self.ok(obj, esq["if"]):
                if "then" in esq:
                    self.validar(obj, esq["then"], caminho, erros)
            elif "else" in esq:
                self.validar(obj, esq["else"], caminho, erros)
