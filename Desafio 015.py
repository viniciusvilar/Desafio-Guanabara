diaCarro = int(input('Quantos dias o carro ficou alugado? '))
kmCarro = float(input('Quantos Km o carro rodou? '))
valorCarro = (60 * diaCarro) + (0.15 * kmCarro)
print('O total a pagar é de R${:.2f}'.format(valorCarro))