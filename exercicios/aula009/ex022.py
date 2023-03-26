# Crie um programa que leia o nome de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# quantas letras ao todo sem considerar os espaços
# quantas letras tem o primeiro nome
nome = str(input('Insira seu nome completo: ')).strip()
print('Nome maiusculo {}'.format(nome.upper()))
print('Nome minusculo {}'.format(nome.lower()))
print('Quantidade de letras {}'.format((len(nome)) - (nome.count(' '))))
print('Primeiro nome {} que tem {} letras'.format(nome[:nome.find(' ')], len(nome[:nome.find(' ')])))
