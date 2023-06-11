"""
Nome: Augusto de Hollanda Vieira Guerner
Disciplina: Programação Orientada a Objeto

"""
"""
NUMERO_DE_TERMOS = 15

def fib(n):
    if n <= 0:
        return 0
    elif n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

print("{", end="")
for cont in range(0, NUMERO_DE_TERMOS):
    print(fib(cont), end="")
    if cont == NUMERO_DE_TERMOS - 1:
        print("", end="")
    else:
        print(", ", end="")
print("}", end="")
"""

QUANTIDADE_DE_TERMOS = 100
contador = QUANTIDADE_DE_TERMOS

termo_0 = 0
termo_n1 = 1
termo_n2 = 0
resultado = 0

print(10*"=" + " Fibonacci " + 10*"=")
print(resultado)
while contador > 0:
    resultado = termo_n1 + termo_n2
    termo_n1 = termo_n2
    termo_n2 = resultado
    print(resultado)
    contador-= 1
print(8*"=" + " Fim do programa " + 8*"=")
    


