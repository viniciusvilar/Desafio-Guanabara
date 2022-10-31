soma = 0
contador = 0
while True:
    flag = int(input('Digite um número [998 para encerrar]:  '))
    if flag != 998:
        soma += flag
        contador += 1
    else:
        break
print('Foram digitados {} números. A soma entre eles é {}!'.format(contador, soma))
