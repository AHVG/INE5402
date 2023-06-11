"""

milhas nauticas para km

1 milhas nauticas -> 1.852 km

nós para km por hora

1 nó -> 1.85 km/hora

"""
FATOR_DIST = 1.852
FATOR_VELO = 1.85
DISTANCIA_COSTA_A_AGUAS_INTER = 12.0 * FATOR_DIST

dist, velocidade_f, velocidade_g = [float(x) for x in input().split()]
dist *= FATOR_DIST
velocidade_f *= FATOR_VELO
velocidade_g *= FATOR_VELO

dist_f = dist
dist_g = 0
while True:
    dist_f += velocidade_f
    dist_g += velocidade_g
    if dist_g >= dist_f:
        print("S")
        break
    elif DISTANCIA_COSTA_A_AGUAS_INTER < dist_f:
        print("N")
        break
