"""
database.py — Configuração da conexão com o PostgreSQL usando SQLAlchemy 2.x.
"""
import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# 1. COLE AQUI A URL QUE VOCÊ COPIOU DO NEON (Exatamente como veio do site):
URL_DA_NEON = "postgresql://neondb_owner:npg_d0v9obmnSKxW@ep-wandering-haze-be15drjd-pooler.c-9.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# 2. Ajuste automático para o driver do Python (psycopg2) que você já usa:
URL_FORMATADA = URL_DA_NEON.replace("postgresql://", "postgresql+psycopg2://")

# 3. Essa linha resolve dois problemas: usa o Neon agora no seu PC,
# mas já deixa 100% pronto para o Render usar as variáveis de ambiente dele depois!
DATABASE_URL = os.getenv("DATABASE_URL", URL_FORMATADA)

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