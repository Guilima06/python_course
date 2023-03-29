#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Insira um número: '))
n2 = num * 2
n3 = num * 3
rz_num = pow(num, (1/2))
print('O dobro de {} é {}\n'.format(num, n2), 'O triplo de {} é {} \n'.format(num, n3),'A raiz quandrade de {} é {:.2f}'.format(num, rz_num))
