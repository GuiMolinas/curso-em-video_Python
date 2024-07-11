from datetime import date

print('Maior Idade')

print('=+=' * 20)

ano = 0
maior = 0
m = 0

for i in range(1,8):
    print('{}° Pessoa'.format(i))
    ano = int(input('Digite o ano em que você nasceu  = '))
    maior = date.today().year - ano

    if(maior >= 18):
        m += 1

print('Pessoas maiores de 18 anos = {}'.format(m))
print('Pessoas menores de idade = {}'.format(7-m))