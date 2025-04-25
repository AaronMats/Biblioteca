# from objects.Usuario import Usuario 
from objects.Admin import Admin
from objects.Livro import Livro
from objects.Pessoa import Pessoa
from objects.Usuario import Usuario
import json
import os
import hashlib

class Registros:
    def cadastro_admin(nome, email, cpf, senha):
        senha_segura =  hashlib.sha256(senha.encode()).hexdigest()

        adm_registrar = Admin(nome, email, cpf, senha_segura)

        adm_novo = adm_registrar.admin_dic()

        dados_json = os.path.join(os.path.dirname(__file__), '../data', 'admins.json')
        

        try:
            if os.path.exists(dados_json) and os.path.getsize(dados_json) > 0:
                with open(dados_json, "r", encoding="utf-8") as arquivo:
                    dados_json_exist = json.load(arquivo)
            else:
                dados_json_exist = []
        except json.JSONDecodeError:
            print("Arquivo JSON mal formatado. Iniciando com uma lista vazia.")
            dados_json_exist = []
        except Exception as e:
            print(f"Error: {e}")
            

        dados_json_exist.append(adm_novo)

        try:
            with open(dados_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_json_exist, arquivo, indent= 4)
            print("cadastrado com sucesso")
        except Exception as e:
            print(f"Error: {e}")

    def cadastro_livro(titulo, autor, genero, descricao, edicao, quantidade):
        livro = Livro(titulo, autor, genero, descricao, edicao, quantidade)

        livro_novo = livro.livro_dic()
        dados_json = os.path.join(os.path.dirname(__file__), '../data', 'books.json')

        try:
            if os.path.exists(dados_json) and os.path.getsize(dados_json) > 0:
                with open(dados_json, "r", encoding="utf-8") as arquivo:
                    dados_exist = json.load(arquivo)
            else:
                dados_exist = []
        except json.JSONDecodeError:
            print("Arquivo JSON mal formatado. Iniciando com uma lista vazia.")
            dados_exist = []
        except Exception as e:
            print(f"Error: {e}")
        
        dados_exist.append(livro_novo)

        try:
            with open(dados_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_exist, arquivo, indent=4)
            print("Livro registrado com sucesso")
        except Exception as e:
            print(f"Error: {e}")

    def cadastro_usuario(nome, email, cpf, telefone):
        
        usuario = Usuario(nome, email, cpf, telefone,[],[])

        usuario_novo = usuario.usuario_dic()
        usuario_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')

        try:
            if os.path.exists(usuario_json) and os.path.getsize(usuario_json) > 0:
                with open(usuario_json, "r", encoding="utf-8") as arquivo:
                    usuarios_exist = json.load(arquivo)
            else:
                usuarios_exist = []
        except json.JSONDecodeError:
            print("Arquivo JSON mal formatado. Iniciando com uma lista vazia.")
            usuarios_exist = []
        except Exception as e:
            print(f"Error: {e}")

        usuarios_exist.append(usuario_novo)

        try:
            with open(usuario_json, "w", encoding="utf-8") as arquivo:
                json.dump(usuarios_exist, arquivo, indent=4)
            return True
        except Exception as e:
            print(f"Error: {e}")