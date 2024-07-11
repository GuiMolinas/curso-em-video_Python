print('Progressão Aritmética')
print('=+=' * 20)

p = int(input('Insira o primeiro termo da PA = '))
r = int(input('Insira a razão da PA = '))

u = p + 9 * r
u += 1

print('=+=' * 20)

print('Os primeiros 10 termos dessa PA são:')

i = p
while i < u:
    print(i)
    i += r

print('==== FIM ====')
