def metade(preco, formata=False):
    met = preco/2
    if formata:
        return valFormat(met)
    else:
        return met


def dobro(preco, formata=False):
    dob = preco*2
    if formata:
        return valFormat(dob)
    else:
        return dob


def aumenta(preco, taxa=0, formata=False):
    aum = preco + ((preco*taxa)/100)
    if formata:
        return valFormat(aum)
    else:
        return aum


def diminuir(preco, taxa=0, formata=False):
    dim = preco - ((preco*taxa)/100)
    if formata:
        return valFormat(dim)
    else:
        return dim

def valFormat(preco):
    return 'R${:.2f}'.format(preco)

def resumo(preco=0, aume=0, dimi=0):
    dobroPreco = dobro(preco)
    metadePreco = metade(preco)
    aumePreco = aumenta(preco, aume)
    dimiPreco = diminuir(preco, dimi)
    print('='*30)
    print('{}'.format('RESUMO DO VALOR'.center(30)))
    print('='*30)
    print('Preço analisado: R${:.2f}'.format(preco))
    print('Dobro do preço: R${:.2f}'.format(dobroPreco))
    print('Metade do preço: R${:.2f}'.format(metadePreco))
    print('{}% de aumento: R${:.2f}'.format(aume, aumePreco))
    print('{}% de redução: R${:.2f}'.format(dimi, dimiPreco))
    print('=' * 30)
