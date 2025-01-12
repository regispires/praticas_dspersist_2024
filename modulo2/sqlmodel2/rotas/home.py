from fastapi import APIRouter

router = APIRouter(
    prefix="",  # Prefixo para todas as rotas
    tags=["Home"],   # Tag para documentação automática
)

# Home
@router.get("/")
async def root():
    return {"msg": "Bem-vindo ao FastAPI!"}
