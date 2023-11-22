fila = []
print('Fila vazia:', fila)

# Chega João 
fila.append('João')

# Chega pedro e Paulo
print('Chegou joão:', fila)
lista = ['Pedro', 'Paulo']
fila.extend(lista)

print('Chegou Pedro e Paulo', fila)

# João foi atendido
fila.pop(0)

print('João foi atendido:', fila)

#Chega Maria
fila.append('Maria')

print('Chegou Maria:', fila)

#Chega Alice
fila.append('Alice')

print('Chegou Alice:', fila)

#Chega Joana 
fila.append('Joana')

print('Chegou Joana:', fila)

#Joana Desiste
fila.pop()

print('Joana desistiu:', fila)

# Maria também desiste
fila.pop(2)

print('Maria também desistiu:', fila)


print()