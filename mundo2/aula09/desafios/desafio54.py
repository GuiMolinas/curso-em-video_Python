print('PALÍNDROMO')

print('=+=' * 20)

f = str(input('Digite uma frase aqui = ')).strip().upper()

palavras = f.split()

junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if(inverso == junto):
    print('{} é um palíndromo!'.format(f))

else:
    print('{} NÃO é um palíndromo!'.format(f))