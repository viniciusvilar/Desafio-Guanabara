numero = int(input('Digite um número (MAIOR QUE 2): '))
contador = 0
numFib0 = 0
numFib1 = 1
numFibNovo = 0
print('{} -> {} '.format(numFib0, numFib1), end='-> ')
while contador < numero-2:
    numFibNovo = numFib0 + numFib1
    numFib0 = numFib1
    numFib1 = numFibNovo
    if contador != numero-3:
        print(numFibNovo, end=' -> ')
    else:
        print(numFibNovo, '-> FIM!')
    contador += 1