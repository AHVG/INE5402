teste = 0
n = int(input())
while n != -1:
    teste += 1
    print("Teste {}\n".format(teste))
    print("{}\n".format((int(pow(4,n) + pow(2,n+1) + 1))))
    n = int(input())
