NUMERO_DE_ENTRADAS = 10
numero_de_pares = 0
numero_de_impares = 0

def par(numero):
    if numero%2 == 0:
        return True
    return False

for i in range(1, NUMERO_DE_ENTRADAS + 1):
    numero = int(input(f"Número {i}: "))
    if par(numero):
        print("Par")
        numero_de_pares += 1
    else:
        print("Ímpar")
        numero_de_impares += 1
        
print(f"Número de pares: {numero_de_pares}")
print(f"Número de ímpares: {numero_de_impares}")