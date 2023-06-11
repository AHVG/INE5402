"""
Augusto de Hollanda Vieira Guerner
22102192
"""

def verificao_pessoas(pessoas):
    if 1 <= pessoas <= 1000:
        return True
    return False

def verificao_tempo(tempo):
    if 0 <= tempo <= 10000:
        return True
    return False

def solucao():
    tempo_de_funcionamento = 10
    quantidade_de_pessoas = int(input()) - 1
    
    if not verificao_pessoas(quantidade_de_pessoas):
        return -1
    
    tempo_anterior = int(input())
    for pessoa in range(quantidade_de_pessoas):
        if not verificao_tempo(tempo_anterior):
            return -1
        tempo_proximo = int(input())
        diferenca = tempo_proximo - tempo_anterior
        tempo_anterior = tempo_proximo
        if diferenca > 10:
            diferenca = 10
        tempo_de_funcionamento += diferenca
    return tempo_de_funcionamento

print(solucao())