print('='*25)
print('CONTADOR DE NOTAS')
print('='*25)
valor = int(input('Digite um valor inteiro: R$'))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    if valor >= 50:
        ced50 = valor // 50
        valor = valor % 50
    elif valor >= 20:
        ced20 = valor // 20
        valor = valor % 20
    elif valor >= 10:
        ced10 = valor // 10
        valor = valor % 10
    elif valor >= 1:
        ced1 = valor // 1
        valor = valor % 1
    else:
        break
print('='*25)
print('{} Cédulas de 50'.format(ced50))
print('{} Cédulas de 20'.format(ced20))
print('{} Cédulas de 10'.format(ced10))
print('{} Cédulas de 1'.format(ced1))
