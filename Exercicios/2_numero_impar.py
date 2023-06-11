"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""

inicio = 1
final = 50
contador_de_numero_impar = 1
for numero_impar in range(inicio, final + 1, 2):
    print("{:2}° - {:2}".format(contador_de_numero_impar, numero_impar))
    contador_de_numero_impar += 1
