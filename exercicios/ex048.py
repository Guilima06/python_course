#Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3
# e que se encontram no intervalo de 1 até 500
input('Aperte enter para prosseguir...')
soma = 0
for num in range (1, 500):
    if num % 2 != 0 and num % 3 == 0:
        print('{} é impar e múltiplo de 3'.format(num))
        soma += num
print(soma)