# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
# No Final, mostre os 10 primeiros termos dessa progressão
p1 = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
pa = p1
for num in range(2, 11):
    pa += razao
    print('{}ºtermo é {}'.format(num, pa))
