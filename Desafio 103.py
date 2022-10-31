def ficha(qtdGols=0, nome='Desconhecido'):
    return 'O jogador {} fez {} gol(s) no campeonato'.format(nome, qtdGols)


nome = input('Nome do jogador: ').strip()
qtdGols = input('Número de gols: ').strip()
if qtdGols.isnumeric():
    int(qtdGols)
else:
    qtdGols = 0
    
if nome == '':
    print(ficha(qtdGols))
elif nome == ' ':
    print(ficha(qtdGols))
else:
    print(ficha(qtdGols, nome))

