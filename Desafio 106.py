from time import sleep

def pyhelp():
    valor = ''
    while True:
        print('='*30)
        print('{}'.format('SISTEMA PYHELP'.center(30)))
        print('=' * 30)
        valor = input('Função ou Biblioteca > ')
        if 'fim' in valor:
            print('='*30)
            print('PROGRAMA FINALIZADO')
            break
        sleep(0.5)
        print('=' * 40)
        print('{}, "{}"'.format('ACESSANDO O MANUAL DO COMANDO'.center(40), valor))
        print('=' * 40)
        sleep(0.5)
        help(valor)


pyhelp()