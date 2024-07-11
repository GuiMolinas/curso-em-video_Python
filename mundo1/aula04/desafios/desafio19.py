from math import cos, sin, tan, radians

n = float(input('Insira o valor do ângulo = '))

print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(sin(radians(n)), cos(radians(n)), tan(radians(n))))