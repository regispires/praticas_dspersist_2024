from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from .user import User, UserBase
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .post import Post

class CommentBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Comment(CommentBase, table=True):
    post_id: int = Field(foreign_key="post.id")
    user_id: int = Field(foreign_key="user.id")
    post: 'Post' = Relationship(back_populates="comments")
    user: User = Relationship(back_populates="comments")

class CommentBaseWithUser(CommentBase):
    user: UserBase