def entrada_valida(pessoas, votos):
    if pessoas < 4 or 233000 < pessoas or pessoas != len(votos):
        return False
    for voto in votos:
        if voto != 1 and voto != 0:
            return False
    return True

def analisar_votos(votos):
    satisfeitos = 0
    insatisfeitos = 0
    
    for voto in votos:
        if voto == 1:
            insatisfeitos += 1
        else:
            satisfeitos += 1
    
    if satisfeitos > insatisfeitos:
        return "Y"
    return "N"
    

numero_pessoas = int(input())
votos = []
[votos.append(int(x)) for x in input().split()]

if entrada_valida(numero_pessoas, votos):
    print(analisar_votos(votos))
    