print('\033[1;36mConversão de bases numéricas\033[m')

num = int(input('Insira um número inteiro = '))

print('Escolha uma das opções:\n1 - Binário\n2 - Octal\n3 - Hexadecimal')
escolha = int(input('Insira aqui = '))

print('\033[1;36m=+=\033[m' * 20)

print('Número digitado = {}'.format(num))

if(escolha == 1):
    conv = bin(num)
    print('Número em binário = {}'.format(conv[2:]))
elif(escolha == 2):
    conv = oct(num)
    print('Número em octal = {}'.format(conv))
elif(escolha==3):
    conv = hex(num)
    print('Número em hexadecimal = {}'.format(conv))
else:
    print('ERROR. O número digitado não é uma escolha.\nPor favor, reinicie o prgrama')

