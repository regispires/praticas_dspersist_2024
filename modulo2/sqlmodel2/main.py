from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables
from rotas import users, posts

# Configurações de inicialização
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Inicializa o aplicativo FastAPI
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"msg": "Bem-vindo ao FastAPI!"}

# Rotas para Endpoints CRUD
app.include_router(users.router)
app.include_router(posts.router)
