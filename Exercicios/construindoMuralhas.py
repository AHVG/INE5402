vezes,tamanho = [int(x) for x in input().split()]
for i in range(vezes):
    entrada = input().split()
    altura = int(entrada[-1])
    del entrada[-1]
    nome = " ".join(entrada)
    if(int(altura) > tamanho):
        print(nome)