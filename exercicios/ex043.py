# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule o seu imc e mostre seu status
# de acordo com a tabela abaixo
# abaixo de 18.5 - abaixo do peso
# entre 18.5 e 25 - peso ideal
# 25 ate 30 - sobrepeso
# 30 até 40 - obesidade
# acima de 40 - obesidade mórbida
import math

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / math.pow(altura, 2)
if imc <= 18.5:
    print('Seu IMC é {:.2f}, Você está abaixo do peso ideal'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f}, você está com o peso normal'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f}, você está com sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f}, você esá com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f}, você está com obesidade mórbida'.format(imc))
