#faça um algoritmo que leia o preço de um produto e
#mostre seu novo preço com 5% de desconto
preço_produto = float(input('Insira o preço do produto: '))
preço_desconto = preço_produto - (preço_produto * (50 / 100))
print('O preço cheio do produto é {:.2f}R$, o preço do produto com 5% de desconto é {:.2f}R$'.format(preço_produto, preço_desconto))
