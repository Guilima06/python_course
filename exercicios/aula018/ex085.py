#Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista única que mantenha
#separado os valores pares e ímpares em ordem crescente.
valores = [[], []]

for i in range(0, 7):
    valor = (int(input('Insira um valor numérico qualquer: ')))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(valores)