#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o numero solicitado for negativo.
valor = 0
multiplicador = 1
while True:
    valor = int(input('Insira um número para exibir sua tabuada: '))
    if 0 > valor:
        print('Encerrado...')
        break
    while multiplicador <= 10:
        print(f'{valor} X {multiplicador} = {valor * multiplicador}')
        multiplicador += 1
    multiplicador = 1

