"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""
ANO_INICIAL = 2004
ANO_FINAL = 2100 # Século XXI termina em 2100
contador_de_anos = 1
for ano_bissexto in range(ANO_INICIAL, ANO_FINAL + 1, 4):
    print("{:2}° ano bissexto. {}".format(contador_de_anos, ano_bissexto))
    contador_de_anos += 1