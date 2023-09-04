#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
#correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.

listanum = []
valor = 0
for val in range(0,5):
    valor = int(input('Insira um valor na lista: '))
    if val == 0 or valor > listanum[-1]:
        listanum.append(valor)
    else:
        pos = 0
        while pos < len(listanum):
            if valor <= listanum[pos]:
                listanum.insert(pos,valor)
                break
            pos += 1
print(listanum)