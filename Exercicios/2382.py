l, a, p, r = [int(x) for x in input().split()]

if (0 <= l and
    0 <= a and
    0 <= p and
    0 <= r    ):
    if r**2 >= (l/2.0)**2 + (a/2.0)**2 + (p/2.0)**2:
        print("S")
    else:
        print("N")
else:
    print("Valores inválido")