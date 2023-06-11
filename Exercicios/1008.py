numero_de_funcionarios = int(input())
carga_horaria          = int(input())
salario_por_hora       = float(input())

salario = (carga_horaria * salario_por_hora)

print('NUMBER = {}'.format(numero_de_funcionarios))
print('SALARY = U$ {:.2f}'.format(salario))
