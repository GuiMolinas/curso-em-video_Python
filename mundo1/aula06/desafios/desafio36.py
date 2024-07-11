l1 = float(input('Insira o valor da primeira reta = '))
l2 = float(input('Insira o valor da segunda reta = '))
l3 = float(input('Insira o valor da terceira reta = '))

if(l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    print('Com essas retas, pode-se formar um triângulo')
else:
    print('Com essas retas, não pode-se formar um triângulo')