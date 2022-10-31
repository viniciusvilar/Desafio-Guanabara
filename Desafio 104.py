def leiaInt(nInt):
    numInt = 0
    while True:
        try:
            numInt = int(input(nInt))
        except (ValueError, TypeError):
            print('ERRO: Digite um valor inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar!')
            return 0
        else:
            return numInt

def leiaFloat(nFloat):
    numReal = 0.0
    while True:
        try:
            numReal = float(input(nFloat))
        except:
            print('ERRO: Digite um valor real válido')
            continue
        else:
            return numReal


nInt = leiaInt('Digite um número inteiro: ')
nFloat = leiaFloat('Digite um número real:')
print('O valor inteiro é {} e o valor real é {}'.format(nInt, nFloat))
