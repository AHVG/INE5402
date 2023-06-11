"""
Nome: Augusto de Hollanda Vieira Guerner
Disciplina: Programação Orientada a Objeto

"""

PERCENTUAL_DE_DESCONTO = 0.11
VALOR_MAXIMO_DE_DESCONTO = 320.0

salario = 0
desconto = 0
percentual_do_desconto = 0

print(10*"=" + " Calculadora de desconto previdenciário " + 10*"=")
while True:
    
    salario = float(input("\nEntre com o salário: "))
    desconto = salario * PERCENTUAL_DE_DESCONTO
    if desconto > VALOR_MAXIMO_DE_DESCONTO:
        percentual_do_desconto = VALOR_MAXIMO_DE_DESCONTO / salario
        salario -= VALOR_MAXIMO_DE_DESCONTO
    else:
        percentual_do_desconto = desconto / salario
        salario -= desconto
        
    print("Novo salário: {:.2f}".format(salario))
    print("Desconto em percentual: {:.4f}".format(percentual_do_desconto))

    print("\n1. [S] para sair")
    print("2. [Qualquer coisa] para continuar\n")
    
    opcao = input("Opcão: ")
    if opcao[0].upper() == "S":
        print()
        break

print(21*"=" + " Fim do programa " + 22*"=")