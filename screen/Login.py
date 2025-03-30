import customtkinter as ctk
# import tools.Login
#from ..objects.Livro import Livro
class Screen_login():
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
    botao_login_entrar = ctk.CTkButton(frame_login, text= "Entar", command= Login_v.login_autent())
    botao_login_entrar.pack(padx=10, pady=2)



    frame_login.pack(fill='both', expand=True)

    screen_login.mainloop()