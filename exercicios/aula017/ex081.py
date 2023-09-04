#Crie um programa que vai ler vários números e colocar em uma lista. depois disso, mostre:
#A) Quantos números foram digitados.  B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

listanum = []
while True:
    listanum.append(int(input('Insira um valor na lista: ')))

    resp = str(input('Deseja inserir outro número? Digite S/N: '))
    if resp in 'Nn':
        break
listanum.sort(reverse=True)
print('-=' * 30)
print(f'A) Foram digitados {len(listanum)} valores')
print(f'Os valores digitados foram {listanum}')
if 5 in listanum:
    print(f'O valor 5 foi digitado e está na lista')
else:
    print(f'O valor 5 Não foi digitado, portanto não está na lista')