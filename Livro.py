class Livro:
    def __init__(self, titulo_livro, autor_livro, genero_livro, descricao_livro):
        self.titulo_livro = titulo_livro
        self.autor_livro = autor_livro
        self.genero_livro = genero_livro
        self.descricao_livro = descricao_livro
    def detalhes_livro(self):
        print(f'Título: {self.titulo_livro}\nAutor: {self.autor_livro}\nGenero: {self.genero_livro}\nDescrição: {self.descricao_livro}')



livro = Livro('duna', 'fulano','sci fi', 'Deserto')
livro.detalhes_livro()