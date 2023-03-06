# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade
# ate 9 anos mirim
# ate 14 anos infantil
# ate 19 anos junior
# ate 20 anos senior
# acima master
import datetime

data_nasc = int(input('Informe a data de nascimento: '))
idade = datetime.datetime.now().year - data_nasc
if idade <= 9:
    print('A categoria do atleta é: Mirim.')
elif 9 < idade <= 14:
    print('A categoria do atleta é: Infantil.')
elif 14 < idade <= 19:
    print('A categoria do atleta é: Junior.')
elif 19 < idade <= 20:
    print('A categoria do atleta é: Senior.')
else:
    print('A categoria do atleta é: Master.')
