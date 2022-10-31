import math
catOpo = float(input('Cateto Oposto: '))
catAdj = float(input('Cateto Adjacente: '))
hip = math.hypot(catOpo, catAdj)
print('O valor da hipotenusa é {:.2f}'.format(hip))