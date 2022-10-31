primTermo = int(input('Informe o primeiro termo da PA: '))
razaoPA = int(input('Informe a razão da PA: '))
print('Os termos da PA são:')
contadorTermos = 10
#print('Termo 1: {}'.format(primTermo))
for c in range(0, 10):
    print(primTermo, end=' -> ')
    primTermo += razaoPA
print('PAUSA!')
novosTermos = int(input('Quantos termos deseja ver novamente? '))
while novosTermos != 0:
    for c in range(0, novosTermos):
        print(primTermo, end=' -> ')
        primTermo += razaoPA
        contadorTermos += 1
    print('PAUSA!')
    novosTermos = int(input('Quantos termos deseja ver novamente? '))
print('Profressão finalizada com {} termos mostrados.'.format(contadorTermos))
