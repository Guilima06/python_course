#refaça o desavfio 009 mostrado a tabuada de un número que o usuário escolher, só que agora utilizando for
num = int(input('Insira um número para exibir a tabuada: '))
print('-'*12)
for valor in range(1, 11):
    print('{} x {} = {}'.format(num, valor, num*valor))
print('-'*12)