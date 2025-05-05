import json
import os
from objects.Usuario import Usuario
from objects.Livro import Livro

class Alugar:
    def alugar(user_selecionado, nome_livro, quantidade_livro):
        try:
            if not user_selecionado:
                raise ValueError('Cliente não selecionado ou inválido.')
            if not nome_livro:
                raise ValueError('Livro não selecionado ou invalido.')
            if quantidade_livro <= 0:
                raise ValueError('Quantidade Inválida')
            if not quantidade_livro:
                raise ValueError('Quantidade não pode ser vazia')
        except ValueError as e:
            return False, str(e)
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
            if user["Nome"] == user_selecionado:
                usuario_aluga = Usuario(user["Nome"], user["Email"], user["CPF"], user["Telefone"], user["livros alugados"], user["quantidade Alugada"])
                break
        dados_users_atualizado = [user for user in users if user["Nome"] != user_selecionado]

        for livro in livros:
            if livro["Nome"] == nome_livro:
                livro_aluga = Livro(livro["Nome"], livro["Autor(a)"], livro["Genero"], livro["Descrição"], livro["Edição"], livro["Quantidade"])
                break
        dados_livros_atualizado = [livro for livro in livros if livro["Nome"] != nome_livro]

        menssagem = usuario_aluga.alugando(livro_aluga, quantidade_livro)

        usuario_att = usuario_aluga.usuario_dic()
        livro_att = livro_aluga.livro_dic()

        dados_livros_atualizado.append(livro_att)
        dados_users_atualizado.append(usuario_att)


        try:
            with open(dados_livros_json, 'w', encoding="utf-8") as arquivo:
                json.dump(dados_livros_atualizado, arquivo, indent=4)
        except Exception as e:
            return False, "Erro ao salvar os livros"
        
        try:
            with open(dados_users_json, 'w', encoding='utf-8') as arquivo:
                json.dump(dados_users_atualizado, arquivo, indent=4)
        except Exception as e:
            return False, "Erro ao salvar os clientes"
        
        return True, menssagem

        