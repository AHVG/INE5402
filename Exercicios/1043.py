a, b, c = [float(x) for x in input().split()]

if (a + b > c and
    a + c > b and
    b + c > a):
    print("Perimetro = {:.1f}".format(a + b + c))
else:
    print("Area = {:.1f}".format((a + b) * c / 2))
    
