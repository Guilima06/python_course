# Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar., mostrando no final quantos palpites foram necessários.
import random

palpites = 1
acertou = False
while not acertou:
    num_sorteado = random.randint(0, 10)
    num_usuario = int(input('Insira um número entre 0 e 10: '))
    while num_usuario < 0 or 10 < num_usuario:
        num_usuario = int(input('Número inválido!\nInsira um número entre 0 e 10: '))
    if num_usuario == num_sorteado:
        print(
            'Parabens, você acertou! Vocês escolheu o número {} e o computador também escolheu {}, você precisou de {'
            '} tentativas'.format(num_usuario, num_sorteado, palpites))
        acertou = True
    else:
        print('Que pena, você errou.\n'
              'Você escolheu o número {} e o computador escolheu o número {}, '
              'tente novamente.'.format(num_usuario, num_sorteado))
        palpites += 1
