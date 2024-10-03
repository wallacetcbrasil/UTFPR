

def determina_conceito(nota):
    if nota > 10 or nota < 0:
        print('Nota invalida!')
    elif nota < 5:
        print('Seu conceito é E')
    elif nota >= 5 and nota < 7:
        print('Seu conceito é D')
    elif nota >= 7 and nota < 8:
        print('Seu conceito é C')
    elif nota >= 8 and nota < 9:
        print('Seu conceito é B')
    else:
        print('Seu conceito é A')