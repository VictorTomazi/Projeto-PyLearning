"""
models.py — Modelos ORM (SQLAlchemy 2.x) que representam as tabelas do banco.

Tabelas:
    usuarios (id, nome, email, senha, xp, vidas)
    licoes   (id, titulo, enunciado, gabarito_saida, xp_recompensa)

Observação: no PostgreSQL, nomes não escritos entre aspas são convertidos para
minúsculas, por isso as tabelas se chamam `usuarios` e `licoes`.
"""
from sqlalchemy import CheckConstraint, Integer, String, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

VIDAS_INICIAIS = 5
XP_RECOMPENSA_PADRAO = 10


class Usuario(Base):
    """Aluno da plataforma."""

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)

    # IMPORTANTE: esta coluna deve guardar o HASH da senha (ex.: bcrypt via
    # passlib), nunca a senha em texto puro. O tamanho 255 comporta hashes.
    senha: Mapped[str] = mapped_column(String(255), nullable=False)

    xp: Mapped[int] = mapped_column(Integer, default=0, server_default="0", nullable=False)
    vidas: Mapped[int] = mapped_column(
        Integer,
        default=VIDAS_INICIAIS,
        server_default=str(VIDAS_INICIAIS),
        nullable=False,
    )

    # Garantias no nível do banco: XP e vidas nunca ficam negativos.
    __table_args__ = (
        CheckConstraint("xp >= 0", name="ck_usuarios_xp_nao_negativo"),
        CheckConstraint("vidas >= 0", name="ck_usuarios_vidas_nao_negativas"),
    )

    def __repr__(self) -> str:
        return f"<Usuario id={self.id} nome={self.nome!r} xp={self.xp} vidas={self.vidas}>"


class Licao(Base):
    """Exercício de programação (prático) ou múltipla escolha (objetiva)."""

    __tablename__ = "licoes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Novo: Organiza a lição dentro dos seus 12-15 módulos
    id_modulo: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    enunciado: Mapped[str] = mapped_column(Text, nullable=False)

    # Novo: Define se a lição é "OBJETIVA" ou "PRATICA"
    tipo: Mapped[str] = mapped_column(String(20), nullable=False, default="PRATICA")

    # Novo: Guarda as alternativas (A, B, C, D) se for objetiva. Fica vazio (None) se for prática.
    opcoes: Mapped[list | None] = mapped_column(JSON, nullable=True)

    # Mantivemos o nome gabarito_saida para não quebrar o código da IA,
    # mas agora ele serve para as duas coisas:
    # Se for OBJETIVA: guarda a letra (ex: "C")
    # Se for PRATICA: guarda a saída do terminal (ex: "Olá, Mundo!")
    gabarito_saida: Mapped[str] = mapped_column(Text, nullable=False)

    xp_recompensa: Mapped[int] = mapped_column(
        Integer,
        default=XP_RECOMPENSA_PADRAO,
        server_default=str(XP_RECOMPENSA_PADRAO),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Licao id={self.id} modulo={self.id_modulo} tipo={self.tipo} titulo={self.titulo!r}>"