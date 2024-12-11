from models import Aluno
from database import get_session

# Obter uma sessão para interagir com o banco de dados
with get_session() as session:
    # Inserir novos registros
    try:
        session.add(Aluno(nome='Maria', apelido='Mari'))
        session.add(Aluno(nome='João'))
        session.commit()
    except Exception as e:
        session.rollback()
        print(f'Erro: {e}')

    # Consultar registros
    alunos = session.query(Aluno).all()
    for aluno in alunos:
        print(aluno)