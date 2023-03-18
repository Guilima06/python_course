# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
num = int(input('Insira um número qualquer: '))
base = int(input('Selecione a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nInsira sua opção: '))
if base == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção inválida')
