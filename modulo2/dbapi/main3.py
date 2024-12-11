import sqlite3
from contextlib import contextmanager

@contextmanager
def get_cursor(connection):
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        cursor.close()

# Conectar ao banco de dados
with sqlite3.connect('exemplo.db') as conn:
    with get_cursor(conn) as cursor:
        try:
            # Criar tabela
            cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INT PRIMARY KEY, nome TEXT)')
            # Inserir dados
            cursor.execute('INSERT INTO alunos (id, nome) VALUES (?, ?)', (1, 'Maria'))
            cursor.execute('INSERT INTO alunos (id, nome) VALUES (?, ?)', (2, 'João'))
            cursor.execute('INSERT INTO alunos (id, nome) VALUES (?, ?)', (3, 'José'))

            # Consultar dados
            busca_nome = 'a'
            cursor.execute('SELECT * FROM alunos where lower(nome) like lower(?)', (f'%{busca_nome}%',))
            resultados = cursor.fetchall()
            for linha in resultados:
                print(linha)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f'Erro: {e}')
