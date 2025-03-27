from .Pessoa import Pessoa
from .Livro import Livro
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
        
    def devolve(self, livro, quant):
        if livro in self.__alugados:
            ind = self.__alugados.index(livro)
            alugados = self.__quantidade[ind]
            livro_alugado = self.__quantidade[ind]
            if quant <= alugados and quant > 0:
                del self.__alugados[ind]
                del self.__quantidade[ind]
                livro_alugado.devolver(quant)
                return print("Devolvido com sucesso!")
            else:
                return print("Valor inválido")
        else:
            return print("Livro não encontrado")




livro1 = Livro("livro1", "Eu", "Ação", "Um livro de ação", "4", 20)
livro2 = Livro("livro2", "Tu", "Aventura", "Um livro de aventura", "4", 2)
usuario1 = Usuario("fulano", "exemplo@email.com", "123456789000", "123456789")



livro1.detalhes()
usuario1.alugando(livro1, 4)
livro1.detalhes()
usuario1.devolve(livro1, 4)
livro1.detalhes()