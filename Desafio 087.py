matriz = [[], [], []]
somaPares = somaColuna3 = maiorLinha2 = 0
for c in range(3):
    for d in range(3):
        numero = int(input('Digite um valor para [{}, {}] '.format(c, d)))
        matriz[c].append(numero)
print('='*25)
for c in range(3):
    for d in range(3):
        print('|{:^5}|'.format(matriz[c][d]), end='')
        if matriz[c][d] % 2 == 0:
            somaPares += matriz[c][d]
    print()
print('='*25)
somaColuna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
maiorLinha2 = max(matriz[1][0], matriz[1][1], matriz[1][2])
''' PEGANDO O MAIOR DA LINHA 2 SEM USAR O max()
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    maiorLinha2 = matriz[1][0]
elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    maiorLinha2 = matriz[1][1]
elif matriz[1][2] > matriz[1][1] and matriz[1][2] > matriz[1][0]:
    maiorLinha2 = matriz[1][2]
'''
print('A soma dos valores pares é {}'.format(somaPares))
print('A soma dos valores da terceira coluna é {}'.format(somaColuna3))
print('A soma dos valores da segunda linha é {}'.format(maiorLinha2))

