# Escreva um programa que calcule a area de um triangulo, cujos valores da base e da altura deverão ser digitados pelo usuário, e mostre o resultado na tela, como no exemplo logo abaixo

# Seu programa deverá solicitar a digitação dos valores da base e da altura do triangulo ao usuario 

height = float(input('Digite a altura: '))
base = float(input('Digite a base: '))
area = base * height / 2
print('A area do triangulo de base', base, 'e altura', height, 'é', area)