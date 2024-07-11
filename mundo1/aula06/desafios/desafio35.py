s = float(input('Insira seu salário aqui = '))

if(s > 1250):
    print('Você teve um aumento de 10%')
    a = s + (s * 0.1)
else:
    print('Você teve um aumento de 15%')
    a = s + (s * 0.15)

print('Seu novo salário é R${:.2f}'.format(a))