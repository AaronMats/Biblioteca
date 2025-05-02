import json
import os


class Deletar:
    def deletar_usuario(nome_user):
        dados_users_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')

        try:
            with open(dados_users_json, "r", encoding="utf-8") as arquivo:
                users = json.load(arquivo)
        except Exception as e:
            return False, f"Erro ao ler o arquivo!\nERROR: {e}"
        
        for user in users:
            if len(user["livros alugados"]) > 0 :
                return False, f"Usuário {nome_user} não pode ser deletado pois tem {len(user['livros_alugados'])} livro(s) alugado(s)"
        
        
        dados_atualizados = [user for user in users if user["Nome"] != nome_user]

        try:
            with open(dados_users_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_atualizados, arquivo, indent=4)
                return True, f"Usuario: {nome_user} deletado com sucesso!!"
        except Exception as e:
            return False, f"Erro ao salvar o arquivo!\nERROR: {e}"
        

    def deletar_admin(nome_admin):
        dados_admin_json = os.path.join(os.path.dirname(__file__), '../data', 'admins.json')

        try:
            with open(dados_admin_json, "r", encoding="utf-8") as arquivo:
                admins = json.load(arquivo)
        except Exception as e:
            return False, f"Erro ao ler o arquivo!\nERROR: {e}"
        
        dados_atualizados = [admin for admin in admins if admin["Nome"] != nome_admin]

        try:
            with open(dados_admin_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_atualizados, arquivo, indent=4)
                return True, f"Administrador {nome_admin} foi deletado!"
        except Exception as e:
            return False, f"Erro ao salvar o arquivo!\nERROR: {e}"