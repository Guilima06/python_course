# Faça um proograma que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# ex: Ana maria de Souza
# primeiro = Ana
# Ultimo = Souza
nome = str(input('Insira seu nome completo: ')).title().strip()
n = nome.split()
print('Primeiro = {}'.format(n[0]))
print('Último = {}'.format(n[len(n) - 1]))
