alcool = 0
gasolina = 0
diesel = 0

print(10*"=" + " Analisador de satisfação " + 10*"=")

print("\n1. Álcool \n2. Gasolina\n3. Diesel\n4. Fim\n")

while True:
    opcao = int(input("Opção: "))
    if opcao == 1:
        alcool += 1
    elif opcao == 2:
        gasolina += 1
    elif opcao == 3:
        diesel += 1
    elif opcao == 4:
        break
    else:
        print("Entrada inválida!")

print()
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
print()

print(10*"=" + " Fim do programa " + 10*"=")


