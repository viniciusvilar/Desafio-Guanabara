def escreva(msg):
    tam = len(msg) + 4
    print('='*tam)
    print('{}'.format(msg.center(tam)))
    print('=' * tam)


escreva('Edilma Maria')
escreva('Aprender a programar')
escreva('oi')

