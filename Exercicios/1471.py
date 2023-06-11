def entrada_valida(R, N):
    if 1 <= R <= N and N <= 10000:
        return True
    return False

def solucao():
    while True:
        mergulharam, retornaram = [int(x) for x in input("Mergulharam Retornaram: ").split()]
        
        if mergulharam == 0 and retornram == 0:
            break
    
        if not entrada_valida(retornaram, mergulharam):
            print("Entrada inválida! Digite novamente.")
            continue
    
        numero_dos_que_morreram = list(range(1, mergulharam + 1))
        numero_dos_que_retornaram = []
        [numero_dos_que_retornaram.append(int(x)) for x in input().split()]
        
        for x in numero_dos_que_retornaram:
            if x in numero_dos_que_morreram:
                numero_dos_que_morreram.remove(x)
        
        if len(numero_dos_que_morreram) > 0:
            for x in numero_dos_que_morreram:
                print(x, end=" ")
            print()
        else:
            print("*")
    
solucao()
    