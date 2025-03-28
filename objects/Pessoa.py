class Pessoa:
    def __init__(self, nome, email, cpf):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_cpf(self):
        return self.__cpf
    
        