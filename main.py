from objects.Usuario import Usuario
from objects.Livro import Livro
from objects.Pessoa import Pessoa
from objects.Admin import Admin
from tools.Registros import Registros

# livro1 = Livro("livro1", "Eu", "Ação", "Um livro de ação", "4", 20)
# livro2 = Livro("livro2", "Tu", "Aventura", "Um livro de aventura", "4", 2)
# usuario1 = Usuario("fulano", "exemplo@email.com", "123456789000", "123456789")



# livro1.detalhes()
# usuario1.alugando(livro1, 4)
# livro1.detalhes()
# usuario1.devolve(livro1, 4)
# livro1.detalhes()

admin_1 = Admin("Fulano", "asdfghjkl", "12345678900", "1234")

Registros.cadastro_admin(admin_1)



