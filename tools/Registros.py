from objects.admin import Admin
from objects.Livro import Livro
from objects.Pessoa import Pessoa
from objects.Usuario import Usuario
import json
import os
import hashlib

class Registros:
    def cadastro_admin(nome, cpf, email, senha):
        try:
            if not nome.strip():
                raise ValueError ('Nome não pode ser vazio.')
            if not all(parte.isalpha() for parte in nome.split()):
                raise ValueError('Nome deve conter apenas letras e espaços.')
            if not cpf.isdigit() or len(cpf) != 11:
                raise ValueError('O CPF deve conter 11 números.')
            if "@" not in email or "." not in email:
                raise ValueError('Email inválido.')
            if not senha.strip():
                raise ValueError('Senha não pode ser vazia')
            if len(senha) != 5:
                raise ValueError('Senha deve conter 5 digitos')
            senha_segura =  hashlib.sha256(senha.encode()).hexdigest()

            adm_registrar = Admin(nome, email, cpf, senha_segura)

            adm_novo = adm_registrar.admin_dic()

            dados_json = os.path.join(os.path.dirname(__file__), '../data', 'admins.json')
        except ValueError as error:
            return False, str(error)

        try:
            if os.path.exists(dados_json) and os.path.getsize(dados_json) > 0:
                with open(dados_json, "r", encoding="utf-8") as arquivo:
                    dados_exist = json.load(arquivo)

                for userAdm in dados_exist:
                    if userAdm.get("CPF", "").strip().lower() == cpf.lower():
                        return False,'Administrador com mesmo CPF já está cadastrado.'
                    if userAdm.get("Email", "").strip() == email.strip():
                        return False,'Administrador com mesmo email já está cadastrado.'
            else:
                dados_exist = []
        except json.JSONDecodeError:
            dados_exist = []
        except Exception as e:
            return False, f"Error: {e}"
            

        dados_exist.append(adm_novo)

        try:
            with open(dados_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_exist, arquivo, indent= 4)
            return True, "Administrador cadastrado com sucesso!"
        except Exception as e:
            return False, "Erro ao registrar Administrador\nErro: {e}"

    def cadastro_livro(titulo, autor, genero, edicao, quantidade, descricao, dados_json="books.json"):
        try:#Verificando cada etapa do cadastro livro
            if not titulo.strip():#Verifica se o titulo esta vazio
                raise ValueError('Título não pode ser vazio.')
            if titulo.isdigit():
                raise ValueError('Título não pode ser apenas números.')
            if not any(parte.isalpha() for parte in titulo.strip()):
                raise ValueError('Título precisa conter pelo menos uma letra.')
            if not autor.strip():#verifica se o autor esta vazio
                raise ValueError('Autor não pode ser vazio.')
            if autor.isdigit():
                raise ValueError('Autor não pode ser apenas números.')
            if not any(parte.isalpha() for parte in autor.strip()):
                raise ValueError('Autor precisa conter pelo menos uma letra.')
            if not genero.strip():#verifica se o genero esta vazio
                raise ValueError('Gênero não pode ser vazio.')
            if not any(char.isalpha() for char in genero):#verifica se o usuario colocou numeros no genero
                raise ValueError('Gênero não pode conter números')
            if not edicao.strip():#verifica se a ediçao esta vazia
                raise ValueError('Edição não pode ser vazia.')
            if not all(parte.isdigit() for parte in edicao.strip()):#verifica se o usuario inseriu uma string na ediçao
                raise ValueError('Edição deve conter apenas números.')
            if not quantidade.strip():#verifica se a quantidade esta vazia
                raise ValueError('Quantidade não pode ser vazia.')
            if not all(parte.isdigit() for parte in quantidade.strip()):#verifica se o usuario inseriu string na quantidade
                raise ValueError('Quantidade deve conter apenas números.')
            if quantidade.strip() == '0':#verifica se a quantidade e menor ou igual a 0
                raise ValueError('Quantidade não pode ser 0.')
            if not descricao.strip():#verifica se a descriçao esta vazia
                raise ValueError('Descrição não pode ser vazia.')
            if not any(parte.isalpha() for parte in descricao.strip()):
                raise ValueError('Descrição precisa conter pelo menos uma letra.')
            livro = Livro(titulo, autor, genero, descricao, edicao, quantidade)
            livro_novo = livro.livro_dic()
            dados_json = os.path.join(os.path.dirname(__file__), '../data', 'books.json')
        except ValueError as error:
            return False, str(error)
        try:
            if os.path.exists(dados_json) and os.path.getsize(dados_json) > 0:
                with open(dados_json, "r", encoding="utf-8") as arquivo:
                    dados_exist = json.load(arquivo)

                for livro in dados_exist:
                    if livro.get("Nome", "").strip().lower() == titulo.lower() and livro.get("Edição", "") .strip() == edicao.strip():
                        return False,'Este livro com mesma ediçao já está cadastrado.'
            else:
                dados_exist = []
        except json.JSONDecodeError:
            dados_exist = []
        except Exception as e:
            return False, f"Erro: {e}"
        
        dados_exist.append(livro_novo)

        try:
            with open(dados_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_exist, arquivo, indent=4)
            return True, "Livro registrado com sucesso"
        except Exception as e:
            return False, "Erro ao cadastrar"

    def cadastro_usuario(nome, cpf, email, telefone):
        try: #verificando cada etapa do cadastro do usuario
            if not nome.strip(): #Verifica se o nome esta vazio
                raise ValueError('Nome não pode ser vazio.')
            
            if not all(parte.isalpha() for parte in nome.split()): #verifica se o usuario colocou numero no nome
                raise ValueError('Nome deve conter apenas letras e espaços.')
            
            if not cpf.isdigit() or len(cpf) != 11: #Verifica se o cpf tem somente numeros e 11 caracteres
                raise ValueError('CPF deve conter 11 números')
            
            if "@" not in email or "." not in email: #Verifica se o usuario inseriu @ e . no email
                raise ValueError('Email inválido.')
            
            if not telefone.isdigit() or len(telefone) < 11: #verifica se o telefone tem 11 digitos
                raise ValueError('Telefone inválido')
            
            usuario = Usuario(nome, email, cpf, telefone,[],[])
            usuario_novo = usuario.usuario_dic()
            usuario_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')
        
        except ValueError as error: #retorna onde o usuario errou
            return False, str(error)
        
        try:
            if os.path.exists(usuario_json) and os.path.getsize(usuario_json) > 0:
                with open(usuario_json, "r", encoding="utf-8") as arquivo:
                    usuarios_exist = json.load(arquivo)

                for userAdm in usuarios_exist:
                    if userAdm.get("CPF", "").strip().lower() == cpf.lower():
                        return False,'Cliente com mesmo CPF já está cadastrado.'
                    if userAdm.get("Email", "").strip() == email.strip():
                        return False,'Cliente com mesmo email já está cadastrado.'
                    if userAdm.get("Telefone", "").strip() == telefone.strip():
                        return False,'Cliente com mesmo telefone já está cadastrado.'
            else:
                usuarios_exist = []
        except json.JSONDecodeError:
            usuarios_exist = []
        except Exception as e:
            return False, f"ERRO: {e}"

        usuarios_exist.append(usuario_novo)

        try:
            with open(usuario_json, "w", encoding="utf-8") as arquivo:
                json.dump(usuarios_exist, arquivo, indent=4)
            return True, "Cliente cadastrado com sucesso!"
        except Exception as e:
            return False, "Erro ao registrar usuário\nErro: {e}"