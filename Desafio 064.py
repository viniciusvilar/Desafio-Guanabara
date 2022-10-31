flag = 0
soma = 0
print('Para finalizar o programa digite 998')
while flag != 998:
    flag = int(input('Digite um valor inteiro: '))
    soma += flag
print('A soma dos números foi {}'.format(soma - 998))