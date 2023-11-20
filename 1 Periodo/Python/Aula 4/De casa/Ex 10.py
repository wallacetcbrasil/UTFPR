# Condição
# Imprimir 2 paralelogramas em sentidos opostos


n = int(input('Digite o valor do lado do paralelograma:'))

for i in range(n):
    print(f"{'*  '*n:>{n*3+i}}")

print()

for i in range(n):
    print(f"{'*  '*n:>{n*4-i}}")