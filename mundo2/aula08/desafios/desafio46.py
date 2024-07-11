from random import randint

print('\033[1;35mJOKENPÔ\033[m')

print('Escolha uma das opções a seguir:\n1 - Pedra\n2 - Papel\n3 - Tesoura')
player = int(input(('Sua escolha = ')))

comp = randint(1,3)

if(player == 1 and comp == 1):
    print('Sua escolha = Pedra\nMinha escolha = Pedra')
    print('\033[1mEmpatamos!\33[m')

elif(player == 1 and comp == 2):
    print('Sua escolha = Pedra\nMinha escolha = Papel')
    print('\033[1mVocê perdeu!\033[m')

elif(player == 1 and comp == 3):
    print('Sua escolha = Pedra\nMinha escolha = Tesoura')
    print('\033[1mVocê ganhou!\033[m')


if(player == 2 and comp == 1):
    print('Sua escolha = Papel\nMinha escolha = Pedra')
    print('\033[1mVocê ganhou!\33[m')

elif(player == 2 and comp == 2):
    print('Sua escolha = Papel\nMinha escolha = Papel')
    print('\033[1mEmpatamos!\033[m')

elif(player == 2 and comp == 3):
    print('Sua escolha = Papel\nMinha escolha = Tesoura')
    print('\033[1mVocê perdeu!\033[m')   


if(player == 3 and comp == 1):
    print('Sua escolha = Tesoura\nMinha escolha = Pedra')
    print('\033[1mVocê perdeu!\33[m')

elif(player == 3 and comp == 2):
    print('Sua escolha = Tesoura\nMinha escolha = Papel')
    print('\033[1mVocê ganhou!\033[m')

elif(player == 3 and comp == 3):
    print('Sua escolha = Tesoura\nMinha escolha = Tesoura')
    print('\033[1mEmpatamos!\033[m') 