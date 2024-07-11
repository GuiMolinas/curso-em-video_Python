from random import randint

print('ADIVINHE O NÙMERO')

print('+=+' * 10)

computer = randint(0,10)

palpite = -1

tentativa = 0

while palpite != computer:
    print('Tentativa {}'.format(tentativa + 1))
    palpite = int(input('Digite aqui seu palpite entre 0 e 10 = '))
    tentativa += 1
    print('+=+' * 10)

print('Parabéns! Você acertou em {} tentativas o número pensado'.format(tentativa))

