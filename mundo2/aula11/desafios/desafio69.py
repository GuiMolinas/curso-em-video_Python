from random import randint

n = s = acertou = vitoria = 0

print('PAR OU ÍMPAR')
print('='*20)

while True:
    n = int(input('Digite um número inteiro aqui = '))
    parimpar = str(input('Par ou Ímpar? [P/I] = ')).strip().upper()
    if parimpar != 'P' and parimpar != 'I':
        parimpar = str(input('Par ou Ímpar? [P/I] = ')).strip().upper()
    else:
        print('='*20)
        comp = randint(0,10)
        s = n + comp
        print(f'Você digitou {n} e o computador escolheu {comp}. O Total foi {s} ', end = '')
        if s % 2 == 0:
            print('DEU PAR')
            acertou = 2
        else:
            print('DEU ÍMPAR')
            acertou = 1
        print('='*20)
        if (acertou == 1 and parimpar == 'P') or (acertou == 2 and parimpar == 'I'):
            print('Você PERDEU!')
            break
        elif (acertou == 1 and parimpar == 'I') or (acertou == 2 and parimpar == 'P'):
            print('Você GANHOU')
            vitoria += 1
            print('='*20)
print('='*20)

print(f'Fim de jogo! Você ganhou {vitoria} vezes.')
