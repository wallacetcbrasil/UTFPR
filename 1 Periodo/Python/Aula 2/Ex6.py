# Escreva um programa que receba a digitação pelo tecladode dois número inteiros e informe se o segundo é multiplo do primeiros 
# Seu programa deverá solicitar a digitação dois números ao usuário
# O moodle validará seu programa executando-o repetidas vezes, simulando a digitação do usuario com valores diferentes para os dois numeros a cada vez

primeiroNumero = int(input('Digite o primeiro inteiro: '))
segundoNumero = int(input('Digite o segundo inteiro: '))

if segundoNumero%primeiroNumero == 0:
    print(segundoNumero, 'é multiplo de', primeiroNumero)
else:
    print(segundoNumero, 'não é múltiplo', primeiroNumero)