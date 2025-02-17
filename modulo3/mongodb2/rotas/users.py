from fastapi import APIRouter, HTTPException
from database import get_engine
from modelos import User
from odmantic import ObjectId

router = APIRouter(
    prefix="/users",  # Prefixo para todas as rotas
    tags=["Users"],   # Tag para documentação automática
)

engine = get_engine()

@router.get("/users/", response_model=list[User])
async def get_all_users() -> list[User]:
    users = await engine.find(User)
    return users

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str) -> User:
    user = await engine.find_one(User, User.id == ObjectId(user_id))

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/", response_model=User)
async def create_user(user: User) -> User:
    await engine.save(user)
    return user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user_data: dict) -> User:
    user = await engine.find_one(User, User.id == ObjectId(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_data.items():
        setattr(user, key, value)
    await engine.save(user)
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: str) -> dict:
    user = await engine.find_one(User, User.id == user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await engine.delete(user)
    return {"message": "User deleted"}
