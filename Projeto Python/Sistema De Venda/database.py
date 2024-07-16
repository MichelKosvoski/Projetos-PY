import sqlite3

conn = sqlite3.connect("Sistema.db")

cursor= conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Username TEXT NOT NULL,Email TEXT NOT NULL, Password TEXT NOT NULL, ConfPassword TEXT NOT NULL)")

print("Conexao ao banco de dados feita com sucesso!")