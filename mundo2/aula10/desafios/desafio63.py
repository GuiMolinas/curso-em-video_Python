print('Progressão Aritmética')
print('=+=' * 20)

p = int(input('Insira o primeiro termo da PA = '))
r = int(input('Insira a razão da PA = '))

termo = p

cont = 1

total = 0

mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')

    mais = int(input('Quantos termos a mais você quer mostrar? = '))


print('=+=' * 20)
print('\nFim da PA.\nTotal de termos = {}'.format(total))

