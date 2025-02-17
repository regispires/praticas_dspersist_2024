from modelos.post import Post
from sqlalchemy.orm import joinedload, selectinload
from sqlmodel import create_engine, Session, select
from dotenv import load_dotenv
import os
import json
load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
with Session(engine) as session:
      statement = select(Post).options(
            joinedload(Post.user),
            selectinload(Post.comments),
            selectinload(Post.tags)
      )
      posts = session.exec(statement).all()

post_list = [
    post.model_dump() | 
    { "user": post.user.model_dump(), 
     "comments": [ comment.model_dump() for comment in post.comments ],
     "tags": [ tag.model_dump() for tag in post.tags ] 
    } for post in posts
]
print(json.dumps(post_list, indent=2, default=str))
