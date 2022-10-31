from utilidades import moeda


preco = float(input('Digite o preço R$'))
print('A metade de {} é {}'.format(preco, moeda.metade(preco)))
print('O dobro de {} é {}'.format(preco, moeda.dobro(preco)))
print('Aumentando 10%, temos {}'.format(moeda.aumenta(preco, 10)))
print('Reduzindo 13%, temos {}'.format(moeda.diminuir(preco, 13)))
