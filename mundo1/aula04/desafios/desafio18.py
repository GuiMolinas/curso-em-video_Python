from math import hypot

oposto = float(input('Insira o valor do cateto oposto = '))
adjacente = float(input('Insira o valor do cateto adjacente = '))

print('O valor da hipotenusa é {:.2f}'.format(hypot(oposto, adjacente)))