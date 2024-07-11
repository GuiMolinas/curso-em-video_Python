print('Pessoas')

print('=+=' * 20)

media = 0
velhoI = 0
velhoN = ''
menores = 0

for i in range(1,5):
    print('{}° Pessoa'.format(i))
    nome = str(input('Insira seu nome aqui = ')).capitalize()
    idade = int(input('Insira sua idade = '))
    sexo = str(input('Digite seu gênero (M/F) = ')).upper()
    
    media += idade

    if(sexo == 'M'):
        if(idade > velhoI):
            velhoI = idade
            velhoN = nome

    if(sexo == 'F'):
        if(idade < 20):
            menores += 1


    print('=+=' * 20)

print('A média das pessoas é = {:.2f}'.format(float(media/4)))
print('O homem mais velho se chama {}'.format(velhoN))
print('Existem {} mulheres menores que 20 anos.'.format(menores))

