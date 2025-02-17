from fastapi import FastAPI
from rotas import home, users, posts

# FastAPI app instance
app = FastAPI()

# Rotas para Endpoints
app.include_router(home.router)
app.include_router(users.router)
app.include_router(posts.router)
