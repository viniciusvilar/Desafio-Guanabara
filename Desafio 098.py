from time import sleep
def contador(i, f, p):
    p = abs(p)
    if p == 0:
        p = 1
    print('Contade de {} até {} de {} em {}'.format(i, f, p, p))
    sleep(0.5)
    if f > i:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.5)
    else:
        i = max(i, f)
        f = min(i, f)
        p *= -1
        '''
        if p == 0:
            p = 1
        elif p < 0:
            p = 1'''
        for c in range(i, f+p, p):
            print(c, end=' ')
            sleep(0.5)
    sleep(0.1)
    print('FIM')
    print('=' * 30)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de contar: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
