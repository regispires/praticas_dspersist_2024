from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    apelido = Column(String)

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(Aluno(nome="Maria", apelido="Mari"))
    session.add(Aluno(nome="Maria José", apelido="Mazé"))
    session.add(Aluno(nome="João", apelido=None))
    session.commit()

    alunos = session.query(Aluno).where(Aluno.nome == "Maria").all()
    for aluno in alunos:
        print(aluno.apelido)