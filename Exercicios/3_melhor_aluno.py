"""

Nome: Augusto de Hollanda Vieira Guerner
Curso: Ciência da Computação
Disciplina: Programação Orientada a Objeto I
Data: 27/04/2022

"""

nome_do_melhor_aluno = ""
media_geral_do_melhor_aluno = -1.0
mensalidade_do_melhor_aluno = 0.0

for i in range(1, 6):
    nome = input("Entre com o nome do aluno {}: ".format(i))
    media_geral = float(input("Entre com a media geral do aluno {}: ".format(i)))
    mensalidade = float(input("Entre com a mensalidade do aluno {}: ".format(i)))
    if media_geral > media_geral_do_melhor_aluno:
        media_geral_do_melhor_aluno = media_geral
        nome_do_melhor_aluno = nome
        mensalidade_do_melhor_aluno = mensalidade

print()
print("Informações do aluno com o benefício: ")
print("> Nome: {}".format(nome_do_melhor_aluno))
print("> Média Geral: {}".format(media_geral_do_melhor_aluno))
print("> Mensalidade antes do desconto: {:.2f}".format(mensalidade_do_melhor_aluno))
print("> Mensalidade depois do desconto: {:.2f}".format(mensalidade_do_melhor_aluno * 0.7))

