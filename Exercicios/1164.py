def eh_perfeito(numero):
    divisores = []
    for divisor in range(1,int(numero/2) + 1):
        if numero % divisor == 0:
            divisores.append(divisor)
    if sum(divisores) == numero:
        return True
    return False

for teste in range(int(input())):
    numero = int(input())
    if eh_perfeito(numero):
        print(f"{numero} eh perfeito")
    else:
        print(f"{numero} nao eh perfeito")