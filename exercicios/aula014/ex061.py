#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while

p1 = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
contador = 10
while contador != 0:
    print('{} '.format(p1), end='-> ')
    p1 += razao
    contador = contador - 1
print('fim')

