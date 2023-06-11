"""
Nome: Augusto de Hollanda Vieira Guerner
Disciplina: Programação Orientada a Objeto

"""

print(10*"=" + " Fatorial Recursão " + 10*"=")
QUANTIDADE_DE_REPETICOES = 15
def fat(n):
    if n <= 1:
        return 1
    else:
        return n*fat(n-1)

for cont in range(QUANTIDADE_DE_REPETICOES):
    print(fat(cont))
print(10*"=" + " Fatorial Recursão " + 10*"=")
