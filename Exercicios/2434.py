dias_de_interesse, saldo_inicial = [int(x) for x in input().split()]

if 1 <= dias_de_interesse <= 30:
    saldo = saldo_inicial
    menor_saldo = saldo
    for x in range(0, dias_de_interesse):    
        movimentacao = int(input())
        saldo += movimentacao
        if saldo < menor_saldo:
            menor_saldo = saldo
            
print(menor_saldo)
