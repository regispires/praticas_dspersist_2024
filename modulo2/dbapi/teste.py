import sqlite3

# Usando gerenciador de contexto para garantir fechamento automático da conexão
with sqlite3.connect("exemplo.db") as conexao:
    with conexao.cursor() as cursor:
        # Consulta parametrizada
        consulta = "SELECT * FROM usuarios WHERE idade > ? AND cidade = ?"
        parametros = (25, "Nova York")

        # Executando a consulta com parâmetros
        cursor.execute(consulta, parametros)

        # Recuperando os resultados
        resultados = cursor.fetchall()

# Imprimindo os resultados
print(resultados)
