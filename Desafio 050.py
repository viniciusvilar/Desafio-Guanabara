soma = 0
for c in range(0, 6):
    num = int(input('Informe um valor inteiro: '))
    if num % 2 == 0:
        soma += num
print('A soma dos NÚMEROS PARES digitado é {}!'.format(soma))