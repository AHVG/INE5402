num_palavras, num_textos = [int(x) for x in input().split()]

palavras = {}
for palavra in range(num_palavras):
    palavra, ponto = [x for x in input().split()]
    ponto = int(ponto)
    palavras[palavra] = ponto

for texto in range(num_textos):
    texto = ""
    while True:
        trecho = input()
        if trecho == ".":
            break
        texto += " " + trecho
    pontuacao = 0
    
    for palavra in texto.split():
        if palavra in palavras:
            pontuacao += palavras[palavra]
    
    print(pontuacao)
