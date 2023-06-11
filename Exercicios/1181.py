def somar_elementos(matriz, linha):
    soma = 0
    for elemento in matriz[linha]:
        soma += elemento
    return soma

def media_elementos(matriz, linha):
    media = somar_elementos(matriz, linha)/12
    return media

def entrar_com_elementos(matriz):
    for linha in range(12):
        for coluna in range(12):
            matriz[linha][coluna] = float(input())
            
def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)
         
def criar_matriz(linha, coluna):
    m = []
    for i in range(linha):
        m.append([])
        [m[i].append(j) for j in range(coluna)]
    return m[:]

def obter_operacao():
    operacao = input()
    return operacao[0].upper()
 

matriz = criar_matriz(12,12)

linha = int(input())
operacao = obter_operacao()
entrar_com_elementos(matriz)

if operacao[0].upper() == "S":
    soma = somar_elementos(matriz, linha)
    print(f"{soma:.1f}")
else:
    media = media_elementos(matriz,linha)
    print(f"{media:.1f}")
