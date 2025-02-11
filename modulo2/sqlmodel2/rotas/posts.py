from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from modelos.post import Post, PostTag, PostBaseWithUserCommentsTags
from modelos.comment import Comment
from modelos.tag import Tag
from database import get_session
from datetime import datetime

router = APIRouter(
    prefix="/posts",  # Prefixo para todas as rotas
    tags=["Posts"],   # Tag para documentação automática
)

# Posts
@router.post("/", response_model=Post)
def create_post(post: Post, session: Session = Depends(get_session)):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

@router.get("/", response_model=list[PostBaseWithUserCommentsTags])
def read_posts(offset: int = 0, limit: int = Query(default=10, le=100), 
               session: Session = Depends(get_session)):
    statement = (select(Post).offset(offset).limit(limit)
                 .options(joinedload(Post.user), joinedload(Post.comments), 
                          joinedload(Post.tags)))
    return session.exec(statement).unique().all()

@router.get("/{post_id}", response_model=PostBaseWithUserCommentsTags)
def read_post(post_id: int, session: Session = Depends(get_session)):
    statement = (select(Post).where(Post.id == post_id)
                 .options(joinedload(Post.user), joinedload(Post.comments), 
                          joinedload(Post.tags)))
    post = session.exec(statement).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, post: Post, session: Session = Depends(get_session)):
    db_post = session.get(Post, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    for key, value in post.dict(exclude_unset=True).items():
        setattr(db_post, key, value)
    db_post.updated_at = datetime.utcnow()
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post

@router.delete("/{post_id}")
def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    session.delete(post)
    session.commit()
    return {"ok": True}

# Comments
@router.post("/{post_id}/comments/", response_model=Comment)
def create_comment_for_post(post_id: int, comment: Comment, session: Session = Depends(get_session)):
    comment.post_id = post_id
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment

@router.get("/{post_id}/comments/", response_model=list[Comment])
def read_comments_for_post(post_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Comment).where(Comment.post_id == post_id)).all()

@router.put("/{post_id}/comments/{comment_id}", response_model=Comment)
def update_comment_for_post(post_id: int, comment_id: int, comment: Comment, session: Session = Depends(get_session)):
    db_comment = session.get(Comment, comment_id)
    if not db_comment or db_comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="Comment not found")
    for key, value in comment.dict(exclude_unset=True).items():
        setattr(db_comment, key, value)
    db_comment.updated_at = datetime.utcnow()
    session.add(db_comment)
    session.commit()
    session.refresh(db_comment)
    return db_comment

@router.delete("/{post_id}/comments/{comment_id}")
def delete_comment_for_post(post_id: int, comment_id: int, session: Session = Depends(get_session)):
    comment = session.get(Comment, comment_id)
    if not comment or comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="Comment not found")
    session.delete(comment)
    session.commit()
    return {"ok": True}

# Tags
@router.post("/{post_id}/tags/", response_model=Tag)
def create_tag_for_post(post_id: int, tag: Tag, session: Session = Depends(get_session)):
    tag_db = session.exec(select(Tag).where(Tag.name == tag.name)).first()
    if tag_db:
        tag = tag_db
    else:
        session.add(tag)
        session.commit()
        session.refresh(tag)
    tag_dump = tag.model_dump()
    post_tag = PostTag(post_id=post_id, tag_id=tag.id)
    session.add(post_tag)
    session.commit()
    return tag_dump

@router.get("/{post_id}/tags/", response_model=list[Tag])
def read_tags_for_post(post_id: int, session: Session = Depends(get_session)):
    statement = select(Tag).join(PostTag).where(PostTag.post_id == post_id)
    return session.exec(statement).all()

@router.put("/{post_id}/tags/{tag_id}", response_model=Tag)
def update_tag_for_post(post_id: int, tag_id: int, tag: Tag, session: Session = Depends(get_session)):
    db_tag = session.get(Tag, tag_id)
    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    for key, value in tag.model_dump(exclude_unset=True).items():
        setattr(db_tag, key, value)
    session.add(db_tag)
    session.commit()
    session.refresh(db_tag)
    return db_tag

@router.delete("/{post_id}/tags/{tag_id}")
def delete_tag_for_post(post_id: int, tag_id: int, session: Session = Depends(get_session)):
    post_tag = session.exec(select(PostTag).where(PostTag.post_id == post_id, PostTag.tag_id == tag_id)).first()
    if not post_tag:
        raise HTTPException(status_code=404, detail="Tag not found for this post")
    session.delete(post_tag)
    session.commit()
    return {"ok": True}
