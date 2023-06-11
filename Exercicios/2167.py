def restricao_quantidade_medidas(testes):
    if testes <= 1 or 100 < testes:
        return 0
    return 1

def restricao_valores_medidas(medidas):
    for medida in medidas:
        if medida < 0 or 10000 < medida:
            return 0
    return 1

testes = int(input())
medidas = [int(x) for x in input().split()]

if restricao_quantidade_medidas(testes) and restricao_valores_medidas(medidas):
    for indice in range(1, testes):
        if medidas[indice] < medidas[indice - 1]:
            break
    print(indice + 1)
