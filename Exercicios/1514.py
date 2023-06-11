def matriz_transposta(matriz):
    nova_matriz = []
    
    for coluna in range(len(matriz[0])):
        linha = []
        [linha.append(matriz[x][coluna]) for x in range(len(matriz))]
        nova_matriz.append(linha[:])
    
    return nova_matriz[:]

def entrada_valida(participantes, problemas):
    if 3 <= participantes <= 100 and 3 <= problemas <= 100:
        return True
    return False
      

def alguem_resolveu_todos_problemas(problemas):
    for aluno in problemas:
        if 0 not in aluno:
            return True
    return False
    

def todo_problema_foi_resolvido(problemas):
    nova_matriz = matriz_transposta(problemas)
    for problema in nova_matriz:
        if 1 not in problema:
            return False
    return True

def tem_algum_problema_resolvido_por_todos(problemas):
    nova_matriz = matriz_transposta(problemas)
    for problema in nova_matriz:
        if 0 not in problema:
            return True
    return False


def todos_resolveram_ao_menos_um_problema(problemas):
    for aluno in problemas:
        if 1 not in aluno:
            return False
    return True


while True:
    participantes, problemas = [int(x) for x in input().split()]
    
    if participantes == 0 and problemas == 0:
        break
    
    if not entrada_valida(participantes, problemas):
        print("Entrada inválida! Digite novamente.")
        continue

    problemas = []
    for i in range(0, participantes):
        linha = []
        [linha.append(int(x)) for x in input().split()]
        problemas.append(linha[:])
        
    numero_de_conquistas = 0
    if not alguem_resolveu_todos_problemas(problemas):
        print(1)
        numero_de_conquistas += 1
    if todo_problema_foi_resolvido(problemas):
        print(2)
        numero_de_conquistas += 1
    if not tem_algum_problema_resolvido_por_todos(problemas):
        print(3)
        numero_de_conquistas += 1
    if todos_resolveram_ao_menos_um_problema(problemas):
        print(4)
        numero_de_conquistas += 1
        
    print(numero_de_conquistas)
    