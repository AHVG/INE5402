
def obterListaDosVencedores(lista, numero_de_jogos):
    numero_do_jogo = 0
    while True:
        if numero_do_jogo >= numero_de_jogos:
            break
        esquerda, direita = [int(pontuacao) for pontuacao in input().split()]
        indice = numero_do_jogo
        if esquerda > direita:
            del lista[indice + 1]
        else:
            del lista[indice]
        numero_do_jogo += 1
    return lista

times = ["A","B","C","D",
         "E","F","G","H",
         "I","J","K","L",
         "M","N","O","P",]
for x in range(3, -1, -1):
    times = obterListaDosVencedores(times[:], 2**x)
print(times)

    
