## Arrumar

def imprime_tabela():
    fahrenheit = 0

    # ERRO - provavelmente em chamar a variavel
    def celsius(fahrenheit):

        cel = (fahrenheit-32) * 5/9 
    #

    print(f"{'Fahrenheit':>12} {'Celsius':>12}")

    for i in range(0, 310, 10):
        
        print(f'{fahrenheit:12}', f'{celsius(fahrenheit):12}')
        fahrenheit += 10

imprime_tabela()