lista = ["maçã", "laranja", "abacate"]

try:
    index = int(input("Digite o índice da lista desejado:"))

    if type(index) == int and index > -4 and index < 3:
        print('O elemento de índice',index, 'é', lista[index])
    else:
        print(f"O elemento de índice {index} não existe!")
except ValueError or TypeError:
        print("Digite somente numeros inteiros")