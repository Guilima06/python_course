#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5!=5*4*3*2*1=120
from math import factorial
n = int(input('Insira o número que será fatorado: '))
c = n
fator = 1
while c > 0:
    print(c, end='*')
    fator *= c
    c -= 1
print('O resultado é {}'.format(fator))