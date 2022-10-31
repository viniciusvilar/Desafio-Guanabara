listaValores = []
listaValoresPar = []
listaValoresImpar = []
flag = ''
while 'N' not in flag:
    num = int(input('Digite um valor: '))
    flag = input('Deseja continuar [S/N]: ').strip().upper()
    listaValores.append(num)
    print('='*25)
for c in listaValores:
    if c % 2 == 0:
        listaValoresPar.append(c)
    else:
        listaValoresImpar.append(c)

print('A lista gerada foi: {}'.format(listaValores))
print('Lista dos pares: {}'.format(listaValoresPar))
print('Lista dos impares: {}'.format(listaValoresImpar))
