#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor
#valor digitado e as suas respectivas posições na lista

list = []
maior = 0
menor = 0
pos_maior = 0
pos_menor = 0

for i in range(0, 5):
    list.append(int(input('insira um valor: ')))
    if i == 0:
        maior = menor = list[i]
        pos_maior = pos_menor = i
    else:
        if list[i] > maior:
            maior = list[i]
            pos_maior = i
        if list[i] < menor:
            menor = list[i]
            pos_menor = i

for pos, val in enumerate(list):
    if val == maior:
        print(pos)

print(list)
print(f'o maior valor é {maior} e está na posição {pos_maior}, o menor valor é {menor} e está na posição {pos_menor}')
# for c, v in enumerate(list):
#     if v

# print(list)
# print(f'O menor valor é {list[0]} e o maior valor é {list[-1]}')
