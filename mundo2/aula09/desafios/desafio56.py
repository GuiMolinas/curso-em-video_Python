print('Maior e menor peso')

maior = 0
menor = float('inf')

print('=+=' * 20)

for i in range(1,6):
    print('Pessoa {}'.format(i))
    p = float(input('Insira seu peso aqui = '))

    if(p > maior):
        maior = p
    if(p < menor):
        menor = p

print('Menor peso = {} kg'.format(menor))
print('Maior peso = {} kg'.format(maior))