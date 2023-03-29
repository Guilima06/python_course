#Melhore o desafio 061, perguntando para o usuários se ele quer mostrar mais algus termos. O programa encerra
#quando ele disser que quer mostrar 0 termos.

p1 = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
num_termos = int(input('Quantos termos deseja que sejam exibidos?: '))
while num_termos != 0:
    print('{} '.format(p1), end='-> ')
    p1 += razao
    num_termos = num_termos - 1
    if num_termos == 0:
        num_termos = int(input('fim\nSe desejar ver mais termos, digite a quantidade de termos, se não, digite 0: '))
print('fim')
