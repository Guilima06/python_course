#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
from time import time
maiores = 0
menores = 0

for c in range(0, 7):
    ano_nasc = int(input('insira o ano em que você nasceu: '))
    if date.today().year - ano_nasc < 18:
        menores += 1
        print('Essa pessoa e menor')
    else:
        print('Essa pessoa é maior')
        maiores += 1
print('São {} maiores e {} menores de 18 anos'. format(maiores, menores))
