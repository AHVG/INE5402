numeros = []

while True:
    numero = int(input("Digite um número (-1 para sair): "))
    if numero == -1:
        break
    numeros.append(numero)
k = int(input())

print(numeros)
for i in range(len(numeros)):
    numeros[i] *= k
print(numeros)