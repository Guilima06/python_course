#Faça um programa aque leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digiitação novamente até ter um valor correto
sexo = str(input('Insria o sexo, M para masculino e F para feminino: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Valor inserido invalido.\nInsira novamente: ')).upper()
if sexo == 'M':
    print('Sexo inserido Masculino')
else:
    print('Sexo inserido Feminino')