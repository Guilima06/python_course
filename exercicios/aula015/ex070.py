#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá pergunar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato
nome = ''
preco = 0
tot_compra = 0
prod_maisk = 0
menor_preco = 0
nome_menor = ''
continua = ''
while True:
    nome = str(input('Insira o nome do produto: ')).strip().upper()
    preco = int(input('Insira o preço do produto: '))
    tot_compra += preco
    if preco > 1000:
        prod_maisk += 1
    if preco < menor_preco:
        menor_preco = preco
        nome_menor = nome
    continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'O total gasto foi {tot_compra}, {prod_maisk} produtos custaram mais que R$1000 e {nome_menor} foi o produto mais barato')