def somar_elementos(matriz):
    soma = 0
    for coluna in range(12):
        for linha in  range(12 - coluna - 1):
            soma += matriz[linha + coluna + 1][coluna]
    return soma

def media_elementos(matriz):
    media = somar_elementos(matriz)/66
    return media

def entrar_com_elementos(matriz):
    for linha in range(12):
        for coluna in range(12):
            #matriz[linha][coluna] = int(input(f"Entre com o elemento{linha}x{coluna}: "))
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
    """
    operacao = input("Operacao: [M media ou S soma]")
    while operacao[0].upper() not in "MS":
        print("Operacao inválida!")
    return operacao[0].upper()
    """

         
matriz = criar_matriz(12,12)
operacao = obter_operacao()
entrar_com_elementos(matriz)
if operacao == "S":
    soma = somar_elementos(matriz)
    print(f"{soma:.1f}")
else:
    media = media_elementos(matriz)
    print(f"{media:.1f}")



