from .Pessoa import Pessoa
from .Livro import Livro
class Usuario(Pessoa):
    def __init__(self, nome, email, cpf, telefone, livros, quantidade):
        super().__init__(nome, email, cpf)
        self.__telefone = telefone
        self.__alugados = livros
        self.__quantidade = quantidade

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
            return f"O livro {livro.get_titulo()} foi alugado com sucesso!!"
        else:
            return "Valor inválido"
        
    def devolve(self, livro, quant):
        if livro in self.__alugados:
            ind = self.__alugados.index(livro)
            quant_alugado = self.__quantidade[ind]
            if quant == quant_alugado:
                del self.__alugados[ind]
                del self.__quantidade[ind]
                livro.devolver(quant)
                return "Todos os livros foram devolvidos!"
            elif quant < quant_alugado and quant > 0:
                sobra = quant_alugado - quant
                self.__alugados.insert(ind, sobra)
                livro.devolver(quant)
                return f"foram devolvidos {quant} livros, ainda faltam {sobra} para devolver"
            else:
                return "Valor inválido"
        else:
            return "Livro não encontrado"

    def usuario_dic(self):
        usuario_dicionario = {
            "Nome": super().get_nome(),
            "CPF": super().get_cpf(),
            "Email": super().get_email(),
            "Telefone": self.__telefone,
            "livros alugados": self.__alugados,
            "quantidade Alugada": self.__quantidade
        }
        return usuario_dicionario