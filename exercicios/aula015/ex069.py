#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
#perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos
idade = 0
sexo = ''
maior = 0
tot_h = 0
mul_men20 = 0
continua = ''
while True:
    idade = int(input('Insira a idade da pessoa: '))
    sexo = str(input('Insira o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        tot_h += 1
    if sexo == 'F':
        if idade < 20:
            mul_men20 += 1
    continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'foram {maior} maiores de 18, {tot_h} homens e {mul_men20} mulheres com menos de 20 anos')