"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""
numero = int(input("Insira um número inteiro: "))

numero_de_divisores = 0
for divisor in range(1, (numero + 2)//2):
    if numero % divisor == 0:
        numero_de_divisores += 1

if numero_de_divisores > 1:
    print("{:2} não é primo!".format(numero))
    print("Divisores:")
    contador = 1
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:        
            print("{:2}°. {}".format(contador, divisor))
            contador += 1
else:
    print("{:2} é primo!".format(numero))

