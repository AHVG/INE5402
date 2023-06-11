a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

PI = 3.14159265358

print('TRIANGULO: {:.3f}'.format(a * c / 2))
print('CIRCULO: {:.3f}'.format((c**2) * PI))
print('TRAPEZIO: {:.3f}'.format(c * (a + b) / 2))
print('QUADRADO: {:.3f}'.format(b**2))
print('RETANGULO: {:.3f}'.format(a * b))
