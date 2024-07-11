"""cont = 1

while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('\nFIM')"""

n = s = 0

while True:
    n = int(input('Digite um número aqui = '))
    if n == 999:
        break
    s += n

print('A soma dos números é {}'.format(s))