KM_POR_L = 12.0

tempo_de_viagem_h = int(input())
velocidade_em_km_h = int(input())

litros_necessarios = (velocidade_em_km_h * tempo_de_viagem_h) / (KM_POR_L)

print("{:.3f}".format(litros_necessarios))





