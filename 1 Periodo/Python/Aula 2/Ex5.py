# Faça um programa que digita se um numero inteiro é par ou ímpar.
# Seu programa deverá solicitar a digitação do número ao usuário
# O moodle validará seu programa executando-o repetidas vezes, simulando a digitação do usuário com valores diferentes para o número a cada vez

numero=int(input('Digite um número inteiro:'))
imparOuPar = numero%2
if imparOuPar == 0:
    print('O numero digitado e par')
else:
    print('o numero digitado e impar')
