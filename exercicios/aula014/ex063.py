#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos
#de uma sequencia de ficonacci. EX: 0 > 1 > 1 > 2 > 3 > 5 > 8
seq = int(input('Quantos termos você quer exibir da sequencia de fibonacci: '))
t1 = 0
t2 = 1
t3 = 0
contador = 0
while contador != seq:
    print('{}'.format(t1),end=' -> ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    contador += 1