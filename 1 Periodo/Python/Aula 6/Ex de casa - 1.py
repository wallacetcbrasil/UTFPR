lista = [i for i in range(1,11)]

print('Lista original:', lista)

for i, num in enumerate(lista):
    lista[i] = num * num
print('Lista modificada:', lista) 