num = int(input('Informe o número que deseja saber a tabuada: '))
for c in range(0, 11):
    print('{} X {} = {}'.format(num, c, num*c))
print('FINALIZADO!')