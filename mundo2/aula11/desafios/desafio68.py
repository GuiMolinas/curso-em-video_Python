n = cont = 0

while True:
    n = int(input('Insira um número para a tabuada (n° negativo para sair) = '))
    if n < 0:
        break
    
    print('='*20)
    print(f'Tabuada do {n}')
    
    while cont <= 10:
        mult = n * cont
        print(f'{n} x {cont} = {mult}')
        cont += 1
    cont = 0
    print('='*20)

print('==== FIM ===')