#O mesmo professor do desafio anterior quer sortear a orde de apresentação de trabalhos dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random

aluno1 = input('Insira o nome do alundo: ')
aluno2 = input('Insira o nome do alundo: ')
aluno3 = input('Insira o nome do alundo: ')
aluno4 = input('Insira o nome do alundo: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))