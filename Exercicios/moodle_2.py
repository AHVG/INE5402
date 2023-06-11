
media = 0
for indice in range(1, 4):
    nota = float(input('Nota ' + str(indice) + ': '))
    media += nota
media = media / 3.0

if media < 5:
    print('Reprovado')
elif media < 7:
    print('Em recuperação')
else:
    print('Aprovado')
