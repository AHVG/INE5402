def encontrar_quadrante(X, Y):
    quadrante = "nenhum"
    if X > 0 and Y > 0:
        quadrante = "primeiro"
    elif X < 0 and Y > 0:
        quadrante = "segundo"
    elif X < 0 and Y < 0:
        quadrante = "terceiro"
    elif X > 0 and Y < 0:
        quadrante = "quarto"
    print(quadrante)

while True:
    x, y = [int(z) for z in input().split()]
    if x == 0 or y == 0:
        break
    encontrar_quadrante(x,y)