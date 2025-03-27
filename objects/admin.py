from .Pessoa import Pessoa

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

    