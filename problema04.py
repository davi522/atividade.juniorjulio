entrada = input("Digite o preço do produto: ")

try:
    preco = float(entrada.strip())
    quantidade = int(input("Digite a quantidade: "))

    total = preco * quantidade

    print("Valor total:", total)

except ValueError:
    print("Erro: digite apenas um valor numérico válido.")