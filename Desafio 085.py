listaFinal = [[], []]

for c in range(7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        listaFinal[0].append(numero)
    else:
        listaFinal[1].append(numero)

print('Valores pares: {}'.format(sorted(listaFinal[0])))
print('Valores impares: {}'.format(sorted(listaFinal[1])))
