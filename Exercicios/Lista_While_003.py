"""
Nome: Augusto de Hollanda Vieira Guerner
Disciplina: Programação Orientada a Objeto

"""

media = 0
indice = 0
print(10*"=" + " Calculadora de média " + 10*"=")
print("\nDigite SAIR para calcular e sair")
print("Digite um número para somar\n")
while True:
    numero = input("Número {}: ".format(indice + 1))
    
    if numero.isnumeric():
        media += int(numero)
        indice += 1
    elif numero[0].upper() == 'S':
        break
    else:
        print("Entrada inválida!")

print()
if indice == 0:
    print("Sem números para calcular a média!")
else:
    print("Média: {:.2f}\n".format(media/indice))
print(12*"=" + " Fim do programa " + 13*"=")