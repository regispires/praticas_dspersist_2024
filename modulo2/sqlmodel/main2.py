from fastapi import FastAPI, Depends
from sqlmodel import select, Session
from contextlib import asynccontextmanager
from database import create_db_and_tables, get_session
from models import Aluno

# Configurações de inicialização
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"msg": "Olá, mundo!"}

@app.post("/alunos", response_model=Aluno)
def inserir_aluno(aluno: Aluno, session: Session = Depends(get_session)) -> Aluno:
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno

@app.get("/alunos", response_model=list[Aluno])
def listar_alunos(session: Session = Depends(get_session)) -> list[Aluno]:
    alunos = session.exec(select(Aluno)).all()
    return alunos
