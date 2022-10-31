import random
numRand = random.randint(0,5)
numUser = int(input('Digite um valor inteiro de 0 a 5: '))
if numUser == numRand:
    print('PARABÉNSSSS!!!!!! VOCÊ ADVINHOU O NÚMERO')
else:
    print('Que pena! Você errou o número')
print('O númeor correto é {}'.format(numRand))
