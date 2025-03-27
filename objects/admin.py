from .Pessoa import Pessoa
import json
import os
class Admin(Pessoa):
    def __init__(self, nome, email, cpf, senha):
        super().__init__(nome, email, cpf)
        self.__senha = senha

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_senha(self, senha):
        self.__senha = senha

    
    def admin_dic(self):
        admin = {
            "Nome": self.__nome,
            "CPF": self.__cpf,
            "Email": self.__email,
            "Senha": self.__senha
        }
        return admin
    
    def cadastro_admin(self, adm_registrar):
        #adm_registrar = adm_registrar.admin_dic()
        dados_json = os.path.join(os.path.dirname(__file__), 'data', 'admins.json')

        try:
            if os.path.exists(dados_json) and os.path.getsize(dados_json) > 0:
                with open(dados_json, "r", encoding="utf-8") as arquivo:
                    dados_json_exist = json.load(dados_json)
            else:
                dados_json_exist = []
        except json.JSONDecodeError:
            print("Arquivo JSON mal formatado. Iniciando com uma lista vazia.")
            dados_json_exist = []
        except Exception as e:
            print(f"Error: {e}")

        dados_json_exist.append(adm_registrar)

        try:
            with open(dados_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados_json_exist, dados_json, indent=4)
            print("cadastrado com sucesso")
        except Exception as e:
            print(f"ERROR: {e}")