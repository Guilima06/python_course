# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
nome = str(input('Insira o seu nome Completo: ')).title().strip()
print(nome)
print('Possui Silva no nome {}'.format('Silva' in nome))
