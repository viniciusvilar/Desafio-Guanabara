num1 = int(input('Informe um valor: '))
num2 = int(input('Informe um valor: '))
num3 = int(input('Informe um valor: '))
num4 = int(input('Informe um valor: '))
numero = (num1, num2, num3, num4)
cont9 = 0
pos3 = False
cont3 = -1
temPar = False
sitPos3 = ''
for c in numero:
    if c == 9:
        cont9 += 1
    if c == 3:
        cont3 = numero.index(3)
        pos3 = True
    if c % 2 == 0:
        temPar = True
if pos3:
    sitPos3 = 'O número 3 foi digitado na posição {}'.format(cont3+1)
else:
    sitPos3 = 'O número 3 não foi digitado'
print('Você digitou os valores: {}'.format(numero))
print('O valor 9 apareceu {} vezes'.format(cont9))
print(sitPos3)
if temPar:
    print('Os valores pares foram: ', end='')
    for c in numero:
        if c % 2 == 0:
            print(c, end=' ')
else:
    print('Não possue valores par')