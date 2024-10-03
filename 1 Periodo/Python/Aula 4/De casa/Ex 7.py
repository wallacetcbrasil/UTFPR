# Condições :
# Loop que recebe valores inteiros
# 0 acaba com o programa, se for negativo é ignorado
# contador de numero valido
# armazena o maior numero 
# ao finalizar informa quantidade de numeros e qual foi o maior
# continue e break

Condicao = 1
Contador = 0
Maior = 0

while Condicao != 0:
    n = int(input('Digite um número inteiro positivo:'))
    if n == 0:
        print(f'Foi digitado {n}, encerrando...')
        Condicao == 0
        break
    elif n > 0:
        if n > Maior:
            Maior = n
        else:
            continue
        Contador += 1
    else:
        print(f'{n} é negativo. Será ignorado...')
        continue

if Contador == 0:
    print('Não foi digitado nenhum número valido')
elif Contador == 1:
    print('Foi digitado somente um número válido')
    print(f'O maior número valido digitado foi {Maior}')
else:
    print(f'Foi digitado somente {Contador} número válido')
    print(f'O maior número valido digitado foi {Maior}')
