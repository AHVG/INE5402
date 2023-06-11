def obter_ventilador_direita(linha, coluna_inicial):
    coluna = coluna_inicial
    potencia = 0
    while True:
        if coluna >= len(linha):
            potencia = 0
            break
        elif linha[coluna] > 0:
            potencia = linha[coluna]
            break
        coluna += 1
    return {'coluna': coluna, 'potencia': potencia}
    
def obter_ventilador_esquerda(linha, coluna_inicial):
    coluna_inicial = (len(linha) - 1) - coluna_inicial
    ventilador = obter_ventilador_direita(linha[::-1], coluna_inicial)
    ventilador['coluna'] = (len(linha) - 1) - ventilador['coluna']
    return ventilador

def atualizar_balao(balao, linha):
    ventilador_esq = obter_ventilador_esquerda(linha, balao['coluna'])
    ventilador_dir = obter_ventilador_direita(linha, balao['coluna'])
    
    diferenca_pot = ventilador_esq['potencia'] - ventilador_dir['potencia']
    nova_coluna = balao['coluna'] + diferenca_pot
    nova_linha = balao['linha']
    novo_estado = True
    
    if ventilador_esq['coluna'] >= nova_coluna:
        nova_coluna = ventilador_esq['coluna']
    elif ventilador_dir['coluna'] <= nova_coluna:
        nova_coluna = ventilador_dir['coluna']
    else:
        novo_estado = False
        nova_linha += 1
        
    balao['coluna'] = nova_coluna
    balao['linha'] = nova_linha
    balao['estourado'] = novo_estado

    

while True:
    linhas, colunas, coluna_balao = [int(x) for x in input().split()]
    balao = {'coluna': coluna_balao - 1, 'linha': 0, 'estourado': False}

    mapa = []
    for i in range(linhas):
        linha = [int(x) for x in input().split()]
        mapa.append(linha[:])

    if linhas == colunas == coluna_balao == 0:
        break

    while True:
        atualizar_balao(balao, mapa[balao['linha']])
        
        if balao['estourado'] == True:
            print(f"BOOM {balao['linha'] + 1} {balao['coluna'] + 1}")
            break
        elif balao['linha'] >= linhas:
            print(f"OUT {balao['coluna'] + 1}")
            break
