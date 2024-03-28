class Aluno:
    def __init__(self, nome, numero, idade, turma):
        self.nome = nome
        self.numero = numero
        self.idade = idade
        self.turma = turma

    def obterNome(self):
        return self.nome

    def obterNumero(self):
        return self.numero

    def obterIdade(self):
        return self.idade

    def obterTurma(self):
        return self.turma


alunos = []

while True:
    print("1. Criar aluno")
    print("2. Consultar alunos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Insira o nome do aluno: ")
        numero = input("Insira o número do aluno: ")
        idade = input("Insira a idade do aluno: ")
        turma = input("Insira a turma do aluno: ")
        aluno = Aluno(nome, numero, idade, turma)
        alunos.append(aluno)
    elif opcao == '2':
        for aluno in alunos:
            print(f"Nome: {aluno.obterNome()}, Número: {aluno.obterNumero()}, Idade: {aluno.obterIdade()}, Turma: {aluno.obterTurma()}")
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")