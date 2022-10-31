listaTotal = list()
pessoasAdd = dict()
totalIdade = 0
flag = '.'
while 'N' not in flag:
    pessoasAdd['nome'] = input('Nome: ')
    pessoasAdd['sexo'] = input('Sexo [M/F]: ').strip().upper()
    pessoasAdd['idade'] = int(input('Idade: '))
    totalIdade += pessoasAdd['idade']
    listaTotal.append(pessoasAdd.copy())
    pessoasAdd.clear()
    flag = input('Quer continuar [S/N]: ').strip().upper()
    print('='*25)

mediaIdade = totalIdade/len(listaTotal)
print('Pessoas cadastradas: {}'.format(len(listaTotal)))
print('Média de idade: {:.2f} anos'.format(mediaIdade))
print('As mulheres cadastradas foram: ',end='')
for c in range(0, len(listaTotal)):
    if listaTotal[c]['sexo'] == 'F':
        print(listaTotal[c]['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
print()
for c in range(0, len(listaTotal)):
    if listaTotal[c]['idade'] > mediaIdade:
        print('Nome = {}; Sexo = {}; Idade = {};'.format(listaTotal[c]['nome'], listaTotal[c]['sexo'], listaTotal[c]['idade']))
print()
print('PROGRAMA FINALIZADO')



