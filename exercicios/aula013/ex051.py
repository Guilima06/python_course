# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
# No Final, mostre os 10 primeiros termos dessa progressão
p1 = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
tot_termos = p1 + (10-1) * razao
for c in range(p1, tot_termos + razao, razao):
    print('{} '.format(c), end='-> ')
print('fim')