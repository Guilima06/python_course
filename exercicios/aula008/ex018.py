#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math

angulo = float(input('Informe o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno do angulo é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, cosseno, tangente))
