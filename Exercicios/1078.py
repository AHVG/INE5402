
print(10*"=" + " Calculadora de tabuada " + 10*"=")
tabuada = int(input("\nTabuada: "))
contador = 1
while True:
    print("{:<5} x {:5} = {:10}".format(contador, tabuada, tabuada*contador))
    contador += 1
    if contador >= 11:
        print()
        break

print(10*"=" + " Fim do programa " + 10*"=")


