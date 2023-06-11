HORAS_NO_DIA = 24

def obter_hora_de_chegada(hora_partida, tempo_de_viagem, fuso):
    print((hora_partida + tempo_de_viagem + fuso)%HORAS_NO_DIA)

S, T, F = [int(x) for x in input().split()]
obter_hora_de_chegada(S,T,F)