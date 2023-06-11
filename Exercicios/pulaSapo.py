pulo,vezes = [int(x) for x in input().split()]
alturas = [int(y) for y in input().split()]
alturaAnt = alturas[0]
mensagem = 'YOU WIN'
for altura in alturas:
    if(alturaAnt + pulo < altura):
        mensagem = 'GAME OVER'
        break
    alturaAnt = altura
print(mensagem)