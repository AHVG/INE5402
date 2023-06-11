print(10*"=" + " Notas e Moedas " + 10*"=")

MULTIPLICADOR = 100

quantidade_nota_100   = 0
quantidade_nota_50    = 0
quantidade_nota_20    = 0
quantidade_nota_10    = 0
quantidade_nota_5     = 0
quantidade_nota_2     = 0

quantidade_moeda_1    = 0
quantidade_moeda_0_5  = 0
quantidade_moeda_0_25 = 0
quantidade_moeda_0_10 = 0
quantidade_moeda_0_05 = 0
quantidade_moeda_0_01 = 0

valor = float(input("Valor: "))
if 0 <= valor <= 1000000.00:
    valor *= MULTIPLICADOR
    valor = int(valor)
    while valor > 0:
        
        if valor >= 100*MULTIPLICADOR:
            valor -= 100*MULTIPLICADOR
            quantidade_nota_100 += 1
            
        elif valor >= 50*MULTIPLICADOR:
            valor -= 50*MULTIPLICADOR
            quantidade_nota_50 += 1
            
        elif valor >= 20*MULTIPLICADOR:
            valor -= 20*MULTIPLICADOR
            quantidade_nota_20 += 1
            
        elif valor >= 10*MULTIPLICADOR:
            valor -= 10*MULTIPLICADOR
            quantidade_nota_10 += 1
            
        elif valor >= 5*MULTIPLICADOR:
            valor -= 5*MULTIPLICADOR
            quantidade_nota_5 += 1
            
        elif valor >= 2*MULTIPLICADOR:
            valor -= 2*MULTIPLICADOR
            quantidade_nota_2 += 1
            
        elif valor >= 1*MULTIPLICADOR:
            valor -= 1*MULTIPLICADOR
            quantidade_moeda_1 += 1
            
        elif valor >= 0.5*MULTIPLICADOR:
            valor -= 0.5*MULTIPLICADOR
            quantidade_moeda_0_5 += 1
            
        elif valor >= 0.25*MULTIPLICADOR:
            valor -= 0.25*MULTIPLICADOR
            quantidade_moeda_0_25 += 1
            
        elif valor >= 0.1*MULTIPLICADOR:
            valor -= 0.1*MULTIPLICADOR
            quantidade_moeda_0_10 += 1
            
        elif valor >= 0.05*MULTIPLICADOR:
            valor -= 0.05*MULTIPLICADOR
            quantidade_moeda_0_05 += 1
            
        elif valor >= 0.01*MULTIPLICADOR:
            valor -= 0.01*MULTIPLICADOR
            quantidade_moeda_0_01 += 1
        
else:
    print("Entrada inválida!")

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(quantidade_nota_100))
print("{} nota(s) de R$  50.00".format(quantidade_nota_50))
print("{} nota(s) de R$  25.00".format(quantidade_nota_20))
print("{} nota(s) de R$  10.00".format(quantidade_nota_10))
print("{} nota(s) de R$   5.00".format(quantidade_nota_5))
print("{} nota(s) de R$   2.00".format(quantidade_nota_2))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(quantidade_moeda_1))
print("{} moeda(s) de R$ 0.50".format(quantidade_moeda_0_5))
print("{} moeda(s) de R$ 0.25".format(quantidade_moeda_0_25))
print("{} moeda(s) de R$ 0.10".format(quantidade_moeda_0_10))
print("{} moeda(s) de R$ 0.05".format(quantidade_moeda_0_05))
print("{} moeda(s) de R$ 0.01".format(quantidade_moeda_0_01))

print(10*"=" + " Fim do programa " + 10*"=")