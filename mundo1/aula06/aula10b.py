n1 = float(input('Insira a primeira nota = '))
n2 = float(input('Insira a segunda nota = '))

m = (n1+n2)/2

print('Sua média foi: {:.2f}'.format(m))

if(m >= 6):
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')