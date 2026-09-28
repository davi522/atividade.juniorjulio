preco = input("Digite o preço do produto: ")

if preco.strip() == "":
    print("Erro: o preço não foi informado.")
else:
    try:
        preco = float(preco)
        print("Preço do produto:", preco)
    except ValueError:
        print("Erro: digite um preço válido.")