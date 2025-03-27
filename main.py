from objects.Usuario import Usuario
from objects.Livro import Livro
from objects.Pessoa import Pessoa


livro1 = Livro("livro1", "Eu", "Ação", "Um livro de ação", "4", 20)
livro2 = Livro("livro2", "Tu", "Aventura", "Um livro de aventura", "4", 2)
usuario1 = Usuario("fulano", "exemplo@email.com", "123456789000", "123456789")



livro1.detalhes()
usuario1.alugando(livro1, 4)
livro1.detalhes()
usuario1.devolve(livro1, 1)
livro1.detalhes()

