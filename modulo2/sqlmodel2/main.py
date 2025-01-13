from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables
from rotas import home, users, posts

# Configurações de inicialização
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Inicializa o aplicativo FastAPI
app = FastAPI(lifespan=lifespan)

# Rotas para Endpoints
app.include_router(home.router)
app.include_router(users.router)
app.include_router(posts.router)
