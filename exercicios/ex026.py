# Faça um programa que leia uam frase pelo teclado e mostre
# quantas vezes aparece a letra 'A'
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece a ultima vez
frase = str(input('Insira uma frase: ')).title().strip()
print(frase)
frase = frase.upper()
print(len(frase))
print('A letra A maiuscula aparece {} vezes'.format(frase.count('A')))
print('Aparece primeiro na posição {}'.format(frase.find('A')+1))
print('Aparece por último na posição {}'.format(frase.rfind('A')+1))