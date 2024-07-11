print('FATORIAL')

print('+=+' * 10)

n = int(input('Insira um número inteiro aqui = '))

print('+=+' * 10)

fat = 1

while(n != 1):
    print('{}'.format(n), end='')
    print(' x ' if n > 2 else ' = ', end='')
    fat *= n
    n -= 1

print('\nFATORIAL = {}'.format(fat))