import math as m

def calcula_volume_cilindro(diâmetro = 1, altura = 1):
    r = diâmetro/2
    vol = m.pi*m.pow(r,2)*altura
    return vol

vol = calcula_volume_cilindro(3,5)
print(f'volume = {vol:5.2f}')
    