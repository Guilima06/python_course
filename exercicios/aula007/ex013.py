#faça um programa que leia o salario de um funcionário e mostre seu novo salario
#com 15% de aumento
valor_salario = float(input('Insira o valor do seu salário: '))
valor_aumento = valor_salario + (valor_salario * (15 / 100))
print('O salário atual é {:.2f}R$, com um aumento de 15% ele será de {:.2f}R$'.format(valor_salario, valor_aumento))
