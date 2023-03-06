# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# - Oprimeiro valor é maior
# - O segundo valor é maior
# - não existe valor maior, os dois são iguais
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(n1, n2))
elif n2 > n1:
    print('O Segundo valor {} é maior que o primeiro valor {}'.format(n2,n1))
else:
    print('Não existe valor maior, {} e {} são iguais'.format(n1,n2))
