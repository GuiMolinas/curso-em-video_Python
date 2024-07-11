pessoa = 1
cont = maior = homem = mulheres = 0


while True:
    print(f'Pessoa {pessoa}')
    idade = int(input('Digite sua idade = '))
    sexo = str(input('Digite seu sexo (M/F) = ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('='*20)
        print('Digite uma opção válida!')
        break
    continua = str(input('Deseja continuar? (S/N) = ')).strip().upper()
    if continua != 'S' and continua != 'N':
        print('='*20)
        print('Digite uma opção válida!')
        break
    print('='*20)
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if continua == 'N':
        break
    pessoa += 1
        
print('='*20)
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulheres} tem menos de 20 anos.')