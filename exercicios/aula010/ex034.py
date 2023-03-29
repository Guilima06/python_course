# Faça um programa que calcule o salário de um funcionário e calcule o valor do seu aumento
# para salários superiores a R$1250,00 calcule um aumento de 10%
# para inferiores o iguais o aumento é de 15%
salario_atual = float(input('Informe seu salário atual: '))
if salario_atual > 1250.00:
    print('Seu salario atual é R${:.2f}, você receberá um aumento de 10%'.format(salario_atual))
    print('Seu novo Salário é R${:.2f} + R${:.2f} = R${:.2f}'.format(salario_atual, salario_atual*(10/100), salario_atual + (salario_atual*(10/100))))
else:
    print('Seu salario atual é R${:.2f}, você receberá um aumento de 15%'.format(salario_atual))
    print('Seu novo Salário é R${:.2f} + R${:.2f} = R${:.2f}'.format(salario_atual, salario_atual*(15/100), salario_atual + (salario_atual*(15/100))))
