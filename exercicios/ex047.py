#Faça um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50]
input('Aperte enter para começar')
for num in range (1, 50):
    if num % 2 == 0:
        print('{} É um número par'.format(num))
