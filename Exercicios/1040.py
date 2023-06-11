import math

N1, N2, N3, N4 = [float(x) for x in input().split()]

media = (N1 * 2.0 + N2 * 3.0 + N3 * 4.0 + N4 * 1.0) / 10.0
media = int(media * 10)

print("Média: {:.1f}".format(media/10.0))

if 70 <= media:
    print("Aluno aprovado.")
elif media < 50:
    print("Aluno reprovado.")
elif 50 <= media <= 69:
    print("Aluno em exame.")
    nota_exame = float(input())
    media += int(nota_exame * 10)
    media /= 2.0
    print("Nota do exame: {:.1f}".format(nota_exame))
    if 50 <= media:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Média final: {:.1f}".format(media/10.0))

