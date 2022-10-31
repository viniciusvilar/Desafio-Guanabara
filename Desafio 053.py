frase = input('Informe uma frase: ').strip().upper().replace(' ','')
fraseInversa = ''
sabedor = 0
tamanho = len(frase) - 1
for c in range(0, len(frase)):
    if frase[c] == frase[tamanho]:
        sabedor += 1
    fraseInversa += frase[tamanho]
    tamanho -= 1
if sabedor == len(frase):
    sit = 'É UM PALÍNDROMO'
else:
    sit = 'NÃO É UM PALÍNDROMO'
print('O inverso de {} é {}'.format(frase, fraseInversa))
print(sit)