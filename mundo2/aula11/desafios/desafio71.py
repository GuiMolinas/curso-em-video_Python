
preco = total = mais = 0
barato = float('inf')

while True:
    n = str(input('Digite o nome do produto = '))
    preco = float(input('Digite o preço do produto (R$) = '))
    continua = str(input('Deseja prosseguir? (S/N) = ')).strip().upper()
    if continua != 'S' and continua != 'N':
        continua = str(input('Deseja prosseguir? (S/N) = ')).strip().upper()
    print('='*20)
    total += preco
    if preco > 1000:
        mais += 1
    if preco < barato:
        nomeBarato = n
        barato = preco
    if continua == 'N':
        break

print(f'Total da compra = R${total:.2f}')
print(f'{mais} produtos custam mais de R$1000,00.')
print(f'{nomeBarato} é o produto mais barato que custa R${barato:.2f}.')