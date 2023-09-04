#Crie um programa que vai ler os vários números e colocar em uma lista. Depois disso, crie duas listas extras que
#vão conter apenas os valores pares e os valores ímpares digitados respectivamente. Ao final mostre o conteúdo das
#três listas geradas
listnum = []
listpar = []
listimpar = []
while True:
    listnum.append(int(input('Insira um valor para a lista: ')))
    user = str(input('Deseja inserir outro valor [S/N]? '))
    if user in 'Nn':
        break
listnum.sort()
for val in listnum:
    if val % 2 == 0:
        listpar.append(val)
    else:
        listimpar.append(val)

print('-='* 30)
print(f'Os valores digitados foram {listnum}.')
print(f'Os valores pares são {listpar}')
print(f'Os valores ímpares são {listimpar}')