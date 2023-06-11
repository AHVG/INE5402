preco_produto = float(input('Preco: '))
print('Dinheiro  [D]')
print('Cartão 1x [C1]')
print('Cartão 2x [C2]')
print('Cartão 3x [C3]')
tipo_pagamento = input('Tipo de pagamento: ')

if tipo_pagamento.upper() == 'D':
    print(preco_produto * 0.9)
elif tipo_pagamento.upper() == 'C1':
    print(preco_produto * 0.95)
elif tipo_pagamento.upper() == 'C2':
    print(preco_produto)  
elif tipo_pagamento.upper() == 'C3':
    print(preco_produto * 1.2)
else:
    print('Tipo de pagamento inválido!')

