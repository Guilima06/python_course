#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. considere U$$ = R$3,27
valor_carteira = float(input('Insira o valor em dinheiro presente na sua carteira: '))
valor_dolar = valor_carteira / 3.27
print('Você tem R${:.2f} em sua carteira, que equivale a U$${:.2f}'.format(valor_carteira, valor_dolar))
