# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. desconsiderando os espaços
# Palindromo é quando a frase ao contrario tem a mesma estrutura ex: apos a sopa
# frase = str(input('Insira uma frase: ')).replace(' ', '')
frase = str(input('insira a frase: ')).replace(' ', '').upper()
print(frase)
tam = len(frase)
invert = ''
for c in range(tam - 1, -1, -1):
    invert += frase[c]
if invert == frase:
    print('Palindromo')
else:
    print('não é palindromo')
print(invert)