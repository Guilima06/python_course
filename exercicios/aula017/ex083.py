#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
# expressão passada está com os parenteses abertos e fechados na ordem correta.
list_open = []
list_close = []
expression = str(input('Insira a expressão matemática que deseja calcular: '))
qtd_p1 = expression.count('(')
qtd_p2 = expression.count(')')
if qtd_p1 > qtd_p2:
    print(f'Existe um erro na expressão, falta o fechamento de parenteses')
elif qtd_p2 > qtd_p1:
    print(f'Existe um erro na epressão, um parentese não foi aberto')
open_parentese = 0
close_parentese = 0
for pos, valor in enumerate(expression):
    if valor == '(':
        list_open.append(pos)
    if valor == ')':
        list_close.append(pos)

print(list_open)
print(list_close)
for pos, valor in enumerate(list_open):
    close = list_close[pos]
    next_open = list_open[pos+1]
    if valor < close < next_open:
        print(f'Posição abertura do parentese {valor}')
        print(f'posição fechamento do parentese {close}')
        print(f'Posição próxima abertura do parentese {next_open}')












