"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""
tabuada = int(input("Qual tabuada deseja calcular? "))

if tabuada > 10 or tabuada < 1:
    print("Valor inválido!")
else:
    print("Tabuada de {}".format(tabuada))
    for multiplicador in range(1, 11):
        print("{:2} x {:2} = {}".format(tabuada, multiplicador, tabuada * multiplicador))
    

