n = 0
continuar = ''
media = 0
i = 0
maior = n
menor = n

while(continuar != 'N'):
    n = int(input('Insira um número inteiro = '))
    i += 1
    media += n

    if i == 1:
        maior = menor = n
    
    else:
        if(n > maior):
            maior = n
        elif(n < menor):
            menor = n

    continuar = str(input('Deseja continuar? (S/N) = ')).strip().upper()

print('A média entre os números digitados é: {:.2f}'.format(float(media/i)))
print('O maior número foi = {}\nO menor número foi = {}'.format(maior, menor))

print('==== FIM ====')
