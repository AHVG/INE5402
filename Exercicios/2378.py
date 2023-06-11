
def processar_entradas_saidas_elevador(leituras, capacidade):
    passou_do_limite_de_pessoas = "N"
    pessoas_dentro_do_elevador = 0
    for i in range(0, leituras):
        pessoas_sairam, pessoas_entraram = [int(x) for x in input().split()]
        pessoas_dentro_do_elevador += pessoas_entraram - pessoas_sairam
        if pessoas_dentro_do_elevador > capacidade:
            passou_do_limite_de_pessoas = "S"
    print(passou_do_limite_de_pessoas)

leituras, capacidade = [int(valores) for valores in input().split()]
processar_entradas_saidas_elevador(leituras, capacidade)


