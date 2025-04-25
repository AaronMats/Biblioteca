class Livro:
    def __init__(self, titulo, autor, genero, descricao, edicao, quantidade):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__descricao = descricao
        self.__edicao = edicao
        self.__quantidade = int(quantidade)

    def alugar(self, quantidade_alugar):
        if quantidade_alugar > 0 and quantidade_alugar <= self.__quantidade:
            alugados = self.__quantidade - quantidade_alugar
            self.__quantidade = alugados
            #print("Livro(s) alugados com sucesso")
        else:
            print("Valor inválido")
        
        
    def devolver(self, quantidade_devolver):
        if quantidade_devolver > 0:
            alugados = quantidade_devolver + self.__quantidade
            self.__quantidade = alugados
            return print("Devolvido!!")
        else:
            return print("Valor inválido")
        
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

    def set_quantidade(self, quantidade):
        self.__quantidade = int(quantidade)

    def livro_dic(self):
        livro = {"Nome": self.__titulo,
                "Autor(a)": self.__autor,
                "Genero": self.__genero,
                "Edição": self.__edicao,
                "Quantidade": self.__quantidade,
                "Descrição": self.__descricao
                }
        return livro

    def get_quantidade(self):
        return self.__quantidade
    
    def get_titulo(self):
        return self.__titulo

    def detalhes(self):
        print(f'Título: {self.__titulo}\nAutor: {self.__autor}\nGenero: {self.__genero}\nEdição: {self.__edicao}ª\nQuantidade: {self.__quantidade}\nDescrição: {self.__descricao}')
        