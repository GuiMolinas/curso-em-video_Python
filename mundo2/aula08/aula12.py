nome = str(input('Digite seu nome = ')).upper()

if(nome=='GUILHERME'):
    print('Que nome lindo!')
elif(nome=='MARIA' or nome=='PEDRO' or nome == 'JOÃO'):
    print('Seu nome é bem comum no Brasil!')
else:
    print('Meh...que nome normal.')

print('Tenho um bom dia, {}!'.format(nome))