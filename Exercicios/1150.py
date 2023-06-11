def obter_quantidade_de_inteiros(X, Z):
    valor_inicial = X
    quantidade = 1
    while valor_inicial < Z:
        X += 1
        valor_inicial += X
        quantidade += 1
    print(quantidade)

X = int(input())
Z = 0
while True:
    Z = int(input())
    if X < Z:
        break

obter_quantidade_de_inteiros(X, Z)
