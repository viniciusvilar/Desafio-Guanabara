listaValores = []
flag = 'o'
while 'N' not in flag:
    valor = int(input('Digite um valor: '))
    if valor not in listaValores:
        listaValores.append(valor)
        print('Valor ADICIONADO!')
    else:
        print('Valor DUPLICADO! Não será adicionado')
    print('='*25)
    flag = input('Quer continuar? [S/N]: ').strip().upper()
    while flag not in 'SN':
        flag = input('Quer continuar? [S/N]: ').strip().upper()
print('='*25)
print('Os valores adicionados foram {}'.format(sorted(listaValores)))
