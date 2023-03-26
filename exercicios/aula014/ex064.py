#Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai para quando o usuário digitar
#o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e fual foi a
#soma entre eles (desconsiderando o flag)
cont = 0
soma = 0
num = int(input('Insira um número inteiro: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Insira um número inteiro: '))
print('Foram digitadados {} números e a soma entre eles é {}'.format(cont, soma))
