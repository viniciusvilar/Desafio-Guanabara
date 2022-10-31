boletimCompleto = []
listaCobaia = []
listaCobaia2 = []
flag = ''
media = 0
'''
listaCobaia.append('João')
listaCobaia2.append(8)
listaCobaia2.append(9)
listaCobaia.append(listaCobaia2[:])
listaCobaia.append(8.5)
boletimCompleto.append(listaCobaia[:])
listaCobaia.clear()
listaCobaia2.clear()
'''
while 'N' not in flag:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    listaCobaia.append(nome)
    listaCobaia2.append(nota1)
    listaCobaia2.append(nota2)
    listaCobaia.append(listaCobaia2[:])
    listaCobaia.append(media)
    boletimCompleto.append(listaCobaia[:])
    listaCobaia.clear()
    listaCobaia2.clear()
    flag = input('Quer continuar [S/N]: ').strip().upper()
    print('='*25)

print('No. Nome {:>14}'.format('MÉDIA'))
print('='*25)
for c in range(len(boletimCompleto)):
    print('{:<2} {:<12} {:>8}'.format(c, boletimCompleto[c][0], boletimCompleto[c][2]))

while True:
    flag2 = int(input('Mostras notas de qual aluno? [998 interrompe]: '))
    if flag2 != 998:
        print('Notas de {} são {}'.format(boletimCompleto[flag2][0], boletimCompleto[flag2][1]))
        print('='*25)
    else:
        break
print('PROGRAMA FINALIZADO!')
