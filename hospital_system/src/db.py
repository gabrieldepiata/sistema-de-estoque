import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/hospital.db")

def conectar():
    conn = sqlite3.connect(DB_PATH)
    return conn

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        senha TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        descricao TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicamento_id INTEGER,
        quantidade INTEGER,
        FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT
    )
    """)

    # Usuário inicial padrão
    cursor.execute("INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES (?, ?)", ("admin", "1234"))

    conn.commit()
    conn.close()
