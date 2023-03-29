# refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# equilátero todos os lados iguais
# isósceles dois lados iguais
# escalento todos os lados diferentes
l1 = float(input('Informe um lado do triangulo: '))
l2 = float(input('Informe outro lado do triangulo: '))
l3 = float(input('Informe outro lado do triangulo: '))
if l1 > (l2 + l3) and l2 > (l1 + l3) and l3 > (l1 + l2):
    print('As medidas informadas não formam um triangulo')
elif l1 == l2 == l3:
    print('As medidas informadas formam um triangulo.')
    print('Este é um triângulo equilátero.')
elif l1 != l2 != l3 != l1:
    print('As medidas informadas formam um triangulo.')
    print('Este é um triângulo escaleno.')
else:
    print('As medidas informadas formam um triangulo.')
    print('Este é um triângulo isósceles.')
