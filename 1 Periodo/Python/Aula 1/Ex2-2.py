# Criar a identidade de euler com 15 casas decimais

import math

# Preencha abaixo o valor da constante PI com 15 casas decimais
PI = math.pi

# Preencha abaixo o valor da constante E com 15 casas decimais 
E = math.e
I = 1j

# Os dois prints a seguir servem para verificar se você preencheu os valores corretos das constantes:
print('PI vale', PI)
print('E vale', E)

# O print a seguir é para informar o que será feito:
print('Verificando a identidade de Euler:')

# Complete o print abaixo como está na bibliografia
print('0 = {:.2f}'.format(E**(PI*I) + 1))