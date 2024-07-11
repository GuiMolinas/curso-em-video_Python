print('\033[1;31mÍndice de Massa Corporal\033[m')

kg = float(input('Insira seu peso aqui = '))
m = float(input('Insira sua altura aqui = '))

imc = kg/(pow(m, 2))

print('IMC = {:.1f}'.format(imc))

if(imc < 18.5):
    print('Você está abaixo do peso!')
elif(imc >= 18.5 and imc < 25):
    print('Você está no peso ideal!')
elif(imc >= 25 and imc < 30):
    print('Você tem sobrepeso!')
elif(imc >= 30 and imc < 40):
    print('Você possui obesidade. Cuidado!')
else:
    print('Você possui obesidade mórbida. Cuidado!')