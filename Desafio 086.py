matriz = [[], [], []]
for c in range(3):
    for d in range(3):
        numero = int(input('Digite um valor para [{}, {}] '.format(c, d)))
        matriz[c].append(numero)
for c in range(3):
    for d in range(3):
        print('|{:^5}|'.format(matriz[c][d]), end='')
    print()
