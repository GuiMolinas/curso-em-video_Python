d = int(input('Digite a distância da viagem = '))

if(d <= 200):
    p = float(0.5 * d)
else:
    p = float(0.45 * d)
print('A distãncia é de {} km'.format(d))
print('O preço da viagem é R${:.2f}'.format(p))