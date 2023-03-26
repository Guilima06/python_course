#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
valor_metros = float(input('Insira a medida em metros: '))
valor_centimetros = valor_metros * 100
valor_milimetros = valor_metros * 1000
print('A medida em metros é {}m \n A medida em centimetros é {:.0f}cm \n A medida em milimetros é {:.0f}mm'.format(valor_metros, valor_centimetros, valor_milimetros))
