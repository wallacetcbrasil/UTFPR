a=int(input('Digite o valor do salário: '))

if (a<=1000):
    novoSalario=(a+((a*20)/100))
    print('Novo salário = ', novoSalario)
elif ((a>1000) and (a<=2000)):
    novoSalario=(a+((a*18)/100))
    print('Novo salário = ', novoSalario)
elif ((a>2000) and (a<=4000)):
    novoSalario=(a+((a*15)/100))
    print('Novo salário = ', novoSalario)
else:
    novoSalario=(a+((a*10)/100))
    print('Novo salário = ', novoSalario)