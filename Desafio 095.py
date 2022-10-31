jogadorDados = dict()
listaGols = list()
listaDadosJog = list()
flagTotal = ''
flag = 0

while "N" not in flagTotal:
    jogadorDados['nome'] = input('Nome do jogador: ')
    jogadorDados['gols'] = 0
    jogadorDados['totalGols'] = 0
    flag = int(input('Quantas partidas {} jogou: '.format(jogadorDados['nome'])))
    for c in range(flag):
        qtdGols = int(input('Quantos gols na partida {}: '.format(c+1)))
        jogadorDados['totalGols'] += qtdGols
        listaGols.append(qtdGols)
    flagTotal = input('Quer continuar [S/N]: ').strip().upper()
    jogadorDados['gols'] = listaGols[:]
    listaDadosJog.append(jogadorDados.copy())
    jogadorDados.clear()
    listaGols.clear()
    print('='*25)
#print(listaDadosJog)
print('{:<5} {:<15} {:<10} {:<}'.format('cod', 'nome', 'gols', 'total'))
print('_'*40)
for c in range(len(listaDadosJog)):
    print('{:<5} {:<15} {:<10} {:<}'.format(str(c), str(listaDadosJog[c]['nome']), str(listaDadosJog[c]['gols']), str(listaDadosJog[c]['totalGols'])))
print('_'*40)
while flag != 998:
    mostrarDado = int(input('Mostrar dados de qual jogador? '))
    if mostrarDado >= len(listaDadosJog):
        if mostrarDado == 998:
            break
        else:
            print('ERRO! Não existe jogador com código {}! Tente novamente'.format(mostrarDado))
    else:
        print('_' * 40)
        print('LEVANTAMENTO DO JOGADOR {}'.format(listaDadosJog[mostrarDado]['nome']))
        for p, g in enumerate(listaDadosJog[mostrarDado]['gols']):
            print('No jogo {} fez {} gols.'.format(p, g))
        print('_' * 40)
