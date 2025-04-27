import json
import os
from ..objects.Usuario import Usuario
from ..objects.Livro import Livro

class Alugar:
    def alugar(user_selecionado, nome_livro, quantidade_livro):
        
        dados_users_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')
        dados_livros_json = os.path.join(os.path.dirname(__file__), '../data', 'books.json')

        try:
            with open(dados_users_json, "r", encoding="utf-8") as arquivo:
                users = json.load(arquivo)
        except Exception as e:
            return False, f"ERROR: {e}"

        try:
            with open(dados_livros_json, "r", encoding="utf-8") as arquivo:
                livros = json.load(arquivo)
        except Exception as e:
            return False, f"ERROR: {e}"

        for user in users:
            if user_selecionado == user["Nome"]:
                usuario_aluga = Usuario(user["Nome"], user["Email"], user["cpf"], user["Telefone"], user["Livros alugados"], user["Quantidade Alugada"])
            else:
                return False, "Usuário não encontrado"
        dados_users_atualizado = [user for user in users if user["Nome"] != user_selecionado]

        for livro in livros:
            if livro["Nome"] == nome_livro:
                livro_aluga = Livro(livro["Titulo"], livro["Autor(a)"], livro["Genero"], livro["Descrição"], livro["Edição"], livro["Quantidade"])
            else:
                return False, "Livro não encontrado"
        dados_livros_atualizado = [livro for livro in livros if livro["Titulo"] != nome_livro]

        menssagem = usuario_aluga.devolve(livro_aluga, quantidade_livro)

        usuario_att = usuario_aluga.usuario_dic()
        livro_att = livro_aluga.livro_dic()

        dados_livros_atualizado.append(livro_att)
        dados_users_atualizado.append(usuario_att)


        try:
            with open(dados_livros_json, 'w', encoding="utf-8") as arquivo:
                json.dumps(dados_livros_atualizado, arquivo, indent=4)
        except Exception as e:
            return False, "Erro ao salvar as informações"
        
        return True, menssagem

        