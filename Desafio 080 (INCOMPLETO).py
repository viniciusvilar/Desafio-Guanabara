listaValores = []
for c in range(5):
    num = int(input('Digite um valor: '))
    if c == 0:
        listaValores.append((num))
        print('Adicionado no final da lista!')
    else:
        if num > max(listaValores):
            listaValores.append(num)
            print('Adicionado no final da lista!')
        elif num < min(listaValores):
            listaValores.insert(0, num)
            print('Adicionado na posição 0 da lista!')
print('='*25)
print('Os valores digitados em ordem foram {}'.format(listaValores))
