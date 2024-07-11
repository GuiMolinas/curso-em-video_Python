f = input('Digite algo = ').strip()

print('A letra A aparece {} vezes.'.format(f.upper().count('A')))
print('Ela aparece a primeira vez na {} posição.'.format(f.upper().find('A')+1))
print('Ela aparce a última vez na {}° posição.'.format(f.upper().rfind('A')+1))