# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla
# No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os numeros pares

numeros = (int(input('Insira um valor: ')), int(input('Insira um valor: ')), int(input('Insira um valor: ')),
           int(input('Insira um valor: ')))

tot_tupl = len(numeros)
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
print('Os valores pares digitados são: ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
