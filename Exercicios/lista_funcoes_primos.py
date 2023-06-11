
def primo(numero):
    if numero == 1 or 0:
        return False
    if numero == 2:
        return True
    for divisor in range(2, int((numero + 1)/2) + 1):
        if numero % divisor == 0:
            return False
    return True

def numero_de_primos_ate(numero):
    quantidade_de_primos = 0
    for i in range(1, numero + 1):
        if primo(i):
            quantidade_de_primos += 1
    return quantidade_de_primos

x, y = [int(valor) for valor in input().split()]
if x > y:
    aux = x
    x = y
    y = aux
numero_de_primos_no_intervalo = numero_de_primos_ate(y) - numero_de_primos_ate(x - 1)
print(f"{numero_de_primos_no_intervalo}")


