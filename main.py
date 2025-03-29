from objects.Usuario import Usuario
from objects.Livro import Livro
from objects.Pessoa import Pessoa
from objects.Admin import Admin
from tools.Registros import Registros
#from screen.Login import Screen_login
livro1 = Livro("livro1", "Eu", "Ação", "Um livro de ação", "4", 20)
# livro2 = Livro("livro2", "Tu", "Aventura", "Um livro de aventura", "4", 2)
# usuario1 = Usuario("fulano", "exemplo@email.com", "123456789000", "123456789")




Registros.cadastro_admin("nome", "email", "CPF", "senha")



