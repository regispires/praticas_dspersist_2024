from sqlmodel import SQLModel, Field, Relationship, create_engine, Session, select
from sqlalchemy.orm import joinedload, selectinload
import logging

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    posts: list["Post"] = Relationship(back_populates="user")

class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="posts")

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine = create_engine("sqlite:///:memory:")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="Alice")
    post1 = Post(title="Post 1", user=user)
    post2 = Post(title="Post 2", user=user)

    session.add(user)
    session.commit()

    # user_from_db = session.get(User, user.id)
    #consulta = select(User).options(joinedload(User.posts))
    consulta = select(User).options(selectinload(User.posts))
    user_from_db = session.exec(consulta).first()
    print(len(user_from_db.posts))