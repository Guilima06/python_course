# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo
# com a media atingida
# media abaido de 5.0: reprovado
# media entre 5.0 e 6.9: recuperacao
# media 7.0 ou superior: aprovado
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2)/2
print('A média atingida foi {:.2f}.'.format(media))
if media < 5:
    print('Você foi reprovado.')
elif 5 <= media < 7:
    print('Você está de recuperação.')
else:
    print('Você foi aprovado.')