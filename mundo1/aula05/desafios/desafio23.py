n = input('Insira seu nome = ').strip()

print('Seu nome com letras maiusculas fica = {}'.format(n.upper()))
print('Seu nome com letras minusculas fica = {}'.format(n.lower()))

print('Seu nome possui {} letras sem considerar espaços'.format(len(n.replace(' ', ''))))
dividido = n.split()
print('Seu primeiro nome possui {} letras.'.format(len(dividido[0])))