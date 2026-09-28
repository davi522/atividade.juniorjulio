senha_correta = "1234"
tentativas = 3

for tentativa in range(tentativas):
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta, tente novamente.")

else:
    print("Acesso bloqueado. Número máximo de tentativas atingido.")