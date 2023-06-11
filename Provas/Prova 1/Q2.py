"""
Augusto de Hollanda Vieira Guerner
22102192
"""

def mostrar_dados(entrevistados, media_idade, mulheres_2000,
                  sexo_menor_salario, idade_menor_salario, menor_salario,
                  idade_mais_velho, nome_mais_velho):
    print()
    print(f"Numero entrevistados: {entrevistados}\nMedia idade:{media_idade:.2f}\n", end="")
    print(f"Mulheres com mais de 2000 de salario: {mulheres_2000}\nIdade pessoa com menor salario: {idade_menor_salario}\n", end="")
    print(f"Menor salario: {menor_salario}\nIdade mais velho: {idade_mais_velho}\nNome mais velho: {nome_mais_velho}")
    print()


numero_de_entrevistados = 0
media_idades = 0
numero_de_mulheres_2000 = 0
sexo_menor_salario = ""
idade_menor_salario = -1
menor_salario = 0
idade_mais_velho = 0
nome_mais_velho = ""

print(10 * "=" + " Entrevista " + 10*"=")
while True:
    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    salario = int(input("Salario: "))
    
    media_idades += idade
    if sexo.upper()[0] == 'F' and salario >= 2000:
        numero_de_mulheres_2000 += 1
    if numero_de_entrevistados == 0 or menor_salario > salario:
        menor_salario = salario
        sexo_menor_salario = sexo
        idade_menor_salario = idade
    if idade_mais_velho < idade:
        idade_mais_velho = idade
        nome_mais_velho = nome
    
    numero_de_entrevistados += 1
    if(input("Deseja continuar? [S/N]\n> ").upper() == 'N'):
        media_idades /= numero_de_entrevistados
        mostrar_dados(numero_de_entrevistados, media_idades, numero_de_mulheres_2000, sexo_menor_salario, idade_menor_salario, menor_salario, idade_mais_velho, nome_mais_velho)
        break
    
print(10 * "=" + " Fim da entrevista " + 10*"=")   



