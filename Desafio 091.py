from random import randint
from time import sleep
jogadores = dict()
jogadoresOrganizados = dict()
listaCobaia = list()
p = 1
print('Valores sorteados:')
for c in range(4):
    numero = randint(0, 6)
    listaCobaia.append(numero)
    print('O jogador {} tirou {}'.format(c+1, numero))
    sleep(0.5)
    jogadores['Jogador{}'.format(c+1)] = numero
print('='*25)
listaCobaia = sorted(listaCobaia)
for c in range(4):
    for k, v in jogadores.items():
        if v == listaCobaia[c]:
            jogadoresOrganizados['{}'.format(k)] = v
print('Ranking dos jogadores:')
for k, v in jogadoresOrganizados.items():
    sleep(0.5)
    print('{}º lugar: {} com {} '.format(p, k, v))
    p += 1
