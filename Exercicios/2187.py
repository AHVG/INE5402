I = 50
J = 10
K = 5
L = 1

teste = 1
while True:
    valor = int(input())
    if valor <= 0:
        break
    quantidade_de_i = 0
    quantidade_de_j = 0
    quantidade_de_k = 0
    quantidade_de_l = 0
    print(f"Teste {teste}")
    while valor > 0:
        if valor >= I:
            valor -= I
            quantidade_de_i += 1

        elif valor >= J:
            valor -= J
            quantidade_de_j += 1

        elif valor >= K:
            valor -= K
            quantidade_de_k += 1
        
        elif valor >= L:
            valor -= L
            quantidade_de_l += 1
    print(f"{quantidade_de_i}", end=" ")
    print(f"{quantidade_de_j}", end=" ")
    print(f"{quantidade_de_k}", end=" ")
    print(f"{quantidade_de_l}")
    teste += 1
    

