class Livro:
    def __init__(self, titulo_livro, autor_livro, genero_livro, descricao_livro, edicao):
        self.__titulo_livro = titulo_livro
        self.__autor_livro = autor_livro
        self.__genero_livro = genero_livro
        self.__descricao_livro = descricao_livro
        self.__edicao = edicao
    def detalhes_livro(self):
        print(f'Título: {self.__titulo_livro}\nAutor: {self.__autor_livro}\nGenero: {self.__genero_livro}\nEdição: {self.__edicao}ª\nDescrição: {self.__descricao_livro}')
  