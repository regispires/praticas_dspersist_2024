import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

try:
    # Criar tabela
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INT PRIMARY KEY, nome TEXT)')
    # Inserir dados
    cursor.execute('INSERT INTO alunos (id, nome) VALUES (?, ?)', (1, 'Maria'))
    cursor.execute('INSERT INTO alunos (id, nome) VALUES (?, ?)', (2, 'João'))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f'Erro: {e}')

# Consultar dados
cursor.execute('SELECT * FROM alunos')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
# Fechar conexões
cursor.close()
conn.close()
