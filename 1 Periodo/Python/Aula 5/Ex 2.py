import math

def raizes(n=0): 
    n = n+(10*i)
    calculo = n**(1/2)
    raiz = f'{calculo:.2f}'
    print(f'{n:>5}', end='   ')
    print(f'{raiz:>5}')

print('    n    raiz')
for i in range(11):
    raizes()