# Condição:
# Recebe n (quantidade de asteriscos)
# Desenhar um quadrado com n de largura

n = int(input('Digite a quantidade de asteriscos por lado:'))

for i in range(n):
    print('*', end=' ')
print()

# Não entendi

for lin in range(n-2):       
    print('*', end=' ')    
    
    for col in range(n-2):      
        print(' ', end=' ')

    print('*', end='')
    print()     

for i in range(n):
    print('*', end=' ')










