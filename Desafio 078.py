valores = []
for c in range(5):
    valores.append((int(input('Digite um valor: '))))
print('='*25)
print('O maior valor digitado foi {} nas posições '.format(max(valores)), end='')
for i, c in enumerate(valores):
    if c == max(valores):
        print(i, end=' ')
print()
print('O menor valor digitado foi {} nas posições '.format(min(valores)), end='')
for i, c in enumerate(valores):
    if c == min(valores):
        print(i, end=' ')
