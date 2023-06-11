numeros = []
repetido = "Sem numero repetido!"

while True:
    numero = int(input("Digite um número (-1 para sair): "))
    if numero == -1:
        break
    numeros.append(numero)

for elemento in numeros:
    if numeros.count(elemento) > 1:
        repetido = "Com numero repetido!"
        break
    
print(f"lista: {numeros}")
print(repetido)