from time import sleep

print('\033[32mContagem regressiva:\033[m')

for c in range(10,-1,-1):
    print(c)
    sleep(0.5)
print('\033[1;34mFELIZ ANO NOVO!\033[m')