import customtkinter as ctk
# from tools.Login import Login_v
import hashlib
import json
import os
#from ..objects.Livro import Livro
#class Screen_login():
def mostrar_tela_principal():
    frame_login.pack_forget()
    frame_principal.pack(fill='both', expand=True)

def mostrar_tela_login():
    frame_principal.pack_forget()
    frame_login.pack(fill='both', expand=True)


def login_autent():
    email = caixa_login_email.get()
    senha = caixa_login_senha.get()
    senha_segura = hashlib.sha256(senha.encode()).hexdigest()
    dados = os.path.join(os.path.dirname(__file__), "../data", "admins.json")

    try:
        with open(dados, "r", encoding="utf-8") as arquivo:
            admins = json.load(arquivo)

        for admin in admins:
            if admin["Email"] == email and admin["Senha"] == senha_segura:
                print("bem-vindo")
                frame_login.pack_forget()
                frame_principal.pack(fill='both', expand=True)
                return 
        print("Email e/ou senha invalidos(s)")
    except FileNotFoundError:
        print("arquivo não encontrado")


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
screen_login = ctk.CTk()
screen_login.title('BiblioTec')
screen_login.geometry('500x600')

frame_login = ctk.CTkFrame(screen_login)
texto_login = ctk.CTkLabel(frame_login, text="Login")
texto_login.pack(padx=10, pady=10)
caixa_login_email = ctk.CTkEntry(frame_login, placeholder_text="Digite seu email")
caixa_login_email.pack(padx=10, pady= 2)
caixa_login_senha = ctk.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*")
caixa_login_senha.pack(padx=10, pady= 2)
botao_login_entrar = ctk.CTkButton(frame_login, text= "Entar", command= login_autent)
botao_login_entrar.pack(padx=10, pady=2)

frame_principal = ctk.CTkFrame(screen_login)
texto_teste = ctk.CTkLabel(frame_principal, text= "Tela Pincipal")
texto_teste.pack(padx= 10, pady=10)
botao_principal_sair= ctk.CTkButton(frame_principal, text= "Sair", command= mostrar_tela_login())
botao_principal_sair.pack(padx=10, pady=10)


mostrar_tela_login()

screen_login.mainloop()

    
