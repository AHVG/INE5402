NUMERO_DE_LEITURAS = 6


def calcular_media(soma, numero_de_termos):
    media = soma / numero_de_termos
    print("{:.1f}".format(media))
    
quantidade_de_valores_positivos = 0
soma_valores_positivos = 0

for i in range(0, NUMERO_DE_LEITURAS):
    leitura = float(input())
    if leitura >= 0:
        soma_valores_positivos += leitura
        quantidade_de_valores_positivos += 1

print(f"{quantidade_de_valores_positivos} valores positivos")
calcular_media(soma_valores_positivos, quantidade_de_valores_positivos)


