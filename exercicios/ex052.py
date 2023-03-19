# faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num_input = int(input('Insira um número para saber se ele é primo: '))
cont = 2
for num in range(1, num_input):
    print(num)
    if num_input % num == 0 and num != 1 and num != num_input:
        print('Este número não é primo. ')

