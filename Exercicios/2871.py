rodando = True
while rodando:
    linhas, colunas = input().split()
    linhas = int(linhas)
    colunas = int(colunas)
    sacas = 0
    litros = 0

    for i in range(linhas):
        linha = [int(x) for x in input().split()]
        litros += sum(linha)

    sacas = litros//60
    litros -= 60*sacas

    print(f"{sacas} saca(s) e {litros} litro(s)")
    while True:
        continuar = input("Quer continuar? ").upper()
        if continuar == "NÃO" or continuar == "NAO" or continuar == "N":
            rodando = False
            break
        elif continuar == "SIM" or continuar == "S":
            break
        else:
            print("Não entendi. Tente novamente!")
        
        
