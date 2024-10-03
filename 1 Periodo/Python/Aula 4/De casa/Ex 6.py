# Condições:
# Calcule a conversão de temperatura Fahrenheit para Celsius entre 0 a 100 com um salto de 10
# C x 9/5 + 32
# F-strings


contador = 0
Conversor = 0
Celsius = 0

while contador != 11:
    Fahrenheit = Celsius * 9/5 + 32
    print(f"{Celsius:3d} Celsius -> {Fahrenheit:>5.1f} Fahrenheit")
    Celsius += 10
    contador += 1

