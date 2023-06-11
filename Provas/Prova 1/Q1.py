"""
Augusto de Hollanda Vieira Guerner
22102192
"""

PORCAO_ANDRE  = 300
PORCAO_PEDRO  = 1500
PORCAO_CAMILA = 600
PORCAO_MANOEL = 1000
PORCAO_LARA   = 150
PORCAO_DONA_FRANCISCA = 225

while True:
    
    andre, pedro, camila, manoel, lara = [int(x) for x in input("Insira as porcoes: ").split()]
    
    estimativa_lasanha = PORCAO_DONA_FRANCISCA
    estimativa_lasanha += andre  * PORCAO_ANDRE
    estimativa_lasanha += pedro  * PORCAO_PEDRO
    estimativa_lasanha += camila * PORCAO_CAMILA
    estimativa_lasanha += manoel * PORCAO_MANOEL
    estimativa_lasanha += lara   * PORCAO_LARA
    
    print(f"{estimativa_lasanha}")
    
    if(input("Deseja continuar? [S/N]\n> ").upper() == 'N'):
        break


