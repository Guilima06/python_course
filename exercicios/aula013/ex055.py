# Faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e o menor peso lidos
import math
peso = []
for c in range(0, 5):
    peso_inform = float(input('Informe o peso: '))
    peso.append(peso_inform)
print('O maior peso registrado é {}'.format(max(peso)))
print('O menor peso registrado é {}'.format(min(peso)))
