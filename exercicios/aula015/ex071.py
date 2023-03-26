#Crie um programa que simule o financiamento de um caixa eletrônico. No inicio, pergunte ao usuário
# qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues. Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        tot