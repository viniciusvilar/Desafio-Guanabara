from utilidades import moeda


preco = float(input('Digite o preço R$'))
print('A metade de {} é {}'.format(moeda.valFormat(preco), moeda.metade(preco, True)))
print('O dobro de {} é {}'.format(moeda.valFormat(preco), moeda.dobro(preco, True)))
print('Aumentando 10%, temos {}'.format(moeda.aumenta(preco, 10, True)))
print('Reduzindo 13%, temos {}'.format(moeda.diminuir(preco, 13, True)))
