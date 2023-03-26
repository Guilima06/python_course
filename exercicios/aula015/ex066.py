#Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usário digitar
#o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
#entre eles. (desconsiderando o flag)
n = 0
s = 0
c = 0
while True:
    n = int(input('Insira um número inteiro: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram inseridos {c} valores, a soma entre eles é {s}')