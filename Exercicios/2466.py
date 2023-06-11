def criar_linha(colunas):
    linha = [*range(colunas)]
    return linha[:]

triangulo = []
bolas_iniciais = int(input())
linha_inicial = [int(x) for x in input().split()]
triangulo.append(linha_inicial[:])
for linha in range(1, bolas_iniciais):
    
    triangulo.append(criar_linha(bolas_iniciais - linha))
    
    for coluna in range(bolas_iniciais - linha):
        if triangulo[linha - 1][coluna] + triangulo[linha - 1][coluna + 1] == 0:
            triangulo[linha][coluna] = -1
        else:
            triangulo[linha][coluna] = 1

print(triangulo)
if triangulo[bolas_iniciais - 1][0] == 1:
    print("preta")
else:
    print("branca")
    