print('Número primo')

print('=+=' * 20)

n = int(input('Insira um numero inteiro aqui = '))

if (n > 1):
    for i in range(2, int(n**0.5)+1):
        if(n % i == 0):
            print('O número {} NÃO é primo'.format(n))
            break
    else:
        print('O número {} é primo'.format(n))

else:
    print('O número {} NÃO é primo'.format(n))
