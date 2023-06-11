def restricao_quantidade_pecas(quantidade):
    if quantidade < 2 or 1000 < quantidade:
        return 0
    return 1

quantidade_pecas = int(input())
if restricao_quantidade_pecas(quantidade_pecas):
    pecas = [int(x) for x in input().split()]
    for numero_peca in range(1, quantidade_pecas + 1):
        if numero_peca not in pecas:
            print(numero_peca)
            break
