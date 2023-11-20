#Arrumar

def imprime_tabela():
    i = 0
    celsius = 0

    # ERRO
    def fahrenheit(celsius):
        F = celsius * 9/5 + 32
    #

    print(f"{'Celsius':>12} {'Fahrenheit':>12}")

    for i in range(11):
        print(f"{celsius:>12}, {fahrenheit(celsius):>12}")
        celsius += 10
        i += 1

imprime_tabela()