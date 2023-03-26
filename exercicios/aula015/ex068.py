#faça um programa que joque par ou impar com o computador. O jogo só será interrompido quando o jogador perder.
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
jogador = 0
computador = 0
p_i = ''
tot = 0
vit_cons = 0
while True:
    p_i = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()[0]
    jogador = int(input('Escolha seu número entre 0 e 10: '))
    computador = random.randint(0, 10)
    tot = jogador + computador
    if tot % 2 == 0:
        print(f'total {tot} é par')
        if p_i == 'P':
            print('Você ganhou!')
            vit_cons +=1
        else:
            print('O computador ganhou!')
            break
    elif p_i == 'I':
        print('Você ganhou!')
        vit_cons += 1
    else:
        print('O computador ganhou!')
        break
print(f'Foram {vit_cons} Vitorias consecutivas')