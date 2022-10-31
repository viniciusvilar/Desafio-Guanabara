jogadorDados = dict()
listaGols = list()
jogadorDados['nome'] = input('Nome do jogador: ')
jogadorDados['gols'] = 0
jogadorDados['totalGols'] = 0
flag = int(input('Quantas partidas {} jogou: '.format(jogadorDados['nome'])))
for c in range(flag):
    qtdGols = int(input('Quantos gols na partida {}: '.format(c+1)))
    jogadorDados['totalGols'] += qtdGols
    listaGols.append(qtdGols)
jogadorDados['gols'] = listaGols[:]
print('='*25)
#parte 1
print(jogadorDados)
print('='*25)

#parte 2
print('Nome do jogador: {}'.format(jogadorDados['nome']))
print('Gols em partidas: {}'.format(jogadorDados['gols']))
print('Total de gols: {}'.format(jogadorDados['totalGols']))

print('='*25)
#parte 3
print('O jogador {} jogou {} partidas.'.format(jogadorDados['nome'], len(jogadorDados['gols'])))
for c in range(len(jogadorDados['gols'])):
    print('Na partida {}, fez {} gols.'.format(c+1, jogadorDados['gols'][c]))
print('Foi um total de {} gols'.format(jogadorDados['totalGols']))
print('='*25)