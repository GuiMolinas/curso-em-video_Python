n = cont = s = 0

while True:
    n = int(input('Digite um número aqui (999 para sair) = '))
    if n == 999:
        break
    
    s += n
    cont += 1
    
print(f'Você digitou {cont} números. A soma entre eles é {s}')