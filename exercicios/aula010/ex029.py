# Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada km acima do limite.
velocidade_registrada = float(input('Informe a velocidade registrada pelo radar: '))
if velocidade_registrada > 80:
    print('Limite de velocidade Ultrapassado! \nA velocidade registrada foi {}km/h \nO limite de velocidade é 80km'.format(velocidade_registrada))
    print('O valor da multa para a velocidade de {}km/h é de R${:.2f}'.format(velocidade_registrada, 7 * (velocidade_registrada - 80)))
else:
    print('Tudo certo! \nA velocidade registrada foi {}, o limite de velocidade é 80km'.format(velocidade_registrada))
