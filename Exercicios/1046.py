TEMPO_MAXIMO_DE_JOGO = 24

hora_inicial, hora_final = [int(x) for x in input().split()]

tempo_de_jogo = 0

if hora_final <= hora_inicial:
    hora_final += TEMPO_MAXIMO_DE_JOGO

tempo_de_jogo = hora_final - hora_inicial

print("O JOGO DUROU {} HORA(S)".format(tempo_de_jogo))
    

