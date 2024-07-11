n = input('Digite o nome da sua cidade = ').strip()

dividido = n.split()

print('Sua cidade começa com o nome Santo? {}'.format('SANTO' in dividido[0].upper()))