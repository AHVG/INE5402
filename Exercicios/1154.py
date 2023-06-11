
def calcular_media(soma, numero_de_termos):
    media = soma / numero_de_termos
    print("{:.2f}".format(media))

quantidade_de_entradas = 0
soma_das_idades = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    soma_das_idades += idade
    quantidade_de_entradas += 1
calcular_media(soma_das_idades, quantidade_de_entradas)


    
    