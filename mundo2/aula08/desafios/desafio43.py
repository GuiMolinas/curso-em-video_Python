print('\033[1;33mLados de um triângulo\033[m')

l1 = float(input('Insira o valor da primeira reta = '))
l2 = float(input('Insira o valor da segunda reta = '))
l3 = float(input('Insira o valor da terceira reta = '))

if(l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    print('Com essas retas, pode-se formar um triângulo')

    if(l1 == l2 == l3):
        print('O triângulo é \033[1mEQUILÁTERO!\033[m')
    elif(l1 == l2 or l2 == l3 or l1 == l3):
        print('O triângulo é \033[1mISÓSCELES!\033[m')
    else:
       print('O triângulo é \033[1mESCALENO!\033[m')
else:
    print('Com essas retas, não pode-se formar um triângulo')

