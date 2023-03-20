# faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num_input = int(input('Insira um número para saber se ele é primo: '))
cont = 0
for num in range(1, num_input+1):
    if num_input % num == 0:
        cont += 1
        print('\033[33m {}'.format(num), end=' ')
    else:
        print('\033[31m {}'.format(num), end=' ')
if cont == 2:
    print('\n{} É um Número primo.'.format(num_input))
else:
    print('\n{} Não é um número primo'.format(num_input))