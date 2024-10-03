# Condição:
# Calcular a media dos valores digitados 
# 0 acaba com o calculo
# Somente numeros positivos 
# Comando while


Contador = 0
Controle = 1
Soma = 0
n = 0

while Controle != 0:

    n = int(input('Digite o número: (0 para terminar)'))

    if n > 0:
        Soma += n
        Contador += 1
    elif n == 0:
        Controle = 0
    else:
        print('Só é aceito numeros positivos')

media = Soma / Contador
print('A média dos', Contador, 'números digitados vale', media)