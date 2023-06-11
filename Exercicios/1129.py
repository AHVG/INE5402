def analisar_resposta(resposta):
    for indice, valor in enumerate(resposta):
        if valor <= 127:
            resposta[indice] = 1
        else:
            resposta[indice] = 0
    alternativas = ("A","B","C","D","E")
    if resposta.count(0) == 4:
        return str(alternativas[resposta.index(1)])
    else:
        return "*"

while True:
    numero_de_testes = int(input())
    if numero_de_testes > 0:
        for teste in range(numero_de_testes):
            resposta = []
            [resposta.append(int(x)) for x in input().split()]
            print(analisar_resposta(resposta))
    else:
        break
