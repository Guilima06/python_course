# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso de zero até vinte. seu programa
# deverá ler um número pelo teclado (entre 0 e 20)) e mostrá-lo por extenso
import num2words

num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
numero = int(input('Insira um número entre 1 e 10: '))
print(num_extenso[numero])
# num_ptbr = num2words.num2words(numero, lang='pt-br')
# print(num_ptbr)