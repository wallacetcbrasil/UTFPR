n = 4 

lista = [x for x in range(1,n+1)]

lista += [x for x in lista[-2::-1]]

str = ['* '*x for x in lista+lista]

for s in str:
    print(f'{s}')