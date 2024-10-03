# Condição:
# Receber um numero inteiro
# soma dos quadrado até n-1
# for e range

soma = 0
x = int(input("Qual o valor final?"))

for n in range(0,x):
    soma += n*n

print('A soma dos quadrados de 1 a', x, '=', soma)
print('Verificação: soma =', soma)