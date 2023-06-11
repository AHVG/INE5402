def restricao_quantidade_numeros(quantidade):
    if quantidade < 1 or 10**5 <= quantidade:
        return 0
    return 1
    
def restricao_valor_numeros(numeros):
    for numero in numeros:
        if numero < 0 or 10**12 < numero:
            return 0
    return 1

while True:
    quantidade = int(input())
    if not restricao_quantidade_numeros(quantidade):
        break
        
    numeros = [int(x) for x in input().split()]
    numeros.sort()
    
    if not restricao_valor_numeros(numeros):
        break
    
    for indice in range(0,quantidade - 1, 2):
        if numeros[0] == numeros[1]:
            del numeros[0:2]
        else:
            break
    print(numeros[0])