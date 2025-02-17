from fastapi import APIRouter, HTTPException
from database import get_engine
from modelos import Post, Comment, User
from odmantic import ObjectId

router = APIRouter(
    prefix="/posts",  # Prefixo para todas as rotas
    tags=["Posts"],   # Tag para documentação automática
)

engine = get_engine()

@router.get("/posts/", response_model=list[Post])
async def get_all_posts() -> list[Post]:
    posts = await engine.find(Post)
    return posts

@router.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: str) -> Post:
    post = await engine.find_one(Post, Post.id == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/posts/", response_model=Post)
async def create_post(post: Post) -> Post:
    user = await engine.find_one(User, User.id == ObjectId(post.user.id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    post.user = user
    await engine.save(post)
    return post

@router.post("/posts/{post_id}/comments/", response_model=Post)
async def add_comment(post_id: str, comment: Comment) -> Post:
    post = await engine.find_one(Post, Post.id == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.comments.routerend(comment)
    await engine.save(post)
    return post

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str) -> dict:
    post = await engine.find_one(Post, Post.id == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await engine.delete(post)
    return {"message": "Post deleted"}
