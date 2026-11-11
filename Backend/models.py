"""
models.py — Modelos ORM (SQLAlchemy 2.x): AQUI é onde as tabelas são definidas.

Cada classe abaixo vira uma tabela do PostgreSQL. Quem cria as tabelas de fato
é o SQLAlchemy (comando `Base.metadata.create_all`, chamado pelo seed.py), então
NÃO é preciso escrever CREATE TABLE à mão no pgAdmin.

Estrutura (documento "Modelagem de Dados e Arquitetura"):

    TRILHAS 1---N TRILHAS_MODULOS 1---N LICOES 1---N PROGRESSO_USUARIO N---1 USUARIOS
    USUARIOS 1---N TENTATIVAS N---1 LICOES

Acréscimos ao documento, necessários para o que o app já faz:
    - licoes.titulo, licoes.tipo (TEORIA / OBJETIVA / PRATICA) e licoes.id_etapa
      (a "bolinha" da trilha em que a lição aparece)
    - tabela opcoes_licao: uma linha por alternativa (A, B, C...) das lições
      OBJETIVA. Guardar a lista numa coluna só violaria a 1ª Forma Normal.

Nomes: o BANCO usa exatamente os nomes do documento (id_usuario, xp_acumulado,
nome_completo...). No código Python usamos apelidos curtos (Usuario.id,
Usuario.xp, Usuario.nome...). A ligação é o primeiro argumento do
`mapped_column("nome_no_banco", ...)`.
"""
from datetime import date, datetime

from sqlalchemy import (
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

VIDAS_INICIAIS = 5
XP_RECOMPENSA_PADRAO = 10


# --------------------------------------------------------------------------
# Tabela 01: USUARIOS
# --------------------------------------------------------------------------
class Usuario(Base):
    """Aluno da plataforma."""

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column("id_usuario", primary_key=True)
    nome: Mapped[str] = mapped_column("nome_completo", String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # Guarda o HASH da senha (ver seguranca.py), nunca a senha em texto puro.
    senha: Mapped[str] = mapped_column("senha_hash", String(255), nullable=False)

    vidas: Mapped[int] = mapped_column(
        "vidas_atuais", Integer, default=VIDAS_INICIAIS, server_default=str(VIDAS_INICIAIS), nullable=False
    )
    xp: Mapped[int] = mapped_column("xp_acumulado", Integer, default=0, server_default="0", nullable=False)
    streak_dias: Mapped[int] = mapped_column(Integer, default=0, server_default="0", nullable=False)

    progresso: Mapped[list["ProgressoUsuario"]] = relationship(back_populates="usuario", passive_deletes=True)
    tentativas: Mapped[list["Tentativa"]] = relationship(back_populates="usuario", passive_deletes=True)

    # Garantias no nível do banco: nada disso pode ficar negativo.
    __table_args__ = (
        CheckConstraint("vidas_atuais >= 0", name="ck_usuarios_vidas_nao_negativas"),
        CheckConstraint("xp_acumulado >= 0", name="ck_usuarios_xp_nao_negativo"),
        CheckConstraint("streak_dias >= 0", name="ck_usuarios_streak_nao_negativo"),
    )

    def __repr__(self) -> str:
        return f"<Usuario id={self.id} nome={self.nome!r} xp={self.xp} vidas={self.vidas}>"


# --------------------------------------------------------------------------
# Tabela 02: TRILHAS
# --------------------------------------------------------------------------
class Trilha(Base):
    """Caminho de aprendizado (ex.: 'Python do Zero')."""

    __tablename__ = "trilhas"

    id: Mapped[int] = mapped_column("id_trilha", primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)

    modulos: Mapped[list["Modulo"]] = relationship(back_populates="trilha", order_by="Modulo.ordem")


# --------------------------------------------------------------------------
# Tabela 03: TRILHAS_MODULOS
# --------------------------------------------------------------------------
class Modulo(Base):
    """Módulo de uma trilha (agrupa as lições)."""

    __tablename__ = "trilhas_modulos"

    id: Mapped[int] = mapped_column("id_modulo", primary_key=True)
    id_trilha: Mapped[int] = mapped_column(ForeignKey("trilhas.id_trilha"), nullable=False, index=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    ordem: Mapped[int] = mapped_column(Integer, nullable=False)  # Posição de exibição na trilha

    trilha: Mapped["Trilha"] = relationship(back_populates="modulos")
    licoes: Mapped[list["Licao"]] = relationship(back_populates="modulo")

    __table_args__ = (UniqueConstraint("id_trilha", "ordem", name="uq_modulos_trilha_ordem"),)


# --------------------------------------------------------------------------
# Tabela 04: LICOES (+ OPCOES_LICAO)
# --------------------------------------------------------------------------
class Licao(Base):
    """Lição: teoria, múltipla escolha (OBJETIVA) ou exercício de código (PRATICA)."""

    __tablename__ = "licoes"

    id: Mapped[int] = mapped_column("id_licao", primary_key=True)
    id_modulo: Mapped[int] = mapped_column(ForeignKey("trilhas_modulos.id_modulo"), nullable=False)

    # Acréscimo: posição ("bolinha") da lição dentro do módulo. Várias lições
    # podem dividir a mesma etapa (ex.: 2 objetivas na bolinha 2).
    id_etapa: Mapped[int] = mapped_column(Integer, nullable=False, default=1, server_default="1")

    titulo: Mapped[str] = mapped_column(String(150), nullable=False)  # Acréscimo
    enunciado: Mapped[str] = mapped_column("enunciado_tarefa", Text, nullable=False)
    tipo: Mapped[str] = mapped_column(String(20), nullable=False, default="PRATICA", server_default="PRATICA")

    # OBJETIVA: a letra correta (ex.: "C"). PRATICA: a saída esperada do programa.
    # TEORIA: valor de controle (ex.: "LEITURA").
    gabarito_saida: Mapped[str] = mapped_column(Text, nullable=False)
    xp_recompensa: Mapped[int] = mapped_column(
        Integer, nullable=False, default=XP_RECOMPENSA_PADRAO, server_default=str(XP_RECOMPENSA_PADRAO)
    )

    modulo: Mapped["Modulo"] = relationship(back_populates="licoes")
    alternativas: Mapped[list["OpcaoLicao"]] = relationship(
        back_populates="licao", cascade="all, delete-orphan", order_by="OpcaoLicao.letra"
    )

    __table_args__ = (
        CheckConstraint("tipo IN ('TEORIA', 'OBJETIVA', 'PRATICA')", name="ck_licoes_tipo"),
        CheckConstraint("xp_recompensa >= 0", name="ck_licoes_xp_nao_negativo"),
        Index("ix_licoes_modulo_etapa", "id_modulo", "id_etapa"),
    )

    @property
    def opcoes(self) -> list[str] | None:
        """Textos das alternativas na ordem A, B, C... (None se a lição não for OBJETIVA).
        Mantém o formato que a API e o frontend já usam."""
        return [alternativa.texto for alternativa in self.alternativas] or None

    def __repr__(self) -> str:
        return f"<Licao id={self.id} modulo={self.id_modulo} etapa={self.id_etapa} tipo={self.tipo} titulo={self.titulo!r}>"


class OpcaoLicao(Base):
    """Alternativa de uma lição OBJETIVA (acréscimo ao documento, para respeitar a 1FN)."""

    __tablename__ = "opcoes_licao"

    id: Mapped[int] = mapped_column("id_opcao", primary_key=True)
    id_licao: Mapped[int] = mapped_column(ForeignKey("licoes.id_licao", ondelete="CASCADE"), nullable=False)
    letra: Mapped[str] = mapped_column(String(1), nullable=False)  # A, B, C, D...
    texto: Mapped[str] = mapped_column(Text, nullable=False)

    licao: Mapped["Licao"] = relationship(back_populates="alternativas")

    __table_args__ = (UniqueConstraint("id_licao", "letra", name="uq_opcoes_licao_letra"),)


# --------------------------------------------------------------------------
# Tabela 05: PROGRESSO_USUARIO
# --------------------------------------------------------------------------
class ProgressoUsuario(Base):
    """Marca que o aluno concluiu uma lição (no máximo uma linha por aluno e lição)."""

    __tablename__ = "progresso_usuario"

    id: Mapped[int] = mapped_column("id_progresso", primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable=False)
    id_licao: Mapped[int] = mapped_column(ForeignKey("licoes.id_licao", ondelete="CASCADE"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="CONCLUIDO", server_default="CONCLUIDO")
    data_conclusao: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

    usuario: Mapped["Usuario"] = relationship(back_populates="progresso")
    licao: Mapped["Licao"] = relationship()

    __table_args__ = (
        UniqueConstraint("id_usuario", "id_licao", name="uq_progresso_usuario_licao"),
        CheckConstraint("status IN ('EM_ANDAMENTO', 'CONCLUIDO')", name="ck_progresso_status"),
    )


# --------------------------------------------------------------------------
# Tabela 06: TENTATIVAS
# --------------------------------------------------------------------------
class Tentativa(Base):
    """Histórico de cada resposta/código enviado por um aluno."""

    __tablename__ = "tentativas"

    id: Mapped[int] = mapped_column("id_tentativa", primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable=False)
    id_licao: Mapped[int] = mapped_column(ForeignKey("licoes.id_licao", ondelete="CASCADE"), nullable=False)
    codigo_enviado: Mapped[str] = mapped_column(Text, nullable=False)  # Código (PRATICA) ou letra (OBJETIVA)
    resultado: Mapped[str] = mapped_column(String(20), nullable=False)  # SUCESSO ou ERRO
    saida_obtida: Mapped[str | None] = mapped_column(Text)
    data_tentativa: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

    usuario: Mapped["Usuario"] = relationship(back_populates="tentativas")
    licao: Mapped["Licao"] = relationship()

    __table_args__ = (
        CheckConstraint("resultado IN ('SUCESSO', 'ERRO')", name="ck_tentativas_resultado"),
        Index("ix_tentativas_usuario_licao", "id_usuario", "id_licao"),
    )