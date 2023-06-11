NUMERO_DE_NOTAS = 3
notas = []

for i in range(NUMERO_DE_NOTAS):
    nota = float(input(f"Nota {i + 1}: "))
    if nota < 0 or 10 < nota:
        nota = float(input(f"Nota inválida!\nDigite novamente: "))
    notas.append(nota)
notas.sort()
media = sum(notas)/len(notas)
maior = notas[len(notas) - 1]
menor = notas[0]
diferenca = maior - menor
print(f"Média: {media:.2f}")
print(f"Maior: {maior:.2f}")
print(f"Menor: {menor:.2f}")
print(f"Diferenca: {diferenca:.2f}")

    

