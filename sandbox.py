"""
sandbox.py — Motor de execução isolada do código enviado pelos alunos.

Fluxo de `executar_codigo`:
    1. Análise estática (módulo `ast`): recusa imports e funções perigosas
       SEM executar nada.
    2. O código é gravado em um arquivo dentro de uma pasta temporária.
    3. Um processo Python novo executa o arquivo, com timeout de 3 segundos.
    4. A saída (stdout) é comparada com o gabarito da lição.

------------------------------------------------------------------------------
AVISO DE SEGURANÇA (leia antes de colocar em produção)
------------------------------------------------------------------------------
Bloquear imports e funções é uma PRIMEIRA CAMADA de defesa, útil para o
contexto acadêmico e para barrar tentativas óbvias. Mas NÃO é uma barreira
de segurança completa: o Python é dinâmico demais para que uma lista de
bloqueio cubra todos os caminhos possíveis.

Para uma plataforma real, execute este mesmo código dentro de um contêiner
Docker descartável (sem rede, sistema de arquivos somente leitura, limites de
CPU/memória) ou use uma ferramenta como nsjail/gVisor. A interface desta
função (`executar_codigo`) não muda: basta trocar o comando executado em
`_executar_arquivo`.
------------------------------------------------------------------------------
"""
from __future__ import annotations

import ast
import os
import signal
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

try:
    import resource  # Disponível apenas em Linux/macOS
except ImportError:  # Windows
    resource = None

# --------------------------------------------------------------------------
# Configurações (ajuste conforme a necessidade)
# --------------------------------------------------------------------------
TIMEOUT_SEGUNDOS = 3
MAX_CODIGO_CHARS = 10_000
MAX_SAIDA_CHARS = 10_000
LIMITE_MEMORIA_BYTES = 256 * 1024 * 1024  # 256 MB (somente Linux/macOS)

# Módulos que o aluno NÃO pode importar (compara-se a raiz: `os.path` -> `os`).
IMPORTS_PROIBIDOS = frozenset({
    # Pedidos no enunciado
    "os", "sys",
    # Outros caminhos comuns para sistema de arquivos, processos e rede
    "subprocess", "shutil", "pathlib", "tempfile", "glob", "io", "fileinput",
    "zipfile", "tarfile", "sqlite3", "socket", "http", "urllib", "ftplib",
    "smtplib", "requests", "webbrowser", "ctypes", "multiprocessing",
    "threading", "_thread", "signal", "resource", "pty", "posix", "nt",
    # Introspecção e importação dinâmica
    "importlib", "builtins", "inspect", "gc", "code", "codeop", "runpy",
    "site", "sysconfig", "platform", "pickle", "marshal",
})

# Nomes de funções/variáveis embutidas que também são bloqueados.
FUNCOES_PROIBIDAS = frozenset({
    "__import__", "__builtins__", "eval", "exec", "compile", "open",
    "breakpoint", "globals", "locals", "getattr", "setattr", "delattr",
})

# Atributos usados em truques clássicos de escape de sandbox.
ATRIBUTOS_PROIBIDOS = frozenset({
    "__subclasses__", "__globals__", "__builtins__", "__bases__", "__mro__",
    "__code__", "__closure__", "__loader__", "__import__",
    "f_globals", "f_back", "gi_frame", "tb_frame",
})


# --------------------------------------------------------------------------
# Tipos de retorno
# --------------------------------------------------------------------------
class StatusExecucao(str, Enum):
    ACERTOU = "acertou"      # Saída igual ao gabarito
    ERROU = "errou"          # Saída diferente, erro de sintaxe ou erro em execução
    TIMEOUT = "timeout"      # Estourou o tempo limite (ex.: laço infinito)
    BLOQUEADO = "bloqueado"  # Código recusado pela análise estática (nada foi executado)


@dataclass(frozen=True)
class ResultadoExecucao:
    status: StatusExecucao
    saida: str = ""      # O que o código do aluno imprimiu (truncado)
    mensagem: str = ""   # Explicação amigável para exibir ao aluno

    @property
    def acertou(self) -> bool:
        return self.status is StatusExecucao.ACERTOU


# --------------------------------------------------------------------------
# API pública
# --------------------------------------------------------------------------
def executar_codigo(codigo_aluno: str, gabarito_esperado: str) -> ResultadoExecucao:
    """
    Executa o código do aluno em um processo isolado e compara a saída com o
    gabarito.

    Args:
        codigo_aluno: código-fonte Python enviado pelo aluno.
        gabarito_esperado: saída exata esperada (stdout) para a lição.

    Returns:
        ResultadoExecucao com status ACERTOU, ERROU, TIMEOUT ou BLOQUEADO.
    """
    if not codigo_aluno.strip():
        return ResultadoExecucao(StatusExecucao.ERROU, mensagem="Nenhum código foi enviado.")

    if len(codigo_aluno) > MAX_CODIGO_CHARS:
        return ResultadoExecucao(
            StatusExecucao.ERROU,
            mensagem=f"O código excede o limite de {MAX_CODIGO_CHARS} caracteres.",
        )

    # 1) Análise estática: nada é executado nesta etapa.
    try:
        arvore = ast.parse(codigo_aluno)
    except SyntaxError as exc:
        return ResultadoExecucao(
            StatusExecucao.ERROU,
            mensagem=f"Erro de sintaxe na linha {exc.lineno}: {exc.msg}",
        )
    except (ValueError, RecursionError, MemoryError):
        return ResultadoExecucao(StatusExecucao.ERROU, mensagem="O código enviado é inválido.")

    violacao = _encontrar_violacao(arvore)
    if violacao:
        return ResultadoExecucao(StatusExecucao.BLOQUEADO, mensagem=violacao)

    # 2) Arquivo temporário numa pasta própria; é apagada ao final do `with`.
    with tempfile.TemporaryDirectory(prefix="sandbox_") as pasta:
        arquivo = Path(pasta) / "solucao.py"
        arquivo.write_text(codigo_aluno, encoding="utf-8")
        return _executar_arquivo(arquivo, gabarito_esperado)


# --------------------------------------------------------------------------
# Funções internas
# --------------------------------------------------------------------------
def _encontrar_violacao(arvore: ast.AST) -> str | None:
    """Percorre a AST e retorna a mensagem da primeira violação (ou None)."""
    for no in ast.walk(arvore):
        if isinstance(no, ast.Import):
            for alias in no.names:
                raiz = alias.name.split(".")[0]
                if raiz in IMPORTS_PROIBIDOS:
                    return f"O módulo '{raiz}' não é permitido nesta plataforma."

        elif isinstance(no, ast.ImportFrom):
            raiz = (no.module or "").split(".")[0]
            if raiz in IMPORTS_PROIBIDOS:
                return f"O módulo '{raiz}' não é permitido nesta plataforma."

        elif isinstance(no, ast.Name) and no.id in FUNCOES_PROIBIDAS:
            return f"O uso de '{no.id}' não é permitido nesta plataforma."

        elif isinstance(no, ast.Attribute) and no.attr in ATRIBUTOS_PROIBIDOS:
            return f"O acesso a '{no.attr}' não é permitido nesta plataforma."

    return None


def _executar_arquivo(arquivo: Path, gabarito_esperado: str) -> ResultadoExecucao:
    """Roda o arquivo em um subprocesso com timeout e compara com o gabarito."""
    comando = [
        sys.executable,
        "-I",          # Modo isolado: ignora variáveis PYTHON* e o site do usuário
        "-X", "utf8",  # Força UTF-8 na entrada/saída (acentos no Windows)
        str(arquivo),
    ]

    with subprocess.Popen(
        comando,
        stdin=subprocess.DEVNULL,   # `input()` falha com EOFError em vez de travar
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=arquivo.parent,         # Diretório de trabalho = pasta temporária
        env=_montar_ambiente(),
        **_opcoes_por_plataforma(),
    ) as processo:
        try:
            saida, erro = processo.communicate(timeout=TIMEOUT_SEGUNDOS)
        except subprocess.TimeoutExpired:
            _encerrar_processo(processo)
            try:
                processo.communicate(timeout=1)  # Esvazia os pipes
            except subprocess.TimeoutExpired:
                pass
            return ResultadoExecucao(
                StatusExecucao.TIMEOUT,
                mensagem=(
                    f"Tempo limite de {TIMEOUT_SEGUNDOS}s excedido. "
                    "Verifique se há algum laço infinito."
                ),
            )

        codigo_retorno = processo.returncode

    if codigo_retorno != 0:
        return ResultadoExecucao(
            StatusExecucao.ERROU,
            saida=_truncar(saida),
            mensagem=_resumir_erro(erro) or "O programa terminou de forma inesperada.",
        )

    if _normalizar_saida(saida) == _normalizar_saida(gabarito_esperado):
        return ResultadoExecucao(StatusExecucao.ACERTOU, saida=_truncar(saida), mensagem="Correto!")

    return ResultadoExecucao(
        StatusExecucao.ERROU,
        saida=_truncar(saida),
        mensagem="A saída do seu código não corresponde ao resultado esperado.",
    )


def _montar_ambiente() -> dict[str, str]:
    """
    Ambiente MÍNIMO para o processo filho.

    Não repassamos as variáveis do servidor (como DB_PASSWORD), para que o
    código do aluno nunca consiga lê-las. PATH e SYSTEMROOT são necessários
    para o Python iniciar corretamente no Windows.
    """
    return {k: os.environ[k] for k in ("PATH", "SYSTEMROOT") if k in os.environ}


def _opcoes_por_plataforma() -> dict:
    """Opções extras do Popen que dependem do sistema operacional."""
    if os.name == "posix":
        return {
            # Novo grupo de processos: permite matar o processo e seus filhos.
            "start_new_session": True,
            # Limites de recursos aplicados no filho antes de executar o código.
            "preexec_fn": _aplicar_limites_posix,
        }
    return {}


def _aplicar_limites_posix() -> None:
    """Executa no processo filho (Linux/macOS) antes de rodar o código do aluno."""
    if resource is None:
        return
    limites = (
        (resource.RLIMIT_AS, LIMITE_MEMORIA_BYTES),        # Memória
        (resource.RLIMIT_CPU, TIMEOUT_SEGUNDOS + 2),       # Tempo de CPU
        (resource.RLIMIT_FSIZE, 1_000_000),                # Tamanho máximo de arquivo criado
    )
    for tipo, valor in limites:
        try:
            resource.setrlimit(tipo, (valor, valor))
        except (ValueError, OSError):
            pass  # Alguns sistemas (ex.: macOS) não suportam todos os limites


def _encerrar_processo(processo: subprocess.Popen) -> None:
    """
    Mata o processo e seus descendentes.

    No Windows, o `python.exe` de um venv (como o do PyCharm) é um "launcher"
    que cria o interpretador real como processo filho. Um simples `kill()`
    mataria só o launcher e deixaria o laço infinito rodando; por isso usamos
    `taskkill /T` para encerrar a árvore inteira.
    """
    try:
        if os.name == "nt":
            subprocess.run(
                ["taskkill", "/F", "/T", "/PID", str(processo.pid)],
                capture_output=True,
                check=False,
            )
        else:
            os.killpg(processo.pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError, OSError):
        pass
    finally:
        processo.kill()  # Garantia extra; não faz mal se já terminou


def _normalizar_saida(texto: str) -> str:
    """Ignora diferenças irrelevantes: quebras de linha do Windows e espaços no fim."""
    linhas = texto.replace("\r\n", "\n").replace("\r", "\n").strip().split("\n")
    return "\n".join(linha.rstrip() for linha in linhas)


def _resumir_erro(stderr: str) -> str:
    """Retorna só a última linha do traceback (ex.: 'NameError: ...'), sem caminhos."""
    linhas = [linha.strip() for linha in stderr.strip().splitlines() if linha.strip()]
    return _truncar(linhas[-1], 300) if linhas else ""


def _truncar(texto: str, limite: int = MAX_SAIDA_CHARS) -> str:
    return texto if len(texto) <= limite else texto[:limite] + "\n... (saída truncada)"