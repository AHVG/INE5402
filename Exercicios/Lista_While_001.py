"""
Nome: Augusto de Hollanda Vieira Guerner
Disciplina: Programação Orientada a Objeto

"""


while True:
    print("1. Masculino [M]\n2. Feminino [F]\n")
    sexo = input("Digite seu Sexo: ")    
    sexo = sexo.upper()
    if sexo[0] == 'M' or sexo[0] == 'F':
        break
    else:
        print("Entrada inválida!\nDigite novamente!\n")

