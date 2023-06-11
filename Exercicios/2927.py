pessoas, computadores, computadores_queimados, computadores_sem_compilador = [int(x) for x in input().split()]

pessoas += 1

computadores_funcionais = computadores - computadores_queimados - computadores_sem_compilador
if pessoas > computadores_funcionais:
    if computadores_queimados > computadores_sem_compilador:
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")
else:
    print("Igor feliz!")

