resultados = []
while True:
    
    nome = ""
    saltos = []
    melhor_salto = 0
    pior_salto = 0
    media = 0
    
    nome = input("Nome: ")
    if nome.upper() == "O":
        break
    for numero_do_salto in range(5):
        saltos.append(float(input(f"{numero_do_salto + 1}º Salto: ")))
    saltos.sort()
    melhor_salto = saltos.pop(-1)
    pior_salto = saltos.pop(0)
    media = sum(saltos)/len(saltos)
    
    resultados.append(f"{nome}: {media:.2f} m")
    print(resultados[-1])
    
print("\nResultado final:")
for resultado in resultados:
    print(resultado)
