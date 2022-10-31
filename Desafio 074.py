from random import randint
numerosRandom = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ',end="")
maior = 0
menor = 11
for c in numerosRandom:
    print(c, end=' ')
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print()
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
