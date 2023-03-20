#Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3
# e que se encontram no intervalo de 1 até 500
soma = 0
for num in range (1, 501, 2):
    if num % 3 == 0:
        print('{} é impar e múltiplo de 3'.format(num))
        soma += num
print(soma)