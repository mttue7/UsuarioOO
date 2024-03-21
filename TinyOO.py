from tinydb import TinyDB, Query

# Inicializa o banco de dados
db = TinyDB('alunos.json')

# Define a classe Aluno
class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}"

# Função para adicionar um novo aluno ao banco de dados
def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matricula = input("Digite a matrícula do aluno: ")
    
    # Verifica se a matrícula já está em uso
    MatriculaQuery = Query()
    aluno_existente = db.search(MatriculaQuery.matricula == matricula)
    if aluno_existente:
        print(f"A matrícula '{matricula}' já está em uso.")
        return
    
    aluno = Aluno(nome, idade, matricula)
    db.insert({'nome': aluno.nome, 'idade': aluno.idade, 'matricula': aluno.matricula})
    print(f"Aluno '{nome}' adicionado com sucesso.")


# Função para listar todos os alunos no banco de dados
def listar_alunos():
    alunos = db.all()
    print("\nTodos os alunos:")
    for aluno in alunos:
        print(Aluno(aluno['nome'], aluno['idade'], aluno['matricula']))
        print('---------------')

# Função para buscar um aluno pelo nome
# Função para buscar um aluno pelo número de matrícula
def buscar_aluno_por_matricula():
    matricula_busca = input("Digite a matrícula do aluno que deseja buscar: ")
    
    # Realiza a busca no banco de dados pelo número de matrícula
    MatriculaQuery = Query()
    aluno_encontrado = db.search(MatriculaQuery.matricula == matricula_busca)
    
    # Verifica se o aluno foi encontrado e imprime suas informações
    if aluno_encontrado:
        print(Aluno(aluno_encontrado[0]['nome'], aluno_encontrado[0]['idade'], aluno_encontrado[0]['matricula']))
    else:
        print("Aluno não encontrado.")

# Função para remover um aluno pelo número de matrícula
def remover_aluno_por_matricula():
    matricula_remover = input("Digite a matrícula do aluno que deseja remover: ")
    
    # Realiza a busca no banco de dados pelo número de matrícula
    MatriculaQuery = Query()
    aluno_encontrado = db.search(MatriculaQuery.matricula == matricula_remover)
    
    # Verifica se o aluno foi encontrado e remove-o do banco de dados
    if aluno_encontrado:
        db.remove(MatriculaQuery.matricula == matricula_remover)
        print("Aluno removido com sucesso.")
    else:
        print("Aluno não encontrado.")


# Loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno por nome")
    print("4. Remover aluno por nome")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        buscar_aluno_por_matricula()
    elif opcao == '4':
        remover_aluno_por_matricula()
    elif opcao == '5':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
