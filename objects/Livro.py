class Livro:
    def __init__(self, titulo, autor, genero, descricao, edicao):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__descricao = descricao
        self.__edicao = edicao
        self.__status_aluguel = False

    def alugar(self):
        if self.__status_aluguel:
            return print("Livro alugado!!!!")
        else:
            self.__status_aluguel = True
            return print("Alugado com sucesso!!!!")
        
    def devolver(self):
        if self.__status_aluguel:
            self.__status_aluguel = False
            return print("Devolvido!!")
        else:
            return print("Comando inválido")
        
    def set_titulo(self, novo_nome):
        self.__titulo = novo_nome

    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    def set_genero(self, novo_genero):
        self.__genero = novo_genero

    def set_edicao(self, nova_edicao):
        self.__edicao = nova_edicao

    def set_descricao(self, nova_descricao):
        self.__descricao = nova_descricao

        
    def detalhes(self):
        print(f'Título: {self.__titulo}\nAutor: {self.__autor}\nGenero: {self.__genero}\nEdição: {self.__edicao}ª\nDescrição: {self.__descricao}')
  