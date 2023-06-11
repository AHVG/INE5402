"""
Augusto de Hollanda Vieira Guerner
22102192
"""

def verificacao(leituras, capacidade):
    if 1 <= leituras <= 1000 and 1 <= capacidade <= 1000:
        return True
    return False

leituras, capacidade = [int(x) for x in input().split()]
passou_do_limite = "N"
if verificacao(leituras, capacidade):    
    pessoas_no_elevador = 0
    for i in range(leituras):
        saiu, entrou = [ int(y) for y in input().split()]
        pessoas_no_elevador -= saiu
        pessoas_no_elevador += entrou
        
        if pessoas_no_elevador > capacidade:
            passou_do_limite = "S"
    print(passou_do_limite)