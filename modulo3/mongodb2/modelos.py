from odmantic import Model, Reference
from typing import Optional

class User(Model):
    name: Optional[str] = None
    email: Optional[str] = None

class Comment(Model):
    user: User = Reference()
    content: str

class Post(Model):
    title: str
    content: str
    user: User = Reference()
    comments: list[Comment] = []
    tags: list[str] = []
