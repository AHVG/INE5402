def preencher_dicionario(dicionario):
    for i in range(int(input())):
        idioma = input()
        mensagem = input()
        dicionario[idioma] = mensagem
        
def obter_criancas(criancas):
    for i in range(int(input())):
        nome = input()
        idioma = input()
        criancas[nome] = idioma
        
def fazer_carta(dicionario, criancas):
    for crianca in criancas:
        carta = [crianca, dicionario[criancas[crianca]]]
        cartas.append(carta[:])
    
def imprimir_cartas(cartas):
    for carta in cartas:
        for info in carta:
            print(info)
        print()


dicionario = {}
criancas = {}
cartas = []

preencher_dicionario(dicionario)
obter_criancas(criancas)
fazer_carta(dicionario, criancas)
imprimir_cartas(cartas)


