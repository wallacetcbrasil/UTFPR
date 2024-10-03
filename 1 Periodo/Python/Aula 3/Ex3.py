l1=int(input('valor lado 1 '))
l2=int(input('valor lado 2 '))
l3=int(input("valor lado 3 "))

if (((l1==l2) and (l2==l3)) and (l1<l2+l3) and (l1<l2+l3) and (l2<l1+l3) and (l3<l1+l2)):
    print('o triangulo é equilátero')
elif (((l1==l2) or (l2==l3) or (l3==l1)) and (l1<l2+l3) and (l2<l1+l3) and (l3<l1+l2)):
    print('o triangulo é isósceles')
elif ((l1!=l2!=l3) and (l1<l2+l3) and (l1<l2+l3) and (l2<l1+l3) and (l3<l1+l2)):
    print('o triangulo é escaleno')
else:
    print('Não é um triângulo')