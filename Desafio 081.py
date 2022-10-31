listaValores = []
flag = ''
while 'N' not in flag:
    num = int(input('Digite um valor: '))
    flag = input('Quer continuar: [S/N] ').strip().upper()
    listaValores.append(num)
if 5 not in listaValores:
    sit = 'O 5 não está na lista'
else:
    sit = 'O 5 está na lista'

print('Você digitou {} elementos!'.format(len(listaValores)))
print('Os valores em ordem decrescente são: {}'.format(sorted(listaValores, reverse=True)))
print(sit)
