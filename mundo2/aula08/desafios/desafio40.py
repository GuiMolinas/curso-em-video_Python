from datetime import date

print('\033[1;32mAlistamento Militar\033[m')

nasc = int(input('Insira o ano em que você nasceu = '))

idade = date.today().year - nasc

if(idade == 18):
    print('Chegou a idade de se alistar!')
elif(idade > 18):
    print('Passou o tempo do seu alistamento em {} anos.'.format(idade - 18))
else:
    print('Faltam {} anos para se alistar! Fique atento.'.format(18 - idade))
