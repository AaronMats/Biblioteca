from Pessoa import Pessoa
from Livro import Livro
class Usuario(Pessoa):
    def __init__(self, nome, email, cpf, telefone):
        super().__init__(nome, email, cpf)
        self.__telefone = telefone
        self.__alugados = list()
        self.__quantidade = list()

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def alugando(self, livro, quantidade):
        livros = livro.get_quantidade() 
        if quantidade > 0 and quantidade <= livros:
            livro.alugar(quantidade)
            self.__alugados.append(livro)
            self.__quantidade.append(quantidade)
            return print(f"O livro {livro.get_titulo()} foi alugado com sucesso!!")
        else:
            return print("Valor inválido")
        
        
    def devolvendo(self, ind):
        lista = len(self.__alugados)
        if lista < ind:
            del self.__alugados[ind]
            del self.__quantidade[ind]
            return print("Devolvido com sucesso")
        else:
            return print("Operação inválida")



    