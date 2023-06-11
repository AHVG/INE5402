QUANTIDADE_DE_NOTAS = 5
contador = 0

maior_nota = -1
menor_nota = 11
nota = 0
nota_final = 0
while contador < QUANTIDADE_DE_NOTAS:
    nota = float(input())
    
    if nota < menor_nota:
        menor_nota = nota
    elif maior_nota < nota:
        maior_nota = nota
        
    nota_final += nota
    contador += 1
nota_final -= (maior_nota + menor_nota)
print("{:.1f}".format(nota_final))

