from random import randint

print('Estou pensando em um número entre 0 e 5...')
p = int(input('Digite seu palpite = '))

n = randint(0,5)

if(p == n):
    print('Parabéns! Você acertou!')
else:
    print('Que pena, você errou! O número pensado foi {}'.format(n))

print('=== FIM ===')