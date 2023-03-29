dias_alugado = int(input('Informe por quantos dias o carro foi alugado: '))
km_veic = float(input('Informe quantos km foram rodados: '))
custo_dias = (dias_alugado * 60.0) + (km_veic * 0.15)
print('O total a pagar é R${:.2f}'.format(custo_dias))
#custo_km = km_veic *0.15
#print('Considerando o custo de R${:.2f} por dia, o aluguel por {} dias é R${:.2f}'.format(60.0, dias_alugado, custo_dias))
#print('Considerando o custo de R${:.2f} por km, o aluguel do veículo após {:.2f}km rodados é R${:.2f}'.format(0.15, km_veic, custo_km))
