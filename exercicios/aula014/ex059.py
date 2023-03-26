#Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair dor programa
# Seu programa devera realizar a operação solicitada em cada caso
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
menu = int(input('Selecione a opção desejada:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos '
                 'números\n[5]sair dor'
                 'programa\nInsira a opção: '))
while menu < 0 or menu > 5:
    menu = int(input(
        'Opção inválida!\nSelecione a opção desejada:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair '
        'dor programa\nInsira a opção: '))
while menu != 5:
    if menu == 4:
        n1 = int(input('\nInsira o primeiro valor: '))
        n2 = int(input('\nInsira o segundo valor: '))
    if menu == 1:
        print('\nA soma entre {} e {} é {}\n'.format(n1, n2, n1+n2))
    elif menu == 2:
        print('\nA multiplicação entre {} e {} é {}\n'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 != n2:
            print('\nO maior número entre {} e {} é {}\n'.format(n1, n2, max(n1, n2)))
        else:
            print('O valores são iguais!')
    menu = int(input('\nSelecione a opção desejada para continuar:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos '
                     'números\n[5]sair dor'
                     'programa\nInsira a opção: '))
print('Programa encerrado.')