soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print('A soma dos números ímpares e múltiplos de 3 no intervalo de 1 até 500 é: {}'.format(soma))