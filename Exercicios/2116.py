def primo(numero):
    for divisor in range(2, int(numero/2) + 1):
        if numero % divisor == 0:
            return False
    return True

def obter_maior_primo_ate(numero):
    ultimo_primo = 2
    for i in range(2, numero + 1):
        if primo(i):
            ultimo_primo = i
    return ultimo_primo

numero_juilherme, numero_jogerio = [int(x) for x in input().split()]

P1 = obter_maior_primo_ate(numero_juilherme)
P2 = obter_maior_primo_ate(numero_jogerio)

multiplicacao_entre_primos = P1 * P2

print(multiplicacao_entre_primos)
