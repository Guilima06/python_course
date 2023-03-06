# Desenvolva um programa que leia o comprimento de tres retas e e diga ao usuario
# se ele pode ou não formar um triangulo
l1 = float(input('Informe um lado do triangulo: '))
l2 = float(input('Informe outro lado do triangulo: '))
l3 = float(input('Informe outro lado do triangulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('As medidas informadas não formam um triangulo')
else:
    print('As medidas informadas formam um triangulo.')
