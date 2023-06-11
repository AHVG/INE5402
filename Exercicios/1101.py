print(10*"=" + " Visualizador de intervalo " + 10*"=")
while True:
    m, n = [int(x) for x in input().split()]
    if m > n:
        aux = m
        m = n
        n = aux
    if m <= 0:
        break
    soma = 0
    while m <= n:
        print(m, end=" ")
        soma += m
        m += 1
    print("Sum={}".format(soma))
print(10*"=" + " Fim do programa " + 10*"=")
