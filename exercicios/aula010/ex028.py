# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir
# qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random

num_sorteado = random.randint(0, 5)
num_usuario = int(input('Insira um número entre 0 e 5: '))
if 0 <= num_usuario <= 5:
    if num_usuario == num_sorteado:
        print('Parabens, você acertou! Vocês escolheu o número {} e o computador também escolheu {}'.format(num_usuario, num_sorteado))
    else:
        print('Que pena, você errou. Você escolheu o número {} e o computador escolheu o número {}'.format(num_usuario, num_sorteado))
else:
    print('O número que você informou não atende os requisitos, escolha um número entre 0 e 5.')
