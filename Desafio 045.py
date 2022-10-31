import random, time
print('=' *25)
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
print('=' *25)
valJogador = ''
valComputador = ''
jogador = int(input('Faça sua jogada: '))
computador = random.randint(0, 2)
if jogador == computador:
    if jogador == 0:
        valJogador = 'PEDRA'
        valComputador = 'PEDRA'
    elif jogador == 1:
        valJogador = 'PAPEL'
        ValComputador = 'PAPEL'
    else:
        valJogador = 'TESOURA'
        valComputador = 'TESOURA'
    sit = 'EMPATE!'
elif jogador == 0 and computador == 1:
    valJogador = 'PEDRA'
    valComputador = 'PAPEL'
    sit = 'COMPUTADOR VENCEU!'
elif jogador == 0 and computador == 2:
    valJogador = 'PEDRA'
    valComputador = 'TESOURA'
    sit = 'JOGADOR VENCEU!'
elif jogador == 1 and computador == 0:
    valJogador = 'PAPEL'
    valComputador = 'PEDRA'
    sit = 'JOGADOR VENCEU!'
elif jogador == 1 and computador == 2:
    valJogador = 'PAPEL'
    valComputador = 'TESOURA'
    sit = 'COMPUTADOR VENCEU!'
elif jogador == 2 and computador == 0:
    valJogador = 'TESOURA'
    valComputador = 'PEDRA'
    sit = 'COMPUTADOR VENCEU!'
elif jogador == 2 and computador == 1:
    valJogador = 'TESOURA'
    valComputador = 'PAPEL'
    sit = 'JOGADOR VENCEU!'

print('=' *25)
print('O computador jogou: {}'.format(valComputador))
print('O jogador jogou: {}'.format(valJogador))
print('=' *25)
print(sit)