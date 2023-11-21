import math as m

def tabela_Raiz(inicio = 1, fim = 11, passo = 1): 
    for i in range(inicio,fim,passo):
        valor = i
        raizV = m.sqrt(i)
        print(f"{i:^7} {raizV:^15.3f}")


print(f"{'valor':^7} {'raiz do valor':^15}")
tabela_Raiz()