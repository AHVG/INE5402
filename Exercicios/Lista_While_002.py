import random
"""
Nome: Augusto de Hollanda Vieira Guerner
Disciplina: Programação Orientada a Objeto

"""

tentativas = 0
chute = -1
numero_gerado = random.randrange(0, 11)

print(10*"=" + " Jogo da advinhação " + 10*"=")
print("\nAdvinhe o número de 0 a 10!")
while True:
    tentativas += 1
    print()
    chute = int(input("Digite um número: "))
    if chute == numero_gerado:
        print("Você acertou!")
        print("Número de tentativas: {}".format(tentativas))
        print()
        break
    elif chute < 1 or 10 < chute:
        print("Digite um número no intervalo (0, 10)")
    else:
        print("Você errou!")
        print("Tente mais uma vez!")
        
print(13*"=" + " Fim do jogo " + 14*"=")