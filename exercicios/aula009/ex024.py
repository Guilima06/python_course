# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
nome_cidade = str(input('Insira o nome da cidade: ')).title().strip()
print(nome_cidade)
print('O primeiro nome da cidade é Santo {}'.format('Santo' in nome_cidade[:nome_cidade.find(' ')]))
