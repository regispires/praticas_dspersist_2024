from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from .user import User, UserBase
from .comment import Comment, CommentBaseWithUser
from .tag import Tag

class PostTag(SQLModel, table=True):
    post_id: int = Field(default=None, foreign_key="post.id", primary_key=True)
    tag_id: int = Field(default=None, foreign_key="tag.id", primary_key=True)

class PostBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Post(PostBase, table=True):
    user_id: int = Field(foreign_key="user.id")
    user: 'User' = Relationship(back_populates="posts")
    comments: list[Comment] = Relationship(back_populates="post")
    tags: list[Tag] = Relationship(link_model=PostTag)

class PostBaseWithUserCommentsTags(PostBase):
    user: UserBase | None
    comments: list[CommentBaseWithUser] = None
    tags: list[Tag] = None

PostBaseWithUserCommentsTags.model_rebuild()
