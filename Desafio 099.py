from time import sleep

def maior(*num):
    maiorValor = 0
    for c in range(len(num)):
        if c == 0:
            maiorValor = num[c]
        if num[c] > maiorValor:
            maiorValor = num[c]
    print('='*30)
    print('Analisando os valores passados: ')
    for c in(num):
        sleep(0.5)
        print(c, end=' ')
    print('Foram informado ao todo {} valores'.format(len(num)))
    print('O maior valor informado foi {}'.format(maiorValor))



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
