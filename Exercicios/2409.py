def max_2(A,B):
    if A > B:
        return A
    else:
        return B
    
def min_2(A,B):
    if A > B:
        return B
    else:
        return A

def max_3(A,B,C):
    if A > B and A > C:
        return A
    if B > A and B > C:
        return B
    if C > A and C > B:
        return C

def esta_dentro_dos_limites(A,B,C,H,L):
    if (1 <= A <= 300 and
        1 <= B <= 300 and
        1 <= C <= 300 and
        1 <= H <= 250 and
        1 <= L <= 250):
        return True
    return False

def consegue_passar_pela_porta(A,B,C,H,L):
    
    maior_dimensao_da_porta = max_2(H,L)
    menor_dimensao_da_porta = min_2(H,L)
    
    maior_dimensao_do_colchao = max_3(A,B,C)
    segunda_maior_dimensao_do_colchao = 0
    terceira_maior_dimensao_do_colchao = 0
    
    if maior_dimensao_do_colchao == A:
        segunda_maior_dimensao_do_colchao = max(B,C)
        terceira_maior_dimensao_do_colchao = min(B,C)
    if maior_dimensao_do_colchao == B:
        segunda_maior_dimensao_do_colchao = max(A,C)
        terceira_maior_dimensao_do_colchao = min(A,C)
    if maior_dimensao_do_colchao == C:
        segunda_maior_dimensao_do_colchao = max(A,B)
        terceira_maior_dimensao_do_colchao = min(A,B)
    
    if (segunda_maior_dimensao_do_colchao <= maior_dimensao_da_porta and
        terceira_maior_dimensao_do_colchao <= menor_dimensao_da_porta):
        return True
    
    return False

A,B,C = [int(x) for x in input().split()]
H, L = [int(x) for x in input().split()]

if esta_dentro_dos_limites(A,B,C,H,L):
    if consegue_passar_pela_porta(A,B,C,H,L):
        print("Parabens pela a excelente compra!")
    else:
        print("Infelizmente você deverá escolher outro colchão!")
else:
    print("Valores inválidos!")