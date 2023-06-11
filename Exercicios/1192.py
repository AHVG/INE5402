for teste in range(int(input())):
    expressao = input()
    resultado = 0
    operando1 = int(expressao[0])
    operando2 = int(expressao[2])
    if operando1 == operando2:
        resultado = operando2 * operando1
    elif expressao[1].isupper():
        resultado = operando2 - operando1
    else:
        resultado = operando1 + operando2
    print(resultado)