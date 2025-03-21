from Livro import Livro

class Livro_digital(Livro):
    def __init__(self, titulo_livro, autor_livro, genero_livro, descricao_livro, edicao, formato):
        super().__init__(titulo_livro, autor_livro, genero_livro, descricao_livro, edicao)
        self.formato = formato