# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.
import random

numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print(numeros)
print(f'O maior número é {max(numeros)} e o menor número é {min(numeros)}')