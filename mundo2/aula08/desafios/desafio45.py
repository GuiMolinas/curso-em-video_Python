print('\033[1;33mLojinha :)\033[m')

preco = float(input('Insira o valor a ser pago (R$) = '))

print('Escolha uma das formar de pagamento:\n1 - À vista no dinheiro/cheque\n2 - À vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão')
opcao = int(input('Insira aqui = '))

if(opcao == 1):
    print('Você escolheu: À vista no dinheiro/cheque')
    print('Isso te dá 10% de desconto')
    valor = preco - (preco * 0.1)
    print('Valor à pagar: R$ {:.2f}'.format(valor))

elif(opcao == 2):
    print('Você escolheu: À vista no cartão')
    print('Isso te dá 5% de desconto')
    valor = preco - (preco * 0.05)
    print('Valor à pagar: R$ {:.2f}'.format(valor))

elif(opcao == 3):
    print('Você escolheu: 2x no cartão')
    print('O preço continua o mesmo')
    valor = preco
    print('Valor à pagar: R$ {:.2f}'.format(valor))

elif(opcao == 4):
    print('Você escolheu: 2x no cartão')
    print('Isso dá 20% de juros')
    valor = preco + (preco * 0.2)
    print('Valor à pagar: R$ {:.2f}'.format(valor))

else:
    print('Opção inválida! Por favor, reinicie o programa')




