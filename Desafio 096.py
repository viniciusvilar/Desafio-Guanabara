def calcArea(larg, comp):
    a = comp * larg
    print('O terreno {}x{} é {}m2'.format(larg, comp, a))


print('='*15)
print('CALCULO DE ÁREA')
print('='*15)

larg = float(input('Informe a altura: '))
comp = float(input('Informe o cumprimeto: '))
calcArea(larg, comp)

