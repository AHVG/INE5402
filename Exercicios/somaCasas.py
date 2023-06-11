def obter_numeros(lista, soma):
    for j in range(len(casas)):
        for k in range(len(casas)):
            if(j != k):
                if(soma == casas[j] + casas[k]):
                    print(casas[j],casas[k])
                    return

casas = []
for i in range(int(input())):
    casas.append(int(input()))
soma = int(input())
obter_numeros(casas, soma)
            