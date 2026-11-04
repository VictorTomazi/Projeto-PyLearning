"""
main.py — Aplicação FastAPI da plataforma educativa de Python.

Como rodar (a partir da pasta do projeto):
    uvicorn main:app --reload
ou execute este arquivo direto no PyCharm (botão Run).

Documentação interativa (Swagger): http://127.0.0.1:8000/docs
"""
import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import func, update
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Licao, Usuario
from sandbox import MAX_CODIGO_CHARS, StatusExecucao, executar_codigo


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Cria as tabelas na inicialização (suficiente para o trabalho acadêmico).
    Em um projeto maior, prefira migrações com Alembic."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Plataforma Educativa de Python",
    description="Backend de uma plataforma gamificada para ensino de Python.",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS: permite que o frontend (em outra porta) chame esta API pelo navegador.
# Ajuste a variável CORS_ORIGINS (separada por vírgulas) conforme seu frontend.
origens_permitidas = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origem.strip() for origem in origens_permitidas],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------------------------------
# Schemas (formato do JSON de entrada e saída)
# --------------------------------------------------------------------------
class ExecutarRequest(BaseModel):
    usuario_id: int = Field(gt=0, description="ID do aluno")
    licao_id: int = Field(gt=0, description="ID da lição sendo resolvida")
    codigo: str = Field(min_length=1, max_length=MAX_CODIGO_CHARS, description="Código Python do aluno")


class ExecutarResponse(BaseModel):
    acertou: bool
    status: StatusExecucao
    saida: str
    mensagem: str
    xp_ganho: int
    xp_total: int
    vidas_restantes: int


# --------------------------------------------------------------------------
# Rotas
# --------------------------------------------------------------------------
# Esta rota usa `def` (e não `async def` de propósito): o sandbox bloqueia por
# até 3 segundos esperando o subprocesso. Com `def`, o FastAPI executa a função
# em uma thread separada e o servidor continua atendendo outras requisições.
@app.post("/api/executar", response_model=ExecutarResponse)
def executar(dados: ExecutarRequest, db: Session = Depends(get_db)) -> ExecutarResponse:
    """
    Executa o código do aluno no sandbox e atualiza XP/vidas:

    - ACERTOU            -> soma o `xp_recompensa` da lição ao XP do aluno.
    - ERROU ou TIMEOUT   -> o aluno perde 1 vida (mínimo 0).
    - BLOQUEADO          -> nada é executado e nada é descontado.
    """
    usuario = db.get(Usuario, dados.usuario_id)
    if usuario is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuário não encontrado.")

    licao = db.get(Licao, dados.licao_id)
    if licao is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Lição não encontrada.")

    if usuario.vidas <= 0:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Você ficou sem vidas. Tente novamente mais tarde.")

    # Etapa lenta (até 3s) — executada ANTES de qualquer escrita no banco.
    resultado = executar_codigo(dados.codigo, licao.gabarito_saida)

    # UPDATEs atômicos feitos pelo próprio banco (`xp = xp + N`) evitam perda de
    # dados caso o mesmo aluno envie duas requisições ao mesmo tempo.
    xp_ganho = 0
    if resultado.status is StatusExecucao.ACERTOU:
        xp_ganho = licao.xp_recompensa
        db.execute(
            update(Usuario).where(Usuario.id == usuario.id).values(xp=Usuario.xp + xp_ganho)
        )
    elif resultado.status in (StatusExecucao.ERROU, StatusExecucao.TIMEOUT):
        db.execute(
            update(Usuario)
            .where(Usuario.id == usuario.id)
            .values(vidas=func.greatest(Usuario.vidas - 1, 0))
        )

    db.commit()
    db.refresh(usuario)  # Recarrega os valores atualizados

    return ExecutarResponse(
        acertou=resultado.acertou,
        status=resultado.status,
        saida=resultado.saida,
        mensagem=resultado.mensagem,
        xp_ganho=xp_ganho,
        xp_total=usuario.xp,
        vidas_restantes=usuario.vidas,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)