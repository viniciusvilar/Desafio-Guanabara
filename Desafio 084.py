totalPessoas = []
listaCobaia = []
pessoasPesadas = []
pessoasLeves = []
maiorPeso = 0
menorPeso = 0
c = 1
flag = ''
while 'N' not in flag:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    listaCobaia.append(nome)
    listaCobaia.append(peso)
    totalPessoas.append(listaCobaia[:])
    if c == 1:
        menorPeso = peso
        c = 2
    if peso >= maiorPeso:
        maiorPeso = peso
    if peso <= menorPeso:
        menorPeso = peso
    listaCobaia.clear()

    flag = input('Deseja continuar [S/N]: ').strip().upper()
    print('='*25)

for c in totalPessoas:
    if c[1] == maiorPeso:
        pessoasPesadas.append(c[0])
    if c[1] == menorPeso:
        pessoasLeves.append(c[0])

print('Você cadastrou {} pessoas.'.format(len(totalPessoas)))
print('O maior peso foi {}. Peso de {}'.format(maiorPeso, pessoasPesadas))
print('O menor peso foi {}. Peso de {}'.format(menorPeso, pessoasLeves))
