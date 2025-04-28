import customtkinter as ctk
import hashlib
import json
import os
from tkinter import messagebox
from tools.Registros import Registros
from tools.Alugar import Alugar
from tools.Devolver import Devolver

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

def mostrar_tela_principal():
    frame_login.pack_forget()
    frame_Lcadastro.pack_forget()
    frame_Ucadastro.pack_forget()
    frame_Acadastro.pack_forget()
    frame_Alug_Devol.pack_forget()
    textbox_livros.pack_forget()
    frame_principal.pack(fill='both', expand=True)

def mostrar_tela_login():
    frame_principal.pack_forget()
    frame_login.pack(fill='both', expand=True)

def mostar_tela_Ucadastro():
    frame_principal.pack_forget()
    frame_Acadastro.pack_forget()
    frame_Ucadastro.pack(fill='both', expand=True)

def mostrar_tela_Acadastro():
    frame_Ucadastro.pack_forget()
    frame_Acadastro.pack(fill = 'both', expand = True)

def mostrar_tela_Lcadastro():
    frame_principal.pack_forget()
    frame_Lcadastro.pack(fill='both', expand=True)

def mostrar_tela_Alug_Devol():
    frame_principal.pack_forget()
    frame_Alug_Devol.pack(fill='both', expand=True)

# Carregar arquivo users.json
def carregar_Users():
    user_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')
    try:
        with open(user_json, 'r', encoding='utf-8') as arquivo:
            users = json.load(arquivo)
            return True, users
    except Exception as e:
        return False, f'ERROR: {e}'
    
# Carregar arquivo books.json
def carregar_Books():
    book_json = os.path.join(os.path.dirname(__file__), '../data', 'books.json')
    try:
        with open(book_json, 'r', encoding='utf-8') as arquivo:
            books = json.load(arquivo)
            return True, books
    except Exception as e:
        return False, f'ERROR: {e}'

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

# Registrar Admin
def registrar_admin():
    nome = caixa_Acadastro_nome.get()
    cpf = caixa_Acadastro_cpf.get()
    email = caixa_Acadastro_email.get()
    senha = caixa_Acadastro_senha.get()
    sucesso, cadastroA = Registros.cadastro_admin(nome, cpf, email, senha)
    if sucesso:
        messagebox.showinfo("SUCESSO", cadastroA)
    else:
        messagebox.showerror("ERRO NO CADASTRO", cadastroA)

# Registrar Livro
def registrar_livro():
    titulo = caixa_Lcadastro_titulo.get()
    autor = caixa_Lcadastro_autor.get()
    genero = caixa_Lcadastro_genero.get()
    descricao = caixa_Lcadastro_descricao.get()
    edicao = caixa_Lcadastro_edicao.get()
    quantidade = caixa_Lcadastro_quantidade.get()
    sucesso, cadastroL = Registros.cadastro_livro(titulo, autor, genero, edicao, quantidade, descricao,)
    if sucesso:
        messagebox.showinfo("SUCESSO", cadastroL)
    else:
        messagebox.showerror("ERRO NO CADASTRO", cadastroL)
# Função de alugar livro
def alugar_livro():
    try:
        usuario = combobox_usuarios.get()
        livro = combobox_livros.get()
        quantidade_str = quantidade_livro.get().strip()
        if not quantidade_str:
            raise ValueError('Por favor, informe a quantidade de livros')
        if not quantidade_str.isdigit():
            raise ValueError('Quantidade invalida. Informe apenas numeros')
        quantidade = int(quantidade_str)

        sucessoA, menssage= Alugar.alugar(usuario, livro, quantidade)
    except ValueError as e:
        messagebox.showerror("ERRO", str(e))
    if sucessoA:
        messagebox.showinfo("SUCESSO", menssage)
    else:
        messagebox.showerror("ERRO", menssage)
# Função de devolver Livro
def devolver_livro():
    try:
        usuario = combobox_usuarios.get()
        livro = combobox_livros.get()
        quantidade_str = quantidade_livro.get().strip()
        if not quantidade_str:
            raise ValueError('Por favor, informe a quantidade de livros')
        if not quantidade_str.isdigit():
            raise ValueError('Quantidade invalida. Informe apenas numeros')
        quantidade = int(quantidade_str)

        sucessoD, menssage= Devolver.devolver(usuario, livro, quantidade)
    except ValueError as e:
        messagebox.showerror("ERRO", str(e))
    if sucessoD:
        messagebox.showinfo("SUCESSO", menssage)
    else:
        messagebox.showerror("ERRO", menssage)


# Set janela
ctk.set_appearance_mode('system') 
ctk.set_default_color_theme('blue')
screen = ctk.CTk()
screen.title('BiblioTec')
screen.geometry('800x600')
#screen.attributes("-fullscreen", True) #ideia para tela cheia
#def sair_tela_cheia(event=None):
    #screen.attributes("-fullscreen", False)#ideia para tela cheia
#screen.state("zoomed") ideia para tela cheia mas com os botoes de minimizacao, janela e

# fram 1: Tela de login
frame_login = ctk.CTkFrame(screen)
#texto_login = ctk.CTkLabel(frame_login, text= "Use Esc para sair da tela cheia", font= ("Candara Light Italic",24))
#texto_login.pack(padx=10, pady=10)
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
texto_apresentacao = ctk.CTkLabel(frame_principal, text= "Bem vindo a Bibliotec", font= ("Roboto",24))
texto_apresentacao.place(x=20, y=20)
botao_principal_sair= ctk.CTkButton(frame_principal, text= "Sair", command= mostrar_tela_login, font= ("Roboto",14))
botao_principal_sair.place(x=650, y=550)
botao_principal_adUsuario = ctk.CTkButton(frame_principal, text= "Cadastrar Usuario", font= ("Roboto",14), command= mostar_tela_Ucadastro)
botao_principal_adUsuario.place(x=130 ,y=100)
botao_principal_adLivro = ctk.CTkButton(frame_principal, text="Cadastrar livro", font= ("Roboto",14), command=mostrar_tela_Lcadastro)
botao_principal_adLivro.place(x=330,y=100)
botao_principal_AluDev = ctk.CTkButton(frame_principal, text="Alugar/Devolver Livro", font= ("Roboto",14), command=mostrar_tela_Alug_Devol)
botao_principal_AluDev.place(x=530, y=100)

textbox_livros = ctk.CTkTextbox(
    frame_principal,
    width=400,
    height=200,
    wrap="word",  # Quebra de linha
    fg_color="#2E64FE",
    scrollbar_button_color="#4b4b4b",
)
textbox_livros.place(x=200, y=200)
sucessoL, books_box = carregar_Books()
if sucessoL:
    box_livros = [f"Título: {book["Nome"]}\nAutor: {book["Autor(a)"]}\n Quantidade:{book["Quantidade"]}\nDescrição: {book["Descrição"]}\n \n" for book in books_box]
    textbox_livros.insert("0.0", box_livros)
else:
    messagebox.showerror("ERRO",box_livros)


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
botao_Acadastro = ctk.CTkButton(frame_Ucadastro, text= "Cadastrar Adiministrador", font = ("Roboto", 14), command = mostrar_tela_Acadastro)
botao_Acadastro.pack(padx=10, pady=10)
botao_Ucadastro_voltar = ctk.CTkButton(frame_Ucadastro, text="Voltar",font=("Roboto", 14), command=mostrar_tela_principal)
botao_Ucadastro_voltar.pack(padx=10, pady=10)

#frame 4: tela de cadastrar administrador
frame_Acadastro = ctk.CTkFrame(screen)
texto_Acadastro = ctk.CTkLabel(frame_Acadastro, text="Cadastrar novo Administrador:", font=("Roboto", 14))
texto_Acadastro.pack(padx=10, pady=10)
texto_Acadastro_nome = ctk.CTkLabel(frame_Acadastro, text="Nome: ", font=("Roboto", 14))
texto_Acadastro_nome.pack(padx=10, pady=2)
caixa_Acadastro_nome = ctk.CTkEntry(frame_Acadastro, placeholder_text="Nome do Usuario", width=300)
caixa_Acadastro_nome.pack(padx=10, pady=2)
texto_Acadastro_cpf = ctk.CTkLabel(frame_Acadastro, text= "CPF: ", font=("Roboto",14))
texto_Acadastro_cpf.pack(padx=10, pady=2)
caixa_Acadastro_cpf = ctk.CTkEntry(frame_Acadastro, placeholder_text="123.456.789-00", width=150)
caixa_Acadastro_cpf.pack(padx=10, pady=2)
texto_Acadastro_email = ctk.CTkLabel(frame_Acadastro, text="Email: ", font=("Roboto",14))
texto_Acadastro_email.pack(padx=10, pady=2)
caixa_Acadastro_email = ctk.CTkEntry(frame_Acadastro, placeholder_text="email@exemplo.com", width= 300)
caixa_Acadastro_email.pack(padx=10, pady=2)
texto_Acadastro_senha = ctk.CTkLabel(frame_Acadastro, text="Senha:", font=("Roboto", 14))
texto_Acadastro_senha.pack(padx=10, pady=2)
caixa_Acadastro_senha = ctk.CTkEntry(frame_Acadastro, placeholder_text="00000", width=150)
caixa_Acadastro_senha.pack(padx=10, pady=2)
botao_Acadastro_registrar = ctk.CTkButton(frame_Acadastro, text="Cadastrar", font=("Roboto", 14), command=registrar_admin)
botao_Acadastro_registrar.pack(padx=10, pady=10)
botao_Acadastro_voltar_principal = ctk.CTkButton(frame_Acadastro, text="Tela principal",font=("Roboto", 14), command= mostrar_tela_principal)
botao_Acadastro_voltar_principal.pack(padx=10, pady=10)
botao_Acadastro_voltar = ctk.CTkButton(frame_Acadastro, text= "Voltar", font=("Roboto", 14), command=mostar_tela_Ucadastro)
botao_Acadastro_voltar.pack(padx=10, pady=10)

# fram 5: tela de cadastro de livros
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

#frame 6: Tela de alugar e devolver
frame_Alug_Devol = ctk.CTkFrame(screen)
texto_Alug_Devol_titulo = ctk.CTkLabel(frame_Alug_Devol, text = "Alugar ou Devolver",font=("Roboto", 24))
texto_Alug_Devol_titulo.place(x=20 , y= 20)

texto_box_usuarios= ctk.CTkLabel(frame_Alug_Devol,text="Usuários",font=("Roboto", 14))
texto_box_usuarios.place(x=20 , y= 60)
sucessoU, users_box = carregar_Users()
if sucessoU:
    box_usuarios = [f"{user["Nome"]}" for user in users_box]
    combobox_usuarios = ctk.CTkComboBox(
        master= frame_Alug_Devol,
        values=box_usuarios,
        width=200,
        height=30,
        dropdown_fg_color="#2b2b2b",
        dropdown_hover_color="#3b3b3b",
        button_color="#2E64FE",
        state="readonly"
    )
    combobox_usuarios.place(x=20 , y= 100)
    
else:
    messagebox.showerror("ERRO", users_box)

texto_box_livro= ctk.CTkLabel(frame_Alug_Devol,text="Livros",font=("Roboto", 14))
texto_box_livro.place(x=400 , y= 60)
sucessoL, books_box = carregar_Books()
if sucessoL:
    box_livros = [f"{book["Nome"]}" for book in books_box]
    combobox_livros = ctk.CTkComboBox(
        master= frame_Alug_Devol,
        values=box_livros,
        width=200,
        height=30,
        dropdown_fg_color="#2b2b2b",
        dropdown_hover_color="#3b3b3b",
        button_color="#2E64FE",
        state="readonly"
    )
else:
    messagebox.showerror("ERRO", books_box)
combobox_livros.place(x=400 ,y= 100)
texto_quantidade_livro = ctk.CTkLabel(frame_Alug_Devol, text= "Unidades", font= ("Roboto", 14))
texto_quantidade_livro.place(x=20,y=430)
quantidade_livro = ctk.CTkEntry(frame_Alug_Devol, placeholder_text= "Unidades", width= 100)
quantidade_livro.place(x=20 ,y= 470)
botao_aluagar = ctk.CTkButton(frame_Alug_Devol, text = "Alugar",font=("Roboto", 14), command=alugar_livro)
botao_aluagar.place(x=20 ,y= 510)
botao_devolver = ctk.CTkButton(frame_Alug_Devol, text = "Devolver",font=("Roboto", 14), command=devolver_livro)
botao_devolver.place(x=20 ,y= 550)
botao_Alug_Devol_Voltar = ctk.CTkButton(frame_Alug_Devol, text="Voltar", command= mostrar_tela_principal)
botao_Alug_Devol_Voltar.place(x=650,y= 550)


mostrar_tela_login()

screen.bind('<Return>', lambda event: login_autent())#so funciona no login (NAO USE FORA DO LOGIN!!)

#screen.bind('<Escape>', sair_tela_cheia)

screen.mainloop()

    
