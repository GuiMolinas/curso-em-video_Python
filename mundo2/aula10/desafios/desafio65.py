n = 0
quantidade = 0
soma = 0

while(n != 999):
    n = int(input('Digite um número inteiro = '))
    quantidade += 1
    soma += n
    

    if(n == 999):
        soma -= 999
        quantidade -= 1

print('A soma dos {} números digitados foi = {}'.format(quantidade, soma))