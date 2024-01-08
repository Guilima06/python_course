#Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre:
#A)Quantas pessoas foram cadastradas . B) Uma listagem com as pessoas mais pesadas
# C)Uma Listagem com as pessoas mais leves
grupo = []
mai = 0
men = 0

while True:
    pessoa = []
    pessoa.append(str(input('Insira o nome da pessoa: ')))
    pessoa.append(float(input('Insira o peso da pessoa: ')))
    print(pessoa)
    if len(grupo) == 0:
        mai = pessoa[1]
        men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    grupo.append(pessoa[:])
    adicionar = str(input('Deseja inserir mais pessoas? S/N '))
    if adicionar in 'Nn':
        break
print(f'Foram cadastradas {len(grupo)} pessoas')

