vel = int(input('Insira a velocidade do veiculo (km/h) = '))

if(vel > 80):
    print('Você foi multado!')
    multa = float(7.00 * (vel - 80))
    print('O valor a ser pago é R${:.2f}'.format(multa))
else:
    print('Parabéns! Continue sendo um bom motorista!')
print('=== FIM ===')