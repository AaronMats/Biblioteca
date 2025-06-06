import json
import hashlib
import os
import customtkinter as ctk
from tkinter import messagebox
class Login_v():
    def login_autent(email, senha):
        senha_segura = hashlib.sha256(senha.encode()).hexdigest()
        dados = os.path.join(os.path.dirname(__file__), "../data", "admins.json")

        try:
            with open(dados, "r", encoding="utf-8") as arquivo:
                admins = json.load(arquivo)

            for admin in admins:
                if admin["Email"] == email and admin["Senha"] == senha_segura:
                    print("bem-vindo")
                else:
                    print("Email e/ou senha invalidos(s)")
        except FileNotFoundError:
            print("arquivo não encontrado")

