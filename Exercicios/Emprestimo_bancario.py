valor_casa = float(input('Entre com o valor da casa: '))
salario = float(input('Entre com o salario: '))
anos = float(input('Entre com os anos: '))

prestacao = valor_casa / (anos * 12.0)

if prestacao > 0.3 * salario:
    print('Emprestimo negado!')
else:
    print('Emprestimo concedido!')
