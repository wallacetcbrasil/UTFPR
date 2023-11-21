def imprime_tabela(inicio = 0, fim = 301, passo = 10):
    f = passo
    fahrenheit = f - passo

    def celsius(fahrenheit):
        cel = (fahrenheit-32) * 5/9 
        return cel

    print(f"{'Fahrenheit':>12} {'Celsius':>12}")

    for i in range(inicio, fim, passo):
        print(f'{fahrenheit:12}', f'{celsius(fahrenheit):12.1f}')
        fahrenheit += passo

imprime_tabela()