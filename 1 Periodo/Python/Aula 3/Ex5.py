peso=int(input('Digite o peso do seu cão: '))
idade=int(input('Digite o idade do seu cão: '))

if idade <= 2 and peso <= 3:
    idadeHumana=idade*12.5 
    print('Classificação: Pequeno')
    print('Idade humana = ', idadeHumana)
elif idade > 2 and peso <= 3:
    idadeHumana=idade*5.2 
    print('Classificação: Pequeno')
    print('Idade humana = ', idadeHumana)

elif idade <= 2 and peso >= 10 and peso <= 23:
    idadeHumana=idade*10.5 
    print('Classificação: Médio')
    print('Idade humana = ', idadeHumana)
elif idade > 2 and peso >= 10 and peso <= 23:
    idadeHumana=idade*5.7
    print('Classificação: Médio')
    print('Idade humana = ', idadeHumana)

elif idade <= 2 and peso > 23:
    idadeHumana=idade*9
    print('Classificação: Grande')
    print('Idade humana = ', idadeHumana)
elif idade > 2 and peso > 23:
    idadeHumana=idade*7.8
    print('Classificação: Grande')
    print('Idade humana = ', idadeHumana)