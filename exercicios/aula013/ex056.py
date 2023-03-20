#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# no final do programa mostre:
#A media de idade do grupo
#Nome do homem mais velho
#Quantas Mulheres tem menos de 20 anos
import datetime

somaidade = 0
hmaior = 0
name_hmaior = ''
totm20 = 0
for c in range(1, 5):
    nome = str(input('Insira o nome da pessoa: '))
    idade = datetime.date.today().year - int(input('Insira o ano que essa pessoa nasceu: '))
    sexo = str(input('Insira o sexo da pessoa, F para feminino e M para Masculino: '))
    somaidade += idade
    if sexo