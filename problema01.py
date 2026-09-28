entrada = input("Digite sua idade: ")

if entrada.strip() == "":
    print("Entrada inválida: a idade não pode ficar vazia.")
else:
    try:
        idade = int(entrada)

        if idade <= 0:
            print("Entrada inválida: a idade deve ser maior que zero.")
        else:
            print(f"Idade válida: {idade} anos.")

    except ValueError:
        print("Entrada inválida: digite apenas um número inteiro.")