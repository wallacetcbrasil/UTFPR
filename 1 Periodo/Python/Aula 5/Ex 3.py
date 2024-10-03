def numeros(n):
    n2 = n*n
    n3 = n*n*n
    print('n =', f'{n:.2f}', end='')
    print(', n'f'{0x00b2:c}', '=', f'{n2:.2f}', end='')
    print(', n'f'{0x00b3:c}', '=', f'{n3:.2f}')

n = int(input('Entre com o valor do números:'))

numeros(n)