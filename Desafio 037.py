numero = int(input('Digite um número inteiro: '))
print('='*30)
print('MENU DE CONVERSÃO')
print('Press 1 para BINÁRIO')
print('Press 2 para OCTAL')
print('Press 3 para HEXADECIMAL')
print('='*30)
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    numBinario = str(bin(numero))
    print('O número {} em BINÁRIO é {}'.format(numero, numBinario[2:]))
elif opcao == 2:
    numOctal = str(oct(numero))
    print('O número {} em OCTAL é {}'.format(numero, numOctal[2:]))
elif opcao == 3:
    numHexa = str(hex(numero))
    print('O número {} em HEXADECIMAL é {}'.format(numero, numHexa[2:]))
else:
    print('Você digitou uma opção inexistente! O programa será encerrado!!!!')