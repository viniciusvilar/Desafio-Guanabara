flag = 's'
soma = 0
maiorNumero = menorNumero = 0
contador = 0
while 'n' not in flag:
    numero = int(input('Digite um número: '))
    soma += numero
    if contador == 0:
        menorNumero = numero
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero
    contador += 1
    flag = input('Deseja continuar (S/N): ').strip().lower()
print('O maior valor foi {}'.format(maiorNumero))
print('O menor valor foi {}'.format(menorNumero))
print('A média dos números foi {:.2f}'.format(soma/contador))
