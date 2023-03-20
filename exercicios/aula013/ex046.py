#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fotos de artificio
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

input('Aperte qualquer tecla para iniciar a contagem regressiva....')
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('FOGOS')