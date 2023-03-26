#crie um programa que leia varios numeros inteiros pelo teclado. no final da execuçao, mostre a média entre todos os
#valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuário se ele quer ou não
#continuar a digitar valores.
cont = 0
soma = 0
num = int(input('Insira um número inteiro: '))
maior = num
menor = num
seguir = 'S'
while seguir == 'S':
    cont += 1
    soma += num
    if num > maior:
        maior = num
        print(maior)
    if num < menor:
        menor = num
        print(menor)
    seguir = str(input('Deseja seguir?\n[S] para sim e [N] para não: ')).upper()
    while seguir != 'S' and seguir != 'N':
        seguir = str(input('Opção inválida!\nDeseja seguir?\n[S] para sim e [N] para não: ')).upper()
    if seguir == 'S':
        num = int(input('Insira um número inteiro: '))
print('Foram digitadados {} números, a soma entre eles é {}, {} é o maior número, {} é o menor número e a média dos '
      'números é {}'.format(cont, soma,maior,menor, soma/cont))
