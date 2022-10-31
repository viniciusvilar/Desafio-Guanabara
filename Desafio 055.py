peso = float(input('Peso da 1ª Pessoa: '))
maiorPeso = menorPeso = peso
for c in range(2, 6):
    peso = float(input('Peso da {}ª Pessoa: '.format(c)))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print('O maior peso foi {:.2f}Kg'.format(maiorPeso))
print('O menor peso foi {:.2f}Kg'.format(menorPeso))