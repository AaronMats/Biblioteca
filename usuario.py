from pessoa import Pessoa

class usuario(Pessoa):
    def __init__(self, nome, email, cpf, senha, telefone, endereco):
        super().__init__(nome, email, cpf, senha)
        self.__telefone = telefone
        self.__endereco = endereco
        self.__alugados = []