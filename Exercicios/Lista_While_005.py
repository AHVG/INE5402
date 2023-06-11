"""
Nome: Augusto de Hollanda Vieira Guerner
Disciplina: Programação Orientada a Objeto

"""

nome_praia_mais_distante = ""
numero_de_praias_entre_15_20 = 0
distancia_media = 0
distancia_maxima = -1
quantidade_de_praias = 0

print(10*"=" + " GPS de probre " + 10*"=")

quantidade_de_praias = int(input("\nDigite o número de praias: "))
contador = quantidade_de_praias
while True:
    if contador <= 0:
        break    
    nome_praia = input("\nDigite o nome da praia: ")
    distancia_praia = int(input("Distância da praia ao centro (km): "))
    
    if distancia_maxima < distancia_praia:
        distancia_maxima = distancia_praia
        nome_praia_mais_distante = nome_praia
    if 15 <= distancia_praia <= 20:
        numero_de_praias_entre_15_20 += 1
    
    distancia_media += distancia_praia/quantidade_de_praias
    contador -= 1

print("\nDistância média: {:.2f}".format(distancia_media))
print("Maior distância: {:.2f}".format(distancia_maxima))
print("Nome da praia mais distante: {}".format(nome_praia_mais_distante))
print("Número de praias entre 15 e 20 km: {}\n".format(numero_de_praias_entre_15_20))

print(9*"=" + " Fim do programa " + 9*"=")