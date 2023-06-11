x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)

dist = ((y1 - y2)**2 + (x1 - x2)**2)**(1/2)
print("{:.4f}".format(dist))
