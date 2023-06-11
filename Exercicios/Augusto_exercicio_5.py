numeros = []

for i in range(20):
    numeros.append(int(input("Digite um número: "))) 
print(numeros)
numeros = numeros[::-1]
print(numeros)