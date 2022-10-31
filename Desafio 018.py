import math
ang = float(input('Digite o valor do ângulo: '))
senoAng = math.sin(math.radians(ang))
cossAng = math.cos(math.radians(ang))
tanAng = math.tan(math.radians(ang))
print('Seno: {:.2f}'.format(senoAng))
print('Cosseno: {:.2f}'.format(cossAng))
print('Tangente: {:.2f}'.format(tanAng))