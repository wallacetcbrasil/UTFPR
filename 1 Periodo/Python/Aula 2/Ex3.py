# Escreva um programa que calcule a quantidade de segundos, apos meia-noite, dado o horario em horas, minutos e segundos - os valores do horário deverão ser digitados pelo usuário - e mostre o resultado na tela, como nos exemplos logo abaixo.
# Seu programa deverá solicitar a digitação dos valores de horas, minutos e segundos ao usuário.

horas=int(input('Digite o valor das horas:'))
horasEmMinutos = horas*60
horasEmSegundos = horasEmMinutos*60

minutos=int(input('Digite o valor dos minutos:'))
minutosEmSegundos= minutos*60

segundos = int(input('Digite o valor de segundos:'))
segundosTotais = int(horasEmSegundos + minutosEmSegundos + segundos)

print('Às', horas, ':', minutos, ':', segundos, 'h', segundosTotais, 'segundos terão transcorrido desde a meia-noite')
