import json
import os
from ..objects.Usuario import Usuario
from ..objects.Livro import Livro

class Alugar:
    def alugar(usuario, nome_livro, quantidade_livro):
        dados_users_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')

        dados_livros_json = os.path.join(os.path.dirname(__file__), '../data', 'books.json')

        try:
            with open(dados_users_json, "r", encoding="utf-8") as arquivo:
                dados_users = json.load(arquivo)
        except Exception as e:
            print(f"Error: {e}")

        try:
            with open(dados_livros_json, "r", encoding="utf-8") as arquivo:
                dados_livros = json.load(arquivo)
        except Exception as e:
            print(f"ERROR: {e}")

        for user in dados_users:
            if usuario == user["Nome"]:
                usuario_aluga = Usuario(user["Nome"], user["Email"], user["cpf"], user["Telefone"], user["Livros alugados"], user["Quantidade Alugada"])
                for user in dados_users:
                    dados_atualizados_users = [
                        if usuario_aluga.getnome() != user["nome"] 
                    ]