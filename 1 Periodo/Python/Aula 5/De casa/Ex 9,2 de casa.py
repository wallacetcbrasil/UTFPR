def imprime_galho(n, max=11, car='*'):
    print(f'{car*n:^{max}}')

imprime_galho(1, car='@')

for i in range(3,6,2):
    imprime_galho(i)

for i in range(3,11,2):
    imprime_galho(i)

for i in range(5,11,2):
    imprime_galho(i)

for i in range(7,12,2):
    imprime_galho(i)

imprime_galho(3, car='|')
imprime_galho(5, car='|')
imprime_galho(11, car='=')