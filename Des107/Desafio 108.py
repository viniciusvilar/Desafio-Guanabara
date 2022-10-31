from utilidades import moeda

#mesma coisa do Desafio 109 so que com ninho de gato nas formatações
preco = float(input('Digite o preço R$'))
print('A metade de {} é {}'.format(moeda.valFormat(preco), moeda.metade(preco, True)))
print('O dobro de {} é {}'.format(moeda.valFormat(preco), moeda.dobro(preco, True)))
print('Aumentando 10%, temos {}'.format(moeda.aumenta(preco, 10, True)))
print('Reduzindo 13%, temos {}'.format(moeda.diminuir(preco, 13, True)))
