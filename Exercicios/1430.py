duracao_notas = {
                    'W': 64,
                    'H': 32,
                    'Q': 16,
                    'E': 8,
                    'S': 4,
                    'T': 2,
                    'X': 1
                }

while True:
    partitura = input()
    if partitura == "*":
        break
    partitura = partitura.split("/")
    
    compassos_corretos = 0
    for compasso in partitura:
        duracao = 0
        for nota in compasso:
            duracao += duracao_notas[nota]
        if duracao == 64:
            compassos_corretos += 1
    
    print(compassos_corretos)
            