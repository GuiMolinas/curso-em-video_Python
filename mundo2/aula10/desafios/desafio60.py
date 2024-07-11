choice = 0

print('CALCULADORA')

print('+=+' * 10)

n1 = int(input('Digite aqui o primeiro número = '))
n2 = int(input('Digite aqui o segundo número = '))

while choice != 5:

    print('+=+' * 10)

    print('SELECIONE UMA DAS OPÇÕES:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
    choice = int(input('Digite aqui = '))

    print('+=+' * 10)

    if(choice == 1):
        operacao = n1 + n2
        print('ESCOLHA: SOMAR')
        print('{} + {} = {}'.format(n1, n2, operacao))

    elif(choice == 2):
        operacao = n1 * n2
        print('ESCOLHA: MULTIPLICAR')
        print('{} x {} = {}'.format(n1, n2, operacao))

    elif(choice == 3):
        if(n1 > n2):
            operacao = n1
        else:
            operacao = n2
        print('ESCOLHA: MAIOR')
        print('{} é o maior número.'.format(operacao))

    elif(choice == 4):
        print('ESCOLHA: NOVOS NÚMEROS')
        n1 = int(input('Digite aqui o primeiro número = '))
        n2 = int(input('Digite aqui o segundo número = '))
print('======= FIM DO PROGRAMA =======')