# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia
# No Final, mostre uma listagem de preços, organizando os dados em forma tabular
produtos = ('Camiseta', 'R$50,00', 'Calça', 'R$100,00', 'Meias', 'R$10,00', 'Tênis', 'R$200,00')
tamanho_tupla = len(produtos)
print('-'*40)
print(' '*10, 'TABELA DE PREÇOS', ' '*10)
print('-'*40)
for c in range(0, 7, 2):
    print(f'{produtos[c]:.<30}', end='')
    print(f'{produtos[c+1]:>10}')