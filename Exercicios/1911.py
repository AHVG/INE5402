
while True:
    assinaturas_falsas = 0
    assinaturas = dict()

    N = int(input())
    if N < 1 or 50 < N:
        break
    
    for teste in range(N):
        aluno, assinatura = input().split()
        assinaturas[aluno] = assinatura
        
    M = int(input())
    if M < 0 or N < M:
        break
    
    for teste in range(M):
        aluno, assinatura = input().split()
        diferencas = 0
        indice = 0
        for letra in assinatura:
            if assinaturas[aluno][indice] != letra:
                diferencas += 1
            indice += 1
        if diferencas > 1:
            assinaturas_falsas += 1

    print(assinaturas_falsas)
