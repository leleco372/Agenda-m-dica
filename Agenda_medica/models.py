import sqlite3
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)""")
cursor.execute("""
INSERT INTO usuarios (nome, email, senha) VALUES ('Leandro', 'leandro@example.com', '123456')
""")
conexao.commit()