import random
numRand = random.randint(0,10)
numUser = int(input('Digite um valor inteiro de 0 a 10: '))
contador = 1
while numUser != numRand:
    numUser = int(input('Digite novamente um valor inteiro de 0 a 10: '))
    contador += 1
print('Você ACERTOU!')
print('Foram necessário {} tentativas'.format(contador))
