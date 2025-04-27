import customtkinter as ctk
import hashlib
import json
import os
from tkinter import messagebox
from tools.Registros import Registros


def mostrar_tela_principal():
    frame_login.pack_forget()
    frame_Lcadastro.pack_forget()
    frame_Ucadastro.pack_forget()
    frame_principal.pack(fill='both', expand=True)

def mostrar_tela_login():
    frame_principal.pack_forget()
    frame_login.pack(fill='both', expand=True)

def mostar_tela_Ucadastro():
    frame_principal.pack_forget()
    frame_Ucadastro.pack(fill='both', expand=True)

def mostrar_tela_Lcadastro():
    frame_principal.pack_forget()
    frame_Lcadastro.pack(fill='both', expand=True)



# Autenticação de login
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
                frame_login.pack_forget()
                frame_principal.pack(fill='both', expand=True)
                return 
        messagebox.showerror("ERROR", "Email e/ou senha inválido(s)")
    except FileNotFoundError:
        messagebox.showerror("ERROR", "Arquivo não encontrado")
        
# Registrar Usuario
def registrar():
    nome = caixa_Ucadastro_nome.get()
    cpf = caixa_Ucadastro_cpf.get()
    email = caixa_Ucadastro_email.get()
    telefone = caixa_Ucadastro_telefone.get()
    sucesso, cadastroU = Registros.cadastro_usuario(nome, cpf, email, telefone)
    if sucesso:
        messagebox.showinfo("SUCESSO", cadastroU)
    else:
        messagebox.showerror("ERRO NO CADASTRO", cadastroU)

# Registrar Livro
def registrar_livro():
    titulo = caixa_Lcadastro_titulo.get()
    autor = caixa_Lcadastro_autor.get()
    genero = caixa_Lcadastro_genero.get()
    descricao = caixa_Lcadastro_descricao.get()
    edicao = caixa_Lcadastro_edicao.get()
    quantidade = caixa_Lcadastro_quantidade.get()
    sucesso, cadastroL = Registros.cadastro_livro(titulo, autor, genero, descricao, edicao, quantidade)
    if sucesso:
        messagebox.showinfo("SUCESSO", cadastroL)
    else:
        messagebox.showerror("ERRO NO CADASTRO", cadastroL)



# Set janela
ctk.set_appearance_mode('system') 
ctk.set_default_color_theme('blue')
screen = ctk.CTk()
screen.title('BiblioTec')
screen.attributes("-fullscreen", True) #ideia para tela cheia
screen.geometry('800x600')
def sair_tela_cheia(event=None):
    screen.attributes("-fullscreen", False)#ideia para tela cheia
#screen.state("zoomed") ideia para tela cheia mas com os botoes de minimizacao, janela e
# fram 1: Tela de login
frame_login = ctk.CTkFrame(screen)
texto_login = ctk.CTkLabel(frame_login, text= "Use Esc para sair da tela cheia", font= ("Candara Light Italic",24))
texto_login.pack(padx=10, pady=10)
texto_login = ctk.CTkLabel(frame_login, text="Login",font= ("Roboto",25))
texto_login.pack(padx=10, pady=10)
caixa_login_email = ctk.CTkEntry(frame_login, placeholder_text="Digite seu email", font= ("Roboto",17), width=250)
caixa_login_email.pack(padx=10, pady= 2)
caixa_login_senha = ctk.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*", font= ("Roboto",17), width=250)
caixa_login_senha["width"] = 50
caixa_login_senha.pack(padx=10, pady= 2)
botao_login_entrar = ctk.CTkButton(frame_login, text= "Entrar", command= login_autent, font= ("Roboto",17))
botao_login_entrar.pack(padx=10, pady=2)
# fram 2: Tela principal
frame_principal = ctk.CTkFrame(screen)
texto_apresentacao = ctk.CTkLabel(frame_principal, text= "Bem vindo a Bibliotec", font= ("Candara Light Italic",24))
texto_apresentacao.grid(row=0, column=0, padx= 10, pady=10)
botao_principal_sair= ctk.CTkButton(frame_principal, text= "Sair", command= mostrar_tela_login, font= ("Roboto",14))
botao_principal_sair.grid(row=0, column=2, padx=10, pady=10)
botao_principal_adUsuario = ctk.CTkButton(frame_principal, text= "Cadastrar Usuario", font= ("Roboto",14), command= mostar_tela_Ucadastro)
botao_principal_adUsuario.grid(row=1, column=0, padx=10, pady=10)
botao_principal_adLivro = ctk.CTkButton(frame_principal, text="Cadastrar livro", font= ("Roboto",14), command=mostrar_tela_Lcadastro)
botao_principal_adLivro.grid(row=1, column=1, padx=10, pady=10)
botao_principal_AluDev = ctk.CTkButton(frame_principal, text="Alugar/Devolver Livro", font= ("Roboto",14))
botao_principal_AluDev.grid(row=1, column=2, padx=10, pady=10)
# fram 3: Tela de cadastro de ususários
frame_Ucadastro = ctk.CTkFrame(screen)
texto_Ucadastro = ctk.CTkLabel(frame_Ucadastro, text="Cadastrar novo usuário:", font=("Roboto", 14))
texto_Ucadastro.pack(padx=10, pady=10)
texto_Ucadastro_nome = ctk.CTkLabel(frame_Ucadastro, text="Nome: ", font=("Roboto", 14))
texto_Ucadastro_nome.pack(padx=10, pady=2)
caixa_Ucadastro_nome = ctk.CTkEntry(frame_Ucadastro, placeholder_text="Nome do Usuario", width=300)
caixa_Ucadastro_nome.pack(padx=10, pady=2)
texto_Ucadastro_cpf = ctk.CTkLabel(frame_Ucadastro, text= "CPF: ", font=("Roboto",14))
texto_Ucadastro_cpf.pack(padx=10, pady=2)
caixa_Ucadastro_cpf = ctk.CTkEntry(frame_Ucadastro, placeholder_text="123.456.789-00", width=150)
caixa_Ucadastro_cpf.pack(padx=10, pady=2)
texto_Ucadastro_email = ctk.CTkLabel(frame_Ucadastro, text="Email: ", font=("Roboto",14))
texto_Ucadastro_email.pack(padx=10, pady=2)
caixa_Ucadastro_email = ctk.CTkEntry(frame_Ucadastro, placeholder_text="email@exemplo.com", width= 300)
caixa_Ucadastro_email.pack(padx=10, pady=2)
texto_Ucadastro_telefone = ctk.CTkLabel(frame_Ucadastro, text="Telefone:", font=("Roboto", 14))
texto_Ucadastro_telefone.pack(padx=10, pady=2)
caixa_Ucadastro_telefone = ctk.CTkEntry(frame_Ucadastro, placeholder_text="(00)12345-6789", width=150)
caixa_Ucadastro_telefone.pack(padx=10, pady=2)
botao_Ucadastro_registrar = ctk.CTkButton(frame_Ucadastro, text="Cadastrar", font=("Roboto", 14), command=registrar)
botao_Ucadastro_registrar.pack(padx=10, pady=10)
botao_Ucadastro_voltar = ctk.CTkButton(frame_Ucadastro, text="Voltar",font=("Roboto", 14), command=mostrar_tela_principal)
botao_Ucadastro_voltar.pack(padx=10, pady=10)

# fram 4: tela de cadastro de livros
frame_Lcadastro = ctk.CTkFrame(screen)
texto_Lcadastro = ctk.CTkLabel(frame_Lcadastro, text= "Cadastro de Livros:", font=("Roboto", 14))
texto_Lcadastro.pack(padx=10, pady=10)
texto_Lcadastro_titulo = ctk.CTkLabel(frame_Lcadastro, text= "Título:", font=("Roboto",14))
texto_Lcadastro_titulo.pack(padx=10, pady=2)
caixa_Lcadastro_titulo = ctk.CTkEntry(frame_Lcadastro, placeholder_text="Título do livro", width=300)
caixa_Lcadastro_titulo.pack(padx=10, pady=2)
texto_Lcadastro_autor = ctk.CTkLabel(frame_Lcadastro, text="Autor(a):", font=("Roboto",14))
texto_Lcadastro_autor.pack(padx=10, pady=2)
caixa_Lcadastro_autor = ctk.CTkEntry(frame_Lcadastro, placeholder_text="Nome do autor(a)", width=300)
caixa_Lcadastro_autor.pack(padx=10, pady=2)
texto_Lcadastro_genero = ctk.CTkLabel(frame_Lcadastro, text="Gênero do livro:", font=("Roboto", 14))
texto_Lcadastro_genero.pack(padx=10, pady=2)
caixa_Lcadastro_genero = ctk.CTkEntry(frame_Lcadastro, placeholder_text="Gênero", width=300)
caixa_Lcadastro_genero.pack(padx=10, pady=2)
texto_Lcadastro_edicao = ctk.CTkLabel(frame_Lcadastro, text="Edição:", font=("Roboto",14))
texto_Lcadastro_edicao.pack(padx=10, pady=2)
caixa_Lcadastro_edicao = ctk.CTkEntry(frame_Lcadastro, placeholder_text="Nº da edição", width=300)
caixa_Lcadastro_edicao.pack(padx=10, pady=2)
texto_Lcadastro_quantidade = ctk.CTkLabel(frame_Lcadastro, text="Quantidade:", font=("Roboto",14))
texto_Lcadastro_quantidade.pack(padx=10, pady=2)
caixa_Lcadastro_quantidade = ctk.CTkEntry(frame_Lcadastro, placeholder_text="Quantidade de livros", width=300)
caixa_Lcadastro_quantidade.pack(padx=10, pady=2)
texto_Lcadastro_descricao = ctk.CTkLabel(frame_Lcadastro, text="Descrição", font=("Roboto", 14))
texto_Lcadastro_descricao.pack(padx=10, pady=2)
caixa_Lcadastro_descricao = ctk.CTkEntry(frame_Lcadastro, placeholder_text="Uma breve descrição do livro", width=350)
caixa_Lcadastro_descricao.pack(padx=10, pady=2)
botao_Lcadastro_registrar = ctk.CTkButton(frame_Lcadastro, text="Registrar", command=registrar_livro)
botao_Lcadastro_registrar.pack(padx=10, pady=2)
botao_Lcadastro_voltar = ctk.CTkButton(frame_Lcadastro, text="Voltar", command= mostrar_tela_principal)
botao_Lcadastro_voltar.pack(padx=10, pady=10)

mostrar_tela_login()

screen.bind('<Return>', lambda event: login_autent())#so funciona no login (NAO USE FORA DO LOGIN!!)

screen.bind('<Escape>', sair_tela_cheia)

screen.mainloop()

    
