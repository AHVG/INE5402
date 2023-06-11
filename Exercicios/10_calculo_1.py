"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""

nome_do_aluno_com_maior_media = ""
maior_media = 0
soma_das_medias = 0
for aluno in range(1, 6):
    nome = input("Insira o nome do aluno {} : ".format(aluno))
    media = float(input("Insira a média do aluno {}: ".format(aluno)))
    if media < 2.75:
        print("{} reprovado".format(nome))
    elif media < 5.75:
        print("{} em recuperação".format(nome))
    else:
        print("{} aprovado".format(nome))
    if maior_media < media:
        maior_media = media
        nome_do_aluno_com_maior_media = nome
        
print("O aluno {} foi o melhor dentre todos com a média de {}.".format(nome_do_aluno_com_maior_media, maior_media))
        