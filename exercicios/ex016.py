#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#ex: digite um número: 6.127 - O numero 6.127 tem a parte inteira 6
import math

num = float(input('Insira um número qualquer: '))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))
