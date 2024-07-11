print('Tabuada')
print('=+=' * 20)

n = int(input('Insira aqui um número inteiro = '))

m = 0

print('=+=' * 20)

for c in range(0,11):
    m = n * c
    print('{} x {} = {}'.format(n,c,m))

print('=== FIM ===')