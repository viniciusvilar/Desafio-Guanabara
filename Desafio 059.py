numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
print('----- MENU DE OPÇÕES -----')
print('[1] SOMAR')
print('[2] MULTIPLICAR')
print('[3] MAIOR')
print('[4] NOVOS NÚMEROS')
print('[5] SAIR DO PROGRAMA')
print('-'*26)
op = int(input('OPÇÃO: '))
while op != 5:
    if op == 1:
        soma = numero1 + numero2
        print('A soma entre {} e {} é {}'.format(numero1, numero2, soma))
    elif op == 2:
        mult = numero1 * numero2
        print('O produto entre {} e {} é {}'.format(numero1, numero2, mult))
    elif op == 3:
        print('O maior número entre {} e {} é {}'.format(numero1, numero2, max(numero1, numero2)))
    elif op == 4:
        numero1 = int(input('Digite um novo valor: '))
        numero2 = int(input('Digite outro valor: '))
    print('='*45)
    op = int(input('Seleciona uma nova OPÇÃO: '))
print('Programa finalizado!!!')
