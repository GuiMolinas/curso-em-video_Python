n1 = int(input('Insira o primeiro número inteiro = '))
n2 = int(input('Insira o segundo número inteiro = '))
n3 = int(input('Insira o terceiro número inteiro = '))

if(n1 > n2 and n1 > n3):
    maior = n1
elif(n2 > n1 and n2 > n3):
    maior = n2
else:
    maior = n3

if(n1 < n2 and n1 < n3):
    menor = n1
elif(n2 < n1 and n2 < n3):
    menor = n2
else:
    menor = n3

print('O maior número digitado foi {} e o menor foi {}'.format(maior,menor))