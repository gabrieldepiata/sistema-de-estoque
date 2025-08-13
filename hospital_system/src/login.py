import tkinter as tk
from tkinter import messagebox
from .db import conectar
from .menu import abrir_menu

def abrir_login():
    def autenticar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        if cursor.fetchone():
            root.destroy()
            abrir_menu()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")
        conn.close()

    root = tk.Tk()
    root.title("Login - Sistema Hospitalar")

    tk.Label(root, text="Usuário:").pack()
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()

    tk.Label(root, text="Senha:").pack()
    entry_senha = tk.Entry(root, show="*")
    entry_senha.pack()

    tk.Button(root, text="Entrar", command=autenticar).pack(pady=10)

    root.mainloop()
