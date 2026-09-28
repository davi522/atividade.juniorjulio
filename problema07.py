identificador = input("Digite o cpf: ")

if not identificador.isdigit():
    print("Erro: o CPF deve conter apenas números.")
elif len(identificador) != 11:
    print("Erro: o CPF deve possuir 11 dígitos.")
else:
    print("CPF válido!")