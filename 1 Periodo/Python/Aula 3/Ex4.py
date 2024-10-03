idade=int(input('Digite a idade da pessoa: '))

if idade >= 0 and idade <= 3:
    print('Classificação: bebê')
elif idade >= 4 and idade <= 7:
    print('Classificação: Criança')
elif idade >= 8 and idade <= 12:
    print('Classificação: Pré-adolescente')
elif idade >= 13 and idade <= 20:
    print('Classificação: Adolescente')
elif idade >= 21 and idade <= 40:
    print('Classificação: Jovem')
elif idade >= 41 and idade <= 64:
    print('Classificação: Meia-idade')
else:
    print('Classificação: Idoso')    