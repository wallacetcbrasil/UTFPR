# Condição:
# uso de f-strings, math.tan(), math.inf -math.inf
# seno cosseno tangente estao com valores errados?

import math as m

g = 0

print(f"{'Graus':>9} {'Radianos':>9} {'Seno':>9} {'Cosseno':>9} {'Tangente':>9}")

for i in range(13):

    def graus(g=f'{g:.2f}', rad=f'{m.radians(g):>.2f}', sen=f'{m.sin(g):>.2f}',  cos=f'{m.cos(g):>.2f}', tan=f'{m.tan(g):>.2f}'):

        print(f'{g:9.2f}', end='')
        print(f'{rad:>9}', end='')
        print(f'{sen:>9}', end='')
        print(f'{cos:>9}', end='')
        print(f'{tan:>9}', end='')
 
    graus(g)
    g =+ g + 30
    print()