print('Soma dos impares')

s = 0

for c in range(1,501):
    if(c % 2 != 0):
        if(c % 3 == 0):
            s += c

print('A soma dos múltiplos de 3 nesse intervalo é = {}'.format(s))
    