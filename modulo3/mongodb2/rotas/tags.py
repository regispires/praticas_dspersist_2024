from fastapi import APIRouter
from database import get_engine
from modelos import Post

router = APIRouter(
    prefix="/tags",  # Prefixo para todas as rotas
    tags=["Tags"],   # Tag para documentação automática
)

engine = get_engine()

@router.get("/tags/{tag}", response_model=list[Post])
async def get_posts_by_tag(tag: str) -> list[Post]:
    posts = await engine.find(Post, Post.tags.contains(tag))
    return posts
