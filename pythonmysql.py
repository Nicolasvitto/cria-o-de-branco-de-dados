import mysql.connector

# Conectando ao servidor MySQL
conexao = mysql.connector.connect(
    host="localhost",       # Endereço do servidor MySQL
    user="seu_usuario",     # Usuário do MySQL
    password="sua_senha"    # Senha do MySQL
)

cursor = conexao.cursor()

# Criando um banco de dados
cursor.execute("CREATE DATABASE meu_banco_de_dados")

print("Banco de dados criado com sucesso!")

# Fechando a conexão
cursor.close()
conexao.close()