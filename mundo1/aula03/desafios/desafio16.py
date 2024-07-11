km = float(input('Quantos km foram percorridos? - '))
d = int(input('Quantos dias o carro foi alugado? - '))
p = (60 * d) + (0.15 * km)
print('Você deve pagar R${:.2f}'.format(p))