"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""

""" SOLUÇÃO 1
numero = int(input("Insira um número inteiro: "))

for divisor in range(2, (numero + 2)//2):
    if numero % divisor == 0:
        print("{} não é primo!".format(numero))
        break
else:
    print("{} é primo!".format(numero))
"""
"""SOLUÇÃO 2"""

numero = int(input("Insira um número inteiro: "))

numero_de_divisores = 0
for divisor in range(1, (numero + 2)//2):
    if numero % divisor == 0:
        numero_de_divisores += 1

if numero_de_divisores > 1:
    print("{:2} não é primo!".format(numero))
else:
    print("{:2} é primo!".format(numero))

