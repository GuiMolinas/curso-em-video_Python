print('\033[1;31mComparador de números\033[m')

n1 = int(input('Insira o primeiro número inteiro = '))
n2 = int(input('Insira o segundo número inteiro = '))

if(n1 == n2):
    print('Os dois números digitador são iguais!')
elif(n1 > n2):
    print('{} é o maior número!'.format(n1))
else:
    print('{} é o maior número!'.format(n2))