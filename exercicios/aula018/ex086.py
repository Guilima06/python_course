#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
#No final mostre a matriz na tela com a formatação correta
matriz = [[], [], []]
for lin in matriz:
    for i in range(0, 3):
        lin.append(int(input(f'Digite um valor para [{i}]: ')))
    print(lin)
print(matriz[0])
print(matriz[1])
print(matriz[2])