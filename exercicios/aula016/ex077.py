# Crie um programa que tenha uma tupla com varias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra. quais são as suas vogais.
palavras = ('TESTE', 'PROGRAMA', 'CURSO', 'TRABALHO')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end=' ')
    for letra in palavra:
            if letra.lower() in 'aeiou':
                print(letra, end=' ')
