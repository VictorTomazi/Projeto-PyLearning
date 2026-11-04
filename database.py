"""
database.py — Configuração da conexão com o PostgreSQL usando SQLAlchemy 2.x.

As credenciais são lidas de variáveis de ambiente (com valores padrão para
desenvolvimento local). No PyCharm: Run > Edit Configurations > Environment
variables, por exemplo:  DB_USER=postgres;DB_PASSWORD=minha_senha

Por que `URL.create` em vez de uma string de conexão?
Ele escapa automaticamente caracteres especiais na senha (como "@" ou "/"),
o que evita erros difíceis de diagnosticar.
"""
import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD", "0000"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME", "plataforma_python"),
)

# `pool_pre_ping` testa a conexão antes de usá-la, evitando erros caso o
# PostgreSQL tenha reiniciado ou derrubado conexões ociosas.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Fábrica de sessões. Cada requisição HTTP recebe a sua própria sessão.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Classe base de todos os modelos ORM (ver models.py)."""


def get_db() -> Generator[Session, None, None]:
    """
    Dependência do FastAPI: abre uma sessão por requisição e garante o
    fechamento ao final, mesmo que ocorra uma exceção.

    Uso nas rotas:  db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()