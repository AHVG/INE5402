
cobaias = 0
coelhos = 0
ratos = 0
sapos = 0

for teste in range(int(input())):
    numero, animal = input().split()
    numero = int(numero)
    if animal == "C":
        coelhos += numero
    elif animal == "R":
        ratos += numero
    elif animal == "S":
        sapos += numero
    cobaias += numero
        
print(f"Total: {cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print("Percentual de coelhos: {:.2f} %".format(coelhos/cobaias * 100))
print("Percentual de ratos: {:.2f} %".format(ratos/cobaias * 100))
print("Percentual de sapos: {:.2f} %".format(sapos/cobaias * 100))
        
        


