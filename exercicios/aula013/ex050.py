# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
# Se o va lor digitado for ímpar, desconsidere-o
soma_pares = 0
for num in range(0, 6):
    num_user = int(input('Insira um número ineiro: '))
    if num_user %2 == 0:
        soma_pares += num_user
print(soma_pares)