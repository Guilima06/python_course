# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento
# a vista dinheiro/cheque = 10% de desconto
# a vista no cartão = 5% de desconto
# em até 2x no cartão = preço normal
# 3x ou mais no cartão = 20% de juros
price_product = float(input('Insira o valor do produto: R$'))
payment_format = int(input('Insira a opção da forma de pagamento desejada\n'
                           '1 - a vista dinheiro/cheque = 10% de desconto\n'
                           '2 - a vista no cartão = 5% de desconto\n'
                           '3 - em até 2x no cartão = preço normal\n'
                           '4 - 3x ou mais no cartão = 20% de juros\n'
                           'Insira a opção desejada: '))
desconto1 = price_product * (10 / 100)
desconto2 = price_product * (5 / 100)
juros = price_product * (20 / 100)
if payment_format == 1:
    price_product = price_product - desconto1
    print('você ganhoum desconto de R${:.2f}'.format(desconto1))
    print('Valor a ser pago a vista dinheiro/cheque R${:.2f}'.format(price_product))
elif payment_format == 2:
    price_product = price_product - desconto2
    print('Você recebeu um desconto de R${:.2f}'.format(desconto2))
    print('Valor a ser pago a vista no cartão R${:.2f}'.format(price_product))
elif payment_format == 3:
    print('Valor a ser pago em até 2x no cartão, 2x de R${:.2f} = R${:.2f}'.format(price_product / 2, price_product))
elif payment_format == 4:
    price_product = price_product + juros
    parcelas = int(input('Insira a quantidade de parcelas desejadas a partir de 3x: '))
    print('Valor a ser pago em {}x de R${:.2f} = R${:.2f}'.format(parcelas, price_product / parcelas, price_product))
else:
    print('Opção inválida')
