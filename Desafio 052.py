numero = int(input('Digite um número inteiro: '))
sabedor = 0
for c in range(1, numero+1):
    if numero % c == 0:
        sabedor += 1
if sabedor == 2:
    sit = 'Número PRIMO!'
else:
    sit = 'Esse número NÃO É PRIMO!'
print(sit)