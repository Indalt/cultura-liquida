"""Funções comuns aos scripts de coleta (bloco 5): o cliente HTTP, a Execução e o log com alcance.

- Cliente: identifica o robô, respeita o robots.txt de cada host e faz no máximo 1 pedido por
  segundo (brief, bloco 5; Fundação l. 430). Proteção anti-robô (403, captcha, verificação de
  navegador) nunca se contorna: o pedido para e o erro vai ao Recorte e ao log.
  Com `fixtures`, responde de arquivos gravados (testes, sem rede); com `gravar_fixtures`, grava as
  respostas reais para virar teste (o curador tira delas todo nome de pessoa antes de versionar).
- Execucao: reserva o id da Execução (EX-nnnn, faixa da conversa; registrar_log.py) antes de gravar
  qualquer registro, porque todo registro traz a Execução na origem (l. 587), e grava no fim o log
  com o alcance calculado (D-030): o que se olhou e o que ficou fora.
"""
from __future__ import annotations

import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from datetime import date
from pathlib import Path

from _comum import RAIZ, carregar_json
import registrar_log

ROBO = "CulturaLiquida-coleta/0.1 (+https://github.com/Indalt/cultura-liquida)"
INTERVALO_S = 1.0  # 1 pedido por segundo (brief, bloco 5)
SINAIS_ANTIROBO = ("captcha", "cf-chl", "challenge-platform", "just a moment", "verificação de navegador")


class BloqueioRobos(Exception):
    """O robots.txt veda o caminho ao robô."""


class BloqueioAntiRobo(Exception):
    """403, captcha ou verificação de navegador: não se contorna (l. 419)."""


class Resposta:
    def __init__(self, url: str, status: int, headers: dict, corpo: str):
        self.url, self.status, self.headers, self.corpo = url, status, headers, corpo

    def json(self):
        return json.loads(self.corpo)


def _nome_fixture(metodo: str, url: str) -> str:
    return hashlib.sha1(f"{metodo} {url}".encode("utf-8")).hexdigest()[:16] + ".json"


class Cliente:
    def __init__(self, fixtures: Path | None = None, gravar_fixtures: Path | None = None,
                 intervalo_s: float = INTERVALO_S):
        self.fixtures, self.gravar_fixtures = fixtures, gravar_fixtures
        self.intervalo_s = 0.0 if fixtures else intervalo_s
        self._ultimo = 0.0
        self._robots: dict[str, urllib.robotparser.RobotFileParser] = {}
        self.pedidos = 0  # pedidos HTTP feitos (ou lidos de fixture), robots.txt incluídos
        self.urls: list[str] = []

    # --- transporte ---
    def _bruto(self, metodo: str, url: str, dados: bytes | None = None) -> Resposta:
        self.pedidos += 1
        self.urls.append(f"{metodo} {url}")
        if self.fixtures:
            arq = self.fixtures / _nome_fixture(metodo, url)
            if not arq.exists():
                raise FileNotFoundError(f"sem fixture para {metodo} {url} ({arq.name})")
            f = carregar_json(arq)
            return Resposta(f["url"], f["status"], f.get("headers", {}), f["corpo"])
        espera = self._ultimo + self.intervalo_s - time.monotonic()
        if espera > 0:
            time.sleep(espera)
        req = urllib.request.Request(url, data=dados, method=metodo, headers={"User-Agent": ROBO})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                resp = Resposta(r.geturl(), r.status, dict(r.headers), r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            resp = Resposta(url, e.code, dict(e.headers or {}), e.read().decode("utf-8", "replace") if e.fp else "")
        finally:
            self._ultimo = time.monotonic()
        if self.gravar_fixtures:
            self.gravar_fixtures.mkdir(parents=True, exist_ok=True)
            (self.gravar_fixtures / _nome_fixture(metodo, url)).write_text(json.dumps(
                {"url": resp.url, "status": resp.status, "headers": {}, "corpo": resp.corpo},
                ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return resp

    # --- robots.txt ---
    def permitido(self, url: str) -> bool:
        p = urllib.parse.urlsplit(url)
        base = f"{p.scheme}://{p.netloc}"
        if base not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            r = self._bruto("GET", base + "/robots.txt")
            if any(s in r.corpo[:4000].lower() for s in SINAIS_ANTIROBO):
                raise BloqueioAntiRobo(f"HTTP {r.status} no robots.txt de {base}: proteção anti-robô, não se contorna")
            if r.status >= 500 or r.status == 429:  # erro da fonte, não regra: repete-se mais tarde, sem guardar (K-108)
                raise RuntimeError(f"HTTP {r.status} no robots.txt de {base}: erro da fonte, nada pedido além dele")
            if r.status >= 400:
                rp.parse([])  # sem robots.txt (404): tudo permitido, como manda o protocolo
                rp.allow_all = r.status in (404, 410)
                rp.disallow_all = not rp.allow_all
            else:
                rp.parse(r.corpo.splitlines())
            self._robots[base] = rp
        return self._robots[base].can_fetch(ROBO, url)

    def pedir(self, url: str, metodo: str = "GET", dados: bytes | None = None) -> Resposta:
        if not self.permitido(url):
            raise BloqueioRobos(f"robots.txt veda {url}")
        r = self._bruto(metodo, url, dados)
        baixo = r.corpo[:4000].lower()
        if r.status == 403 or any(s in baixo for s in SINAIS_ANTIROBO):  # também o desafio entregue com 200 (A-001)
            raise BloqueioAntiRobo(f"HTTP {r.status} em {url}: proteção anti-robô, não se contorna")
        if r.url != url and not self.permitido(r.url):  # o destino do redirecionamento também passa pelo robots.txt
            raise BloqueioRobos(f"robots.txt veda o destino do redirecionamento {r.url}")
        return r


class Execucao:
    """Uma Execução de script: o id reservado no começo e o log gravado no fim, com o alcance."""

    def __init__(self, agente: str, entrada_ref: str, id_: str | None = None, simular: bool = False):
        self.id = id_ or registrar_log.proximo_id()
        self.agente, self.entrada_ref, self.simular = agente, entrada_ref, simular
        self.inicio = time.monotonic()
        self.acoes: list[str] = []
        self.resultados: list[str] = []
        self.saidas: list[str] = []
        self.decisoes: list[dict] = []
        self.erros: list[str] = []
        self.olhado: list[str] = []
        self.fora: list[str] = []
        self.ambientes: set[str] = set()
        self.consultas: set[str] = set()
        self.recortes: set[str] = set()

    def origem(self, criado_por: str, versao_regra: str | None = None) -> dict:
        o = {"criado_por": criado_por, "data": date.today().isoformat(), "execucao": self.id}
        if versao_regra:
            o["versao_regra"] = versao_regra
        return o

    def log(self, fonte: str = "script") -> dict:
        e = {
            "id": self.id, "agente": self.agente, "habilidade": "n/a", "versao_harness": "n/a",
            "entrada_ref": self.entrada_ref, "acoes": self.acoes or ["nenhuma"],
            "resultados": self.resultados or ["nenhum"], "saidas": self.saidas, "decisoes": self.decisoes,
            "tokens": None, "chamadas": None,
            "motivo_sem_consumo": "script sem IA" if fonte == "script" else "registro de pessoa (Vicente), sem IA",
            "duracao_s": round(time.monotonic() - self.inicio), "erros": self.erros,
            "alcance": {"olhado": self.olhado or ["nada"], "fora": self.fora},
            "fonte_do_registro": fonte,
        }
        for k in ("ambientes", "consultas", "recortes"):
            if getattr(self, k):
                e[k] = sorted(getattr(self, k))
        return e

    def gravar_log(self, fonte: str = "script") -> str:
        e = registrar_log.preparar(self.log(fonte))
        erros = registrar_log.conferir(e)
        if erros:
            raise SystemExit("log reprovado: " + "; ".join(erros))
        if self.simular:
            return "log simulado (nada gravado)"
        return registrar_log.gravar(e).relative_to(RAIZ).as_posix()


def gravar_json(arq: Path, obj: dict) -> None:
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
