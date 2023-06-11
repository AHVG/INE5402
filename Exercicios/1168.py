numero_de_leds = "6255456376"

for teste in range(int(input())):
    entrada = input()
    leds_totais = 0
    for digito in entrada:
        leds_totais += int(numero_de_leds[int(digito)])
    print(f"{leds_totais} leds")


"""import time

NUMERO_DE_LEDS = (6,2,5,5,4,5,6,3,7,6)

def versao_conversao(numero):
    leds_totais = 0
    for digito in numero:
        leds_totais += NUMERO_DE_LEDS[int(digito)]
    return leds_totais
    
    
def versao_if(numero):
    leds_totais = 0
    for digito in numero:
        if digito == '0':
            leds_totais += 6
        elif digito == '1':
            leds_totais += 2
        elif digito == '2':
            leds_totais += 5
        elif digito == '3':
            leds_totais += 5
        elif digito == '4':
            leds_totais += 4
        elif digito == '5':
            leds_totais += 5
        elif digito == '6':
            leds_totais += 6
        elif digito == '7':
            leds_totais += 3
        elif digito == '8':
            leds_totais += 7
        else:
            leds_totais += 6
    return leds_totais
    
    
vitorias_com_conversao = 0
vitorias_sem_conversao = 0
contagem = 0
for numero in range(1, 1001):
    numero = str(numero)

    start = time.perf_counter()
    resultado_co = versao_if(numero)
    end = time.perf_counter()
    tempo_sem_conversao = end - start
    
    start = time.perf_counter()
    resultado_if = versao_conversao(numero)
    end = time.perf_counter()
    tempo_com_conversao = end - start

    if tempo_com_conversao >= tempo_sem_conversao:
        vitorias_sem_conversao += 1
    else:
        vitorias_com_conversao += 1
        
    if resultado_if == resultado_co:
        contagem += 1
        
print(f"Vitorias com: {vitorias_com_conversao}")
vitorias_com_conversao /= 10
print(f"Vitorias com: {vitorias_com_conversao} %")
print()
print(f"Vitorias sem: {vitorias_sem_conversao}")
vitorias_sem_conversao /= 10
print(f"Vitorias sem: {vitorias_sem_conversao} %")
print()
print(f"Contagem de igualdade: {contagem}")
"""
