
numero_do_teste = 1
while True:
    numero_de_casos = int(input())
    if numero_de_casos <= 0:
        break
    print("Teste {}".format(numero_do_teste))
    diferenca = 0
    while numero_de_casos > 0:
        cofre_1, cofre_2 = [int(x) for x in input().split()]
        diferenca += (cofre_1 - cofre_2)
        print(diferenca)
        numero_de_casos -= 1
    print()
    numero_do_teste += 1