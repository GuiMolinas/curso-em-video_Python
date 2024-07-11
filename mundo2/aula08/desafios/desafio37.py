print('\033[1;34mEmpréstimo bancário\033[m')
casa = float(input('Insira o valor da casa (R$) = '))
salario = float(input('Insira o seu salário (R$) = '))
ano = int(input('Insira em quantos anos pretende pagar = '))

prestacao = casa/(ano * 12)

porcentagem  = salario * 0.3

print('Valor da prestação/mês = R$ {:.2f}'.format(prestacao))
print('30% do salário = R$ {:.2f}'.format(porcentagem))

if(prestacao > porcentagem):
    print('Seu empréstimo foi negado! A prestação da casa ultrapassou 30% do seu salário')
else:
    print('Seu empréstimo foi aprovado!')
