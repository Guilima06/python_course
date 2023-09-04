#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
#Já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
#crescente
listanum = []
exist = []
tamanho = int(input('Quantos valores deve ter a lista? '))
for num in range(0,tamanho):
    valor = int(input('Insira um valor único: '))
    if valor in listanum:
        exist.append(valor)
        while valor in listanum:
            valor = int(input('Valor repetido, insira outro valor: '))
        listanum.append(valor)

    else:
        listanum.append(valor)
listanum.sort()
print(f'Os valores únicos digitados foram: {listanum}, os valores {exist} foram digitados mas já existiam na lista')
