def distância(x1,y1,x2,y2):
    import math as m
    
    dis = m.sqrt(((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1)))
    print(f'Distância entre ({x1},{y1}) e ({x2},{y2}) = {dis:.2f}')

distância(3,-3,5,-5)