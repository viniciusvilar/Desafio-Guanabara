num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
numMaior = 0
numMenor = 0
if num1 == num2 == num3:
    print('Números iguais!')
else:
    if num1 >= num2 and num1 >= num3:
        numMaior = num1
    else:
        if num2 >= num1 and num2 >= num3:
            numMaior = num2
        else:
            numMaior = num3
    if num1 <= num2 and num1 <= num3:
        numMenor = num1
    else:
        if num2 <= num1 and num2 <= num3:
            numMenor = num2
        else:
            numMenor = num3
    print("Maior número: {}".format(numMaior))
    print('Menor número: {}'.format(numMenor))


