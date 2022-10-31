primTermo = int(input('Informe o primeiro termo da PA: '))
razaoPA = int(input('Informe a razão da PA: '))
print('Os termos da PA são:')
#print('Termo 1: {}'.format(primTermo))
for c in range(2, 12):
    #print('Termo {}: {}'.format(c, primTermo))
    print(primTermo, end=' -> ')
    primTermo += razaoPA
print('FINALIZADO!')

