# Crie um programa que faça o computador jogar jokenpo com você]
import random
print('='*20 + 'JOKENPO' +'='*20)
itens = ('Pedra', 'Papel', 'Tesoura')
computer = random.randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua jogada? '))
print('-='*12)
print('Computador jogou {}'.format(itens[computer]))
print('Jogador jogou {}'.format(itens[player]))
print('-='*12)
if computer == 0:#Pedra
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR GANHOU!')
    elif player == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computer == 1:#Papel
    if player == 0:
        print('COMPUTADOR GANHOU')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computer ==2:#Tesoura
    if player == 0:
        print('JOGADOR GANHOU')
    elif player == 1:
        print('COMPUTADOR GANHOU!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
