#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele,
#lendo o nome deles e esvrevendo o nome escolhido
import random

aluno1 = input('Insira o nome do alundo: ')
aluno2 = input('Insira o nome do alundo: ')
aluno3 = input('Insira o nome do alundo: ')
aluno4 = input('Insira o nome do alundo: ')
lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))
