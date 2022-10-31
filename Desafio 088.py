from random import randint
from time import sleep
listaMegaSena = []
listaCobaia = []
print('='*25)
print('{:^25}'.format('MEGA SENA'))
print('='*25)
flag = int(input('Quantos jogos você quer sortear? '))
for c in range(flag):
    for d in range(6):
        while True:
            numero = randint(0, 60)
            if numero not in listaCobaia:
                listaCobaia.append(numero)
                break
    listaMegaSena.append(listaCobaia[:])
    listaCobaia.clear()
print('='*25)
print('SORTEANDO {} JOGOUS'.format(flag))
print('='*25)
for c in range (len(listaMegaSena)):
    print('Jogo {}: {}'.format(c+1, sorted(listaMegaSena[c])))
    sleep(0.5)
print('='*25)
print('SORTEIO FINALIZADO!')
