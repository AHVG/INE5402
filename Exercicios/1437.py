NUMERO_DE_DIRECOES = 4
FACES = 'NLSO'

while True:
    
    quantidade_de_comandos = int(input())
    if quantidade_de_comandos < 1:
        break
    
    comandos = input()
    face = 0
    for i in range(0,quantidade_de_comandos):
        comando = comandos[i]
        if comando in 'Dd':
            face += 1
        elif comando in 'Ee':
            face -= 1
        
        if face < 0:
            face = NUMERO_DE_DIRECOES + face
        elif face >= NUMERO_DE_DIRECOES:
            face = face - NUMERO_DE_DIRECOES

    print(FACES[face])
    
