codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

"""
valor_da_conta = quantidade
if codigo == 1:
    valor_da_conta *= 4.00
    print("Total: R$ {:.2f}".format(valor_da_conta))
elif codigo ==  2:
    valor_da_conta *= 4.50
    print("Total: R$ {:.2f}".format(valor_da_conta))
elif codigo ==  3:
    valor_da_conta *= 5.00
    print("Total: R$ {:.2f}".format(valor_da_conta))
elif codigo ==  4:
    valor_da_conta *= 2.00
    print("Total: R$ {:.2f}".format(valor_da_conta))
elif codigo ==  5:
    valor_da_conta *= 1.50
    print("Total: R$ {:.2f}".format(valor_da_conta))
else:
    print("Código inválido")
"""
preco_dos_produtos = [4.0, 4.5, 5.0, 2.0, 1.5]
if 0 < codigo < 6:
    valor_da_conta = quantidade * preco_dos_produtos[codigo - 1]
    print("Total: R$ {:.2f}".format(valor_da_conta))
else:
    print("Código inválido")