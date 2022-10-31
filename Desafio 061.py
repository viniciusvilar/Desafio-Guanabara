primTermo = int(input('Informe o primeiro termo da PA: '))
razaoPA = int(input('Informe a razão da PA: '))
print('Os termos da PA são:')
#print('Termo 1: {}'.format(primTermo))
c = 1
while c < 11:
    #print('Termo {}: {}'.format(c, primTermo))
    print(primTermo, end=' -> ')
    primTermo += razaoPA
    c += 1
print('FINALIZADO!')

