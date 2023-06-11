terceiro_link = int(input())

if 1 <= terceiro_link <= 1000:
    segundo_link = terceiro_link * 2
    primeiro_link = segundo_link * 2
    print(primeiro_link)
else:
    print("Valor inválido")
