alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]

posicao = int(input("Digite a posição do aluno (1 a 5): "))

if 1 <= posicao <= len(alunos):
    print("Aluno:", alunos[posicao - 1])
else:
    print("Erro: essa posição não existe na lista.")