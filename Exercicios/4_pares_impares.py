
"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""
QUANTIDADE_DE_NUMEROS = 10
quantidade_de_pares = 0

for i in range(0, QUANTIDADE_DE_NUMEROS):
    numero = int(input("Número {:2} - ".format(i + 1)))
    if numero % 2 == 0:
        quantidade_de_pares += 1
print("Quantidade de números:")
print("Pares   - {}".format(quantidade_de_pares))
print("Ímpares - {}".format(QUANTIDADE_DE_NUMEROS - quantidade_de_pares))