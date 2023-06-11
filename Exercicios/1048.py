
def obter_reajuste(valor):
    reajuste = 0
    if 0 <= valor <= 400.0:
        reajuste = 0.15
    elif 400.01 <= valor <= 800.0:
        reajuste =  0.12
    elif 800.01 <= valor <= 1200.0:
        reajuste =  0.10
    elif 1200.01 <= valor <= 2000.0:
        reajuste =  0.07
    else:
        reajuste =  0.04
        
    reajuste_em_percentual = int(100*reajuste)
    reajuste_em_dinheiro = reajuste * valor
    novo_valor = valor + reajuste_em_dinheiro
    print("Novo salario: {:.2f}".format(novo_valor))
    print("Reajuste ganho: {:.2f}".format(reajuste_em_dinheiro))
    print("Em percentual: {} %".format(int(reajuste_em_percentual)))

valor = float(input())
obter_reajuste(valor)