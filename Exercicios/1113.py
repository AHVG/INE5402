print(10*"=" + " Crescente e Decrescente " + 10*"=")
while True:
    x, y = [int(x) for x in input().split()]

    if x == y:
        break
    
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
print(10*"=" + " Fim do programa " + 10*"=")

