# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando
# R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
dist = int(input('Qual a distnacia da viagem em km? '))
if dist <= 200:
    print('Considerando a distancia de {}km, o preço da passagem para essa viagem é R${:.2f}.'.format(dist, dist * 0.50))
else:
    print('Considerando a distancia de {}km, o preço da passagem para essa viagem é R${:.2f}.'.format(dist, dist * 0.45))
