n = int(input('Insira um número aqui = '))

u = n //1 % 10
d = n //10 % 10
c = n //100 % 10
m = n //1000 % 10

print('O número digitado tem:\nUnidades: {}\nDezenas: {}\nCentenas: {}\nMilhares: {}'.format(u,d,c,m))