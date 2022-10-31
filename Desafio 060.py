''' FATORIAL COM WHILE
numero = int(input('Digite um número DIFERENTE DE 0: '))
fatorialNum = 1
print('{}!'.format(numero), end=' = ')
while numero != 0:
    if numero != 1:
        print('{}'.format(numero), end=' x ')
    else:
        print('{}'.format(numero), end=' = ')
    fatorialNum *= numero
    numero -= 1
print(fatorialNum)'''

numero = int(input('Digite um número DIFERENTE DE 0: '))
fatorialNum = 1
print('{}!'.format(numero), end=' = ')
for c in range(numero, 0, -1):
    if c != 1:
        print('{}'.format(c), end=' x ')
    else:
        print('{}'.format(c), end=' = ')
    fatorialNum *= c
print(fatorialNum)