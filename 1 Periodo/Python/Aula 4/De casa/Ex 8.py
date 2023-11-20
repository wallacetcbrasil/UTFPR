# Condição:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# 9 linhas, 5 colunas
# Uma lista, um loop externo, um loop interno 

lines = [1, 2, 3, 4, 5, 4, 3, 2, 1]

for lin in lines:
    for col in range(lin):
        print('*',end=' ')
    print()




