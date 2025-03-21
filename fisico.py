from Livro import Livro
class Livro_fisico(Livro):
    def __init__(self, titulo_livro, autor_livro, genero_livro, descricao_livro, edicao):
        super().__init__(titulo_livro, autor_livro, genero_livro, descricao_livro, edicao)
        self.status_aluguel = False


    def alugar(self):
        if self.status_aluguel:
            return print("Livro alugado!!!!")
        else:
            self.status_aluguel = True
            return print("Alugado com sucesso!!!!")
        
    def devolver(self):
        if self.status_aluguel:
            self.status_aluguel = False
            return print("Devolvido!!")
        else:
            return print("Comando inválido")
