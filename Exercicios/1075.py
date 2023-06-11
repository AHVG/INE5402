RESTO = 2
LIMITE = 10000
numero = int(input("Entre com um número: "))
contador = 0
resultado = 0
if 0 < numero < LIMITE:    
    while resultado < LIMITE:
        print("{}".format(resultado + RESTO))
        contador += 1
        resultado = contador * numero
else:
    print("Entrada inválida!")
