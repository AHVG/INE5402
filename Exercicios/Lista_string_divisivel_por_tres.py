
while True:
    quantidade_de_algarismo, numero = input().split()
    soma_digitos = 0
    for digito in numero:
        soma_digitos += int(digito)
    print(str(soma_digitos) + " ", end="")
    if int(numero) % 3:
        print("nao")
    else:
        print("sim")
        
    opcao = input("Quer continuar? Sim [S] Não [N]")
    if opcao[0].upper() != 'S':
        break