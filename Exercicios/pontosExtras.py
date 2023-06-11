for i in range(int(input())):
    provas,alunos = [int(x) for x in input().split()]
    for j in range(alunos):
        notas = [float(x) for x in input().split()]
        notas.sort()
        media = sum(notas)/provas
               
        if media >= 7.0:
            print(f"{notas[provas-1]:.2f}")
        elif media >= 4.0:
            for indice in range(provas, 0, -1):
                if 7.0 > notas[indice - 1] >= 4.0 and notas[indice - 1] > media:
                    print(f"{notas[indice - 1]:.2f}")
                    break
            else:
                print(f"{media:.2f}")
        else:
            print(f"{media:.2f}")
    