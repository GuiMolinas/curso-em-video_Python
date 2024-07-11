l = float(input('Digite a largura em metros: '))
a = float(input('Digite a altura em metros: '))
a = l * a
t = int(a/2)
print('A área da parede é {:.2f}m2 e serão necessárias {} latas de tinta para pintá-la'.format(a,t))