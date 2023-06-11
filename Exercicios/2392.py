def entrada_valida(N, M, S):
    if N < 1 or 100 < N or M < 1 or 100 < M:
        return False
    for s in S:
        if s[0] < 1 or N < s[0] or s[1] < 1 or N < s[1]:
            return False
    return True
    
numero_de_pedras, numero_de_sapos = [int(x) for x in input().split()]
pedras = [0 for i in range(numero_de_pedras)]
sapos = []
for i in range(numero_de_sapos):
    ponto_de_partida, passo = [int(x) for x in input().split()]
    info_sapo = []
    info_sapo.append(ponto_de_partida)
    info_sapo.append(passo)
    sapos.append(info_sapo)

if entrada_valida(numero_de_pedras, numero_de_sapos, sapos):
    for sapo in sapos:
        sapo[0] -= 1
        ponto_atual = sapo[0]
        while ponto_atual < numero_de_pedras:
            pedras[ponto_atual] = 1
            ponto_atual += sapo[1]
        ponto_atual = sapo[0]
        while ponto_atual > -1:
            pedras[ponto_atual] = 1
            ponto_atual -= sapo[1]    
    for pedra in pedras:
        print(pedra)
