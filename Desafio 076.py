prodEPrecos = ('Lápis', 1.75, 'Borracha', 2.00, "Caderno", 15.90, 'Estojo', 25.00,
               'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
               'Livro', 34.90)
print('='*35)
print('LISTAGEM DE PREÇOS'.center(35))
print('='*35)
for c in range(len(prodEPrecos)):
    if c % 2 == 0:
        print('{:.<30}'.format(prodEPrecos[c]),end='')
    else:
        print(prodEPrecos[c])
print('='*35)
