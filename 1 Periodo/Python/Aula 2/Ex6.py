# Escreva um programa que receba a digitação pelo teclado de dois número inteiros e informe se o segundo é múltiplo do primeiros 
# Seu programa deverá solicitar a digitação dois números ao usuário
# O moodle validará seu programa executando-o repetidas vezes, simulando a digitação do usuário com valores diferentes para os dois números a cada vez

primeiroNumero = int(input('Digite o primeiro inteiro: '))
segundoNumero = int(input('Digite o segundo inteiro: '))

if segundoNumero%primeiroNumero == 0:
    print(segundoNumero, 'é múltiplo de', primeiroNumero)
else:
    print(segundoNumero, 'não é múltiplo', primeiroNumero)