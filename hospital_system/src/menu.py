import tkinter as tk
from .pacientes import abrir_pacientes
from .medicamentos import abrir_medicamentos
from .estoque import abrir_estoque
from .fornecedores import abrir_fornecedores

def abrir_menu():
    root = tk.Tk()
    root.title("Menu Principal - Sistema Hospitalar")
    root.geometry("300x300")

    tk.Button(root, text="Pacientes", width=20, command=abrir_pacientes).pack(pady=5)
    tk.Button(root, text="Medicamentos", width=20, command=abrir_medicamentos).pack(pady=5)
    tk.Button(root, text="Estoque", width=20, command=abrir_estoque).pack(pady=5)
    tk.Button(root, text="Fornecedores", width=20, command=abrir_fornecedores).pack(pady=5)
    tk.Button(root, text="Sair", width=20, command=root.destroy).pack(pady=20)

    root.mainloop()
