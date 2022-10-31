import random
print('-'*25)
print('PAR OU IMPAR')
print('-'*25)
contVitoria = 0
while True:
    pComputador = random.randint(0, 10)
    pJogador = int(input('Digite um valor: '))
    parOuImpar = input('Par ou Impar [P/I]: ').strip().upper()
    if 'P' in parOuImpar:
        if (pComputador + pJogador) % 2 == 0:
            contVitoria += 1
            print('Você jogou {} e o computadpr {}. Total de {} DEU PAR!'.format(pJogador, pComputador, pJogador+pComputador))
            print('Você VENCEU!')
            print('Valor jogar novamente...')
            print('-'*25)
        else:
            print('Você jogou {} e o computadpr {}. Total de {} DEU IMPAR!'.format(pJogador, pComputador,
                                                                                 pJogador + pComputador))
            print('Você PERDEU!!')
            break
    else:
        if (pComputador + pJogador) % 2 != 0:
            contVitoria += 1
            print('Você jogou {} e o computadpr {}. Total de {} DEU IMPAR!'.format(pJogador, pComputador,
                                                                                 pJogador + pComputador))
            print('Você VENCEU!')
            print('Valor jogar novamente...')
            print('-' * 25)
        else:
            print('Você jogou {} e o computadpr {}. Total de {} DEU PAR!'.format(pJogador, pComputador,
                                                                                 pJogador + pComputador))
            print('Você PERDEU!!')
            break
print('GAME OVER! Você venceu {} vezes.'.format(contVitoria))