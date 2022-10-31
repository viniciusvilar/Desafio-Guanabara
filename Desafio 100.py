from random import randint

def somaPares(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    #print('A soma dos pares de {} é {}'.format(numeros, soma))
    return soma
    #print(soma)

def sortear():
    numeros = list()
    #print('Sorteando os valores da lista: ', end='')
    for c in range(5):
        sorteado = randint(0, 10)
        #print(sorteado, end=' ')
        numeros.append(sorteado)
    #print('FINALIZADO!')
    return numeros


numeros = sortear()
pares = somaPares(numeros)
print('Sorteando 5 valores na lista: ', end='')
for c in numeros:
    print(c, end=' ')
print('FINALIZADO!')
print('A soma dos pares de {} é {}'.format(numeros, pares))
