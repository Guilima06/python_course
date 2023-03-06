#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
#pinta uma área de 2m^2
largura_parede = float(input('Insira a largura da parede: '))
altura_parede = float(input(('Insira a altura da parede: ')))
area_parede = largura_parede * altura_parede
quantidade_tinta = area_parede / 2
print('A parede informada possui {:.2f}m de altura e {:.2f}m de largura, sendo necessário {:.2f}L de tinta para pintar '
      'por completo a parede.'.format(altura_parede, largura_parede, quantidade_tinta))
