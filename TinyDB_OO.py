from tinydb import TinyDB, Query

# Inicializa o banco de dados
db = TinyDB('usuarios.json')

# Define a classe Usuario
class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"

# Função para adicionar um novo usuário ao banco de dados
def adicionar_usuario(usuario):
    db.insert({'nome': usuario.nome, 'idade': usuario.idade, 'email': usuario.email})

# Função para listar todos os usuários no banco de dados
def listar_usuarios():
    usuarios = db.all()
    for usuario in usuarios:
        print(Usuario(usuario['nome'], usuario['idade'], usuario['email']))
        print('---------------')

# Criando alguns usuários
usuario1 = Usuario('Alice', 25, 'alice@example.com')
usuario2 = Usuario('Bob', 30, 'bob@example.com')

# Adicionando os usuários ao banco de dados
adicionar_usuario(usuario1)
adicionar_usuario(usuario2)

# Listando todos os usuários no banco de dados
print("Usuários no banco de dados:")
listar_usuarios()

# Fechando o banco de dados
db.close()
