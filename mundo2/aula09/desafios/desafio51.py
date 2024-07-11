print('Soma dos números')

print('=+=' * 20)

s = 0

for i in range(1,7):
    print('{}° número'.format(i))
    n = int(input('Insira um número inteiro = '))
    if(n % 2==0 ):
        s += n

print('A soma dos números pares digitados é = {}'.format(s))