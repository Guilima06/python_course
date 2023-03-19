# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. desconsiderando os espaços
# Palindromo é quando a frase ao contrario tem a mesma estrutura ex: apos a sopa
# frase = str(input('Insira uma frase: ')).replace(' ', '')
frase = 'abc abc abc'.replace(' ', '')
tam = len(frase)
print(tam)
# print(frase[8:9])
invert = ''
for c in range(tam+1, 0, -1):
    invert += frase[c-1:c]
    print(invert)
if invert == frase:
    print('a frase é um palindromo')
else:
    print('não entendi nada')