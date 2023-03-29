# Faça um programa que leia o ano de nascimento de um jovem e infome de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se ja passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
import datetime

ano_nasc = int(input('Informe o ano do seu nascimento: '))
idade = datetime.datetime.now().year - ano_nasc
if idade < 18:
    print('Ainda não esta na hora, você deve se alistar qunado completar 18 anos em {}'.format(ano_nasc + 18))
elif idade == 18:
    print('Você completou 18 anos, está na hora de se alistar.')
else:
    print('O prazo para se alistar já passou, você deveria ter se alistado em {}'.format(ano_nasc + 18))
