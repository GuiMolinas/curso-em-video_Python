from datetime import date

print('\033[1;44mConfederação Nacional de Natação\033[m')

nasc = int(input('Insira o ano em que você nasceu = '))

idade = date.today().year - nasc

print('SUA IDADE = {}'.format(idade))

if(idade <= 9):
    print('Você está na categoria: \033[1;34mMIRIM!\033[m')

elif(idade > 9 and idade <= 14):
    print('Você está na categoria: \033[1;34mINFANTIL!\033[m')

elif(idade > 14 and idade <= 19):
    print('Você está na categoria: \033[1;34mJUNIOR!\033[m')

elif(idade > 19 and idade <= 20):
   print('Você está na categoria: \033[1;34mSÊNIOR!\033[m') 

else:
   print('Você está na categoria: \033[1;34mMASTER!\033[m')  

