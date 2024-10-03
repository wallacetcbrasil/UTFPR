# Condições
# Receber um numero inteiro n e verifica-lo
# Somar os quadrados dos numeros de 1 a n-1
# Porém desta vez usando o método comprehension list

soma = 0

n = int(input('qual o número final?'))

if n <= 0:
    print('Use numeros positivos!')

else:
    soma = sum([i*i for i in range(1,n)])
    print('A soma dos quadrados de 1 a', n-1, '=', soma)
    print('Verificação: soma = ', soma)