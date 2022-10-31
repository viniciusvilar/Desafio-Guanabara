def fatorial(num, show=False):
    """
    CALCULA O FATORIAL DE UM NÚMERO
    :param num: Número que deseja calcular o fatorial
    :param show: Se quer ou não mostrar o calculo
    :return: Retorna fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        for c in range(num, 1, -1):
            print('{} x'.format(c), end=' ')
        print('1 = ',end='')
        return f
    else:
        return f

print(fatorial(5))
#help(fatorial)
