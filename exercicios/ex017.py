#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa
import math

cateto_oposto = float(input('Informe a medida do cateto oposto: '))
cateto_adjacente = float(input('Informe a medida do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa é {:.2f}'.format(hipotenusa))
