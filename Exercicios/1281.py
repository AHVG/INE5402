def calcular_custo(compras):
    custo = 0
    for fruta in compras:
        custo += compras[fruta]['preco'] * compras[fruta]['quantidade']
    return custo

for teste in range(int(input())):
    compras = {}
    for x in range(int(input())):
        nome, preco = input().split()
        preco = float(preco)
        fruta = {}
        fruta['preco'] = preco
        fruta['quantidade'] = 0
        compras[nome] = fruta.copy()
        
    for x in range(int(input())):
        nome, quantidade = input().split()
        quantidade = int(quantidade)
        compras[nome]['quantidade'] = quantidade

    print(f"R$ {calcular_custo(compras):.2f}")
