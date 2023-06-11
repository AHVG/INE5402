numero_pessoas = int(input())

pessoas = {}
for pessoa in range(numero_pessoas):
    informacoes = input().split()
    pessoas[informacoes[0]] = informacoes[1:4]

print(pessoas)

rodando = True
while rodando:
    informacoes = input().split()
    
    if informacoes[1] in pessoas[informacoes[0]]:
        print("Uhul! Seu amigo secreto vai adorar o/")
    else:
        print("Tente novamente!")
    
    while True:
        continuar = input("Quer continuar? ").upper()
        if continuar == "NÃO" or continuar == "NAO" or continuar == "N":
            rodando = False
            break
        elif continuar == "SIM" or continuar == "S":
            break
        else:
            print("Não entendi. Tente novamente!")
        
