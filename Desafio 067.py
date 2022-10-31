while True:
    numero = int(input('Digite um número (PARA FINALIZAR DIGITE UM VALOR NEGATIVO): '))
    if numero > -1:
        for c in range(0, 11):
            print('{} X {} = {}'.format(numero, c, numero*c))
        print('-'*25)
    else:
        break
        