# Faça um programa que leia duas notas de dois exames de um aluno, digitadas pelos usuário calcule a média e decida se o aluno foi aprovado ou deve fazer um prova final.
# Critério: se a média for >= 7 o aluno terá sido aprovado. Caso contrario deverá fazer a prova final.
# Seu programa deverá solicitar a digitação dos valores das duas notas ao usuário.
# O moodle validará seu programa executando-o repetidas vezes, simulando a digitação do usuário com valores diferentes para as duas notas a cada vez.

primeiraNota = float(input('Qual é sua primeira nota? '))
segundaNota = float(input('E a segunda nota? '))
media = (primeiraNota+segundaNota)/2
print('A média é', media)
if media >= 7.0:
    print('Passou direto!')
else:
    print('Ficou pra prova final :( ')