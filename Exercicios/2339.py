c, p, f = [int(x) for x in input().split()]

if not ((1 <= c <= 1000) and
        (1 <= p <= 1000) and
        (1 <= f <= 1000)    ):
    print("Valores invalidos")
elif p/c >= f:
    print("S")
else:
    print("N")