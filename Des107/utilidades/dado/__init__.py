def leiaDinheiro(preco):
    while True:
        preco = input('Digite o preço: R$').strip().replace(',', '.')
        if preco == '':
            preco = 'd'
        if ((preco.isalpha()==False) and (preco.isalnum()==False)) or preco.isnumeric():
            preco = float(preco)
            break
        print('ERRO! "{}" é um preço inválido!'.format(preco))

    return preco

print(leiaDinheiro('Digite o preço: R$'))
