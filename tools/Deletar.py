import json
import os


class Deletar:
    def deletar_usuario(nome_user):
        try:
            if not nome_user.strip():
                raise ValueError("Usuario não selecionado.")
            dados_users_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')
        except ValueError as e:
            return False, str(e)

        try:
            with open(dados_users_json, "r", encoding="utf-8") as arquivo:
                users = json.load(arquivo)
        except Exception as e:
            return False, f"Erro ao ler o arquivo!\nERROR: {e}"
        
        for user in users:
            if user["Nome"] == nome_user:
                user_selecionado = user
                if len(user_selecionado["livros alugados"]) > 0:
                    return False, f"Usuário {nome_user} não pode ser deletado pois tem livro(s) alugado(s)"
                break

            
        
        
        dados_atualizados = [user for user in users if user["Nome"] != nome_user]

        try:
            with open(dados_users_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_atualizados, arquivo, indent=4)
                return True, f"Usuario: {nome_user} deletado com sucesso!!"
        except Exception as e:
            return False, f"Erro ao salvar o arquivo!\nERROR: {e}"
        

    def deletar_admin(nome_admin):
        try:
            if not nome_admin.strip():
                raise ValueError("Administrador não selecionado.")
            dados_admin_json = os.path.join(os.path.dirname(__file__), '../data', 'admins.json')
        except ValueError as e:
            return False, str(e)

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
    

    def deletar_livro(nome_livro):
        try:
            if not nome_livro.strip():
                raise ValueError("Livro não selecionado.")
            dados_livros_json = os.path.join(os.path.dirname(__file__), '../data', 'books.json')
            dados_users_json = os.path.join(os.path.dirname(__file__), '../data', 'users.json')
        except ValueError as e:
            return False, str(e)

        try:
            with open(dados_users_json, "r", encoding="utf-8") as arquivo:
                users = json.load(arquivo)
        except Exception as e:
            return False, f"ERRO: {e}"
        
        for user in users:
            if nome_livro in user["livros alugados"]:
                return False, f"O livro nãopode ser deletado pois a um ou mais usuarios com ele alugado"
        
        try:
            with open(dados_livros_json, "r", encoding="utf-8") as arquivo:
                livros = json.load(arquivo)
        except Exception as e:
            return False, f"ERRO: {e}"
        
        dados_atualizados_livros = [livro for livro in livros if livro["Nome"] != nome_livro]

        try:
            with open(dados_livros_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_atualizados_livros, arquivo, indent=4)
                return True, f"O livro {nome_livro} foi deletado!"
        except Exception as e:
            return False, f"Erro ao salvar o arquivo\nERRO: {e}"
        