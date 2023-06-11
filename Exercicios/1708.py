"""

Fórmula:

n * Ta = (n - 1) * Tb
n * Ta = n * Tb - Tb
n * Ta - n * Tb = - Tb
n * (Ta - Tb) = - Tb
n = Tb / (Tb - Ta)

Para o caso de Ta = 5 e Tb = 7:

n = 7 / (7 - 5)
n = 7 / 2
n = 3.5

Para o caso de Ta = 1 e Tb = 2:

n = 1 / (2 - 1)
n = 2 / 1
n = 2

"""

Ta, Tb = [int(x) for x in input().split()]
volta = 1
while volta * (Tb - Ta) < Tb:
    volta += 1
print(volta)
