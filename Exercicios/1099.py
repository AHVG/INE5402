print(10*"=" + " Soma de ímpares " + 10*"=")
N = int(input("\nQuantidade de casos: "))

while N > 0:
    X, Y = [int(valor) for valor in input("\nEntre com os valores: ").split()]
    if X > Y:
        aux = X
        X = Y
        Y = aux
    X += 1
    soma = 0
    while X < Y:
        if X % 2:
            soma += X
        X += 1
    N -= 1
    print("Soma: {}".format(soma))
print()
print(10*"=" + " Fim do programa " + 10*"=")