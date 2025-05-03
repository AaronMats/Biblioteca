import customtkinter as ctk
import hashlib
import json
import os
from tkinter import messagebox
from tools.Registros import Registros
from tools.Alugar import Alugar
from tools.Devolver import Devolver
from PIL import Image, ImageTk
from customtkinter import CTkImage

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

def mostrar_tela_principal():
    frame_login.pack_forget()
    frame_Lcadastro.pack_forget()
    frame_Ucadastro.pack_forget()
    frame_Acadastro.pack_forget()
    frame_Alug_Devol.pack_forget()
    tela_de_usuarios.pack_forget()
    caixa_de_usuarios.pack_forget()
    frame_principal.pack(fill='both', expand=True)

def mostar_usuarios():
    frame_principal.pack_forget()
    tela_de_usuarios.pack(fill="both", expand=True)

def mostrar_tela_login():
    frame_admin.pack_forget()
    frame_principal.pack_forget()
    frame_login.pack(fill='both', expand=True)
    screen.unbind("<Return>") #recurso para o enter funcionar 
    screen.bind("<Return>", login_autent)#recurso para o enter funcionar 

def mostar_tela_Ucadastro():
    frame_principal.pack_forget()
    frame_Acadastro.pack_forget()
    frame_Ucadastro.pack(fill='both', expand=True)
    screen.unbind("<Return>")#recurso para o enter funcionar 
    screen.bind("<Return>", registrar)#recurso para o enter funcionar 

def mostrar_tela_Acadastro():
    frame_Ucadastro.pack_forget()
    frame_Acadastro.pack(fill = 'both', expand = True)
    screen.unbind("<Return>")#recurso para o enter funcionar 
    screen.bind("<Return>", registrar_admin)#recurso para o enter funcionar 

def mostrar_tela_Lcadastro():
    frame_principal.pack_forget()
    frame_Lcadastro.pack(fill='both', expand=True)
    screen.unbind("<Return>")#recurso para o enter funcionar 
    screen.bind("<Return>", registrar_livro)#recurso para o enter funcionar 

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
    
def tabela_livros(book_json):
    book_json = os.path.join(os.path.dirname(__file__), '../data', 'books.json')
    try:
        with open(book_json, 'r', encoding='utf-8') as arquivo:
            books = json.load(arquivo)
            return books
    except FileExistsError:
        return []
    except json.JSONDecodeError:
        return []
    
def tabela_usuarios(user_json):
    user_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')
    try:
        with open(user_json, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileExistsError, json.JSONDecodeError):
        return[]
    
def abrir_tela_admin_v():
    frame_admin.pack(fill='both', expand=True)

    caminho_logo = os.path.join(os.path.dirname(__file__), "../assets", "kixw0iv01jib1.jpg")

    imagem = Image.open(caminho_logo)
    
    imagem_ctk = CTkImage(light_image=imagem, dark_image=imagem, size=(150,150))
    label_img = ctk.CTkLabel(master=frame_admin, image=imagem_ctk, text="")
    label_img.image = imagem_ctk
    label_img.pack(pady= 20)

    label_nome = ctk.CTkLabel(master=frame_admin, text="Bibliotec", font=("Roboto", 24, "bold"))
    label_nome.pack(pady=10)

    botao_voltar = ctk.CTkButton(master=frame_admin, text="Voltar", command=mostrar_tela_login)
    botao_voltar.pack(pady=20)

# Autenticação de login
def login_autent(event=None):
    email = caixa_login_email.get()
    senha = caixa_login_senha.get()
    caixa_login_senha.delete(0, 'end')
    senha_segura = hashlib.sha256(senha.encode()).hexdigest()
    dados = os.path.join(os.path.dirname(__file__), "../data", "admins.json")

    try:
        with open(dados, "r", encoding="utf-8") as arquivo:
            admins = json.load(arquivo)

        for admin in admins:
            if admin["Email"] == email and admin["Senha"] == senha_segura:
               
                if admin["Email"] == "vegetalendo@email.com":
                    frame_login.pack_forget()
                    abrir_tela_admin_v() 
                else:
                    frame_login.pack_forget()
                    frame_principal.pack(fill='both', expand=True)
                return 
        messagebox.showerror("ERROR", "Email e/ou senha inválido(s)")
    except FileNotFoundError:
        messagebox.showerror("ERROR", "Arquivo não encontrado")
        
# Registrar Usuario
def registrar(event=None):
    nome = caixa_Ucadastro_nome.get()
    cpf = caixa_Ucadastro_cpf.get()
    email = caixa_Ucadastro_email.get()
    telefone = caixa_Ucadastro_telefone.get()

    #para resetar os campos de entrada
    caixa_Ucadastro_nome.delete(0, 'end')
    caixa_Ucadastro_cpf.delete(0, 'end')
    caixa_Ucadastro_email.delete(0, 'end')
    caixa_Ucadastro_telefone.delete(0,'end')
    
    # Opcional: voltar o foco para o primeiro campo
    caixa_Ucadastro_nome.focus()

    sucesso, cadastroU = Registros.cadastro_usuario(nome, cpf, email, telefone)
    if sucesso:
        messagebox.showinfo("SUCESSO", cadastroU)
    else:
        messagebox.showerror("ERRO NO CADASTRO", cadastroU)

# Registrar Admin
def registrar_admin(event= None):
    nome = caixa_Acadastro_nome.get()
    cpf = caixa_Acadastro_cpf.get()
    email = caixa_Acadastro_email.get()
    senha = caixa_Acadastro_senha.get()

    #para resetar os campos de entrada
    caixa_Acadastro_nome.delete(0, 'end')
    caixa_Acadastro_cpf.delete(0, 'end')
    caixa_Acadastro_email.delete(0, 'end')
    caixa_Acadastro_senha.delete(0,'end')
    
    # Opcional: voltar o foco para o primeiro campo
    caixa_Acadastro_nome.focus()

    sucesso, cadastroA = Registros.cadastro_admin(nome, cpf, email, senha)
    if sucesso:
        messagebox.showinfo("SUCESSO", cadastroA)
    else:
        messagebox.showerror("ERRO NO CADASTRO", cadastroA)

# Registrar Livro
def registrar_livro(event= None):
    titulo = caixa_Lcadastro_titulo.get()
    autor = caixa_Lcadastro_autor.get()
    genero = caixa_Lcadastro_genero.get()
    descricao = caixa_Lcadastro_descricao.get()
    edicao = caixa_Lcadastro_edicao.get()
    quantidade = caixa_Lcadastro_quantidade.get()

    #para resetar os campos de entrada
    caixa_Lcadastro_titulo.delete(0, 'end')
    caixa_Lcadastro_autor.delete(0, 'end')
    caixa_Lcadastro_genero.delete(0, 'end')
    caixa_Lcadastro_descricao.delete(0,'end')
    caixa_Lcadastro_edicao.delete(0 ,'end')
    caixa_Lcadastro_quantidade.delete(0, 'end')

    # Opcional: voltar o foco para o primeiro campo
    caixa_Lcadastro_titulo.focus()
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
        combobox_usuarios.set("")
        combobox_livros.set("")
        quantidade_livro.delete(0,'end')
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
        combobox_usuarios.set("")
        combobox_livros.set("")
        quantidade_livro.delete(0,'end')
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
screen.minsize(width=500, height=350)
# screen.state('zoomed')# se der errado pode tirar
# forcar_zoom = True# se der errado pode tirar

# cont = 0# se der errado pode tirar

# def forcar_maximizado():# se der errado pode tirar
#     global cont
#     if forcar_zoom and cont < 10:
#         screen.state('zoomed')
#         cont += 1
#         screen.after(500, forcar_maximizado)

# def sair_tela_cheia(event=None):# se der errado pode tirar
#     global forcar_zoom
#     forcar_zoom = False
#     screen.state("normal")
#     screen.geometry('800x600')

# fram 1: Tela de login
frame_login = ctk.CTkFrame(master=screen)
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
texto_apresentacao.pack(padx=10, pady=10)
botao_principal_adUsuario = ctk.CTkButton(frame_principal, text= "Cadastrar Usuario", font= ("Roboto",14), command= mostar_tela_Ucadastro)
botao_principal_adUsuario.place(relx=0.1, rely=0.1, relwidth=0.20, relheight=0.05)
botao_principal_adLivro = ctk.CTkButton(frame_principal, text="Cadastrar livro", font= ("Roboto",14), command=mostrar_tela_Lcadastro)
botao_principal_adLivro.place(relx=0.4, rely=0.1, relwidth=0.20, relheight=0.05)
botao_principal_AluDev = ctk.CTkButton(frame_principal, text="Alugar/Devolver Livro", font= ("Roboto",14), command=mostrar_tela_Alug_Devol)
botao_principal_AluDev.place(relx=0.7, rely=0.1, relwidth=0.20, relheight=0.05)
botao_principal_usuarios = ctk.CTkButton(frame_principal, text="Usuarios", font=("Roboto", 14), command=mostar_usuarios)
botao_principal_usuarios.place(relx=0.4, rely=0.2, relwidth=0.20, relheight=0.05)

#caixa de livros
livros = tabela_livros("books.json")
cabecalho = ["Título", "Edição", "Genêro", "Autor", "Quantidade" ]
caixa_de_livros = ctk.CTkScrollableFrame(frame_principal, width=600, height=300)
caixa_de_livros.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.5)

for coluna, titulo in enumerate(cabecalho):
    tabela_org = ctk.CTkLabel(
        caixa_de_livros,
        text = titulo, 
        font=("Arial", 14),
        width=120,
        height=30
    )
    tabela_org.grid(row=0, column=coluna, padx=5,pady=5)
for linha, pessoa in enumerate(livros, start=1):
    ctk.CTkLabel(
        caixa_de_livros,
        text=pessoa["Nome"],
        wraplength=100,
        width= 200,
        height=30
    ).grid(row=linha, column=0, padx=4, pady=2)
    ctk.CTkLabel(
        caixa_de_livros,
        text=pessoa["Edição"],
        width= 80,
        height=30
    ).grid(row=linha, column=1, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_livros,
        text=pessoa["Genero"],
        width= 120,
        height=30
    ).grid(row=linha, column=2, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_livros,
        text=pessoa["Autor(a)"],
        wraplength=100,
        width= 120,
        height=30
    ).grid(row=linha, column=3, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_livros,
        text=pessoa["Quantidade"],
        width= 120,
        height=30
    ).grid(row=linha, column=4, padx=2, pady=2)

for col in range(len(cabecalho)):
    caixa_de_livros.grid_columnconfigure(col, weight=1)
    
botao_principal_sair= ctk.CTkButton(frame_principal, text= "Sair", command= mostrar_tela_login, font= ("Roboto",14))
botao_principal_sair.place(relx=0.75, rely=0.9, relwidth=0.20, relheight=0.05)

#Tela de Usuários
tela_de_usuarios= ctk.CTkFrame(screen)
texto_tela_usuarios = ctk.CTkLabel(tela_de_usuarios, text="Usuários Cadastrados", font= ("Roboto",24)).pack(pady=20)
voltar_user_principal = ctk.CTkButton(tela_de_usuarios, text="Voltar", command= mostrar_tela_principal)
voltar_user_principal.place(x=650,y= 550)
remover_usuario = ctk.CTkButton(tela_de_usuarios, text= "Remover usuário")
remover_usuario.place(x=10, y=550)
cabecalho = ["Nome", "CPF", "Email", "Telefone", "Alugados", "Quantidade"]
users = tabela_usuarios("users.json")
caixa_de_usuarios = ctk.CTkScrollableFrame(tela_de_usuarios, width=800, height=200)
caixa_de_usuarios.place(x=0,y=80)

for coluna, titulo in enumerate(cabecalho):
    cabecalho_texto = ctk.CTkLabel(
        caixa_de_usuarios,
        text = titulo, 
        font=("Arial", 14),
        width=150,
        height=30
    )
    cabecalho_texto.grid(row=0, column=coluna, padx=5,pady=5)
for linha, pessoa in enumerate(users, start=1):
    livros = pessoa.get("livros alugados", [])
    livros_usuarios = ", ".join(livros) if isinstance(livros, list) else str(livros)
    quantidade_de_livros = pessoa.get("quantidade Alugada", 0)
    if isinstance(quantidade_de_livros, list):
        quantidade_livro_alugada = sum(quantidade_de_livros)
    
    ctk.CTkLabel(
        caixa_de_usuarios,
        text=pessoa.get("Nome", ""),
        wraplength=80, 
        width= 150,
        height=30
    ).grid(row=linha, column=0, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_usuarios,
        text=pessoa.get("CPF", ""),
        width= 90,
        height=30
    ).grid(row=linha, column=1, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_usuarios,
        text=pessoa.get("Email", ""),
        width= 150,
        height=30
    ).grid(row=linha, column=2, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_usuarios,
        text=pessoa.get("Telefone", ""),
        wraplength=100,
        width= 120,
        height=30
    ).grid(row=linha, column=3, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_usuarios,
        text=livros_usuarios,
        wraplength=80,
        width= 120,
        height=30
    ).grid(row=linha, column=4, padx=2, pady=2)
    ctk.CTkLabel(
        caixa_de_usuarios,
        text=str(quantidade_livro_alugada),
        wraplength=80,
        width= 120,
        height=30
    ).grid(row=linha, column=5, padx=2, pady=2)

for col in range(len(cabecalho)):
    caixa_de_usuarios.grid_columnconfigure(col, weight=1)
#combobox para remover selecionar e remover usuário
texto_box_usuarios= ctk.CTkLabel(tela_de_usuarios,text="Usuários",font=("Roboto", 14))
texto_box_usuarios.place(x=300, y=320)
sucessoU, users_box = carregar_Users()
if sucessoU:
    box_usuarios = [f"{user["Nome"]}" for user in users_box]
    combobox_usuarios = ctk.CTkComboBox(
        master= tela_de_usuarios,
        values=box_usuarios,
        width=200,
        height=30,
        dropdown_fg_color="#2b2b2b",
        dropdown_hover_color="#3b3b3b",
        button_color="#2E64FE",
        state="readonly"
    )
    combobox_usuarios.place(x=300,y=350)
    
else:
    messagebox.showerror("ERRO", users_box)


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
botao_Acadastro = ctk.CTkButton(frame_Ucadastro, text= "Cadastrar Administrador", font = ("Roboto", 14), command = mostrar_tela_Acadastro)
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
caixa_Acadastro_senha = ctk.CTkEntry(frame_Acadastro, placeholder_text="Ex:00000", width=150)
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
texto_Lcadastro_descricao = ctk.CTkLabel(frame_Lcadastro, text="Descrição",wraplength=150, font=("Roboto", 14))
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
texto_quantidade_livro = ctk.CTkLabel(frame_Alug_Devol, text= "Quantidade:", font= ("Roboto", 14))
texto_quantidade_livro.place(x=20,y=430)
quantidade_livro = ctk.CTkEntry(frame_Alug_Devol, placeholder_text= "0", width= 100)
quantidade_livro.place(x=20 ,y= 470)
botao_aluagar = ctk.CTkButton(frame_Alug_Devol, text = "Alugar",font=("Roboto", 14), command=alugar_livro)
botao_aluagar.place(x=20 ,y= 510)
botao_devolver = ctk.CTkButton(frame_Alug_Devol, text = "Devolver",font=("Roboto", 14), command=devolver_livro)
botao_devolver.place(x=20 ,y= 550)
botao_Alug_Devol_Voltar = ctk.CTkButton(frame_Alug_Devol, text="Voltar", command= mostrar_tela_principal)
botao_Alug_Devol_Voltar.place(x=650,y= 550)

frame_admin = ctk.CTkFrame(master= screen) #frame do admin secreto
#Frame 7: tela de usuários


mostrar_tela_login()

# forcar_maximizado()# se der errado pode tirar

# screen.bind("<Escape>", sair_tela_cheia)# se der errado pode tirar

screen.mainloop()