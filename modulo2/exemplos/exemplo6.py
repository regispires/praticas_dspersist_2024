from modelos.post import Post
from modelos.user import User
from sqlmodel import create_engine, Session, select
from dotenv import load_dotenv
import os
import logging

load_dotenv()
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine = create_engine(os.getenv("DATABASE_URL"))
with Session(engine) as session:
      statement = select(Post, User).join(User)
      resultados = session.exec(statement).all()
      for post, user in resultados:
            print(post, user)