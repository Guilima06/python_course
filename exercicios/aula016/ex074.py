# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.
import random

numeros = ()
contador = 0
while contador < 5:
    numeros[contador] = random.randint(1, 5)
    contador += 1
print(numeros)

