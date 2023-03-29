# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
num = int(input('Insira um número para descobrir se ele é par ou impar: '))
if num % 2 == 0:
    print('O numéro {} é par.'.format(num))
else:
    print('O número {} é impar.'.format(num))
