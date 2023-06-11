
while True:
    materias = {'EPR': 0,
                'EHD': 0,
                'INTRUSOS': 0}
    testes = int(input())
    if 1 <= testes <= 100000:
        for teste in range(testes):
            _, materia = input().split()
            if materia in materias:
                materias[materia] += 1
            else:
                materias['INTRUSOS'] += 1
        
        for materia in materias:
            print(materia + ": " + str(materias[materia]))
