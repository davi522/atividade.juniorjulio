idade = int(input("Digite a idade: "))
curso = input("Digite o curso: ")
ano = int(input("Digite o ano: "))

if idade <= 0:
    print("Cadastro inválido: idade inválida.")
elif curso.strip() == "":
    print("Cadastro inválido: o curso não pode ficar vazio.")
elif ano < 1:
    print("Cadastro inválido: ano inválido.")
else:
    print("Cadastro realizado com sucesso!")