print('CAIXA ELETRÔNICO')
print('='*20)

valor = int(input('Digite o valor que deseja sacar (R$) = '))

total = valor

ced = 50
totalCed = 0

while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'R${ced} = {totalCed} cédulas.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print('='*20)
print('Obrigado! Volte sempre ;)')

    
    