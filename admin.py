from pessoa import Pessoa

class Admin(Pessoa):
    def __init__(self, nome, email, cpf, senha):
        super().__init__(nome, email, cpf, senha)