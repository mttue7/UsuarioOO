from tinydb import TinyDB, Query

# Inicializa os bancos de dados
db_alunos = TinyDB('alunos.json')
db_cursos = TinyDB('cursos.json')

# Define a classe Aluno
class Aluno:
    def __init__(self, nome, idade, matricula, curso_id):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.curso_id = curso_id

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Curso ID: {self.curso_id}"

# Função para adicionar um novo aluno ao banco de dados
def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matricula = input("Digite a matrícula do aluno: ")

    # Verifica se a matrícula já está em uso
    if db_alunos.search(Query().matricula == matricula):
        print(f"A matrícula '{matricula}' já está em uso.")
        return
    
    curso_id = input("Digite o ID do curso que o aluno está matriculado: ")
    
    # Verifica se o curso existe no banco de dados de cursos
    if not db_cursos.contains(doc_id=int(curso_id)):
        print("Curso não encontrado.")
        return
    
    aluno = Aluno(nome, idade, matricula, curso_id)
    db_alunos.insert({'nome': aluno.nome, 'idade': aluno.idade, 'matricula': aluno.matricula, 'curso_id': aluno.curso_id})
    print(f"Aluno '{nome}' adicionado com sucesso.")


   # Função para adicionar um curso a um aluno existente
def adicionar_curso_para_aluno_existente():
    matricula_aluno = input("Digite a matrícula do aluno: ")
    
   # Verifica se o aluno existe no banco de dados de alunos
    aluno_existente = db_alunos.search(Query().matricula == matricula_aluno)
    if not aluno_existente:
        print("Aluno não encontrado.")
        return
    
    # Verifica se o aluno já está matriculado em um curso
    if 'curso_id' in aluno_existente[0]:
        print("O aluno já está matriculado em um curso.")
        return
    

    curso_id = input("Digite o ID do curso que deseja adicionar ao aluno: ")
    
    # Verifica se o curso existe no banco de dados de cursos
    if not db_cursos.contains(doc_id=int(curso_id)):
        print("Curso não encontrado.")
        return
    
    # Atualiza o aluno existente para adicionar o novo curso
    db_alunos.update({'curso_id': curso_id}, Query().matricula == matricula_aluno)
    print(f"Curso adicionado com sucesso para o aluno com matrícula '{matricula_aluno}'.")

    # Atualiza o aluno existente para adicionar o novo curso
    db_alunos.update({'curso_id': curso_id}, Query().matricula == matricula_aluno)
    print(f"Curso adicionado com sucesso para o aluno com matrícula '{matricula_aluno}'.")


# Função para listar todos os alunos no banco de dados
def listar_alunos():
    alunos = db_alunos.all()
    print("\nTodos os alunos:")
    for aluno in alunos:
        if 'curso_id' in aluno:
            curso = db_cursos.get(doc_id=int(aluno['curso_id']))
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}, Curso: {curso['nome_curso']}")
        else:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}, Curso: Não informado")
        print('---------------')

# Função para listar todos os cursos
def listar_cursos():
    cursos = db_cursos.all()
    if cursos:
        print("\nCursos disponíveis:")
        for curso in cursos:
            print(f"ID: {curso.doc_id}, Nome: {curso['nome_curso']}")
    else:
        print("Não há cursos disponíveis.")


# Função para buscar um aluno pelo número de matrícula
def buscar_aluno_por_matricula():
    matricula_busca = input("Digite a matrícula do aluno que deseja buscar: ")
    
    # Realiza a busca no banco de dados de alunos pelo número de matrícula
    MatriculaQuery = Query()
    aluno_encontrado = db_alunos.search(MatriculaQuery.matricula == matricula_busca)
    
    # Verifica se o aluno foi encontrado e imprime suas informações
    if aluno_encontrado:
        curso = db_cursos.get(doc_id=int(aluno_encontrado[0]['curso_id']))
        print(f"Nome: {aluno_encontrado[0]['nome']}, Idade: {aluno_encontrado[0]['idade']}, Matrícula: {aluno_encontrado[0]['matricula']}, Curso: {curso['nome_curso']}")
    else:
        print("Aluno não encontrado.")

# Função para remover um aluno pelo número de matrícula
def remover_aluno_por_matricula():
    matricula_remover = input("Digite a matrícula do aluno que deseja remover: ")
    
    # Realiza a busca no banco de dados de alunos pelo número de matrícula
    MatriculaQuery = Query()
    aluno_encontrado = db_alunos.search(MatriculaQuery.matricula == matricula_remover)
    
    # Verifica se o aluno foi encontrado e remove-o do banco de dados
    if aluno_encontrado:
        db_alunos.remove(MatriculaQuery.matricula == matricula_remover)
        print("Aluno removido com sucesso.")
    else:
        print("Aluno não encontrado.")

# Função para adicionar um novo curso ao banco de dados
def adicionar_curso():
    nome_curso = input("Digite o nome do curso: ")
    descricao = input("Digite a descrição do curso: ")
    
    # Verifica se o curso já existe no banco de dados de cursos
    if db_cursos.contains(Query().nome_curso == nome_curso):
        print("Curso já existente.")
        return
    
    # Insere o novo curso no banco de dados de cursos
    curso_id = db_cursos.insert({'nome_curso': nome_curso, 'descricao': descricao})
    print(f"Curso '{nome_curso}' adicionado com sucesso. ID do curso: {curso_id}")

# Loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno por matrícula")
    print("4. Remover aluno por matrícula")
    print("5. Adicionar curso")
    print("6. Adicionar curso para aluno existente")
    print("7. Listar cursos")
    print("8. Sair")

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
        adicionar_curso()
    elif opcao == '6':
        adicionar_curso_para_aluno_existente()
    elif opcao == '7':
        listar_cursos()
    elif opcao == '8':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
