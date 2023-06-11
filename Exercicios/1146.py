x = 0

print(10*"=" + " Calculadora de intervalo " + 10*"=")
while True:
    x = int(input("\nNúmero: "))
    if x == 0:
        print()
        break
    contador = 1
    while contador <= x:
        print(contador, end="")
        if contador != x:
            print(" ", end="")
        contador += 1
    
print(10*"=" + " Fim do programa " + 10*"=")

