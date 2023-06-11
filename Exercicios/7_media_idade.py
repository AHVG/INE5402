"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""

numero_de_pessoas = int(input("Insira o número de pessoas: "))

media_da_idade = 0
for i in range(1, numero_de_pessoas + 1):
    idade = int(input("Idade da pessoa {}. ".format(i)))
    media_da_idade += idade
media_da_idade /= numero_de_pessoas
media_da_idade = int(0.5 + media_da_idade) # arredondar para o inteiro mais próximo


if 0 < media_da_idade <= 25:
    print("Turma jovem")
elif media_da_idade <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
    