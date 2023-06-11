"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""

numero_1 = int(input("Insira o primeiro número: "))
numero_2 = int(input("Insira o segundo número : "))

if numero_1 > numero_2:
    aux = numero_1
    numero_1 = numero_2
    numero_2 = aux

soma = 0
print("{", end='')
for numero_do_intervalo in range(numero_1, numero_2 + 1):
    if numero_do_intervalo != numero_2:
        print("{}, ".format(numero_do_intervalo), end='')
    else:
        print("{}".format(numero_do_intervalo), end='')
    soma += numero_do_intervalo
print("}")
print("Soma dos número do intervalo: {}".format(soma))
