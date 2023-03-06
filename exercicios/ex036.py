# Escreva um programa para aprovar o empréstimo bancário de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não  pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Informe o valor do imovel que será financiado: '))
salario_comprador = float(input('Informe o salário do comprador: '))
prazo_pagamento = int(input('Informe o prazo para pagamento: '))
valor_prestacao = valor_casa / prazo_pagamento
salario_minimo = salario_comprador * 30/100
if valor_prestacao > salario_minimo:
    print('Valor prestação R${:.2f} em {}x, salário de R${:.2f} sendo 30% R${:.2f}'.format(valor_prestacao, prazo_pagamento, salario_comprador, salario_minimo))
    print('Empréstimo negado, O valor da prestação excede 30% do salário')
else:
    print('Valor prestação R${:.2f} em {}x, salário de R${:.2f} sendo 30% R${:.2f}'.format(valor_prestacao, prazo_pagamento, salario_comprador, salario_minimo))
    print('Empréstimo concedido.')